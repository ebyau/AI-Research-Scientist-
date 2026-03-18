# Agent Specifications

The AI Research Scientist stack currently uses three role-specialized agents. Their canonical instructions live in the OpenClaw workspace (`~/.openclaw/workspace/agents/...`); this document summarizes each role and links back to the source SOUL files.

## Kadosh — Research Architect
- **SOUL file:** `agents/kadosh/SOUL.md`
- **Mission:** Convert raw ideas into structured research briefs.
- **Key responsibilities:**
  - Interpret ambiguous prompts and clarify assumptions.
  - Generate candidate framings, problem statements, and hypotheses.
  - Sketch initial methodology, literature scope, and experiment scope.
  - Capture risks/unknowns and prepare handoffs to downstream agents.
- **Output template:** Topic, problem statement, motivation, questions, hypotheses, methodology direction, literature scope, experiment scope, risks, handoff checklist.

## Hard-guy — Literature Cartographer
- **SOUL file:** `agents/hard-guy/SOUL.md`
- **Mission:** Map prior work, cluster approaches, and surface actionable gaps.
- **Key responsibilities:**
  - Translate Kadosh’s brief into search strategies.
  - Query academic sources (arXiv, Semantic Scholar, etc.) and cite everything.
  - Summarize existing approaches, identify limitations, propose positioning.
  - Highlight baselines/datasets/metrics Bazalel must consider.
- **Output template:** Scope recap, search log, landscape overview (with citations), gap analysis, recommended positioning, baseline references, open questions.

## Bazalel — Experiment Architect
- **SOUL file:** `agents/bazalel/SOUL.md`
- **Mission:** Design methodology, datasets, baselines, evaluation metrics, and ablations.
- **Key responsibilities:**
  - Align experiments with Kadosh’s hypotheses and Hard-guy’s literature findings.
  - Specify datasets, preprocessing, model choices, training schedules, and infra needs.
  - Define evaluation metrics, baselines, ablation matrices, and risks.
  - Produce an execution-ready blueprint for implementation teams.
- **Output template:** Objectives, dataset plan, model/training plan, evaluation protocol, baselines, ablations, infra/tooling, risks, next actions.

## Collaboration Pattern
1. **Intake:** Dubois → Kadosh (idea & constraints)
2. **Literature:** Kadosh → Hard-guy (brief & keywords)
3. **Experiments:** Kadosh + Hard-guy → Bazalel (brief + literature map)
4. **Execution:** Bazalel → implementation agents/humans (blueprint) → feedback to Kadosh/Hard-guy as needed.

Future agents (Archivist, Reviewer, etc.) can be added following the same structure when needed.
