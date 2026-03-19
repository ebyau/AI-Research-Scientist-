# Changelog

Chronological record of notable steps while building the AI Research Scientist stack. Timestamps in UTC.

## 2026-03-18
- Defined Kadosh, Hard-guy, and Bazalel SOUL files under `~/.openclaw/workspace/agents/` with detailed workflows and templates.
- Added `agents/README.md` and `agents/TOOLING.md` in the workspace to document pipeline + integration plans.
- Configured Brave Search API (`plugins.entries.brave.config.webSearch.apiKey`) and set `tools.web.search.provider = brave`; restarted the OpenClaw gateway.
- Verified `web_search` calls succeed via Brave.
- Created GitHub repo `ebyau/AI-Research-Scientist-` and began seeding documentation (`README.md` + `docs/`).

## 2026-03-19
- Installed QMD (`npm install -g @tobilu/qmd`) and switched `memory.backend` to `qmd` with scoped access + update cadence.
- Added `tools/arxiv_search.py` and `tools/tooling_smoke_test.sh` for arXiv queries and tooling verification; documented usage in `docs/tooling.md`.
- Captured secrets guidance in `docs/secrets-template.md` and stored local tokens under `~/.openclaw/.env` / `~/.huggingface/token`.
- Updated agent SOULs (toolboxes + Bazalel coding posture) and created `agents/bazalel/scripts/` for helper pipelines.
- Added provenance logging via `tools/log_citation.py`, documented the memory layout in `docs/memory.md`, and seeded `memory/provenance/general.md`.
- Pushed commits `9249f65` and `8a060a2` to GitHub with all documentation updates.

(Extend this log whenever new capabilities or docs are added.)
