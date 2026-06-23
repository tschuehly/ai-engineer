# Make the LLM Gateway the Agent Observability Chokepoint

Summary: If every model call must pass through one gateway node, that node sees every tool call, bash command, and MCP request the agent makes — without instrumenting inside the container or the harness — and becomes the place to enforce cross-provider budgets, quotas, and guaranteed webhooks. The LLM layer is the right chokepoint over the MCP layer precisely because agents increasingly bypass structured tool calls for code and bash.

Use when:
- Deciding where to put agent observability and policy: inside the container, at the MCP layer, or at the model-call layer.
- Building a gateway that needs complete, instrumentation-free visibility into what fleets of agents actually do.

Details:
- Aperture is an LLM gateway like any other (single provider key for Anthropic/OpenAI/Gemini/Vertex/Bedrock on the gateway), but because it is also a network node it sees the verified identity of every caller, and because every model call routes through it you get "a guarantee I've seen every tool call this thing has ever made" — "not happening from inside the container... not from the harness." (05:42-07:10, 10:39-11:13)
- The visibility is total and per-identity: tokens, models, spend per model, every request including full request/response headers and bodies ("everything that Claude code sends at the very beginning"), drillable to a single session. A PR review bot's 30-day history shows each request, the bash commands it ran (three at once for 4 cents), and a concrete trajectory (MCP tool call to update the review → bash → grep → re-update the comment). (07:28-11:13)
- Cross-provider controls live at the gateway because everything passes through it: budgets that span every provider ("not 'here's a thousand dollars for everybody'... here's just a thousand dollars and you can decide how to use it"), per-day quotas, and webhooks fired on each tool call to a third party — "guaranteed to exist and run no matter what." Quota permissioning can mix team and individual limits ("use as much as you want of the internal GPU, but if it's Opus 4.6 you only get this amount"). (13:59-15:35, 20:25-21:28)
- Choose the LLM layer over the MCP layer deliberately: "a lot of agents are moving away from tool calls and executing code," which makes traffic harder to parse, "and it's the whole reason we chose to do this." They considered the MCP layer but the LLM layer is "way more valuable" because even with skills/code "you're still running something" through the gateway. (21:28-22:41)
- Even visibility-only is valuable: many teams "don't even know what tools people are using — forget about blocking it, just tell me what people are doing." A reported production datum: internally "bash dominates everything else" over MCP/structured tool calls. Planned guardrails layer on top (e.g. block `rm -rf /`). The honest caveat: an agent could "write the thing, obfuscate the thing, then run the thing." (22:41-23:41)
- Design tradeoff: the gateway requires setting the agent's base URL explicitly rather than transparently intercepting at the network layer — a deliberate choice, because hidden interception "can start to break and shift and move out from under you." (18:46-20:25)

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)

Related concepts:
- [Move Agent Access Control to the Network Layer So the Sandbox Holds No Credential](move-agent-access-control-to-the-network-layer.md)
- [MCP Gateways Create an Enterprise Root of Trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Abstract LLM Inference Behind One Routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Govern MCP Tool Calls With Tool-Level Policy and End-to-End Traces](govern-mcp-tool-calls-with-tool-level-policy-and-end-to-end-traces.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)

Sources:
- [What if the network was the sandbox? — Remy Guercio, Tailscale](../sources/20260601_BM2JX9hqsVQ.md), 05:42-11:13, 13:59-15:35, 18:46-23:41
