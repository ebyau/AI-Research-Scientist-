# Tooling & Data Access

This file tracks the external services wired (or planned) for the AI Research Scientist stack.

## 1. Brave Search (web_search)
- **Status:** Configured on 2026-03-18.
- **Config path:** `plugins.entries.brave.config.webSearch.apiKey` in `~/.openclaw/openclaw.json`.
- **Tools:** Enables the `web_search` tool (provider = `brave`).
- **Usage:** Kadosh and Hard-guy rely on Brave for general discovery, terminology lookup, and citation leads.

## 2. Other Planned Integrations
| Service | Purpose | Status | Notes |
| --- | --- | --- | --- |
| Semantic Scholar API | Fetch abstracts, references, citation graphs | Pending | Store key in `SEMANTIC_SCHOLAR_API_KEY` or a secrets file, log query strings in outputs. |
| arXiv API/RSS | Track latest preprints | Pending | No key required; integrate into Hard-guy’s search workflow. |
| Hugging Face Hub | Dataset/model pull for Bazalel | Pending | Requires HF token if private/gated sets are needed. |
| Kaggle API | Dataset download or competition baselines | Pending | Store credentials in Kaggle config (~/.kaggle). |
| GitHub access | Inspect baseline repos, store docs | 🟢 | Repo `ebyau/AI-Research-Scientist-` cloned into `~/.openclaw/workspace/AI-Research-Scientist-`. Fine-grained PAT managed manually. |

## 3. Credential Handling Notes
- Sensitive keys should be stored in local env files or secrets stores (`~/.openclaw/.env`, SecretRefs, or service-specific configs). Avoid committing them to Git.
- Each agent’s output should record which external tools were used (queries, datasets, repos) so provenance is preserved.

## 4. Memory Upgrades (QMD + Flush Contracts)
- **Video takeaway:** Ray Fernando's "Making OpenClaw Actually Remember Things" stream shows how QMD (Query-Memory-Document) dramatically improves recall accuracy by combining BM25 keyword search with vectors + reranking.
- **Action plan:**
  1. Install QMD via Bun (`bun install -g https://github.com/tobi/qmd`) and keep it running as a local sidecar.
  2. Update `~/.openclaw/openclaw.json` with `memory.backend = "qmd"`, `memory.qmd.includeDefaultMemory = true`, and scoped access rules (default deny + explicit allow for direct chats).
  3. Set `memory.qmd.update.interval = 5m` with `debounceMs = 15000` to avoid thrashing the index.
  4. Leave `memory.qmd.limits.maxResults` around 6 and `maxSnippetChars` around 700 for readable responses.
  5. Keep `agents.defaults.compaction.memoryFlush.enabled = true` so the pre-compaction reminder writes durable notes before context is trimmed.
- **Expected benefit:** better recall of specific facts (ports, dataset names) and higher-quality semantic matches without abandoning the Markdown memory source of truth.

## 5. Next Steps
1. Wire up Semantic Scholar (and optionally arXiv) as the next data sources.
2. Implement the QMD backend switch once the sidecar is installed.
3. Extend `agents/TOOLING.md` and this doc whenever new integrations go live.
4. Restart the OpenClaw gateway after each config change so agents pick up new tooling immediately.
