# Start Expensive With Agents, Then Collapse Proven Steps

Summary: When building a new LLM pipeline, optimizing for cost too early hides the solution. Run an agent freely on the problem first — even at "unfeasible" cost — to discover how it solves the task, then collapse the proven step into a one-shot LLM call or a smaller trained model once the pattern is clear.

Use when:
- Designing a high-volume pipeline where running an agent on every input looks too expensive.
- Tempted to avoid agents or push them as late as possible in the pipeline to save tokens before you know what the task actually requires.

Details:
- PostHog's mistake while experimenting was over-focusing on cost: with a huge volume of input signals, they tried to avoid agents where possible and delay them as late as possible in the pipeline (12:35-12:59).
- The reframe is "tokens are free" — explicitly acknowledged as not literally true, but the right stance during experimentation: throwing an agent at the same problem 100 times surfaces the clever solutions it finds and, eventually, the similarities across runs (12:59-13:16).
- Once those similarities are visible, an expensive agent step can be turned into a one-shot LLM call or a trained model that is much faster and cheaper (13:16-13:34).
- This let the project move from a starting point where the pipeline was "completely unfeasible" and "way too costly to generate a PR" to a feasible one — the agent is a discovery tool for the solution shape, not necessarily the production runtime for every step (13:16-13:34).
- The pattern complements eval discipline: you need representative production data to judge whether a collapsed one-shot step still matches the agent's behavior before replacing it.

Related topics:
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Sequence Production AI by Pillars and Choose the Model Last](sequence-production-ai-by-pillars-and-choose-the-model-last.md)
- [Distill reasoning traces into small models](distill-reasoning-traces-into-small-models.md)
- [Parallel agent prototypes turn design choices into measurements](parallel-agent-prototypes-turn-design-choices-into-measurements.md)
- [Observability-to-PR Agents Turn Incidents Into Reviewable Fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)

Sources:
- [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](../sources/20260610_zMiSRliEzv4.md), 12:35-13:34
