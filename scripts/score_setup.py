"""Calculate setup readiness; evidence quality is assessed by the auditor."""
import json
import sys
from pathlib import Path

CATEGORIES = ("context", "connections", "capabilities", "cadence")

def calculate(data):
    categories = data.get("categories", {})
    if set(categories) != set(CATEGORIES):
        raise ValueError("Exactly four rubric categories are required.")
    for key in ("manual_only", "material_conflict"):
        if type(data.get(key)) is not bool:
            raise ValueError(key + " must be boolean.")
    runs = data.get("successful_due_runs")
    if type(runs) is not int or runs < 0:
        raise ValueError("successful_due_runs must be a nonnegative integer.")
    totals = {}
    for category in CATEGORIES:
        items = categories[category]
        if not isinstance(items, list) or len(items) != 5:
            raise ValueError("Each category requires five criteria.")
        scores = []
        for item in items:
            score = item.get("score")
            if score is not None and (type(score) is not int or score not in (0, 1, 3, 5)):
                raise ValueError("Scores must be 0, 1, 3, 5, or null.")
            if score is not None and (not isinstance(item.get("evidence"), str) or not item["evidence"].strip()):
                raise ValueError("Every assessed criterion requires evidence.")
            scores.append(score)
        totals[category] = None if None in scores else sum(scores)
    if None in totals.values():
        return {"score": None, "partial": True, "categories": totals, "caps": [], "raw_sum": None}
    raw_sum = sum(totals.values())
    caps = []
    if any(item["score"] == 0 for item in categories["context"][:2]):
        totals["context"] = min(totals["context"], 10)
        caps.append("Missing business foundation or failed retrieval caps context at 10/25")
    if data["manual_only"] and totals["cadence"] > 10:
        totals["cadence"] = 10
        caps.append("Manual cadence capped at 10/25")
    minimum = min(totals.values())
    score = sum(totals.values())
    if categories["connections"][2]["score"] == 0 or categories["capabilities"][3]["score"] == 0:
        score = min(score, 49)
        caps.append("Missing credential or action safeguards cap total at 49")
    if minimum < 10:
        score = min(score, 49)
        caps.append("A category below 10 caps total at 49")
    if minimum < 15 or runs < 2:
        score = min(score, 69)
        caps.append("Category below 15 or fewer than two due automatic runs caps total at 69")
    if minimum < 20 or data["material_conflict"]:
        score = min(score, 84)
        caps.append("Category below 20 or material conflict caps total at 84")
    return {"score": score, "partial": False, "categories": totals, "caps": caps, "raw_sum": raw_sum}

if __name__ == "__main__":
    try:
        assessment = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(json.dumps(calculate(assessment), indent=2))
    except (IndexError, OSError, ValueError, TypeError, AttributeError) as error:
        print("Invalid assessment: " + str(error), file=sys.stderr)
        sys.exit(1)
