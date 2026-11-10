#!/usr/bin/env python3
"""Read-only Markdown checks for this documentation repository.

Exit 0 when there is no hard failure. Network errors and non-404 HTTP
statuses are warnings. HTTP 404 and 410 on a tool URL are hard failures.
This script does not modify files and does not touch product-site source.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

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
SECRET_PATTERNS = [
    ("private_key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----")),
    ("github_token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b")),
    ("github_fine_grained", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("access_token_url", re.compile("x-access-" + r"token:[^\s@]+")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("stripe_live", re.compile(r"\bsk_live_[0-9a-zA-Z]{16,}\b")),
]
TRANSIENT_HTTP = {408, 429, 500, 502, 503, 504}
HARD_HTTP = {404, 410}
USER_AGENT = "CalculatorDocCheck/1.0 (+https://github.com/ddcodedog/Calculator)"


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
    body = section(text, "Verification")
    match = re.search(r"^\|\s*Status\s*\|\s*([A-Z_]+)\s*\|", body, re.M)
    return match.group(1) if match else None


def online_calculator_urls(text: str) -> list[str]:
    body = section(text, "Online Calculator")
    return re.findall(r"https?://[^\s)<>]+", body)


def markdown_links(text: str) -> list[str]:
    links = []
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
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


class Report:
    def __init__(self) -> None:
        self.failures: list[dict] = []
        self.warnings: list[dict] = []

    def fail(self, check: str, message: str, **extra: object) -> None:
        self.failures.append({"check": check, "message": message, **extra})

    def warn(self, check: str, message: str, **extra: object) -> None:
        self.warnings.append({"check": check, "message": message, **extra})


def check_titles(report: Report, files: list[Path]) -> None:
    seen: dict[str, str] = {}
    formula = {path.resolve() for path in formula_files()}
    for path in files:
        titles = h1_titles(path.read_text(encoding="utf-8"))
        if path.resolve() in formula and len(titles) != 1:
            report.fail("titles", f"{rel(path)} has {len(titles)} H1 headings; expected 1")
        for title in titles:
            key = title.casefold()
            if key in seen:
                report.fail("titles", f"duplicate H1 {title!r}", paths=[seen[key], rel(path)])
            else:
                seen[key] = rel(path)


def check_links(report: Report, files: list[Path]) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in markdown_links(text):
            if is_external(target) or target.startswith("#"):
                continue
            path_part, _, _fragment = target.partition("#")
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


def check_math(report: Report, files: list[Path]) -> None:
    del files
    for path in formula_files():
        raw = path.read_text(encoding="utf-8")
        text = strip_code_fences(raw)
        if text.count("```") % 2:
            report.fail("math_fences", f"{rel(path)} has an unclosed code fence")
        display = 0
        for line in text.splitlines():
            if line.strip() == "$$":
                display += 1
            elif line.count("$$") % 2:
                report.fail("math_fences", f"{rel(path)} has an odd $$ count on one line")
                break
        else:
            if display % 2:
                report.fail("math_fences", f"{rel(path)} has an unclosed $$ display block")
        if text.count(r"\(") != text.count(r"\)"):
            report.fail("math_fences", f"{rel(path)} has unbalanced \\( \\) math")


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

    for document, path in disks.items():
        text = path.read_text(encoding="utf-8")
        status = verification_status(text)
        recorded = by_doc.get(document, {}).get("status")
        if status is None:
            report.fail("verification_status", f"{document} has no Verification status row")
            continue
        if status != recorded:
            report.fail(
                "verification_status",
                f"{document} status {status} does not match JSON {recorded}",
            )
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


def fetch_url(url: str, timeout: float, retries: int) -> dict:
    last_error = ""
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                response.read(128)
                status = response.getcode()
                final = response.geturl()
                return {
                    "url": url,
                    "class": "ok",
                    "status": status,
                    "finalUrl": final,
                    "attempts": attempt,
                }
        except urllib.error.HTTPError as exc:
            if exc.code in HARD_HTTP:
                return {
                    "url": url,
                    "class": "hard_404",
                    "status": exc.code,
                    "finalUrl": exc.geturl(),
                    "attempts": attempt,
                }
            last_error = f"HTTP {exc.code}"
            if exc.code in TRANSIENT_HTTP and attempt < retries:
                time.sleep(2 ** (attempt - 1))
                continue
            return {
                "url": url,
                "class": "http_error",
                "status": exc.code,
                "finalUrl": exc.geturl(),
                "attempts": attempt,
                "error": last_error,
            }
        except Exception as exc:  # noqa: BLE001 — classified for the report, not hidden
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt < retries:
                time.sleep(2 ** (attempt - 1))
                continue
    return {"url": url, "class": "network_error", "attempts": retries, "error": last_error}


def tool_urls() -> list[str]:
    found: list[str] = []
    seen: set[str] = set()

    def add(url: str) -> None:
        cleaned = url.rstrip(").,]")
        if cleaned not in seen:
            seen.add(cleaned)
            found.append(cleaned)

    for path in formula_files():
        for url in online_calculator_urls(path.read_text(encoding="utf-8")):
            add(url)
    root = (ROOT / "README.md").read_text(encoding="utf-8")
    domain = section(root, "2. Domain entry points (11 sites)")
    for url in re.findall(r"https?://[^\s)<>|]+", domain):
        add(url)
    return found


def check_urls(report: Report, timeout: float, retries: int) -> list[dict]:
    urls = tool_urls()
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(fetch_url, url, timeout, retries) for url in urls]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: item["url"])
    for item in results:
        kind = item["class"]
        if kind == "hard_404":
            report.fail("tool_urls", f"hard {item['status']} for {item['url']}", **item)
        elif kind == "network_error":
            report.warn("tool_urls", f"network error for {item['url']}: {item.get('error')}", **item)
        elif kind == "http_error":
            report.warn("tool_urls", f"HTTP {item.get('status')} for {item['url']}", **item)
        elif item.get("status") and int(item["status"]) >= 400:
            report.warn("tool_urls", f"unexpected status {item['status']} for {item['url']}", **item)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Calculator documentation. Read-only.")
    parser.add_argument("--skip-urls", action="store_true", help="Skip live tool URL requests")
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
    check_verification(report)
    check_toc(report)
    check_secrets(report)
    url_results = [] if args.skip_urls else check_urls(report, args.timeout, args.retries)

    payload = {
        "failures": report.failures,
        "warnings": report.warnings,
        "failureCount": len(report.failures),
        "warningCount": len(report.warnings),
        "formulaCount": len(formula_files()),
        "urlChecks": url_results,
        "urlsSkipped": args.skip_urls,
    }
    text = json.dumps(payload, indent=2)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")
    print(text)
    print(
        f"\nfailures={payload['failureCount']} warnings={payload['warningCount']} formulas={payload['formulaCount']}",
        file=sys.stderr,
    )
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
