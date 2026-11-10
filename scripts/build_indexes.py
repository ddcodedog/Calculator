#!/usr/bin/env python3
"""Rebuild machine-readable topic and verification indexes from the repo.

Read-only with respect to formula prose. Writes indexes/topics.json and
indexes/verification-index.json. Does not contact the network.
"""

from __future__ import annotations

import json
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


def english_topics() -> list[Path]:
    found = []
    for site in SITES:
        folder = ROOT / site
        for path in sorted(folder.glob("*.md")):
            if path.name != "README.md" and not path.name.endswith(".zh-CN.md"):
                found.append(path)
    return found


def chinese_topics() -> list[Path]:
    found = []
    for site in SITES:
        found.extend(sorted((ROOT / site).glob("*.zh-CN.md")))
    return found


def title_of(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def main() -> None:
    verification = json.loads((ROOT / "reports" / "FORMULA_VERIFICATION.json").read_text(encoding="utf-8"))
    by_doc = {topic["document"]: topic for topic in verification["topics"]}
    inventory = json.loads((ROOT / "reports" / "GATE1_TOOL_INVENTORY.json").read_text(encoding="utf-8"))
    inventory_urls = {tool["ProductionURL"].rstrip("/"): tool for tool in inventory["tools"]}
    topics = []
    for path in english_topics():
        document = path.relative_to(ROOT).as_posix()
        topic = by_doc[document]
        companion = path.with_name(path.name.replace(".md", ".zh-CN.md"))
        topics.append(
            {
                "website": topic["website"],
                "toolId": topic["toolId"],
                "document": document,
                "title": title_of(path),
                "chineseDocument": companion.relative_to(ROOT).as_posix() if companion.exists() else None,
                "productionUrl": topic["productionUrl"],
                "calculationStatus": topic["calculationStatus"],
                "standardsStatus": topic["standardsStatus"],
                "inventoryToolId": inventory_urls.get(topic["productionUrl"].rstrip("/"), {}).get("ToolID"),
            }
        )
    pairs = {(item["website"], item["toolId"]) for item in topics}
    published_urls = {item["productionUrl"].rstrip("/") for item in topics}
    payload = {
        "generatedFrom": "reports/FORMULA_VERIFICATION.json",
        "englishFormulaCount": len(topics),
        "chineseFormulaCount": len(chinese_topics()),
        "uniqueSiteToolPairs": len(pairs),
        "distinctToolIdStrings": len({item["toolId"] for item in topics}),
        "inventoryTools": inventory["totalTools"],
        "publishedInventoryTools": len(published_urls & set(inventory_urls)),
        "inventoryToolsWithoutTopic": inventory["totalTools"] - len(published_urls & set(inventory_urls)),
        "topics": topics,
    }
    standards_verified = sum(1 for topic in verification["topics"] if topic["standardsStatus"] == "VERIFIED")
    standards_pending = sum(1 for topic in verification["topics"] if topic["standardsStatus"] == "PENDING")
    standards_na = sum(1 for topic in verification["topics"] if topic["standardsStatus"] == "NOT_APPLICABLE")
    calculation_verified = sum(1 for topic in verification["topics"] if topic["calculationStatus"] == "VERIFIED")
    calculation_review = sum(1 for topic in verification["topics"] if topic["calculationStatus"] == "REVIEW_REQUIRED")
    verification_index = {
        "source": "reports/FORMULA_VERIFICATION.json",
        "englishFormulaCount": len(verification["topics"]),
        "calculationVerified": calculation_verified,
        "calculationReviewRequired": calculation_review,
        "standardsVerified": standards_verified,
        "standardsPending": standards_pending,
        "standardsNotApplicable": standards_na,
        "topics": [
            {
                "document": topic["document"],
                "website": topic["website"],
                "toolId": topic["toolId"],
                "calculationStatus": topic["calculationStatus"],
                "standardsStatus": topic["standardsStatus"],
                "standards": topic.get("standards"),
                "standardsEvidence": topic.get("standardsEvidence"),
                "standardsCheckedDate": topic.get("standardsCheckedDate"),
                "sourceEvidence": topic.get("sourceEvidence"),
                "exampleResult": topic.get("exampleResult"),
                "boundary": topic.get("boundary"),
            }
            for topic in verification["topics"]
        ],
    }
    out_dir = ROOT / "indexes"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "topics.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out_dir / "verification-index.json").write_text(
        json.dumps(verification_index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"topics={payload['englishFormulaCount']} chinese={payload['chineseFormulaCount']} "
        f"pairs={payload['uniqueSiteToolPairs']} standardsPending={standards_pending}"
    )


if __name__ == "__main__":
    main()
