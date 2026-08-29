# Measure AI Engineering Impact Across Utilization, Impact, and Cost

Summary: AI engineering measurement should mature from "who used the tool" into a combined view of utilization, delivery impact, quality impact, and cost. Usage metrics are useful context, but they do not prove that AI improved the engineering system.

Use when:
- Designing dashboards for AI-assisted engineering adoption.
- Explaining why tool usage, token volume, or accept rates need to be tied to quality and throughput outcomes.

Details:
- The talk distinguishes telemetry, experience sampling, and survey data: telemetry shows API-visible behavior, experience sampling can capture PR-level AI use, and effective surveys can capture developer experience as a system problem. (08:01-09:08)
- API telemetry can mislead when treated alone; an IDE accept event does not show whether the engineer rewrote the suggested code afterward. (08:05-08:29)
- DX's measurement framework normalizes signals into utilization, impact, and cost, with maturity moving from "what is happening?" to correlations with velocity, quality, and spend. (09:56-11:04)
- Leaders should watch speed and quality together: higher PR throughput is not useful if change failure rate, maintainability, change confidence, or perceived quality degrade. (07:35-08:01)
- Organization averages can hide extreme variance: company-level slices showed some organizations improving while others declined on the same impact measures. (02:40-03:23)
- A later Stanford ROI talk makes the same point with a team case study: PR count increased after AI adoption, but code quality fell, rework increased, and effective output did not meaningfully increase. (12:57-15:28)
- Jellyfish adds a PR-telemetry version of the framework: developer adoption rate correlated with PR throughput and cycle-time improvements, while PR size, bug tickets, and revert rates served as guardrails against reading volume as value by itself. (03:00-10:54)
- **A skills-layer instrument panel, offered as a sketch.** Touil's simulation tracks four per-team measures: skills per engineer contribution, average skills utilization (how often skills are pulled per day), duplication ratio across teams, and a combined quality-and-security ratio. ([Touil](../sources/20260828_M05vON8i0aI.md), 15:32-16:05) Utilization is the one that earns its place here — it separates a library that is stocked from one that is used, which no adoption or spend metric distinguishes. The important caveat is that these are parameters of a model he wrote rather than measurements from a deployment: no baseline, no threshold, and no real organization's data behind any of them.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Do not use token volume as a developer productivity metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)
- [Measure AI developer productivity with field experiments, not benchmark extrapolation alone](measure-ai-developer-productivity-with-field-experiments-not-benchmark-extrapolation-alone.md)
- [Measure AI coding adoption with PR telemetry and guardrails](measure-ai-coding-adoption-with-pr-telemetry-and-guardrails.md)
- [Measure AI ROI with primary output and guardrails](measure-ai-roi-with-primary-output-and-guardrails.md)
- [A Missing Skill Is Billed as Tokens, Not Recorded as a Gap](a-missing-skill-is-billed-as-tokens-not-recorded-as-a-gap.md)

Sources:
- [Leadership in AI Assisted Engineering - Justin Reock, DX (acq. Atlassian)](../sources/20251219_PmZDupFP3UM.md), 02:40-03:23, 07:35-11:04
- [Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) - Yegor Denisov-Blanch, Stanford](../sources/20251211_JvosMkuNxF8.md), 12:57-15:28
- [What Data from 20m Pull Requests Reveal About AI Transformation - Nick Arcolano, Jellyfish](../sources/20251124_WqZq8L-v9pA.md), 03:00-10:54
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 15:32-16:05
