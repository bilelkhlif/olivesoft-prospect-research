# OliveSoft — Agentic Prospect Research

**CSTAM 3.0 Challenge:** CSTAM-OliveSoft — Automated RFP Intelligence & Commercial Proposal Generation System
**Phase 1 component — 10 / 100 points**

## Scope

Autonomous AI agent workflow to research prospect details: sector, estimated revenue, past projects, key partners, specific domain requirements.

### Responsibilities
- Given a client/company name (extracted from an RFP by `olivesoft-tender-detection`), run an autonomous research agent to answer:
  - What does the company do? Industry & market position
  - Current technology & digital infrastructure
  - Possible pain points
  - Competitors
  - Why OliveSoft can help
- Use web/news search tools (e.g. SerpAPI, NewsAPI) as agent tools
- Produce structured client insights consumable by the proposal generator

### Out of scope
- Matching OliveSoft's own capabilities to the RFP → `olivesoft-rag-retrieval`
- Detecting the RFP in the first place → `olivesoft-tender-detection`

## Suggested stack
Python, LangChain/LangGraph or CrewAI/AutoGen, SerpAPI/NewsAPI, OpenAI/Anthropic API — not mandatory, see CSTAM Book "Recommended Skills."

## Status
🚧 Scaffolding — Phase 1 MVP in progress. Deadline: Oct 1, 2026.

## Related repos
- Hub: [olivesoft-rfp-intelligence](https://github.com/bilelkhlif/olivesoft-rfp-intelligence)
- [olivesoft-tender-detection](https://github.com/bilelkhlif/olivesoft-tender-detection)
- [olivesoft-rag-retrieval](https://github.com/bilelkhlif/olivesoft-rag-retrieval)
- [olivesoft-n8n-orchestration](https://github.com/bilelkhlif/olivesoft-n8n-orchestration)
