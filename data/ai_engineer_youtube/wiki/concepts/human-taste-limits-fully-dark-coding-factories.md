# Human Taste Limits Fully Dark Coding Factories

Summary: Fully automated coding factories are weaker when product direction is still being discovered. Human taste, iterative play, and changing prompts remain important when the first plan is unlikely to be the final product.

Use when:
- Deciding whether to let coding agents merge work without human product review.
- Designing a coding-agent workflow for exploratory product or UI work.

Details:
- Steinberger describes running many concurrent coding-agent sessions partly as a workaround for slow agent loops; faster loops reduced the need for ten simultaneous sessions to around five or six, 25:32-26:30.
- He argues that fully dark factories can imply deciding everything upfront, but good software usually changes direction as builders see results, discover shortcuts, and refine ideas, 26:53-27:44.
- His workflow is iterative: build steps, play with the result, see how it feels, get new ideas, and change prompts, 27:44-27:57.
- For PRs, he warns against automatic merging because contributors and agents can pull the product in many directions, and the AI is unlikely to know the right product direction without human guidance, 27:57-28:27.
- Taste includes detecting AI-smelling writing or UI and spending saved implementation time on small details that would not appear from a high-level prompt alone, 28:28-29:52.
- Co-maintainer corroboration from the same OpenClaw project: with tokens cheap, the hard part is not saying yes (you can merge everything and turn the codebase into a "fire dump") but deciding who to say no to; the bottleneck "becomes taste," and curation matters more than throughput. (Koc, 03:31-03:38, 07:43-08:02)
- They used a plugin architecture as a structural way to say no without bloat: split the codebase so a provider (OpenAI, Mistral, Anthropic) owns its own plugin separate from everything else, rather than absorbing every contributor's feature into the core. (Koc, 08:02-08:21)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [AI agents still need human taste for interaction quality](ai-agents-still-need-human-taste-for-interaction-quality.md)
- [Run Parallel Coding Sessions as Typed Swim Lanes](run-parallel-coding-sessions-as-typed-swim-lanes.md)

Sources:
- [State of the Claw - Peter Steinberger](../sources/20260417_zgNvts_2TUE.md), 25:32-29:52
- [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](../sources/20260605_pmoDeA3RBZY.md), 03:31-08:21
