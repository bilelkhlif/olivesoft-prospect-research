"""Phase 1 MVP prospect research: rule-based/templated insight generation.

This is a placeholder for the real Agentic Prospect Research (10 pts): an
LLM agent with web/news search tools (SerpAPI/NewsAPI) investigating the
buyer's industry, tech, pain points, and competitors. Kept dependency-free
and API-key-free here so the end-to-end pipeline can run without secrets;
swap `generate_insights()` internals for a real agent while keeping the
same input/output contract (docs/schema/client_insights.schema.json).
"""
from __future__ import annotations

from datetime import datetime, timezone

SECTOR_HINTS = [
    (["college", "university", "school", "institute", "academy"], "Higher Education / Academia"),
    (["hospital", "clinic", "health"], "Healthcare"),
    (["bank", "financial", "insurance"], "Financial Services"),
    (["municipal", "ministry", "government", "department", "agency"], "Public Sector / Government"),
    (["logistics", "transport", "freight"], "Logistics & Transportation"),
]


def guess_industry(buyer_name: str) -> str:
    name = buyer_name.lower()
    for keywords, label in SECTOR_HINTS:
        if any(kw in name for kw in keywords):
            return label
    return "Unclassified — needs manual review"


def generate_insights(tender: dict) -> dict:
    buyer_name = tender.get("buyer_name", "")
    buyer_country = tender.get("buyer_country", "")
    industry = guess_industry(buyer_name)
    cpv_labels = tender.get("cpv_labels", [])
    required_tech = tender.get("required_tech", [])

    notes = [
        f"Buyer '{buyer_name}' is procuring via TED (EU public procurement) from {buyer_country or 'an EU member state'}.",
        f"Guessed sector: {industry} (heuristic match on buyer name -- verify manually).",
        f"Procurement category: {', '.join(cpv_labels) if cpv_labels else 'unclassified'}.",
        "Public-sector/EU procurement implies formal tender rules, transparent evaluation criteria, and likely GDPR data-handling requirements.",
    ]

    why = []
    if any(t in required_tech for t in ["scheduling", "timetabling", "booking"]):
        why.append("OliveSoft has direct prior delivery experience in scheduling/booking systems (see EduSchedule, MedConnect) -- strong capability match.")
    if industry == "Higher Education / Academia":
        why.append("OliveSoft's EduSchedule platform was built for a comparable education-sector use case, reducing delivery risk.")
    if not why:
        why.append("No strong direct precedent found in OliveSoft's knowledge base for this sector/tech combination -- flag for manual review before bidding.")

    return {
        "tender_id": tender["tender_id"],
        "buyer_name": buyer_name,
        "industry_guess": industry,
        "notes": notes,
        "why_olivesoft_can_help": why,
        "researched_at": datetime.now(timezone.utc).isoformat(),
    }
