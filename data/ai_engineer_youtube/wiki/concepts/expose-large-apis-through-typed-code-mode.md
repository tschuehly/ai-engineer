# Expose Large APIs Through Typed Code Mode

Summary: Typed code mode lets an agent access a broad API by writing code against generated SDK types instead of loading every endpoint as a separate tool schema. Types become a compact interface contract that the model can reason over.

Use when:
- A full API surface is too large to expose as MCP tools, but partial product-specific servers lose important coverage.
- The agent can generate code and the runtime can execute it with controlled credentials and policy.

Details:
- Pai frames code mode as replacing slow JSON tool-call loops with model-generated JavaScript that can use typed APIs, syntax checking, loops, state, sequencing, and parallelism inside one execution. (01:31-03:00)
- Cloudflare's example exposed a large API through two code-accepting operations, search and execute, reducing a roughly 1.2-1.5 million-token API surface to about 1,000 tokens for the initial tool interface. (03:09-04:05)
- The same DDoS-response workflow that would need many ordinary MCP round trips can be generated as one code string and executed next to the API surface. (04:21-05:18)
- Cloudflare's code-mode pattern generates TypeScript or SDK types from API specifications and asks the model to write code against those types. (07:20-08:20)
- The talk frames types as a concise representation of inputs and outputs that can make an entire API accessible in far fewer tokens than endpoint-by-endpoint tool descriptions. (07:42-08:20)
- Generated code can compose operations such as listing workers, deploying a worker, and adding Cloudflare Access protection while keeping the API spec as the source of truth. (08:20-09:06)
- The approach depends on MCP clients or agent runtimes supporting code execution; Cloudflare found client support lagged because running untrusted model-written code is an obvious security concern. (09:06-10:08)
- Programmatic tool calling can also compose MCP tool results inside a REPL-like execution environment instead of spending a latency-sensitive inference turn after every low-level tool call. (09:39-10:56)
- MCP structured output can give the model return-value type information, making code-mode composition more reliable than parsing opaque natural-language tool results. (10:56-11:49)
- A later Cloudflare session restates the headline figure: code mode in an MCP server can expose all 2,600 Cloudflare API endpoints in just ~1,000 tokens of tool interface, the same "we fixed MCP twice" claim that pairs with capability-scoped Dynamic Workers for safe execution. (SKDJo2CopRs 09:44-10:22)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Discover Large API Tool Surfaces Progressively](discover-large-api-tool-surfaces-progressively.md)
- [Run Agent-Written API Code Inside Programmable Sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)

Sources:
- [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](../sources/20260419_8txf05vVVl4.md), 01:31-05:18
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md), 07:20-10:08
- [The Future of MCP - David Soria Parra, Anthropic](../sources/20260419_v3Fr2JR47KA.md), 09:39-11:49
- [Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](../sources/20260608_SKDJo2CopRs.md), 09:44-10:22
