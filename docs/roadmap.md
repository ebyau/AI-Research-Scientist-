# Capability Roadmap

The table below tracks the 13 best-practice patterns identified for top-tier AI research stacks. ✅ indicates completed, ❌ pending, ⏸️ intentionally deferred.

| # | Capability | Status | Notes |
| --- | --- | --- | --- |
| 1 | Workflow-specialized agents | ✅ | Kadosh → Hard-guy → Bazalel, with SOULs and handoff contracts. |
| 2 | Integrated tooling + data access | ✅ | Brave + arXiv + Hugging Face wired; helper scripts + smoke test documented. |
| 3 | Memory + provenance | ✅ | QMD-backed Markdown + `memory/provenance` log_citation workflow in place. |
| 4 | Human-in-the-loop checkpoints | ❌ | Define review gates (idea sign-off, experiment approval). |
| 5 | Evaluation harnesses | ❌ | Plan/test templates for experiments still outstanding. |
| 6 | Feedback & learning loops | ❌ | No rubric-based scoring or continuous improvement yet. |
| 7 | Security / ethics guardrails | ❌ | Need formal policy + enforcement mechanisms. |
| 8 | Shared knowledge graphs / embeddings | ❌ | Requires design for internal knowledge base. |
| 9 | Automated project/backlog management | ❌ | No coordinator agent tracking dependencies yet. |
| 10 | Simulation & sandboxing | ❌ | Placeholder for surrogate-task checks before full experiments. |
| 11 | Agent debate / cross-review | ❌ | Could add paired reviewer agents later. |
| 12 | Auto-documentation & paper drafting | ❌ | No dedicated writer/archivist agent yet. |
| 13 | Resource-aware scheduling | ⏸️ | Deferred per current scope (no scheduler integration planned). |

## Immediate Priorities
1. **Capability #5** — formalize evaluation harnesses (templates, scripts, automated checks for Bazalel’s plans).
2. **Capability #4** — define human-in-the-loop checkpoints (idea sign-off, experiment approval gates).
3. **Capability #6** — add feedback/learning loops so agent outputs get scored and iteratively improved.

Use this file to track progress as additional capabilities come online.
