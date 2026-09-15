"""CLI entry point for Agentic Prospect Research.

Example:
    python src/main.py --tender ../shared-data/tender.json --out ../shared-data/client_insights.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from research import generate_insights


def main() -> None:
    parser = argparse.ArgumentParser(description="Research the prospect behind a structured tender.")
    parser.add_argument("--tender", required=True, help="Path to a StructuredTender JSON file.")
    parser.add_argument("--out", required=True, help="Path to write ClientInsights JSON.")
    args = parser.parse_args()

    tender = json.loads(Path(args.tender).read_text(encoding="utf-8"))
    insights = generate_insights(tender)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(insights, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Wrote client insights to {out_path}")
    print(f"  Industry guess: {insights['industry_guess']}")
    for n in insights["notes"]:
        print(f"  - {n}")


if __name__ == "__main__":
    main()
