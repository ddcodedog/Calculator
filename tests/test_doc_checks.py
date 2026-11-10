"""Unit checks for documentation helpers. No network."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_checker():
    spec = importlib.util.spec_from_file_location("check_docs", ROOT / "scripts" / "check-docs.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DocCheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_checker()

    def test_math_blocks_match_for_every_chinese_companion(self):
        mismatches = []
        for path in self.mod.chinese_formula_files():
            english = path.with_name(path.name.replace(".zh-CN.md", ".md"))
            zh = self.mod.math_blocks(path.read_text(encoding="utf-8"))
            en = self.mod.math_blocks(english.read_text(encoding="utf-8"))
            if zh != en:
                mismatches.append(path.name)
        self.assertEqual(mismatches, [])

    def test_normalize_math_ignores_whitespace_only(self):
        self.assertEqual(self.mod.normalize_math("a + b"), self.mod.normalize_math("a+b"))
        self.assertNotEqual(self.mod.normalize_math("a - b"), self.mod.normalize_math("a+b"))

    def test_number_tokens_keep_sign_and_decimals(self):
        self.assertEqual(self.mod.number_tokens("remaining 17.60 dB and -4.60"), ["17.60", "-4.60"])

    def test_homepage_detector(self):
        self.assertTrue(self.mod.url_is_site_root("https://netengineerlab.com/"))
        self.assertTrue(self.mod.url_is_site_root("https://netengineerlab.com"))
        self.assertFalse(self.mod.url_is_site_root("https://netengineerlab.com/tools/fiber-loss/"))
        self.assertFalse(self.mod.url_is_site_root("https://netengineerlab.com/tools/stp-path-cost-calculator/zh/"))

    def test_error_page_detector(self):
        html = "<html><title>Page not found | Example</title></html>"
        self.assertTrue(self.mod.looks_like_error_page("https://example.com/missing", html))
        self.assertFalse(
            self.mod.looks_like_error_page(
                "https://netengineerlab.com/tools/fiber-loss/",
                "<html><title>Fiber Loss Calculator</title></html>",
            )
        )

    def test_status_split_counts_match_the_json(self):
        data = json.loads((ROOT / "reports" / "FORMULA_VERIFICATION.json").read_text(encoding="utf-8"))
        pending = sum(1 for topic in data["topics"] if topic["standardsStatus"] == "PENDING")
        verified = sum(1 for topic in data["topics"] if topic["standardsStatus"] == "VERIFIED")
        self.assertEqual(pending, data["countStandardsPending"])
        self.assertEqual(verified, data["countStandardsVerified"])
        self.assertEqual(verified, 1)
        self.assertEqual(
            data["topics"][0]["status"] if False else sum(topic["calculationStatus"] == topic["status"] for topic in data["topics"]),
            len(data["topics"]),
        )

    def test_chinese_companions_are_not_in_the_english_count(self):
        english = {path.name for path in self.mod.formula_files()}
        chinese = {path.name for path in self.mod.chinese_formula_files()}
        self.assertTrue(chinese)
        self.assertTrue(all(name.endswith(".zh-CN.md") for name in chinese))
        self.assertEqual(set(english) & set(chinese), set())

    def test_review_list_is_empty_because_blocks_match(self):
        review = json.loads((ROOT / "reports" / "ZH_FORMULA_REVIEW.json").read_text(encoding="utf-8"))
        self.assertEqual(review["reviewedDifferences"], [])

    def test_final_audit_counts_match_the_indexes(self):
        audit = json.loads((ROOT / "reports" / "CALCULATOR_V2_FINAL_AUDIT.json").read_text(encoding="utf-8"))
        topics = json.loads((ROOT / "indexes" / "topics.json").read_text(encoding="utf-8"))
        verification = json.loads((ROOT / "indexes" / "verification-index.json").read_text(encoding="utf-8"))
        locale = json.loads((ROOT / "config" / "locale-routes.json").read_text(encoding="utf-8"))
        counts = audit["counts"]
        self.assertEqual(counts["publishedFormulaTopics"], topics["englishFormulaCount"])
        self.assertEqual(counts["chineseEditions"], topics["chineseFormulaCount"])
        self.assertEqual(counts["uniqueSiteToolPairs"], topics["uniqueSiteToolPairs"])
        self.assertEqual(counts["publishedInventoryTools"], topics["publishedInventoryTools"])
        self.assertEqual(counts["inventoryToolsWithoutExactTopicUrl"], topics["inventoryToolsWithoutTopic"])
        self.assertEqual(counts["calculationVerified"], verification["calculationVerified"])
        self.assertEqual(counts["standardsPending"], verification["standardsPending"])
        self.assertEqual(counts["standardsVerified"], verification["standardsVerified"])
        route_counts = {}
        for row in locale["routes"]:
            route_counts[row["routeStatus"]] = route_counts.get(row["routeStatus"], 0) + 1
        self.assertEqual(counts["localeRouteVerified"], route_counts.get("VERIFIED", 0))
        self.assertEqual(counts["localeRouteNotSupported"], route_counts.get("NOT_SUPPORTED", 0))

    def test_required_anchors_still_exist_on_english_topics(self):
        for path in self.mod.formula_files():
            text = path.read_text(encoding="utf-8")
            self.assertIn("## Online Calculator", text, path.name)
            self.assertIn("## Verification", text, path.name)
            self.assertRegex(text, r"\|\s*Status\s*\|\s*(VERIFIED|REVIEW_REQUIRED)\s*\|")


class Gate81HttpServer(unittest.TestCase):
    """Drive fetch_url against a local server. Sleep between retries is disabled."""

    @classmethod
    def setUpClass(cls):
        from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

        class Handler(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def do_GET(self):
                self.server.hits[self.path] = self.server.hits.get(self.path, 0) + 1
                spec = self.server.routes.get(self.path)
                if spec is None:
                    body = b"<html lang=\"en\"><title>missing</title></html>"
                    self._send(404, body, "en")
                    return
                self._send(spec["status"], spec.get("body", b""), spec.get("lang"), spec.get("location"), spec.get("content_language"))

            def _send(self, status, body, lang, location=None, content_language=None):
                self.send_response(status)
                if location:
                    self.send_header("Location", location)
                if content_language:
                    self.send_header("Content-Language", content_language)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, fmt, *args):
                return

        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.server.hits = {}
        cls.server.routes = {}
        cls.thread = __import__("threading").Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.mod = load_checker()
        cls.base = f"http://127.0.0.1:{cls.server.server_address[1]}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def setUp(self):
        self.server.hits.clear()
        self.server.routes.clear()

    def page(self, lang, canonical):
        html = (
            f"<html lang=\"{lang}\"><head><title>Sample tool</title>"
            f"<link rel=\"canonical\" href=\"{canonical}\"></head><body>tool</body></html>"
        )
        return html.encode()

    def route(self, path, status=200, lang="en", canonical=None, location=None, content_language=None):
        target = canonical if canonical is not None else self.base + path
        self.server.routes[path] = {
            "status": status,
            "lang": lang,
            "location": location,
            "content_language": content_language,
            "body": b"" if location else self.page(lang, target),
        }

    def assert_status_probe(self, status, hits, item_class, failures, warnings, exit_code):
        path = f"/status/{status}"
        self.route(path, status=status, lang="en")
        item, report, code = self.mod.probe_status(
            self.base + path,
            retries=3,
            timeout=2,
            sleeper=lambda _delay: None,
        )
        counts = self.mod.summary_counts(report, [], [item])
        self.assertEqual(self.server.hits[path], hits, status)
        self.assertEqual(item["attempts"], hits, status)
        self.assertEqual(item["class"], item_class, status)
        self.assertEqual(item["status"], status, status)
        self.assertEqual(len(report.failures), failures, status)
        self.assertEqual(len(report.warnings), warnings, status)
        self.assertEqual(code, exit_code, status)
        self.assertEqual(counts["http5xx"], 1 if item_class == "HTTP_SERVER_ERROR" else 0, status)
        self.assertNotEqual(item["class"], "ok", status)

    def test_server_error_range_is_only_500_through_599(self):
        self.assertFalse(self.mod.is_http_server_error(499))
        self.assertFalse(self.mod.is_http_server_error(600))
        for status in (500, 501, 502, 503, 504, 505, 507, 599):
            self.assertTrue(self.mod.is_http_server_error(status), status)

    def test_retried_request_classifies_499_through_600(self):
        self.assert_status_probe(499, 1, "inconclusive", 0, 1, 0)
        for status in (500, 501, 502, 503, 504, 505, 507, 599):
            self.server.hits.clear()
            self.assert_status_probe(status, 3, "HTTP_SERVER_ERROR", 1, 0, 1)
        self.server.hits.clear()
        self.assert_status_probe(600, 1, "inconclusive", 0, 1, 0)
        self.server.hits.clear()
        self.assert_status_probe(403, 1, "inconclusive", 0, 1, 0)
        self.server.hits.clear()
        self.assert_status_probe(429, 1, "inconclusive", 0, 1, 0)

    def test_locale_pass_and_identity_failures(self):
        cases = []

        path = "/zh-CN/tools/sample"
        self.route(path, lang="zh-CN", content_language="zh-CN")
        cases.append((path, "zh-CN", "ok", 0, path, "zh-CN", "tools/sample", 200, 1))

        path = "/zh-CN/tools/english-body"
        self.route(path, lang="en", content_language="en")
        cases.append((path, "zh-CN", "WRONG_LANGUAGE", 1, path, "en", "tools/english-body", 200, 1))

        path = "/tools/sample"
        self.route(path, lang="zh-CN")
        cases.append((path, "en", "WRONG_LANGUAGE", 1, path, "zh-CN", "tools/sample", 200, 1))

        self.route("/zh/", lang="zh-CN")
        self.route("/zh-CN/", lang="zh-CN")
        self.route("/", lang="en")
        self.route("/tools/other/", lang="zh-CN")
        for path, location in (
            ("/zh-CN/tools/to-zh", self.base + "/zh/"),
            ("/zh-CN/tools/to-zh-cn", self.base + "/zh-CN/"),
            ("/zh-CN/tools/to-root", self.base + "/"),
            ("/zh-CN/tools/to-other", self.base + "/tools/other/"),
        ):
            self.route(path, status=302, location=location, lang="zh-CN")
        cases.append(("/zh-CN/tools/to-zh", "zh-CN", "LOCALIZED_HOMEPAGE_FALLBACK", 1, "/zh/", "zh-CN", "", 200, 1))
        cases.append(("/zh-CN/tools/to-zh-cn", "zh-CN", "LOCALIZED_HOMEPAGE_FALLBACK", 1, "/zh-CN/", "zh-CN", "", 200, 1))
        cases.append(("/zh-CN/tools/to-root", "zh-CN", "LOCALIZED_HOMEPAGE_FALLBACK", 1, "/", "en", "", 200, 1))
        cases.append(("/zh-CN/tools/to-other", "zh-CN", "WRONG_TOOL", 1, "/tools/other/", "zh-CN", "tools/other", 200, 1))

        path = "/zh-CN/tools/bad-canonical"
        self.route(path, lang="zh-CN", canonical=self.base + "/")
        cases.append((path, "zh-CN", "WRONG_CANONICAL", 1, path, "zh-CN", "tools/bad-canonical", 200, 1))

        self.route("/missing", status=404, lang="en")
        self.route("/gone", status=410, lang="en")
        cases.append(("/missing", "zh-CN", "hard_404", 1, "/missing", "en", "missing", 404, 1))
        cases.append(("/gone", "zh-CN", "hard_404", 1, "/gone", "en", "gone", 410, 1))

        for status in (500, 501, 502, 503, 504, 505, 507, 599):
            path = f"/locale-status/{status}"
            self.route(path, status=status, lang="zh-CN")
            cases.append((path, "zh-CN", "HTTP_SERVER_ERROR", 1, path, "zh-CN", "locale-status/" + str(status), status, 3))

        self.route("/forbidden", status=403, lang="en")
        self.route("/limited", status=429, lang="en")
        cases.append(("/forbidden", "zh-CN", "inconclusive", 0, "/forbidden", "en", "forbidden", 403, 1))
        cases.append(("/limited", "zh-CN", "inconclusive", 0, "/limited", "en", "limited", 429, 1))

        for path, language, locale_class, failures, final_suffix, page_language, identity, status, hits in cases:
            item, judged, report, code = self.mod.probe_locale(
                self.base + path,
                language,
                retries=3,
                timeout=2,
                sleeper=lambda _delay: None,
            )
            self.assertEqual(self.server.hits[path], hits, path)
            self.assertEqual(item["attempts"], hits, path)
            self.assertEqual(judged, locale_class, path)
            self.assertEqual(len(report.failures), failures, path)
            self.assertEqual(code, 1 if failures else 0, path)
            self.assertEqual(item["status"], status, path)
            self.assertTrue(str(item["finalUrl"]).endswith(final_suffix), (path, item["finalUrl"]))
            self.assertEqual(item["pageLanguage"], page_language, path)
            self.assertEqual(self.mod.tool_identity(item["finalUrl"]), identity, path)
            if locale_class == "inconclusive":
                self.assertEqual(len(report.warnings), 1, path)
                self.assertEqual(len(report.failures), 0, path)
            if locale_class == "ok":
                self.assertEqual(report.failures, [])

    def test_transport_error_stays_inconclusive_after_retries(self):
        _item, judged, report, code = self.mod.probe_locale(
            "http://127.0.0.1:9/zh-CN/tools/sample",
            "zh-CN",
            retries=3,
            timeout=0.5,
            sleeper=lambda _delay: None,
        )
        self.assertEqual(_item["attempts"], 3)
        self.assertEqual(_item["class"], "inconclusive")
        self.assertIsNone(_item["status"])
        self.assertIsNone(_item["finalUrl"])
        self.assertIsNone(_item["pageLanguage"])
        self.assertEqual(judged, "inconclusive")
        self.assertEqual(len(report.failures), 0)
        self.assertEqual(len(report.warnings), 1)
        self.assertEqual(code, 0)
        self.assertNotIn("200", str(_item.get("status")))


class Gate81IndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_checker()

    def write_fixture(self, root: Path) -> None:
        site = root / "NetEngineerLab"
        site.mkdir()
        (site / "sample.md").write_text("# Sample tool\n\nBody.\n", encoding="utf-8")
        (site / "sample.zh-CN.md").write_text("# 示例\n", encoding="utf-8")
        record = {
            "website": "NetEngineerLab",
            "toolId": "sample-tool",
            "document": "NetEngineerLab/sample.md",
            "productionUrl": "https://example.com/tools/sample/",
            "sourceEvidence": "engine.js",
            "exampleResult": "1",
            "calculationStatus": "VERIFIED",
            "standardsStatus": "VERIFIED",
            "standardsEvidence": "clause",
            "standardsCheckedDate": "2026-11-10",
            "status": "VERIFIED",
        }
        (root / "reports").mkdir()
        (root / "reports" / "FORMULA_VERIFICATION.json").write_text(
            json.dumps({"topics": [record]}),
            encoding="utf-8",
        )
        inventory = {
            "domainsAssumed": {"NetEngineerLab": "https://example.com"},
            "countsByWebsite": {"NetEngineerLab": 1},
            "totalTools": 1,
            "tools": [
                {
                    "Website": "NetEngineerLab",
                    "ToolID": "sample-tool",
                    "ProductionURL": "https://example.com/tools/sample/",
                }
            ],
        }
        (root / "reports" / "GATE1_TOOL_INVENTORY.json").write_text(json.dumps(inventory), encoding="utf-8")
        topics = {
            "englishFormulaCount": 1,
            "chineseFormulaCount": 1,
            "uniqueSiteToolPairs": 1,
            "distinctToolIdStrings": 1,
            "inventoryTools": 1,
            "publishedInventoryTools": 1,
            "inventoryToolsWithoutTopic": 0,
            "topics": [
                {
                    "website": "NetEngineerLab",
                    "toolId": "sample-tool",
                    "document": "NetEngineerLab/sample.md",
                    "title": "Sample tool",
                    "chineseDocument": "NetEngineerLab/sample.zh-CN.md",
                    "productionUrl": "https://example.com/tools/sample/",
                    "calculationStatus": "VERIFIED",
                    "standardsStatus": "VERIFIED",
                    "inventoryToolId": "sample-tool",
                }
            ],
        }
        verification = {
            "englishFormulaCount": 1,
            "calculationVerified": 1,
            "calculationReviewRequired": 0,
            "standardsVerified": 1,
            "standardsPending": 0,
            "standardsNotApplicable": 0,
            "topics": [
                {
                    "document": "NetEngineerLab/sample.md",
                    "website": "NetEngineerLab",
                    "toolId": "sample-tool",
                    "calculationStatus": "VERIFIED",
                    "standardsStatus": "VERIFIED",
                    "standardsEvidence": "clause",
                    "standardsCheckedDate": "2026-11-10",
                    "sourceEvidence": "engine.js",
                    "exampleResult": "1",
                }
            ],
        }
        (root / "indexes").mkdir()
        (root / "indexes" / "topics.json").write_text(json.dumps(topics), encoding="utf-8")
        (root / "indexes" / "verification-index.json").write_text(json.dumps(verification), encoding="utf-8")

    def audit(self, root: Path):
        report = self.mod.Report()
        self.mod.audit_indexes(report, root)
        return report

    def test_fixture_and_real_indexes_match_source_files(self):
        import tempfile

        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            self.write_fixture(root)
            self.assertEqual(self.audit(root).failures, [])
        real = self.mod.Report()
        self.mod.audit_indexes(real, ROOT)
        self.assertEqual(real.failures, [])

    def test_negative_index_mutations_fail(self):
        import tempfile

        def mutate_empty(root: Path) -> None:
            path = root / "indexes" / "verification-index.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"] = []
            path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_deleted_row(root: Path) -> None:
            path = root / "reports" / "FORMULA_VERIFICATION.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"] = []
            path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_missing_document(root: Path) -> None:
            path = root / "indexes" / "topics.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"].append(dict(data["topics"][0], document="NetEngineerLab/missing.md", title="Missing"))
            path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_duplicate(root: Path) -> None:
            path = root / "indexes" / "verification-index.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"].append(dict(data["topics"][0]))
            path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_title(root: Path) -> None:
            path = root / "indexes" / "topics.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"][0]["title"] = "Tampered title"
            path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_url(root: Path) -> None:
            path = root / "indexes" / "topics.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"][0]["productionUrl"] = "https://example.com/tools/other/"
            path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_tool(root: Path) -> None:
            path = root / "indexes" / "topics.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"][0]["toolId"] = "other-tool"
            path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_standards(root: Path) -> None:
            path = root / "indexes" / "verification-index.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"][0]["standardsStatus"] = "PENDING"
            path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_calculation(root: Path) -> None:
            path = root / "indexes" / "verification-index.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"][0]["calculationStatus"] = "REVIEW_REQUIRED"
            path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_evidence(root: Path) -> None:
            for relative in ("reports/FORMULA_VERIFICATION.json", "indexes/verification-index.json"):
                path = root / relative
                data = json.loads(path.read_text(encoding="utf-8"))
                data["topics"][0]["sourceEvidence"] = None
                data["topics"][0]["exampleResult"] = None
                data["topics"][0]["standardsEvidence"] = None
                data["topics"][0]["standardsCheckedDate"] = None
                path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_companion(root: Path) -> None:
            path = root / "indexes" / "topics.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"][0]["chineseDocument"] = "NetEngineerLab/missing.zh-CN.md"
            path.write_text(json.dumps(data), encoding="utf-8")

        def mutate_counts(root: Path) -> None:
            path = root / "indexes" / "topics.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["englishFormulaCount"] = data["englishFormulaCount"] + 11
            data["chineseFormulaCount"] = 0
            path.write_text(json.dumps(data), encoding="utf-8")
            verify = root / "indexes" / "verification-index.json"
            payload = json.loads(verify.read_text(encoding="utf-8"))
            payload["standardsVerified"] = 0
            payload["standardsPending"] = 9
            verify.write_text(json.dumps(payload), encoding="utf-8")

        mutations = (
            mutate_empty,
            mutate_deleted_row,
            mutate_missing_document,
            mutate_duplicate,
            mutate_title,
            mutate_url,
            mutate_tool,
            mutate_standards,
            mutate_calculation,
            mutate_evidence,
            mutate_companion,
            mutate_counts,
        )
        for mutate in mutations:
            with tempfile.TemporaryDirectory() as name:
                root = Path(name)
                self.write_fixture(root)
                mutate(root)
                report = self.audit(root)
                self.assertGreater(len(report.failures), 0, mutate.__name__)
                self.assertTrue(all(item["check"] == "indexes" for item in report.failures), mutate.__name__)


class Gate81LocalePlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_checker()

    def test_verified_rows_are_covered_without_counting_not_supported(self):
        shared = "https://example.com/tools/shared/"
        rows = [
            {
                "routeStatus": "VERIFIED",
                "englishDocument": "Site/a.md",
                "toolId": "TOOL-A",
                "productionEnglishUrl": shared,
                "productionChineseUrl": "https://example.com/zh-CN/tools/a",
                "englishPageLanguage": "en",
                "chinesePageLanguage": "zh-CN",
            },
            {
                "routeStatus": "VERIFIED",
                "englishDocument": "Site/b.md",
                "toolId": "TOOL-B",
                "productionEnglishUrl": shared,
                "productionChineseUrl": "https://example.com/zh-CN/tools/b",
                "englishPageLanguage": "en",
                "chinesePageLanguage": "zh-CN",
            },
            {
                "routeStatus": "NOT_SUPPORTED",
                "englishDocument": "Site/c.md",
                "toolId": "TOOL-C",
                "productionEnglishUrl": "https://example.com/tools/c/",
                "productionChineseUrl": "https://example.com/tools/c/zh/",
                "englishPageLanguage": "en",
                "chinesePageLanguage": "en",
            },
        ]
        plan = self.mod.plan_locale_checks(rows)
        self.assertEqual(len(plan["verifiedRows"]), 2)
        self.assertEqual(len(plan["notSupportedRows"]), 1)
        self.assertEqual(len(plan["targets"]), 4)
        self.assertEqual(len(plan["uniqueUrls"]), 3)
        self.assertNotIn("https://example.com/tools/c/", plan["uniqueUrls"])
        self.assertNotIn("https://example.com/tools/c/zh/", plan["uniqueUrls"])
        covered = {(item["document"], item["toolId"], item["side"]) for item in plan["targets"]}
        self.assertEqual(
            covered,
            {
                ("Site/a.md", "TOOL-A", "en"),
                ("Site/a.md", "TOOL-A", "zh"),
                ("Site/b.md", "TOOL-B", "en"),
                ("Site/b.md", "TOOL-B", "zh"),
            },
        )
        languages = {item["expectedLanguage"] for item in plan["targets"]}
        self.assertEqual(languages, {"en", "zh-CN"})

    def test_real_locale_plan_uses_the_config_file(self):
        rows = json.loads((ROOT / "config" / "locale-routes.json").read_text(encoding="utf-8"))["routes"]
        plan = self.mod.plan_locale_checks(rows)
        verified = [row for row in rows if row["routeStatus"] == "VERIFIED"]
        not_supported = [row for row in rows if row["routeStatus"] == "NOT_SUPPORTED"]
        self.assertEqual(len(plan["verifiedRows"]), len(verified))
        self.assertEqual(len(plan["notSupportedRows"]), len(not_supported))
        self.assertEqual(len(plan["targets"]), len(verified) * 2)
        self.assertLessEqual(len(plan["uniqueUrls"]), len(plan["targets"]))
        self.assertTrue(all(row["chinesePageLanguage"] == "zh-CN" for row in verified))
        self.assertNotIn("NOT_SUPPORTED", {row["routeStatus"] for row in plan["verifiedRows"]})


class Gate82IndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_checker()
        cls.helper = Gate81IndexTests("test_fixture_and_real_indexes_match_source_files")
        cls.helper.mod = cls.mod

    def audit(self, root: Path):
        report = self.mod.Report()
        self.mod.audit_indexes(report, root)
        return report

    def test_website_and_inventory_identity_mutations_fail(self):
        import tempfile

        def tamper_website(root: Path) -> None:
            path = root / "indexes" / "topics.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"][0]["website"] = "PCDog"
            path.write_text(json.dumps(data), encoding="utf-8")

        def tamper_inventory_id(root: Path) -> None:
            path = root / "indexes" / "topics.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"][0]["inventoryToolId"] = "not-a-real-inventory-id"
            path.write_text(json.dumps(data), encoding="utf-8")

        def sync_wrong_website(root: Path) -> None:
            for relative in (
                "reports/FORMULA_VERIFICATION.json",
                "indexes/topics.json",
                "indexes/verification-index.json",
            ):
                path = root / relative
                data = json.loads(path.read_text(encoding="utf-8"))
                data["topics"][0]["website"] = "PCDog"
                path.write_text(json.dumps(data), encoding="utf-8")

        for mutate in (tamper_website, tamper_inventory_id, sync_wrong_website):
            with tempfile.TemporaryDirectory() as name:
                root = Path(name)
                self.helper.write_fixture(root)
                mutate(root)
                report = self.audit(root)
                self.assertGreater(len(report.failures), 0, mutate.__name__)

    def test_mismatched_standards_evidence_and_date_fail(self):
        import tempfile

        def tamper_evidence(root: Path) -> None:
            path = root / "indexes" / "verification-index.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"][0]["standardsEvidence"] = "fabricated replacement"
            path.write_text(json.dumps(data), encoding="utf-8")

        def tamper_date(root: Path) -> None:
            path = root / "indexes" / "verification-index.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["topics"][0]["standardsCheckedDate"] = "1900-01-01"
            path.write_text(json.dumps(data), encoding="utf-8")

        for mutate in (tamper_evidence, tamper_date):
            with tempfile.TemporaryDirectory() as name:
                root = Path(name)
                self.helper.write_fixture(root)
                mutate(root)
                report = self.audit(root)
                self.assertGreater(len(report.failures), 0, mutate.__name__)
                self.assertTrue(any("standards" in item["message"] for item in report.failures), mutate.__name__)

    def test_recomputed_inventory_summary_fields_fail_when_tampered(self):
        import tempfile

        fields = (
            "distinctToolIdStrings",
            "inventoryTools",
            "publishedInventoryTools",
            "inventoryToolsWithoutTopic",
        )
        for field in fields:
            with tempfile.TemporaryDirectory() as name:
                root = Path(name)
                self.helper.write_fixture(root)
                path = root / "indexes" / "topics.json"
                data = json.loads(path.read_text(encoding="utf-8"))
                data[field] = data[field] + 9
                path.write_text(json.dumps(data), encoding="utf-8")
                report = self.audit(root)
                self.assertGreater(len(report.failures), 0, field)


class Gate82LocaleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

        class Handler(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def do_GET(self):
                spec = self.server.routes[self.path]
                body = spec["body"]
                self.send_response(spec["status"])
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, fmt, *args):
                return

        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.server.routes = {}
        cls.thread = __import__("threading").Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.mod = load_checker()
        cls.base = f"http://127.0.0.1:{cls.server.server_address[1]}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def html(self, lang, canonicals, title="Sample tool"):
        links = "".join(f"<link rel=\"canonical\" href=\"{href}\">" for href in canonicals)
        return f"<html lang=\"{lang}\"><head><title>{title}</title>{links}</head><body>tool</body></html>".encode()

    def put(self, path, body, status=200):
        self.server.routes[path] = {"status": status, "body": body}

    def judge(self, path, language="zh-CN"):
        return self.mod.probe_locale(
            self.base + path,
            language,
            retries=1,
            timeout=2,
            sleeper=lambda _delay: None,
        )

    def test_controlled_url_alias_rules(self):
        same = self.mod.same_controlled_target
        self.assertTrue(same("https://example.com/tools/a", "https://www.example.com/tools/a/"))
        self.assertTrue(same("https://example.com/tools/a", "http://example.com:443/tools/a"))
        self.assertFalse(same("https://example.com/zh-CN/tools/a", "https://example.com/tools/a"))
        self.assertFalse(same("https://example.com/tools/a", "https://evil.example/tools/a"))
        self.assertFalse(same("https://example.com/tools/a", "https://example.com:8080/tools/a"))

    def test_canonical_and_error_page_negatives(self):
        path = "/zh-CN/tools/sample"
        self.put(path, self.html("zh-CN", [self.base + path]))
        _item, judged, report, code = self.judge(path)
        self.assertEqual(judged, "ok")
        self.assertEqual(code, 0)
        self.assertEqual(report.failures, [])

        path = "/zh-CN/tools/english-canonical"
        self.put(path, self.html("zh-CN", [self.base + "/tools/english-canonical"]))
        _item, judged, report, code = self.judge(path)
        self.assertEqual(judged, "CANONICAL_NOT_LANGUAGE_ROUTE")
        self.assertEqual(code, 1)

        path = "/zh-CN/tools/foreign"
        self.put(path, self.html("zh-CN", ["https://evil.example/zh-CN/tools/foreign"]))
        _item, judged, _report, code = self.judge(path)
        self.assertEqual(judged, "WRONG_CANONICAL")
        self.assertEqual(code, 1)
        self.assertEqual(_item["finalUrl"], self.base + path)

        path = "/zh-CN/tools/missing-canonical"
        self.put(path, self.html("zh-CN", []))
        _item, judged, _report, code = self.judge(path)
        self.assertEqual(judged, "NOT_PRESENT")
        self.assertEqual(code, 1)

        path = "/zh-CN/tools/conflict"
        self.put(
            path,
            self.html("zh-CN", [self.base + path, self.base + "/tools/conflict"]),
        )
        _item, judged, _report, code = self.judge(path)
        self.assertEqual(judged, "CONFLICTING_CANONICAL")
        self.assertEqual(code, 1)

        path = "/zh-CN/tools/duplicate"
        self.put(path, self.html("zh-CN", [self.base + path, self.base + path]))
        _item, judged, report, code = self.judge(path)
        self.assertEqual(judged, "ok")
        self.assertEqual(code, 0)
        self.assertEqual(len(report.warnings), 1)
        self.assertEqual(report.failures, [])

        path = "/zh-CN/tools/soft-404"
        self.put(path, self.html("zh-CN", [self.base + path], title="Page not found"))
        _item, judged, report, code = self.judge(path)
        self.assertEqual(judged, "error_page")
        self.assertEqual(_item["status"], 200)
        self.assertEqual(_item["pageLanguage"], "zh-CN")
        self.assertEqual(code, 1)
        self.assertGreater(len(report.failures), 0)

    def test_check_urls_rejects_locale_only_soft_404(self):
        path = "/zh-CN/tools/locale-only"
        url = self.base + path
        self.put(path, self.html("zh-CN", [url], title="Page not found | Example"))
        row = {
            "routeStatus": "VERIFIED",
            "englishDocument": "NetEngineerLab/sample.md",
            "toolId": "sample-tool",
            "productionEnglishUrl": self.base + "/tools/sample",
            "productionChineseUrl": url,
            "englishPageLanguage": "en",
            "chinesePageLanguage": "zh-CN",
            "englishCanonicalStatus": "MATCH",
            "chineseCanonicalStatus": "MATCH",
        }
        english = self.base + "/tools/sample"
        self.put("/tools/sample", self.html("en", [english], title="Sample tool"))
        report = self.mod.Report()
        self.mod.check_urls(
            report,
            2,
            1,
            False,
            locale_rows=[row],
            only_urls=[(english, "tool"), (url, "locale")],
        )
        chinese = [item for item in report.stats["localeJudged"] if item["side"] == "zh"]
        self.assertEqual(len(chinese), 1)
        self.assertEqual(chinese[0]["localeClass"], "error_page")
        self.assertEqual(chinese[0]["status"], 200)
        self.assertEqual(report.stats["localeLivePass"], 1)
        self.assertGreater(len(report.failures), 0)
        self.assertEqual(report.warnings, [])


if __name__ == "__main__":
    unittest.main()
