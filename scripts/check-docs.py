#!/usr/bin/env python3
"""Read-only Markdown checks for this documentation repository.

Exit 0 when there is no hard failure. This script does not modify files
and does not touch product-site source.

Tool-page HTTP rules:

- 301 and 302 are acceptable when the final page is the tool page.
- 404 and 410 fail.
- 5xx after the retry budget fails.
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
RETRY_HTTP = {408, 500, 502, 503, 504}
HARD_HTTP = {404, 410}
INCONCLUSIVE_HTTP = {403, 429}
FIVE_XX = {500, 502, 503, 504}
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


def formula_files() -> list[Path]:
    found = []
    for site in SITES:
        folder = ROOT / site
        if not folder.is_dir():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.name != "README.md" and not is_locale_translation(path):
                found.append(path)
    return found


def chinese_formula_files() -> list[Path]:
    found = []
    for site in SITES:
        folder = ROOT / site
        if not folder.is_dir():
            continue
        found.extend(sorted(folder.glob("*.zh-CN.md")))
    return found


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
            if url_is_site_root(final):
                report.fail("locale_routes", f"{document} Chinese final URL is the site homepage")


def check_indexes(report: Report) -> None:
    topic_path = ROOT / "indexes" / "topics.json"
    verify_path = ROOT / "indexes" / "verification-index.json"
    if not topic_path.exists() or not verify_path.exists():
        report.fail("indexes", "indexes/topics.json and indexes/verification-index.json are required")
        return
    topics = json.loads(topic_path.read_text(encoding="utf-8"))
    verification = json.loads(verify_path.read_text(encoding="utf-8"))
    disk = {rel(path) for path in formula_files()}
    indexed = {item.get("document") for item in topics.get("topics", [])}
    if indexed != disk:
        report.fail("indexes", "topics index does not match English formula files")
    if topics.get("englishFormulaCount") != len(formula_files()):
        report.fail("indexes", "topics index englishFormulaCount is stale")
    if topics.get("chineseFormulaCount") != len(chinese_formula_files()):
        report.fail("indexes", "topics index chineseFormulaCount is stale")
    if verification.get("englishFormulaCount") != len(formula_files()):
        report.fail("indexes", "verification index count is stale")
    pending = verification.get("standardsPending")
    if pending != report.stats.get("standardsPending"):
        report.fail("indexes", f"verification index standardsPending {pending} does not match records")


def url_is_site_root(url: str) -> bool:
    path = urlparse(url).path or "/"
    return path in {"", "/"}


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


def fetch_url(url: str, timeout: float, retries: int, kind: str) -> dict:
    last_error = ""
    for attempt in range(1, retries + 1):
        recorder = RedirectRecorder()
        opener = urllib.request.build_opener(recorder)
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"})
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
                }
                lang = re.search(r"<html[^>]*\blang=[\"']([^\"']+)", html, re.I)
                item["pageLanguage"] = lang.group(1) if lang else None
                if status in HARD_HTTP:
                    item["class"] = "hard_404"
                    return item
                if status in FIVE_XX:
                    last_error = f"HTTP {status}"
                    if attempt < retries:
                        time.sleep(2 ** (attempt - 1))
                        continue
                    item["class"] = "hard_5xx"
                    item["error"] = last_error
                    return item
                if status in INCONCLUSIVE_HTTP:
                    item["class"] = "inconclusive"
                    item["error"] = f"HTTP {status}"
                    return item
                if kind == "tool" and url_is_site_root(final):
                    item["class"] = "homepage"
                    item["error"] = "final URL is the site homepage"
                    return item
                if kind == "tool" and looks_like_error_page(final, html):
                    item["class"] = "error_page"
                    item["error"] = "final page is an error page"
                    return item
                if "/zh/" in urlparse(url).path and item["pageLanguage"] and not item["pageLanguage"].lower().startswith("zh"):
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
            }
            if status in HARD_HTTP or looks_like_error_page(exc.geturl(), body):
                item["class"] = "hard_404"
                return item
            if status in FIVE_XX:
                last_error = f"HTTP {status}"
                if attempt < retries:
                    time.sleep(2 ** (attempt - 1))
                    continue
                item["class"] = "hard_5xx"
                return item
            if status in INCONCLUSIVE_HTTP or status in RETRY_HTTP:
                item["class"] = "inconclusive"
                return item
            item["class"] = "inconclusive"
            return item
        except Exception as exc:  # noqa: BLE001 — classified for the report, not hidden
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt < retries:
                time.sleep(2 ** (attempt - 1))
                continue
    return {
        "url": url,
        "kind": kind,
        "class": "inconclusive",
        "attempts": retries,
        "error": last_error or "network error",
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
        elif kind == "hard_5xx":
            report.fail("tool_urls", f"persistent {item.get('status')} for {item['url']}", **item)
        elif kind == "homepage":
            report.fail("tool_urls", f"tool URL landed on the homepage: {item['url']}", **item)
        elif kind == "error_page":
            report.fail("tool_urls", f"tool URL landed on an error page: {item['url']}", **item)
        elif kind == "wrong_language":
            report.fail("tool_urls", f"wrong language for {item['url']}: {item.get('error')}", **item)
        elif kind == "inconclusive":
            report.warn("tool_urls", f"INCONCLUSIVE for {item['url']}: {item.get('error')}", **item)
        elif kind != "ok":
            report.warn("tool_urls", f"unclassified result for {item['url']}", **item)


def check_urls(report: Report, timeout: float, retries: int, include_standards: bool) -> list[dict]:
    homes = domain_urls()
    urls = [(url, "domain" if url in homes else "tool") for url in tool_urls()]
    if include_standards:
        urls.extend((url, "standard") for url in standards_urls())
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(fetch_url, url, timeout, retries, kind) for url, kind in urls]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: (item.get("kind", ""), item["url"]))
    # Standards fetches are evidence. They do not fail the documentation gate.
    tool_results = [item for item in results if item.get("kind") != "standard"]
    classify_results(report, tool_results)
    for item in results:
        if item.get("kind") == "standard" and item["class"] != "ok":
            report.warn("standards_urls", f"INCONCLUSIVE standard URL {item['url']}: {item.get('error') or item['class']}", **item)
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
    hard_5xx = sum(1 for item in url_results if item.get("class") == "hard_5xx" and item.get("kind") != "standard")
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
        f"formulas={payload['formulaCount']} chinese={payload['chineseFormulaCount']}",
        file=sys.stderr,
    )
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
