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

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Do not use token volume as a developer productivity metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)
- [Measure AI developer productivity with field experiments, not benchmark extrapolation alone](measure-ai-developer-productivity-with-field-experiments-not-benchmark-extrapolation-alone.md)

Sources:
- [Leadership in AI Assisted Engineering - Justin Reock, DX (acq. Atlassian)](../sources/20251219_PmZDupFP3UM.md), 02:40-03:23, 07:35-11:04
