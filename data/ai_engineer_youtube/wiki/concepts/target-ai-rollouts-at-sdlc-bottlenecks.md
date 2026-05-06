# Target AI Rollouts at SDLC Bottlenecks

Summary: AI adoption should be aimed at the real software-delivery bottleneck, not only at code generation. Saving time on a non-constraint can leave throughput unchanged while other delays dominate the system.

Use when:
- Choosing which engineering workflows should receive AI investment first.
- Evaluating whether code completion, agent coding, onboarding, incident response, or legacy analysis is the highest-leverage target.

Details:
- Reock argues that for many organizations writing code has never been the bottleneck, so code completion may only produce modest gains while larger SDLC constraints remain untouched. (04:56-05:13)
- The talk uses theory-of-constraints framing: an hour saved outside the bottleneck is worthless if interruptions, context switching, meeting-heavy days, or other workflow delays dominate. (15:01-15:34)
- Morgan Stanley's legacy-code example is framed as a bottleneck-oriented workflow: AI creates specs for modernization work so developers avoid repeated reverse engineering before starting implementation. (15:36-16:07)
- Zapier's onboarding agents are framed as a throughput lever because reducing time-to-effectiveness changes hiring and scaling economics, not merely individual code speed. (16:10-16:55)
- Spotify's incident workflow shows an operations bottleneck: collecting runbook steps, context, and documentation into incident channels can reduce critical minutes during response. (16:55-17:25)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI pushes software engineers toward broader product and operations ownership](ai-pushes-software-engineers-toward-broader-product-and-operations-ownership.md)
- [Agents reduce dependency-chain chores through parallel execution](agents-reduce-dependency-chain-chores-through-parallel-execution.md)

Sources:
- [Leadership in AI Assisted Engineering - Justin Reock, DX (acq. Atlassian)](../sources/20251219_PmZDupFP3UM.md), 04:56-05:13, 15:01-17:25
