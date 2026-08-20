# Defer Tool Definitions Out of Context and Let the Model Search for Them

Summary: Instead of choosing which tools to load before the request, mark tools as deferred so their definitions never enter the context window at all, and let the model pull one in with a tool-search call when it decides it wants it. In the responses API this is a per-tool flag plus either a built-in search tool or one you implement.

Use when:
- The tool registry grows with whatever the user installed (MCP servers, plugins, extensions) and you cannot predict its size at design time.
- A pre-request retrieval step over a tool catalog is either too coarse or arrives before the model knows what it needs.
- You are deciding whether progressive tool disclosure belongs in your harness or can be pushed down into the inference API.

Details:
- Codex marks some tools as deferred, "and that means that they're not added directly to the context window, but instead are available through tool search later on." The deferred set is not a smaller eager set — the definitions are absent until requested. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 05:59-06:16)
- The mechanism sits in the inference API rather than the harness, which is what makes it portable: "Tool search specifically is actually something that is available in the responses API. So, even if you're building your own harness, you can leverage this. Since GPT-5.4, you can mark any tool as deferred loading." ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 06:36-06:52)
- Discovery is pluggable: the model can use "our built-in tool search tool or implement your own if you feel like you can better do that discovery yourself." A team that already has an embedding index over its tool catalog can keep it and still get the context saving. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 06:52-06:59)
- **Why this is different from retrieving tools before the call.** The wiki's existing pattern — [Retrieve Tool Descriptions Before Loading Large Tool Catalogs](retrieve-tool-descriptions-before-loading-large-tool-catalogs.md) — narrows the catalog using the user's query, before the model has reasoned about the task. Deferral moves the decision to the point where the model already knows what it is doing, at the cost of an extra round trip. Both leave the *selected* tools in context; only deferral keeps the unselected ones out from the start, which answers the caveat recorded on [Discover Large API Tool Surfaces Progressively](discover-large-api-tool-surfaces-progressively.md) that "irrelevant selected tools still occupy context after the model chooses the one it needs."
- The motivation is the unpredictable half of the context. Model instructions "are fairly structured and don't really change in size or like mess around with [cachability]," but "the tool registry, where especially if you install MCPs… you might have additional context that is like growing as you're installing more MCPs." Deferral is a fix aimed at the growth term specifically. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 05:29-05:59)
- **What the source does not establish.** No number is given for context saved, no accuracy comparison against eager loading is offered, and nothing is said about the failure mode where the model's search does not surface a tool it needed — which is the cost this pattern trades for. The talk is an OpenAI vendor talk with no measurement of this feature. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), Provenance and Caveats)

Related topics:
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Retrieve Tool Descriptions Before Loading Large Tool Catalogs](retrieve-tool-descriptions-before-loading-large-tool-catalogs.md)
- [Discover Large API Tool Surfaces Progressively](discover-large-api-tool-surfaces-progressively.md)
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [The Fat-Agent Tool Overload Collapses Accuracy and Inflates Latency](fat-agent-tool-overload-collapses-accuracy-and-latency.md)
- [Cap the Skills List as a Share of the Context Window](cap-the-skills-list-as-a-share-of-the-context-window.md)
- [Match Agent Tooling to the Model's Training Distribution](match-agent-tooling-to-the-models-training-distribution.md)

Sources:
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 05:29-06:59
