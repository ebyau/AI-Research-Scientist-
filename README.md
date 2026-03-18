# AI Research Scientist Stack

This repository captures how the OpenClaw workspace is being shaped into a reusable "AI Research Scientist" pipeline. It documents the agent architecture, tooling integrations, and the roadmap for advanced capabilities so the setup can be replicated or extended later.

## Repository Guide

| File / Folder | Purpose |
| --- | --- |
| `README.md` | High-level overview (this file). |
| `docs/overview.md` | Narrative summary of the system goals and current status. |
| `docs/agents.md` | Detailed specs for Kadosh, Hard-guy, and Bazalel (with pointers to their SOUL files). |
| `docs/tooling.md` | Records API integrations, credentials setup steps, and data-access plans. |
| `docs/roadmap.md` | Tracks the 13 best-practice capabilities (✅/❌) and what to implement next. |
| `docs/changelog.md` | Timestamped log of major actions taken during setup. |

All paths referenced in the docs assume the OpenClaw workspace root at `~/.openclaw/workspace/` unless stated otherwise.

## Current Highlights

- Multi-agent workflow defined (research → literature → experiment design).
- Brave Search API integrated so research agents can call `web_search`.
- GitHub repo established to version-control documentation of the build.

See the `docs/` folder for the full narrative and next steps.
