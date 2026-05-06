# Leadership in AI Assisted Engineering - Justin Reock, DX (acq. Atlassian)

Source: [Leadership in AI Assisted Engineering - Justin Reock, DX (acq. Atlassian)](https://www.youtube.com/watch?v=PmZDupFP3UM)
Uploaded: 2025-12-19
Transcript: `raw/20251219_PmZDupFP3UM/PmZDupFP3UM.en-orig.vtt`

## Summary

Justin Reock argues that AI-assisted engineering rollouts need leadership ownership, not adoption mandates. The useful operating pattern is to combine utilization, impact, and cost measurement with psychological safety, real enablement time, prompt-rule feedback loops, compliance partnership, and SDLC bottleneck analysis so AI improves engineering outcomes instead of merely increasing tool usage.

## Extracted Concepts

- [Measure AI engineering impact across utilization, impact, and cost](../concepts/measure-ai-engineering-impact-across-utilization-impact-and-cost.md) - This source describes a measurement maturity path that starts with usage but must correlate it to quality, speed, and cost outcomes.
- [Create psychological safety for AI adoption](../concepts/create-psychological-safety-for-ai-adoption.md) - This source ties AI adoption to transparent augmentation intent, fear reduction, and time for learning.
- [Target AI rollouts at SDLC bottlenecks](../concepts/target-ai-rollouts-at-sdlc-bottlenecks.md) - This source argues that saving time outside the actual delivery bottleneck does not improve throughput.
- [Govern agent rules through feedback gatekeepers](../concepts/govern-agent-rules-through-feedback-gatekeepers.md) - This source recommends a maintained feedback loop for system prompts, Cursor rules, and `AGENTS.md`-style instructions.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

## Notes

- Average AI impact can hide large organization-level variance: Reock cites company-level spreads where some teams see around 20% improvement while others see around 20% decline in change confidence, maintainability, or change failure rate. (02:40-03:23)
- Top-down adoption mandates can create compliant but low-value behavior; one example is ritual tool usage that satisfies an adoption target without improving engineering work. (03:27-03:46)
- Useful enablement includes clear AI policies, time to learn, and space to experiment rather than only turning on the tool or sending training material. (04:33-04:50)
- The talk frames psychological safety as central because engineers need to understand that the rollout is meant to augment them, not replace them, before they will openly learn and report failures. (06:13-07:25)
- AI measurement should combine telemetry, experience sampling, and effective surveys; API telemetry such as accept-versus-suggest can miss later rewrites or actual usefulness. (08:01-09:28)
- DX's framework normalizes AI measurement into utilization, impact, and cost, with maturity moving from who uses tools to what usage does to velocity, quality, and spend. (09:56-11:04)
- Prompt governance needs a gatekeeper or group that can receive feedback and continuously improve shared system prompts, Cursor rules, and agent Markdown. (11:18-12:04)
- Temperature should be selected by use case: lower settings improve repeatability, while higher settings create more divergent approaches for creative tasks. (12:07-13:25)
- Leaders should look for SDLC bottlenecks because code completion may not matter if interruptions, meetings, incident context gathering, onboarding, or reverse engineering dominate the system constraint. (04:56-05:13, 15:01-17:25)
