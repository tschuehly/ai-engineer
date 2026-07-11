# Agent harnesses combine model, tools, prompts, filesystem, skills, hooks, and memory

Summary: A practical agent product is a harness around the model, not only a model call. The reusable harness owns the tool loop, prompt surfaces, filesystem context, skills, subagents, compaction, hooks, and memory that let the agent build context and continue work.

Use when:
- Designing an agent framework or deciding what belongs outside the model call.
- Explaining why a coding-agent SDK includes filesystem, tool, memory, and hook primitives.

Details:
- The source defines agents as systems that build their own context, decide their own trajectories, and work autonomously, which makes the surrounding harness responsible for the environment in which those choices happen. 03:08-03:27
- Anthropic built the Claude Agent SDK on Claude Code because internal agent projects kept rebuilding the same pieces around the model. 04:01-04:18
- The named harness pieces include tools, loop prompts and transition prompts, filesystem-backed context, skills, subagents, web search, research, compaction, hooks, and memory. 04:25-05:52
- Context engineering in this framing includes files, scripts, and tools the agent can use, not only initial prompt text. 05:16-05:31
- Agent tiers ("you can't fix stupid"): the harness+model tier must match the stakes of the work — "friends don't let friends use really bad harnesses or low intelligent models for important work." A tier-two-or-better harness needs a powerful reasoning model plus sub-agents, plan mode, full MCP support, and file editing; don't hand a team the bare ChatGPT web interface and expect a great result. ([Upside](../sources/20260711_YZQsWVeN3rE.md), 15:24-16:34)
- Pricing warning for AI features built on managed products: any AI capability "crowbarred into a per-seat subscription model" probably can't be trusted for important work, because the plan margin "doesn't leave enough space for an intelligent reasoning model to work" — e.g. Slackbot's MCP-client feature was judged "horrifically stupid" for this reason. ([Upside](../sources/20260711_YZQsWVeN3rE.md), 15:57-16:14)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Unified coding-agent harnesses combine models, tools, environments, and safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)

Sources:
- [Claude Agent SDK [Full Workshop] - Thariq Shihipar, Anthropic](../sources/20260105_TqC1qOfiVcQ.md), 03:08-05:52
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](../sources/20260711_YZQsWVeN3rE.md), 15:24-16:34
