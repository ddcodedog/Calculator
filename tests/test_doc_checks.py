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


if __name__ == "__main__":
    unittest.main()
