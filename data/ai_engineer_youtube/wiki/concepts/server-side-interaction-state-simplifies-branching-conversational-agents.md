# Server-side interaction state simplifies branching conversational agents

Summary: A conversational-agent API can store interaction turns server-side and let clients continue by passing the prior interaction ID. This reduces client-side history plumbing while still requiring retention, retrieval, and context-window limits to be handled explicitly.

Use when:
- Designing chat, research, or multimodal agent sessions that need continuation across turns.
- Deciding whether conversation state belongs in client-managed history or server-managed interaction records.

Details:
- The Interactions API is described as a unified surface for both models and agents, so the same continuation pattern can move between ordinary model calls, Deep Research-like agents, image generation, and audio generation. 09:19-10:38
- A client can continue a conversation by passing the previous interaction ID; the service appends the new user input to the stored user and model turns rather than forcing the client to rebuild a local history object. 15:14-15:51
- Keeping interaction IDs on the client allows branching from an earlier point: a builder can reuse a base interaction, launch parallel follow-up requests, or retrieve the chain through `interactions.get`. 42:55-43:56
- Server-side state is not infinite context. The source says Gemini models still have a context limit, expired interaction IDs are pruned, and compaction remains a client-side responsibility until the API provides stronger support. 44:14-45:17

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context development lifecycle treats context as an engineered artifact](context-development-lifecycle-treats-context-as-an-engineered-artifact.md)
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)

Sources:
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md), 09:19-10:38, 15:14-15:51, 42:55-45:17
