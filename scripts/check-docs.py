#!/usr/bin/env python3
"""Read-only Markdown checks for this documentation repository.

Exit 0 when there is no hard failure. This script does not modify files
and does not touch product-site source.

Tool-page HTTP rules:

- 301 and 302 are acceptable when the final page is the tool page.
- 404 and 410 fail.
- Every HTTP status from 500 through 599 fails after the retry budget.
- DNS and other network errors are INCONCLUSIVE, never a pass.
- 403 and 429 are INCONCLUSIVE, never treated as 200.
- A tool URL whose final path is the site root fails.
- A final error page (path or title containing 404) fails.

External standards URLs are fetched only with --external-standards.
Paywall, login, 403, 429, and network results stay INCONCLUSIVE.
They are not rewritten and they do not fail the run.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
SITES = [
    "NetEngineerLab",
    "PCDog",
    "AIMarkTool",
    "PowerEngineerLab",
    "HVACEngineerLab",
    "PrivacyFileLab",
    "DataFileLab",
    "WaterEngineerLab",
    "StructuralEngineerLab",
    "DevEngineerLab",
    "DIYCalcLab",
]
ALLOWED_STATUS = {"VERIFIED", "REVIEW_REQUIRED"}
CALCULATION_STATUS = {"VERIFIED", "REVIEW_REQUIRED", "NOT_VERIFIED"}
STANDARDS_STATUS = {"VERIFIED", "PENDING", "NOT_APPLICABLE"}
LOCALE_ROUTE_STATUS = {"VERIFIED", "MISSING", "REDIRECTED", "INCONCLUSIVE", "NOT_SUPPORTED"}
SECRET_PATTERNS = [
    ("private_key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----")),
    ("github_token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b")),
    ("github_fine_grained", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("access_token_url", re.compile("x-access-" + r"token:[^\s@]+")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("stripe_live", re.compile(r"\bsk_live_[0-9a-zA-Z]{16,}\b")),
]
RETRY_HTTP = {408}
HARD_HTTP = {404, 410}
INCONCLUSIVE_HTTP = {403, 429}
LOCALE_ROOTS = {"zh", "zh-cn", "en", "es"}
USER_AGENT = "CalculatorDocCheck/2.0 (+https://github.com/ddcodedog/Calculator)"
FORMULA_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:\.zh-CN)?\.md$")
NUMBER_RE = re.compile(r"(?<![\w.])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?")
UNIT_TOKENS = (
    "dB/km",
    "dBm",
    "dB",
    "Gbit/s",
    "Mbit/s",
    "kbit/s",
    "GPa",
    "kN",
    "m/s",
    "m³/s",
    "m³",
    "µs",
    "ps",
    "nm",
    "km",
    "mm",
    "kW",
    "hp",
    "Pa",
    "Ω",
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def markdown_files() -> list[Path]:
    """Markdown subject to title and link checks.

    ``promo/`` holds outreach drafts, not formula topics, so it stays out of
    those gates. Verification still reads only top-level site folders.
    """
    files = []
    for path in ROOT.rglob("*.md"):
        rel_parts = path.relative_to(ROOT).parts
        if any(part.startswith(".") for part in rel_parts) or "promo" in rel_parts:
            continue
        files.append(path)
    return sorted(files)


def is_locale_translation(path: Path) -> bool:
    """Same topic in another language. Not a second formula."""
    return path.name.endswith(".zh-CN.md")


def formula_files(root: Path | None = None) -> list[Path]:
    base = ROOT if root is None else root
    found = []
    for site in SITES:
        folder = base / site
        if not folder.is_dir():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.name != "README.md" and not is_locale_translation(path):
                found.append(path)
    return found


def chinese_formula_files(root: Path | None = None) -> list[Path]:
    base = ROOT if root is None else root
    found = []
    for site in SITES:
        folder = base / site
        if not folder.is_dir():
            continue
        found.extend(sorted(folder.glob("*.zh-CN.md")))
    return found


def is_http_server_error(status: object) -> bool:
    """True only for HTTP 500 through 599. 499 and 600 are outside that range."""
    return isinstance(status, int) and 500 <= status <= 599


def strip_code_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def h1_titles(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^#\s+(.+?)\s*$", text, re.M)]


def section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.M)
    if not match:
        return ""
    rest = text[match.end() :]
    nxt = re.search(r"^##\s+", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def verification_status(text: str) -> str | None:
    body = section(text, "Verification") or section(text, "核对")
    match = re.search(r"^\|\s*Status\s*\|\s*([A-Z_]+)\s*\|", body, re.M)
    return match.group(1) if match else None


def table_status(text: str, label: str) -> str | None:
    body = section(text, "Verification") or section(text, "核对")
    match = re.search(rf"^\|\s*{re.escape(label)}\s*\|\s*([A-Z_]+)\s*\|", body, re.M)
    return match.group(1) if match else None


def online_calculator_urls(text: str) -> list[str]:
    body = section(text, "Online Calculator") or section(text, "在线计算器")
    return re.findall(r"https?://[^\s)<>]+", body)


def markdown_links(text: str) -> list[str]:
    links = []
    for match in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        links.append(target.split()[0])
    return links


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def normalize_url(url: str) -> str:
    url = url.rstrip(").,]")
    if url.endswith("/") and url.count("/") > 3:
        return url[:-1]
    return url


def normalize_math(block: str) -> str:
    return re.sub(r"\s+", "", block)


def math_blocks(text: str) -> list[str]:
    fenced = strip_code_fences(text)
    return [normalize_math(block) for block in re.findall(r"\$\$(.+?)\$\$", fenced, flags=re.S)]


def number_tokens(text: str) -> list[str]:
    return [token.replace(",", "") for token in NUMBER_RE.findall(text)]


def github_slug(title: str) -> str:
    text = title.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def heading_slugs(text: str) -> set[str]:
    slugs: set[str] = set()
    counts: Counter[str] = Counter()
    for match in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.M):
        base = github_slug(match.group(1))
        if not base:
            continue
        count = counts[base]
        counts[base] += 1
        slugs.add(base if count == 0 else f"{base}-{count}")
    return slugs


class Report:
    def __init__(self) -> None:
        self.failures: list[dict] = []
        self.warnings: list[dict] = []
        self.stats: Counter[str] = Counter()

    def fail(self, check: str, message: str, **extra: object) -> None:
        self.failures.append({"check": check, "message": message, **extra})

    def warn(self, check: str, message: str, **extra: object) -> None:
        self.warnings.append({"check": check, "message": message, **extra})


def check_titles(report: Report, files: list[Path]) -> None:
    seen: dict[str, str] = {}
    formula = {path.resolve() for path in formula_files()}
    chinese = {path.resolve() for path in chinese_formula_files()}
    for path in files:
        titles = h1_titles(path.read_text(encoding="utf-8"))
        if path.resolve() in formula or path.resolve() in chinese:
            if len(titles) != 1:
                report.fail("titles", f"{rel(path)} has {len(titles)} H1 headings; expected 1")
        for title in titles:
            key = title.casefold()
            if key in seen:
                report.fail("titles", f"duplicate H1 {title!r}", paths=[seen[key], rel(path)])
            else:
                seen[key] = rel(path)


def check_links(report: Report, files: list[Path]) -> int:
    checked = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in markdown_links(text):
            if target.startswith("#"):
                checked += 1
                slug = target[1:]
                if slug and slug not in heading_slugs(text):
                    report.fail("anchors", f"{rel(path)} broken anchor: {target}")
                continue
            if is_external(target):
                continue
            checked += 1
            path_part, _, fragment = target.partition("#")
            if not path_part:
                continue
            dest = (path.parent / path_part).resolve()
            try:
                dest.relative_to(ROOT.resolve())
            except ValueError:
                report.fail("relative_links", f"{rel(path)} link escapes the repo: {target}")
                continue
            if not dest.exists():
                report.fail("relative_links", f"{rel(path)} broken link: {target}")
                continue
            if fragment and dest.suffix == ".md":
                try:
                    dest_text = dest.read_text(encoding="utf-8")
                except OSError:
                    continue
                if fragment not in heading_slugs(dest_text):
                    report.fail("anchors", f"{rel(path)} broken anchor: {target}")
    report.stats["internalLinkChecks"] = checked
    return checked


def check_math_text(report: Report, path: Path, text: str) -> None:
    visible = strip_code_fences(text)
    if visible.count("```") % 2:
        report.fail("math_fences", f"{rel(path)} has an unclosed code fence")
    display = 0
    for line in visible.splitlines():
        if line.strip() == "$$":
            display += 1
        elif line.count("$$") % 2:
            report.fail("math_fences", f"{rel(path)} has an odd $$ count on one line")
            break
    else:
        if display % 2:
            report.fail("math_fences", f"{rel(path)} has an unclosed $$ display block")
    if visible.count(r"\(") != visible.count(r"\)"):
        report.fail("math_fences", f"{rel(path)} has unbalanced \\( \\) math")
    if visible.count(r"\[") != visible.count(r"\]"):
        report.fail("math_fences", f"{rel(path)} has unbalanced \\[ \\] math")


def check_math(report: Report, files: list[Path]) -> None:
    del files
    for path in formula_files() + chinese_formula_files():
        check_math_text(report, path, path.read_text(encoding="utf-8"))


def check_markdown_quality(report: Report, files: list[Path]) -> None:
    for path in files:
        raw = path.read_text(encoding="utf-8")
        if not raw.strip():
            report.fail("empty_content", f"{rel(path)} is empty")
            continue
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", raw):
            report.fail("invalid_characters", f"{rel(path)} contains a control character")
        if path.parent.name in SITES and path.name != "README.md" and not FORMULA_NAME.match(path.name):
            report.fail("filenames", f"{rel(path)} has an irregular filename")
        for match in re.finditer(r"^#{1,6}\s*$", raw, re.M):
            report.fail("empty_headings", f"{rel(path)} has an empty heading", line=raw[: match.start()].count("\n") + 1)
        visible = strip_code_fences(raw)
        if visible.count("```") % 2:
            report.fail("code_fences", f"{rel(path)} has an unclosed code fence")
        ids = re.findall(r"\bid\s*=\s*[\"']([^\"']+)[\"']", raw)
        seen: set[str] = set()
        for item in ids:
            if item in seen:
                report.fail("duplicate_ids", f"{rel(path)} repeats id {item!r}")
            seen.add(item)
        for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", raw):
            target = match.group(1).strip().split()[0]
            if is_external(target) or target.startswith("data:"):
                continue
            dest = (path.parent / target.split("#", 1)[0]).resolve()
            if not dest.exists():
                report.fail("images", f"{rel(path)} broken image: {target}")
        check_tables(report, path, visible)


def pipe_count(row: str) -> int:
    """Column separators only. Escaped pipes and pipes inside code spans are cell text."""
    without_code = re.sub(r"`[^`]*`", "", row)
    without_escaped = re.sub(r"\\\|", "", without_code)
    return without_escaped.count("|")


def check_tables(report: Report, path: Path, text: str) -> None:
    visible = re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)
    lines = visible.splitlines()
    index = 0
    while index < len(lines):
        if not lines[index].strip().startswith("|"):
            index += 1
            continue
        block = []
        while index < len(lines) and lines[index].strip().startswith("|"):
            block.append(lines[index].strip())
            index += 1
        if len(block) < 2:
            report.fail("tables", f"{rel(path)} has a table row without a delimiter")
            continue
        if not re.match(r"^\|\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$", block[1]):
            report.fail("tables", f"{rel(path)} has a table that does not start with a delimiter row")
            continue
        width = pipe_count(block[0])
        for row in block:
            if pipe_count(row) != width:
                report.fail("tables", f"{rel(path)} has a table row with a different column count")
                break


def load_verification() -> dict:
    path = ROOT / "reports" / "FORMULA_VERIFICATION.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def check_verification(report: Report) -> None:
    data = load_verification()
    topics = data.get("topics")
    if not isinstance(topics, list):
        report.fail("verification_status", "reports/FORMULA_VERIFICATION.json has no topics list")
        return
    by_doc = {}
    for topic in topics:
        document = topic.get("document")
        status = topic.get("status")
        if not document or not status:
            report.fail("verification_status", "a verification topic is missing document or status")
            continue
        if document in by_doc:
            report.fail("verification_status", f"duplicate verification record for {document}")
        by_doc[document] = topic
        if status not in ALLOWED_STATUS:
            report.fail("verification_status", f"{document} has status {status}, not {sorted(ALLOWED_STATUS)}")
        calculation = topic.get("calculationStatus")
        standards = topic.get("standardsStatus")
        if calculation not in CALCULATION_STATUS:
            report.fail("verification_status", f"{document} calculationStatus {calculation} is not allowed")
        elif calculation != status and not (calculation == "NOT_VERIFIED" and status == "REVIEW_REQUIRED"):
            if calculation != status:
                report.fail(
                    "verification_status",
                    f"{document} calculationStatus {calculation} does not match status {status}",
                )
        if standards not in STANDARDS_STATUS:
            report.fail("verification_status", f"{document} standardsStatus {standards} is not allowed")
        if standards == "VERIFIED" and not (topic.get("standardsEvidence") and topic.get("standardsCheckedDate")):
            report.fail(
                "verification_status",
                f"{document} is standards VERIFIED without evidence and a checked date",
            )

    disks = {rel(path): path for path in formula_files()}
    if set(disks) != set(by_doc):
        missing = sorted(set(disks) - set(by_doc))
        extra = sorted(set(by_doc) - set(disks))
        if missing:
            report.fail("verification_status", "formula files missing from FORMULA_VERIFICATION.json", files=missing)
        if extra:
            report.fail("verification_status", "verification records without a formula file", files=extra)

    claimed = data.get("countVerified")
    actual_verified = sum(1 for topic in by_doc.values() if topic.get("status") == "VERIFIED")
    if claimed != actual_verified:
        report.fail(
            "verification_status",
            f"countVerified is {claimed}, topic records say {actual_verified}",
        )
    pending = sum(1 for topic in by_doc.values() if topic.get("standardsStatus") == "PENDING")
    standards_verified = sum(1 for topic in by_doc.values() if topic.get("standardsStatus") == "VERIFIED")
    not_applicable = sum(1 for topic in by_doc.values() if topic.get("standardsStatus") == "NOT_APPLICABLE")
    report.stats["standardsPending"] = pending
    if data.get("countStandardsPending") != pending:
        report.fail(
            "verification_status",
            f"countStandardsPending is {data.get('countStandardsPending')}, records say {pending}",
        )
    if data.get("countStandardsVerified") != standards_verified:
        report.fail(
            "verification_status",
            f"countStandardsVerified is {data.get('countStandardsVerified')}, records say {standards_verified}",
        )
    if data.get("countStandardsNotApplicable") != not_applicable:
        report.fail(
            "verification_status",
            f"countStandardsNotApplicable is {data.get('countStandardsNotApplicable')}, records say {not_applicable}",
        )

    for document, path in disks.items():
        text = path.read_text(encoding="utf-8")
        compare_status_rows(report, document, text, by_doc[document])
        urls = online_calculator_urls(text)
        if len(urls) != 1:
            report.fail(
                "verification_status",
                f"{document} Online Calculator section has {len(urls)} URLs; expected 1",
            )
        elif normalize_url(urls[0]) != normalize_url(str(by_doc[document].get("productionUrl", ""))):
            report.fail(
                "verification_status",
                f"{document} Online Calculator URL does not match productionUrl",
                page=urls[0],
                json=by_doc[document].get("productionUrl"),
            )

    for path in chinese_formula_files():
        english = path.with_name(path.name.replace(".zh-CN.md", ".md"))
        document = rel(english)
        if document not in by_doc:
            report.fail("verification_status", f"{rel(path)} has no English verification record")
            continue
        compare_status_rows(report, rel(path), path.read_text(encoding="utf-8"), by_doc[document])


def compare_status_rows(report: Report, document: str, text: str, topic: dict) -> None:
    status = verification_status(text)
    recorded = topic.get("status")
    if status is None:
        report.fail("verification_status", f"{document} has no Verification status row")
        return
    if status != recorded:
        report.fail(
            "verification_status",
            f"{document} status {status} does not match JSON {recorded}",
        )
    calculation = table_status(text, "Calculation status")
    standards = table_status(text, "Standards status")
    if calculation != topic.get("calculationStatus"):
        report.fail(
            "verification_status",
            f"{document} Calculation status {calculation} does not match JSON {topic.get('calculationStatus')}",
        )
    if standards != topic.get("standardsStatus"):
        report.fail(
            "verification_status",
            f"{document} Standards status {standards} does not match JSON {topic.get('standardsStatus')}",
        )


def readme_status_for(readme: str, filename: str) -> str | None:
    for line in readme.splitlines():
        if f"]({filename})" not in line and f"]({filename} " not in line:
            continue
        match = re.match(r"^\|\s*([A-Z_]+)\s*\|", line)
        if match:
            return match.group(1)
    return None


def check_toc(report: Report) -> None:
    root_text = (ROOT / "README.md").read_text(encoding="utf-8")
    total = 0
    for site in SITES:
        folder = ROOT / site
        readme_path = folder / "README.md"
        if not readme_path.exists():
            report.fail("toc", f"missing {site}/README.md")
            continue
        readme = readme_path.read_text(encoding="utf-8")
        topics = sorted(
            p for p in folder.glob("*.md")
            if p.name != "README.md" and not is_locale_translation(p)
        )
        total += len(topics)
        match = re.search(r"^Published topics:\s*(\d+)\s*$", readme, re.M)
        if not match:
            report.fail("toc", f"{site}/README.md is missing a 'Published topics: N' line")
        elif int(match.group(1)) != len(topics):
            report.fail(
                "toc",
                f"{site}/README.md says {match.group(1)} topics; directory has {len(topics)}",
            )
        linked = set()
        for target in markdown_links(readme):
            if is_external(target):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            dest = (readme_path.parent / path_part).resolve()
            if dest.parent == folder.resolve() and dest.suffix == ".md" and dest.name != "README.md":
                if not dest.exists():
                    report.fail("toc", f"{site}/README.md links to missing {dest.name}")
                    continue
                if is_locale_translation(dest):
                    continue
                linked.add(dest.name)
        names = {path.name for path in topics}
        if linked != names:
            report.fail(
                "toc",
                f"{site}/README.md topic links do not match formula files",
                linked=sorted(linked),
                files=sorted(names),
            )
        for path in topics:
            row_status = readme_status_for(readme, path.name)
            doc_status = verification_status(path.read_text(encoding="utf-8"))
            if row_status != doc_status:
                report.fail(
                    "toc",
                    f"{site}/README.md status for {path.name} is {row_status}, document is {doc_status}",
                )
            root_link = f"{site}/{path.name}"
            if f"]({root_link})" not in root_text:
                report.fail("toc", f"root README does not link {root_link}")
    root_count = re.search(r"^Published formula topics:\s*(\d+)\s*$", root_text, re.M)
    if not root_count:
        report.fail("toc", "root README is missing 'Published formula topics: N'")
    elif int(root_count.group(1)) != total:
        report.fail("toc", f"root README says {root_count.group(1)} topics; found {total}")


def check_secrets(report: Report) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part.startswith(".") or part == "node_modules" for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".ico"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for name, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                report.fail("secrets", f"{rel(path)} matches {name}")


def load_review_differences() -> set[str]:
    path = ROOT / "reports" / "ZH_FORMULA_REVIEW.json"
    if not path.exists():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    items = data.get("reviewedDifferences") or []
    return {item.get("document", "") for item in items if isinstance(item, dict)}


def check_language_pairs(report: Report) -> None:
    reviewed = load_review_differences()
    english_names = {path.name for path in formula_files()}
    for path in chinese_formula_files():
        english_name = path.name.replace(".zh-CN.md", ".md")
        english = path.with_name(english_name)
        if english_name not in english_names or not english.exists():
            report.fail("language_pair", f"{rel(path)} has no English topic beside it")
            continue
        zh = path.read_text(encoding="utf-8")
        en = english.read_text(encoding="utf-8")
        if "Locale: zh-CN" not in zh:
            report.fail("language_marker", f"{rel(path)} is missing Locale: zh-CN")
        if "Locale: en" not in en:
            report.fail("language_marker", f"{rel(english)} is missing Locale: en")
        if "简体中文" not in zh:
            report.fail("language_marker", f"{rel(path)} does not identify itself as Simplified Chinese")
        zh_blocks = math_blocks(zh)
        en_blocks = math_blocks(en)
        if zh_blocks != en_blocks and rel(path) not in reviewed:
            report.fail(
                "language_pair",
                f"{rel(path)} formula blocks differ from {rel(english)} and are not on the human-review list",
                zhBlocks=len(zh_blocks),
                enBlocks=len(en_blocks),
            )
        en_example = section(en, "Worked Example") or section(en, "算例")
        # English cross-tool notes use other headings. Compare the whole note's
        # numbers only inside the sections both files actually share.
        zh_example = section(zh, "算例") or section(zh, "Worked Example")
        if en_example and zh_example:
            missing_numbers = Counter(number_tokens(en_example)) - Counter(number_tokens(zh_example))
            if missing_numbers:
                report.fail(
                    "language_pair",
                    f"{rel(path)} worked-example numbers drop or change English values",
                    missing=dict(missing_numbers),
                )
        en_limits = section(en, "Limitations") or section(en, "Limits")
        zh_limits = section(zh, "限制") or section(zh, "Limitations")
        if en_limits and zh_limits:
            missing_limits = Counter(number_tokens(en_limits)) - Counter(number_tokens(zh_limits))
            if missing_limits:
                report.fail(
                    "language_pair",
                    f"{rel(path)} limitation numbers drop or change English values",
                    missing=dict(missing_limits),
                )
        en_formula = section(en, "Formula") or section(en, "公式")
        zh_visible = strip_code_fences(zh)

        def has_unit(haystack: str, token: str) -> bool:
            return re.search(rf"(?<![A-Za-z]){re.escape(token)}(?![A-Za-z])", haystack) is not None

        for token in UNIT_TOKENS:
            if has_unit(en_formula, token) and not has_unit(zh_visible, token):
                report.fail("language_pair", f"{rel(path)} drops unit {token} from the English formula")
        if en_formula.count("%") > zh_visible.count("%"):
            report.fail("language_pair", f"{rel(path)} has fewer percent signs than the English formula")
        for target in markdown_links(zh):
            if is_external(target) or target.startswith("#"):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part.endswith(".md") or path_part.endswith(".zh-CN.md"):
                continue
            linked = (path.parent / path_part).resolve()
            companion = linked.with_name(linked.name.replace(".md", ".zh-CN.md")) if linked.suffix == ".md" else None
            if path_part == english_name:
                continue
            if companion and companion.exists():
                report.fail(
                    "language_pair",
                    f"{rel(path)} links {path_part} even though {companion.name} exists",
                )
        related = section(zh, "相关公式") or section(zh, "Related Formulas")
        related_targets = [item.split("#", 1)[0] for item in markdown_links(related)]
        duplicates = [item for item, count in Counter(related_targets).items() if count > 1]
        if duplicates:
            report.fail("language_pair", f"{rel(path)} repeats a related-formula link", links=duplicates)
        zh_urls = online_calculator_urls(zh)
        en_urls = online_calculator_urls(en)
        if len(zh_urls) != 1:
            report.fail("language_pair", f"{rel(path)} 在线计算器 section has {len(zh_urls)} URLs; expected 1")
        elif en_urls:
            zh_host = urlparse(zh_urls[0]).netloc
            en_host = urlparse(en_urls[0]).netloc
            if zh_host != en_host:
                report.fail("language_pair", f"{rel(path)} tool host {zh_host} does not match {en_host}")
    for path in formula_files():
        if "Locale: en" not in path.read_text(encoding="utf-8"):
            report.fail("language_marker", f"{rel(path)} is missing Locale: en")


def check_locale_config(report: Report) -> None:
    path = ROOT / "config" / "locale-routes.json"
    if not path.exists():
        report.fail("locale_routes", "config/locale-routes.json is missing")
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data.get("routes")
    if not isinstance(rows, list):
        report.fail("locale_routes", "locale-routes.json has no routes list")
        return
    documents = {row.get("englishDocument") for row in rows}
    expected = {rel(path) for path in formula_files()}
    if documents != expected:
        report.fail(
            "locale_routes",
            "locale routes do not match English formula files",
            missing=sorted(expected - documents),
            extra=sorted(d for d in documents - expected if d),
        )
    required = [
        "website",
        "toolId",
        "englishDocument",
        "chineseDocument",
        "productionEnglishUrl",
        "productionChineseUrl",
        "englishHttpStatus",
        "chineseHttpStatus",
        "englishFinalUrl",
        "chineseFinalUrl",
        "englishPageLanguage",
        "chinesePageLanguage",
        "canonicalStatus",
        "hreflangStatus",
        "routeStatus",
        "verificationDate",
    ]
    chinese_docs = {rel(path) for path in chinese_formula_files()}
    seen_docs = set()
    for row in rows:
        for key in required:
            if key not in row:
                report.fail("locale_routes", f"locale row missing {key}", document=row.get("englishDocument"))
                break
        status = row.get("routeStatus")
        if status not in LOCALE_ROUTE_STATUS:
            report.fail("locale_routes", f"routeStatus {status} is not allowed", document=row.get("englishDocument"))
        document = row.get("englishDocument")
        if document in seen_docs:
            report.fail("locale_routes", f"duplicate locale row for {document}")
        seen_docs.add(document)
        companion = row.get("chineseDocument")
        if companion:
            if companion not in chinese_docs:
                report.fail("locale_routes", f"{companion} is not a Chinese file in the repo")
            elif row.get("routeStatus") == "VERIFIED" and row.get("chineseHttpStatus") != 200:
                report.fail("locale_routes", f"{document} is VERIFIED but chineseHttpStatus is not 200")
        if row.get("routeStatus") == "VERIFIED":
            final = str(row.get("chineseFinalUrl") or "")
            if url_is_site_root(final) or is_localized_homepage(final):
                report.fail("locale_routes", f"{document} Chinese final URL is a homepage")
            if not row.get("englishPageLanguage") or not row.get("chinesePageLanguage"):
                report.fail("locale_routes", f"{document} VERIFIED row has no expected language")
        if row.get("routeStatus") == "NOT_SUPPORTED" and row.get("chineseHttpStatus") == 200 and str(row.get("chinesePageLanguage") or "").lower().startswith("zh"):
            report.fail("locale_routes", f"{document} NOT_SUPPORTED row is recorded as a published Chinese page")


def first_h1(path: Path) -> str:
    titles = h1_titles(path.read_text(encoding="utf-8"))
    return titles[0] if titles else ""


def audit_indexes(report: Report, root: Path) -> None:
    """Compare both index files with formula files and FORMULA_VERIFICATION.json.

    The two JSON files are not treated as proof of each other. Counts are
    recomputed from the files under ``root``. Chinese companions are not
    English topics.
    """
    topic_path = root / "indexes" / "topics.json"
    verify_path = root / "indexes" / "verification-index.json"
    source_path = root / "reports" / "FORMULA_VERIFICATION.json"
    for path in (topic_path, verify_path, source_path):
        if not path.is_file():
            report.fail("indexes", f"missing {path.relative_to(root).as_posix()}")
            return
    topics = json.loads(topic_path.read_text(encoding="utf-8"))
    verification_index = json.loads(verify_path.read_text(encoding="utf-8"))
    source = json.loads(source_path.read_text(encoding="utf-8"))
    records = source.get("topics")
    if not isinstance(records, list):
        report.fail("indexes", "FORMULA_VERIFICATION.json has no topics list")
        return
    by_doc: dict[str, dict] = {}
    for record in records:
        document = record.get("document")
        if not document or document in by_doc:
            report.fail("indexes", f"verification source document is empty or duplicated: {document!r}")
            continue
        by_doc[document] = record

    english = formula_files(root)
    chinese = chinese_formula_files(root)
    english_docs = {path.relative_to(root).as_posix() for path in english}
    if english_docs & {path.relative_to(root).as_posix() for path in chinese}:
        report.fail("indexes", "a Chinese companion was counted as an English topic")

    def require_count(payload: dict, key: str, actual: int, label: str) -> None:
        if payload.get(key) != actual:
            report.fail("indexes", f"{label} {key} is {payload.get(key)}, recomputed {actual}")

    inventory_path = root / "reports" / "GATE1_TOOL_INVENTORY.json"
    inventory = None
    if not inventory_path.is_file():
        report.fail("indexes", "missing reports/GATE1_TOOL_INVENTORY.json")
    else:
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    require_count(topics, "englishFormulaCount", len(english), "topics index")
    require_count(topics, "chineseFormulaCount", len(chinese), "topics index")
    pairs = {(record.get("website"), record.get("toolId")) for record in by_doc.values()}
    require_count(topics, "uniqueSiteToolPairs", len(pairs), "topics index")
    if inventory is not None:
        _check_inventory_summary(report, topics, by_doc, english_docs, inventory)
    topic_rows = topics.get("topics")
    if not isinstance(topic_rows, list):
        report.fail("indexes", "topics index has no topics list")
        topic_rows = []
    topic_docs = [row.get("document") for row in topic_rows]
    if any(not doc for doc in topic_docs):
        report.fail("indexes", "topics index has an empty document key")
    if len(topic_docs) != len(set(topic_docs)):
        report.fail("indexes", "topics index repeats a document key")
    if set(topic_docs) != english_docs:
        report.fail(
            "indexes",
            "topics index documents do not match English formula files",
            missing=sorted(english_docs - set(topic_docs)),
            extra=sorted(doc for doc in set(topic_docs) - english_docs if doc),
        )
    for row in topic_rows:
        document = row.get("document")
        if not document:
            continue
        path = root / document
        if not path.is_file():
            report.fail("indexes", f"topics index document is not a file: {document}")
            continue
        if row.get("title") != first_h1(path):
            report.fail("indexes", f"{document} title does not match its H1", index=row.get("title"), h1=first_h1(path))
        record = by_doc.get(document)
        if record is None:
            report.fail("indexes", f"{document} is missing from FORMULA_VERIFICATION.json")
            continue
        for key in ("toolId", "productionUrl", "calculationStatus", "standardsStatus"):
            if row.get(key) != record.get(key):
                report.fail("indexes", f"{document} {key} does not match the verification record")
        _check_row_identity(report, document, row, record, inventory)
        companion = path.with_name(path.name.replace(".md", ".zh-CN.md"))
        expected_companion = companion.relative_to(root).as_posix() if companion.is_file() else None
        recorded_companion = row.get("chineseDocument")
        if recorded_companion != expected_companion:
            report.fail("indexes", f"{document} chineseDocument does not match the companion on disk")
        if recorded_companion and not (root / recorded_companion).is_file():
            report.fail("indexes", f"{document} chineseDocument does not exist: {recorded_companion}")
        _require_evidence(report, document, record, record)

    verify_rows = verification_index.get("topics")
    if not isinstance(verify_rows, list):
        report.fail("indexes", "verification index has no topics list")
        verify_rows = []
    verify_docs = [row.get("document") for row in verify_rows]
    if any(not doc for doc in verify_docs):
        report.fail("indexes", "verification index has an empty document key")
    if len(verify_docs) != len(set(verify_docs)):
        report.fail("indexes", "verification index repeats a document key")
    if set(verify_docs) != english_docs:
        report.fail("indexes", "verification index documents do not match English formula files")
    calculation_verified = sum(1 for record in by_doc.values() if record.get("calculationStatus") == "VERIFIED")
    calculation_review = sum(1 for record in by_doc.values() if record.get("calculationStatus") == "REVIEW_REQUIRED")
    standards_verified = sum(1 for record in by_doc.values() if record.get("standardsStatus") == "VERIFIED")
    standards_pending = sum(1 for record in by_doc.values() if record.get("standardsStatus") == "PENDING")
    standards_na = sum(1 for record in by_doc.values() if record.get("standardsStatus") == "NOT_APPLICABLE")
    require_count(verification_index, "englishFormulaCount", len(english), "verification index")
    require_count(verification_index, "calculationVerified", calculation_verified, "verification index")
    require_count(verification_index, "calculationReviewRequired", calculation_review, "verification index")
    require_count(verification_index, "standardsVerified", standards_verified, "verification index")
    require_count(verification_index, "standardsPending", standards_pending, "verification index")
    require_count(verification_index, "standardsNotApplicable", standards_na, "verification index")
    for row in verify_rows:
        document = row.get("document")
        if not document or not (root / document).is_file():
            report.fail("indexes", f"verification index document is not a file: {document}")
            continue
        record = by_doc.get(document)
        if record is None:
            report.fail("indexes", f"{document} is in the verification index without a source record")
            continue
        for key in (
            "website",
            "toolId",
            "calculationStatus",
            "standardsStatus",
            "sourceEvidence",
            "exampleResult",
            "standardsEvidence",
            "standardsCheckedDate",
        ):
            if row.get(key) != record.get(key):
                report.fail("indexes", f"verification index {document} {key} does not match the source record")
        _require_evidence(report, document, record, row)
        site = document.split("/", 1)[0]
        if row.get("website") != site or record.get("website") != site:
            report.fail("indexes", f"{document} website does not match its site directory")


def _check_inventory_summary(report: Report, topics: dict, by_doc: dict, english_docs: set[str], inventory: dict) -> None:
    """Recompute inventory totals from the inventory file and the source records."""
    tools = inventory.get("tools")
    if not isinstance(tools, list):
        report.fail("indexes", "inventory has no tools list")
        return
    urls = {}
    for tool in tools:
        url = str(tool.get("ProductionURL") or "").rstrip("/")
        if url:
            urls.setdefault(url, []).append(tool)
    published = set()
    tool_ids = set()
    for document, record in by_doc.items():
        if document not in english_docs:
            continue
        tool_ids.add(record.get("toolId"))
        if record.get("productionUrl"):
            published.add(str(record["productionUrl"]).rstrip("/"))
    overlap = {url for url in published if url in urls}
    total = len(tools)
    require = {
        "distinctToolIdStrings": len(tool_ids),
        "inventoryTools": total,
        "publishedInventoryTools": len(overlap),
        "inventoryToolsWithoutTopic": total - len(overlap),
    }
    for key, actual in require.items():
        if topics.get(key) != actual:
            report.fail("indexes", f"topics index {key} is {topics.get(key)}, recomputed {actual}")


def _check_row_identity(report: Report, document: str, row: dict, record: dict, inventory: dict | None) -> None:
    """website follows the file's site directory. inventoryToolId is an inventory key, not toolId."""
    site = document.split("/", 1)[0]
    if row.get("website") != site or record.get("website") != site:
        report.fail("indexes", f"{document} website does not match its site directory {site}")
    if site not in SITES or inventory is None:
        if site not in SITES:
            report.fail("indexes", f"{document} website {site} is not a site in this repo")
        return
    known_sites = set((inventory.get("domainsAssumed") or {})) | set((inventory.get("countsByWebsite") or {}))
    if site not in known_sites:
        report.fail("indexes", f"{document} website {site} is not in the tool inventory")
    expected = _inventory_tool_id(inventory, site, row.get("productionUrl") or record.get("productionUrl"))
    if row.get("inventoryToolId") != expected:
        report.fail(
            "indexes",
            f"{document} inventoryToolId does not match the inventory row for its production URL",
            recorded=row.get("inventoryToolId"),
            expected=expected,
        )


def _inventory_tool_id(inventory: dict, website: str, production_url: str | None) -> str | None:
    if not production_url:
        return None
    target = str(production_url).rstrip("/")
    for tool in inventory.get("tools") or []:
        url = str(tool.get("ProductionURL") or "").rstrip("/")
        if tool.get("Website") == website and url == target:
            return tool.get("ToolID")
    return None


def _require_evidence(report: Report, document: str, record: dict, row: dict) -> None:
    if record.get("calculationStatus") == "VERIFIED" and not (row.get("sourceEvidence") or row.get("exampleResult")):
        report.fail("indexes", f"{document} is calculation VERIFIED without sourceEvidence or exampleResult")
    if record.get("standardsStatus") == "VERIFIED" and not (row.get("standardsEvidence") and row.get("standardsCheckedDate")):
        report.fail("indexes", f"{document} is standards VERIFIED without evidence and a checked date")


def check_indexes(report: Report) -> None:
    audit_indexes(report, ROOT)


def url_is_site_root(url: str) -> bool:
    path = urlparse(url).path or "/"
    return path in {"", "/"}


def is_localized_homepage(url: str) -> bool:
    """Site root or a language-only homepage such as /zh/ or /zh-CN/."""
    parts = [part for part in (urlparse(url).path or "/").split("/") if part]
    if not parts:
        return True
    return len(parts) == 1 and parts[0].casefold() in LOCALE_ROOTS


def tool_identity(url: str) -> str:
    parts = [
        part
        for part in (urlparse(url).path or "").split("/")
        if part and part.casefold() not in LOCALE_ROOTS
    ]
    return "/".join(parts).casefold()


def same_tool(left: str, right: str) -> bool:
    identity = tool_identity(left)
    return bool(identity) and identity == tool_identity(right)


def language_matches(expected: str | None, actual: str | None) -> bool:
    if not expected or not actual:
        return False
    left = expected.strip().lower().replace("_", "-")
    right = actual.strip().lower().replace("_", "-")
    if left == right:
        return True
    left_primary = left.split("-", 1)[0]
    right_primary = right.split("-", 1)[0]
    if left_primary != right_primary:
        return False
    if "-" in left and "-" in right:
        return left == right
    return True


def primary_content_language(header: str | None) -> str | None:
    if not header:
        return None
    token = header.split(",", 1)[0].strip().split(";", 1)[0].strip()
    return token or None


def canonical_hrefs(html: str) -> list[str]:
    found = []
    for tag in re.findall(r"<link\b[^>]*>", html or "", re.I):
        if re.search(r"rel=[\"']canonical[\"']", tag, re.I):
            match = re.search(r"href=[\"']([^\"']+)", tag, re.I)
            if match:
                found.append(match.group(1))
    return found


def canonical_href(html: str) -> str | None:
    found = canonical_hrefs(html)
    return found[0] if found else None


def controlled_url_key(url: str) -> tuple[str, str] | None:
    """Host and path after the allowed alias rules.

    Allowed differences are www versus apex, http versus https, the default
    port, and a trailing slash. A foreign host is a different key.
    """
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return None
    host = parsed.hostname.lower()
    if host.startswith("www."):
        host = host[4:]
    # Omitted, 80, and 443 are the same default port. Any other port must match exactly.
    port = None if parsed.port in {None, 80, 443} else parsed.port
    path = parsed.path or "/"
    if path != "/":
        path = path.rstrip("/")
    return host, port, path.casefold()


def same_controlled_target(left: str, right: str) -> bool:
    key = controlled_url_key(left)
    return key is not None and key == controlled_url_key(right)


def looks_like_error_page(url: str, html: str) -> bool:
    path = urlparse(url).path.lower()
    if path.rstrip("/").endswith("/404") or path == "/404":
        return True
    title = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    if not title:
        return False
    label = re.sub(r"\s+", " ", title.group(1)).lower()
    return "page not found" in label or label.strip().startswith("404")


class RedirectRecorder(urllib.request.HTTPRedirectHandler):
    def __init__(self) -> None:
        super().__init__()
        self.chain: list[dict] = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.chain.append({"status": code, "url": urljoin(req.full_url, newurl)})
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _page_fields(html: str, headers) -> dict:
    lang = re.search(r"<html[^>]*\blang=[\"']([^\"']+)", html or "", re.I)
    content_language = None
    if headers is not None:
        content_language = headers.get("Content-Language")
    hrefs = canonical_hrefs(html)
    return {
        "pageLanguage": lang.group(1) if lang else None,
        "contentLanguage": content_language,
        "canonical": hrefs[0] if hrefs else None,
        "canonicals": hrefs,
    }


def fetch_url(url: str, timeout: float, retries: int, kind: str, sleeper=time.sleep) -> dict:
    """Request ``url`` up to ``retries`` times.

    HTTP 500–599 is retried and then classified ``HTTP_SERVER_ERROR``.
    403 and 429 are inconclusive on the first response. DNS, TLS, timeout,
    and other transport errors use the same retry budget and stay inconclusive.
    """
    last_error = ""
    for attempt in range(1, retries + 1):
        recorder = RedirectRecorder()
        opener = urllib.request.build_opener(recorder)
        request = urllib.request.Request(
            url,
            headers={"User-Agent": USER_AGENT, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"},
        )
        try:
            with opener.open(request, timeout=timeout) as response:
                html = response.read(65536).decode("utf-8", "replace")
                status = response.getcode()
                final = response.geturl()
                item = {
                    "url": url,
                    "kind": kind,
                    "status": status,
                    "finalUrl": final,
                    "redirects": recorder.chain,
                    "attempts": attempt,
                    **_page_fields(html, response.headers),
                }
                if is_http_server_error(status):
                    last_error = f"HTTP {status}"
                    if attempt < retries:
                        sleeper(2 ** (attempt - 1))
                        continue
                    item["class"] = "HTTP_SERVER_ERROR"
                    item["error"] = last_error
                    return item
                if status in HARD_HTTP:
                    item["class"] = "hard_404"
                    return item
                if status in INCONCLUSIVE_HTTP:
                    item["class"] = "inconclusive"
                    item["error"] = f"HTTP {status}"
                    return item
                if kind == "tool" and url_is_site_root(final):
                    item["class"] = "homepage"
                    item["error"] = "final URL is the site homepage"
                    return item
                if kind in {"tool", "locale"} and looks_like_error_page(final, html):
                    item["class"] = "error_page"
                    item["error"] = "final page is an error page"
                    return item
                if "/zh/" in urlparse(url).path and item["pageLanguage"] and not str(item["pageLanguage"]).lower().startswith("zh"):
                    item["class"] = "wrong_language"
                    item["error"] = f"page language is {item['pageLanguage']}"
                    return item
                if status and status >= 400:
                    item["class"] = "inconclusive"
                    item["error"] = f"HTTP {status}"
                    return item
                item["class"] = "ok"
                return item
        except urllib.error.HTTPError as exc:
            status = exc.code
            body = exc.read(65536).decode("utf-8", "replace") if exc.fp else ""
            item = {
                "url": url,
                "kind": kind,
                "status": status,
                "finalUrl": exc.geturl(),
                "redirects": recorder.chain,
                "attempts": attempt,
                "error": f"HTTP {status}",
                **_page_fields(body, exc.headers),
            }
            if is_http_server_error(status):
                last_error = f"HTTP {status}"
                if attempt < retries:
                    sleeper(2 ** (attempt - 1))
                    continue
                item["class"] = "HTTP_SERVER_ERROR"
                return item
            if status in HARD_HTTP or looks_like_error_page(exc.geturl(), body):
                item["class"] = "hard_404"
                return item
            item["class"] = "inconclusive"
            return item
        except Exception as exc:  # noqa: BLE001 — classified for the report, not hidden
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt < retries:
                sleeper(2 ** (attempt - 1))
                continue
    return {
        "url": url,
        "kind": kind,
        "class": "inconclusive",
        "attempts": retries,
        "status": None,
        "finalUrl": None,
        "pageLanguage": None,
        "error": last_error or "network error",
    }


def assess_locale_page(requested: str, expected_language: str | None, item: dict) -> str:
    """Decide whether one fetched URL still supports a VERIFIED locale row.

    HTTP 200 by itself is not enough. Expected language comes from the caller,
    which reads it from that row rather than from a global language.
    """
    if item.get("class") == "HTTP_SERVER_ERROR" or is_http_server_error(item.get("status")):
        return "HTTP_SERVER_ERROR"
    if item.get("class") == "inconclusive" or item.get("status") in INCONCLUSIVE_HTTP:
        return "inconclusive"
    if item.get("class") == "hard_404" or item.get("status") in HARD_HTTP:
        return "hard_404"
    if item.get("class") == "error_page":
        return "error_page"
    final = item.get("finalUrl") or ""
    if not final or is_localized_homepage(final) or url_is_site_root(final):
        return "LOCALIZED_HOMEPAGE_FALLBACK"
    if not same_tool(requested, final):
        return "WRONG_TOOL"
    if not language_matches(expected_language, item.get("pageLanguage")):
        return "WRONG_LANGUAGE"
    header_language = primary_content_language(item.get("contentLanguage"))
    if header_language and not language_matches(expected_language, header_language):
        return "WRONG_LANGUAGE"
    canonical_class = _canonical_class(final, item)
    if canonical_class != "ok":
        return canonical_class
    if item.get("status") != 200:
        return "inconclusive"
    return "ok"


def _canonical_class(final: str, item: dict) -> str:
    """Compare canonical tags with the final URL, not with a language-stripped path.

    VERIFIED rows declare canonicalStatus MATCH. A missing tag is NOT_PRESENT.
    The same tool on the English route is not a match for a Chinese final URL.
    Identical repeated tags are allowed and marked for a warning. Conflicting
    tags fail. www, https, the default port, and a trailing slash are aliases.
    """
    raw = item.get("canonicals")
    if not isinstance(raw, list):
        raw = [item["canonical"]] if item.get("canonical") else []
    resolved = [urljoin(final, href) for href in raw if href]
    if not resolved:
        return "NOT_PRESENT"
    keys = []
    for url in resolved:
        key = controlled_url_key(url)
        if key not in keys:
            keys.append(key)
    if len(keys) > 1:
        return "CONFLICTING_CANONICAL"
    if len(resolved) > 1:
        item["duplicateCanonical"] = True
    target = resolved[0]
    if same_controlled_target(final, target):
        return "ok"
    final_key = controlled_url_key(final)
    target_key = controlled_url_key(target)
    if (
        final_key
        and target_key
        and final_key[0] == target_key[0]
        and same_tool(final, target)
    ):
        return "CANONICAL_NOT_LANGUAGE_ROUTE"
    return "WRONG_CANONICAL"


def locale_route_rows(root: Path | None = None) -> list[dict]:
    base = ROOT if root is None else root
    path = base / "config" / "locale-routes.json"
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data.get("routes")
    return rows if isinstance(rows, list) else []


def plan_locale_checks(rows: list[dict]) -> dict:
    """Map every VERIFIED row to its English and Chinese URLs.

    Requests are deduplicated by URL. Shared tool URLs stay attached to every
    document and tool id. NOT_SUPPORTED rows are counted separately and are
    not treated as published Chinese pages.
    """
    verified_rows = [row for row in rows if row.get("routeStatus") == "VERIFIED"]
    not_supported_rows = [row for row in rows if row.get("routeStatus") == "NOT_SUPPORTED"]
    targets: list[dict] = []
    for row in verified_rows:
        targets.append(
            {
                "document": row.get("englishDocument"),
                "toolId": row.get("toolId"),
                "side": "en",
                "url": row.get("productionEnglishUrl"),
                "expectedLanguage": row.get("englishPageLanguage"),
            }
        )
        targets.append(
            {
                "document": row.get("englishDocument"),
                "toolId": row.get("toolId"),
                "side": "zh",
                "url": row.get("productionChineseUrl"),
                "expectedLanguage": row.get("chinesePageLanguage"),
            }
        )
    unique_urls: list[str] = []
    seen: set[str] = set()
    for target in targets:
        url = target.get("url")
        if url and url not in seen:
            seen.add(url)
            unique_urls.append(url)
    return {
        "verifiedRows": verified_rows,
        "notSupportedRows": not_supported_rows,
        "targets": targets,
        "uniqueUrls": unique_urls,
    }


def tool_urls() -> list[str]:
    found: list[str] = []
    seen: set[str] = set()

    def add(url: str) -> None:
        cleaned = url.rstrip(").,]")
        if cleaned not in seen:
            seen.add(cleaned)
            found.append(cleaned)

    for path in formula_files() + chinese_formula_files():
        for url in online_calculator_urls(path.read_text(encoding="utf-8")):
            add(url)
    root = (ROOT / "README.md").read_text(encoding="utf-8")
    domain = section(root, "2. Domain entry points (11 sites)")
    for url in re.findall(r"https?://[^\s)<>|]+", domain):
        add(url)
    return found


def domain_urls() -> set[str]:
    root = (ROOT / "README.md").read_text(encoding="utf-8")
    domain = section(root, "2. Domain entry points (11 sites)")
    return {url.rstrip(").,]") for url in re.findall(r"https?://[^\s)<>|]+", domain)}


def standards_urls() -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    headings = ("Reference Standards", "参考标准")
    for path in formula_files() + chinese_formula_files():
        text = path.read_text(encoding="utf-8")
        body = ""
        for heading in headings:
            body += "\n" + section(text, heading)
        for url in re.findall(r"https?://[^\s)<>]+", body):
            cleaned = url.rstrip(").,]")
            host = urlparse(cleaned).netloc
            if any(site in host for site in ("engineerlab", "pcdog", "aimarktool", "diycalclab", "privacyfilelab", "datafilelab")):
                continue
            if cleaned not in seen:
                seen.add(cleaned)
                found.append(cleaned)
    return found


def classify_results(report: Report, results: list[dict]) -> None:
    for item in results:
        kind = item["class"]
        if kind == "hard_404":
            report.fail("tool_urls", f"hard {item.get('status')} for {item['url']}", **item)
        elif kind == "HTTP_SERVER_ERROR":
            report.fail("tool_urls", f"persistent {item.get('status')} for {item['url']}", **item)
        elif kind == "homepage":
            report.fail("tool_urls", f"tool URL landed on the homepage: {item['url']}", **item)
        elif kind == "error_page":
            report.fail("tool_urls", f"tool URL landed on an error page: {item['url']}", **item)
        elif kind == "wrong_language":
            report.fail("tool_urls", f"wrong language for {item['url']}: {item.get('error')}", **item)
        elif kind in {"LOCALIZED_HOMEPAGE_FALLBACK", "WRONG_TOOL", "WRONG_CANONICAL", "WRONG_LANGUAGE"}:
            report.fail("locale_routes", f"{kind} for {item['url']}", **item)
        elif kind == "inconclusive":
            report.warn("tool_urls", f"INCONCLUSIVE for {item['url']}: {item.get('error')}", **item)
        elif kind != "ok":
            report.warn("tool_urls", f"unclassified result for {item['url']}", **item)


def probe_status(url: str, retries: int = 3, timeout: float = 5.0, sleeper=time.sleep) -> tuple[dict, Report, int]:
    """Fetch one URL and apply the same failure rules as the CLI."""
    item = fetch_url(url, timeout, retries, "tool", sleeper=sleeper)
    report = Report()
    classify_results(report, [item])
    return item, report, (1 if report.failures else 0)


def probe_locale(url: str, expected_language: str, retries: int = 3, timeout: float = 5.0, sleeper=time.sleep) -> tuple[dict, str, Report, int]:
    """Fetch one URL and apply the VERIFIED-route language, canonical, and tool checks."""
    item = fetch_url(url, timeout, retries, "tool", sleeper=sleeper)
    locale_class = assess_locale_page(url, expected_language, item)
    judged = dict(item)
    judged["class"] = locale_class
    report = Report()
    if locale_class == "inconclusive":
        report.warn("locale_routes", f"INCONCLUSIVE for {url}: {item.get('error')}", **judged)
    elif locale_class != "ok":
        report.fail("locale_routes", f"{locale_class} for {url}", **judged)
    elif item.get("duplicateCanonical"):
        report.warn("locale_routes", f"duplicate canonical for {url}", **judged)
    return item, locale_class, report, (1 if report.failures else 0)


def apply_locale_results(report: Report, fetched: dict[str, dict], plan: dict) -> list[dict]:
    """Judge every VERIFIED row from URL results. Shared URLs are fetched once."""
    judged: list[dict] = []
    for target in plan["targets"]:
        url = target.get("url")
        item = fetched.get(url) if url else None
        if item is None:
            report.fail("locale_routes", f"{target.get('document')} has no fetch for {url}")
            judged.append({**target, "localeClass": "missing_fetch"})
            continue
        if not target.get("expectedLanguage"):
            report.fail("locale_routes", f"{target.get('document')} VERIFIED row has no expected language")
            locale_class = "missing_language"
        else:
            locale_class = assess_locale_page(url, target.get("expectedLanguage"), item)
        row_result = {
            **target,
            "localeClass": locale_class,
            "status": item.get("status"),
            "finalUrl": item.get("finalUrl"),
            "pageLanguage": item.get("pageLanguage"),
            "contentLanguage": item.get("contentLanguage"),
            "canonical": item.get("canonical"),
            "toolIdentity": tool_identity(item.get("finalUrl") or ""),
            "attempts": item.get("attempts"),
        }
        judged.append(row_result)
        if locale_class == "inconclusive":
            report.warn(
                "locale_routes",
                f"INCONCLUSIVE {target.get('side')} {url} for {target.get('document')}: {item.get('error')}",
                **row_result,
            )
        elif locale_class != "ok":
            report.fail(
                "locale_routes",
                f"{locale_class} {target.get('side')} {url} for {target.get('document')}",
                **row_result,
            )
        elif item.get("duplicateCanonical"):
            report.warn(
                "locale_routes",
                f"duplicate canonical {target.get('side')} {url} for {target.get('document')}",
                **row_result,
            )
    report.stats["localeVerifiedRows"] = len(plan["verifiedRows"])
    report.stats["localeVerifiedUniqueUrls"] = len(plan["uniqueUrls"])
    report.stats["localeNotSupportedRows"] = len(plan["notSupportedRows"])
    report.stats["localeTargets"] = len(plan["targets"])
    report.stats["localeLivePass"] = sum(1 for row in judged if row.get("localeClass") == "ok")
    report.stats["localeLiveInconclusive"] = sum(1 for row in judged if row.get("localeClass") == "inconclusive")
    return judged


def check_urls(
    report: Report,
    timeout: float,
    retries: int,
    include_standards: bool,
    *,
    locale_rows: list[dict] | None = None,
    only_urls: list[tuple[str, str]] | None = None,
) -> list[dict]:
    if only_urls is None:
        homes = domain_urls()
        urls = [(url, "domain" if url in homes else "tool") for url in tool_urls()]
        plan = plan_locale_checks(locale_route_rows() if locale_rows is None else locale_rows)
    else:
        urls = list(only_urls)
        plan = plan_locale_checks([] if locale_rows is None else locale_rows)
    for row in plan["notSupportedRows"]:
        if row.get("routeStatus") == "VERIFIED":
            report.fail("locale_routes", f"{row.get('englishDocument')} NOT_SUPPORTED row is marked VERIFIED")
    known = {url for url, _kind in urls}
    for url in plan["uniqueUrls"]:
        if url not in known:
            known.add(url)
            urls.append((url, "locale"))
    if include_standards:
        urls.extend((url, "standard") for url in standards_urls())
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(fetch_url, url, timeout, retries, kind) for url, kind in urls]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: (item.get("kind", ""), item["url"]))
    by_url = {item["url"]: item for item in results}
    # Standards fetches are evidence. They do not fail the documentation gate.
    tool_results = [item for item in results if item.get("kind") != "standard"]
    classify_results(report, [item for item in tool_results if item.get("kind") != "locale"])
    for item in results:
        if item.get("kind") == "standard" and item["class"] != "ok":
            report.warn("standards_urls", f"INCONCLUSIVE standard URL {item['url']}: {item.get('error') or item['class']}", **item)
    locale_judged = apply_locale_results(report, by_url, plan)
    report.stats["localeJudged"] = locale_judged
    return results


def summary_counts(report: Report, files: list[Path], url_results: list[dict]) -> dict:
    classes = Counter(item.get("class") for item in url_results if item.get("kind") != "standard")
    external = [item for item in url_results if item.get("kind") == "standard"]
    formula_errors = sum(
        1
        for item in report.failures
        if item["check"] in {"math_fences", "code_fences", "tables", "empty_headings", "empty_content"}
    )
    language_errors = sum(1 for item in report.failures if item["check"] in {"language_pair", "language_marker"})
    hard_404 = sum(1 for item in url_results if item.get("class") == "hard_404" and item.get("kind") != "standard")
    hard_5xx = sum(
        1
        for item in url_results
        if item.get("kind") != "standard" and item.get("class") == "HTTP_SERVER_ERROR"
    )
    inconclusive = sum(
        1
        for item in url_results
        if item.get("class") in {"inconclusive", "network_error"} or (item.get("kind") == "standard" and item.get("class") != "ok")
    )
    return {
        "totalFiles": len(files),
        "englishFormulaCount": len(formula_files()),
        "chineseFormulaCount": len(chinese_formula_files()),
        "internalLinkChecks": report.stats.get("internalLinkChecks", 0),
        "externalUrlChecks": len(external),
        "toolUrlChecks": len([item for item in url_results if item.get("kind") != "standard"]),
        "http404Or410": hard_404,
        "http5xx": hard_5xx,
        "inconclusive": inconclusive,
        "formulaFormatErrors": formula_errors,
        "languagePairErrors": language_errors,
        "standardsCitationsPending": report.stats.get("standardsPending", 0),
        "totalFailures": len(report.failures),
        "okUrlChecks": classes.get("ok", 0),
        "localeVerifiedRows": report.stats.get("localeVerifiedRows", 0),
        "localeVerifiedUniqueUrls": report.stats.get("localeVerifiedUniqueUrls", 0),
        "localeNotSupportedRows": report.stats.get("localeNotSupportedRows", 0),
        "localeTargets": report.stats.get("localeTargets", 0),
        "localeLivePass": report.stats.get("localeLivePass", 0),
        "localeLiveInconclusive": report.stats.get("localeLiveInconclusive", 0),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Calculator documentation. Read-only.")
    parser.add_argument("--skip-urls", action="store_true", help="Skip live tool URL requests")
    parser.add_argument("--external-standards", action="store_true", help="Also request cited external standards URLs")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--json-out", type=Path, help="Write the JSON report to this path")
    args = parser.parse_args()

    report = Report()
    files = markdown_files()
    if not (ROOT / "README.md").exists():
        report.fail("structure", "root README.md is missing")
    for site in SITES:
        if not (ROOT / site).is_dir():
            report.fail("structure", f"missing site directory {site}")

    check_titles(report, files)
    check_links(report, files)
    check_math(report, files)
    check_markdown_quality(report, files)
    check_verification(report)
    check_toc(report)
    check_secrets(report)
    check_language_pairs(report)
    check_locale_config(report)
    check_indexes(report)
    if args.skip_urls:
        plan = plan_locale_checks(locale_route_rows())
        report.stats["localeVerifiedRows"] = len(plan["verifiedRows"])
        report.stats["localeVerifiedUniqueUrls"] = len(plan["uniqueUrls"])
        report.stats["localeNotSupportedRows"] = len(plan["notSupportedRows"])
        report.stats["localeTargets"] = len(plan["targets"])
    url_results = [] if args.skip_urls else check_urls(report, args.timeout, args.retries, args.external_standards)
    counts = summary_counts(report, files, url_results)

    payload = {
        "summary": counts,
        "failures": report.failures,
        "warnings": report.warnings,
        "failureCount": len(report.failures),
        "warningCount": len(report.warnings),
        "formulaCount": len(formula_files()),
        "chineseFormulaCount": len(chinese_formula_files()),
        "urlChecks": url_results,
        "localeChecks": report.stats.get("localeJudged", []),
        "urlsSkipped": args.skip_urls,
        "externalStandardsChecked": args.external_standards,
    }
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")
    print(text)
    print(
        f"\nfailures={payload['failureCount']} warnings={payload['warningCount']} "
        f"formulas={payload['formulaCount']} chinese={payload['chineseFormulaCount']} "
        f"localeRows={counts.get('localeVerifiedRows', 0)} "
        f"localeUniqueUrls={counts.get('localeVerifiedUniqueUrls', 0)} "
        f"localeNotSupported={counts.get('localeNotSupportedRows', 0)} "
        f"localeLivePass={counts.get('localeLivePass', 0)} "
        f"localeLiveInconclusive={counts.get('localeLiveInconclusive', 0)}",
        file=sys.stderr,
    )
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
