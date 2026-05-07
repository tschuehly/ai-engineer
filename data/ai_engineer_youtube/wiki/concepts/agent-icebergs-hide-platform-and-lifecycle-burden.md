# Agent Icebergs Hide Platform and Lifecycle Burden

Summary: Building a production customer-facing agent is much larger than choosing a model, framework, embeddings model, vector database, and a few tools. The hidden work includes lifecycle testing, model upgrades, voice edge cases, nontechnical coaching tools, and operational surfaces for scaled customer interactions.

Use when:
- Evaluating build-versus-buy decisions for production agent platforms.
- Auditing whether an agent prototype has enough lifecycle infrastructure to become customer-facing.

Details:
- Bavor describes an "agent iceberg" where technical teams often see model choice, LangGraph or LangChain, embeddings, vector databases, and tool integrations as the whole project. (09:16-09:46)
- Below the surface are regression testing, unit testing, model migration, model upgrades, voice-specific issues such as speaker separation and interruptions, and the broader agent development lifecycle. (09:55-10:10)
- Sierra's platform framing combines an in-code agent-building toolkit with no-code tools for nontechnical users to build, refine, coach, edit, and update agents, with both sides interoperating. (10:14-10:48)
- The build-your-own failure pattern is that companies underestimate the hidden depth, spend months on the platform work, and return after discovering the production burden. (10:50-11:35)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent-Native SDLC Platforms Need Context, Reliability, and Parallelism](agent-native-sdlc-platforms-need-context-reliability-and-parallelism.md)
- [Use stable agent harnesses as model-evolution boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md)

Sources:
- [Rise of the AI Architect - Clay Bavor, Cofounder, Sierra w/ Alessio Fanelli](../sources/20250724_C3geUfBR2js.md), 09:16-11:35
