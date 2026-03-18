# Overview

This project tracks the ongoing effort to turn an OpenClaw deployment into a reusable **AI Research Scientist**. The intent is to codify every architectural decision, integration step, and quality gate so the setup can be reproduced quickly in future environments.

## Objectives

1. **Workflow-specialized agents:** Chain dedicated roles (ideation, literature, experimentation) with clear handoffs.
2. **Integrated tooling:** Give agents direct access to web search, literature APIs, datasets, and repos.
3. **Repeatability:** Version-control the configuration and instructions so the process doubles as a playbook.
4. **Scalability:** Leave room for future capabilities (memory, QA agents, experiment automation, etc.).

## Current Status (2026-03-18)

- 🟢 Agent roles (Kadosh, Hard-guy, Bazalel) defined in `~/.openclaw/workspace/agents/` with detailed SOUL files.
- 🟢 Brave Search API configured (`plugins.entries.brave.config.webSearch.apiKey`) so `web_search` works for research tasks.
- 🟢 GitHub repo initialized to capture documentation and future changes.
- 🔴 Remaining enhancements (memory, evaluation harnesses, auto-documentation, etc.) tracked on the roadmap.

## Key Locations

| Purpose | Path |
| --- | --- |
| Main OpenClaw workspace | `~/.openclaw/workspace/` |
| Agent SOUL files | `~/.openclaw/workspace/agents/{kadosh,hard-guy,bazalel}/SOUL.md` |
| Tooling plan | `~/.openclaw/workspace/agents/TOOLING.md` |
| OpenClaw config | `~/.openclaw/openclaw.json` |

Use the other docs in this folder for more detail on agents, tooling, and roadmap items.
