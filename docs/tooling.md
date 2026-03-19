# Tooling & Data Access

This file tracks the external services wired (or planned) for the AI Research Scientist stack.

## 1. Brave Search (web_search)
- **Status:** Configured on 2026-03-18.
- **Config path:** `plugins.entries.brave.config.webSearch.apiKey` in `~/.openclaw/openclaw.json`.
- **Tools:** Enables the `web_search` tool (provider = `brave`).
- **Usage:** Kadosh and Hard-guy rely on Brave for general discovery, terminology lookup, and citation leads.

## 2. Academic Scripts & APIs
| Tool | Purpose | Status | Notes |
| --- | --- | --- | --- |
| `tools/arxiv_search.py` | Structured arXiv search (BM25 via official API) | 🟢 | Run with `python3 tools/arxiv_search.py --query "..." --max-results 10 --json`; Hard-guy drops JSON + Markdown into literature reports. |
| Semantic Scholar API | Fetch abstracts, references, citation graphs | Pending | Store key in `SEMANTIC_SCHOLAR_API_KEY` / `.env.agents`. |
| arXiv API/RSS | Track latest preprints | 🟢 | Backed by the helper script above (no key needed). |
| Hugging Face Hub | Dataset/model pull for Bazalel | 🟢 | Token stored locally (`~/.huggingface/token`, `~/.openclaw/.env`). |
| Kaggle API | Dataset download or competition baselines | Pending | Add `~/.kaggle/kaggle.json` when competitions arise. |
| GitHub access | Inspect baseline repos, store docs | 🟢 | Repo `ebyau/AI-Research-Scientist-` managed via fine-grained PAT. |

## 3. Credential Handling Notes
- Sensitive keys live in local env files (`~/.openclaw/.env`, `~/.huggingface/token`) or service-specific configs. **Template:** see `docs/secrets-template.md`.
- Use `tools/tooling_smoke_test.sh` after changes to confirm arXiv/QMD/Hugging Face access.
- Each agent’s output should record which external tools were used (queries, datasets, repos) so provenance is preserved.

## 4. Memory Upgrades (QMD + Flush Contracts)
- **Video takeaway:** Ray Fernando's "Making OpenClaw Actually Remember Things" stream shows how QMD (Query-Memory-Document) dramatically improves recall accuracy by combining BM25 keyword search with vectors + reranking.
- **Action plan:**
  1. Install QMD (`npm install -g @tobilu/qmd`) and keep it available on PATH.
  2. Update `~/.openclaw/openclaw.json` with `memory.backend = "qmd"`, `memory.qmd.includeDefaultMemory = true`, and scoped access rules (default deny + explicit allow for direct chats).
  3. Set `memory.qmd.update.interval = 5m` with `debounceMs = 15000` to avoid thrashing the index.
  4. Leave `memory.qmd.limits.maxResults` around 6 and `maxSnippetChars` around 700 for readable responses.
  5. Keep `agents.defaults.compaction.memoryFlush.enabled = true` so the pre-compaction reminder writes durable notes before context is trimmed.
- **Expected benefit:** better recall of specific facts (ports, dataset names) and higher-quality semantic matches without abandoning the Markdown memory source of truth.

## 5. Next Steps
1. Add Semantic Scholar support once a key is available.
2. Extend dataset tooling (e.g., Kaggle, proprietary storage) as projects demand.
3. Keep `agents/TOOLING.md` and this doc in sync whenever new integrations go live.
4. Restart the OpenClaw gateway after each config change so agents pick up new tooling immediately.
