# The Fat-Agent Tool Overload Collapses Accuracy and Inflates Latency

Summary: Loading every tool's name, description, and schema into every prompt (the "Fat Agent") makes tool selection collapse and latency inflate as the catalog grows — benchmarked accuracy falls from ~78% at 10 tools to ~13.6% at 741 tools while the catalog alone costs ~127k tokens per request — because long tool lists trigger lost-in-the-middle; keep the model's per-request tool working set small even as the catalog grows.

Use when:
- Deciding whether an agent's growing tool catalog needs a router, and needing the evidence for why static loading breaks.
- Diagnosing an agent that got slower, more expensive, and less accurate as tools were added even though no single tool is broken.

Details:
- The Fat Agent gives the model every tool definition on every request — every function name, description, and JSON schema — whether or not the user needs it. It works in a demo and at ~10 tools but breaks as the catalog grows to 30, 100, or more. (02:19-03:00)
- The failure is structural, not per-tool: "the design does not fail because one tool is badly written. It fails because every request is forced to carry the entire catalog." (03:31-03:47)
- Accuracy collapse (fat agent): ~78% correct-tool at 10 tools, ~40% at ~100 tools, 13.6% at 741 tools (≈1 correct in 8). A semantic router stays above 83% across the same catalog sizes because the model chooses from a small relevant set, not hundreds. (04:31-05:20, 26:10-27:20)
- Root cause is lost-in-the-middle: models attend more strongly to the beginning and end of long context, so hundreds of tool schemas packed in the middle are used unreliably — "we end up paying for a huge prompt, and that prompt makes the decisions even harder." (05:24-05:55)
- Token cost: 741 tools ≈ 127,000 tokens of descriptions/schemas paid on every request before the user's question; at 100k requests/day that is billions of tokens/day just to describe tools. (06:00-06:30)
- Latency: fat-agent time-to-first-token grows with the catalog because the model must process a larger prompt before answering; ~500 tools can push first-token latency past 5 seconds, which makes a real-time product feel slow and unpredictable. Router TTFT stays almost flat. (06:50-07:25, 15:00-15:20)
- The core lesson: "the catalog can grow, but the model's working set should stay small." The router also *removes* the wrong tools from the model's choice set, not only adds the right one, which cuts cross-tool confusion. (15:10-15:20, 18:30-20:00)
- Threshold: fewer than 20 tools, a router may be unnecessary — load directly (fine for 10–15); past ~50 tools in production a router is justified. But tool confusion can appear with only a few tools, long before 100, so treat rising add-a-tool failures as a possible architecture problem, not automatically a bad prompt. (08:40-09:10, 26:20-27:00)
- **A first-party harness reaches the same conclusion and puts the fix in the model's hands.** Codex identifies the tool registry as the term in the context that grows without bound — "especially if you install MCPs… you might have additional context that is like growing as you're installing more MCPs" — and its answer is per-tool deferred loading plus a tool-search tool the model calls itself ([Defer Tool Definitions Out of Context and Let the Model Search for Them](defer-tool-definitions-out-of-context-and-let-the-model-search-for-them.md)). That agrees with this page's prescription — keep the working set small while the catalog grows — but relocates the selector from a retriever in front of the model to the model itself, which trades a router's flat accuracy curve for a round trip and for the model's own judgment about when to look. No accuracy figures accompany the Codex version, so the measured comparison on this page remains the only quantified one. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 05:29-06:59)

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Retrieve tool descriptions before loading large tool catalogs](retrieve-tool-descriptions-before-loading-large-tool-catalogs.md)
- [Tune a tool router with a K-sweep and guard its failure modes](tune-a-tool-router-with-k-sweep-and-guard-its-failure-modes.md)
- [Inject Tool Context Just-in-Time During Agent Sequencing](inject-tool-context-just-in-time-during-agent-sequencing.md)
- [Curate context strategically because models drop the middle](curate-context-strategically-because-models-drop-the-middle.md)
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Defer Tool Definitions Out of Context and Let the Model Search for Them](defer-tool-definitions-out-of-context-and-let-the-model-search-for-them.md)

Sources:
- [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](../sources/20260628_vh2VGuQ3zhY.md), 02:19-07:25, 26:10-27:00
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 05:29-06:59
