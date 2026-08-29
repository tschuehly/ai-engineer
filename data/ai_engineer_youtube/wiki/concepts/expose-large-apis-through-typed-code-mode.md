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

- **Code mode generalizes past tool calling to any operation over a corpus too large to put in context.** Ben Hylak transplants it to observability: "you've heard about code mode in the context of MCPs… I highly recommend just uh trying to apply this to traces. Like you can just write uh these classifiers and you can run them in a sandbox and you can run them at production scale." The invariant that carries across is the same one that motivates typed code mode here — the model authors a program against a described surface and the runtime executes it over the data, so the model's context holds the question rather than the payload ([Run Trace Classifiers as Code Mode in a Sandbox](run-trace-classifiers-as-code-mode-in-a-sandbox.md)). ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 18:14-18:36)

- **Code mode as the last stage of a migration, applied only where it pays.** Uber reached code mode after two cheaper interface changes and scoped it narrowly: "of late we also have a code mode skill which is auto-installed which on the fly creates Python scripts to hyper optimize some of the top MCP token consuming use cases" ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 05:06-05:41). Two choices are worth separating from the technique itself. It targets the measured top consumers rather than the whole catalog, which means code mode is treated as an optimization with a cost, not as the right default shape for every tool. And it ships as an *auto-installed skill*, so the optimization reaches engineers who never asked for it — the distribution problem that usually decides whether an interface improvement is realized fleetwide. The combined reported effect of this and the two preceding stages is "more than 40% fleetwide savings" across 1,000-plus tools. See [Stage the MCP Token Tax Down](stage-the-mcp-token-tax-down-direct-omni-cli-then-code-mode.md).

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Discover Large API Tool Surfaces Progressively](discover-large-api-tool-surfaces-progressively.md)
- [Run Agent-Written API Code Inside Programmable Sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Run Trace Classifiers as Code Mode in a Sandbox](run-trace-classifiers-as-code-mode-in-a-sandbox.md)
- [Stage the MCP Token Tax Down: Direct, Omni, CLI, Then Code Mode](stage-the-mcp-token-tax-down-direct-omni-cli-then-code-mode.md)

Sources:
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 18:14-18:36
- [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](../sources/20260419_8txf05vVVl4.md), 01:31-05:18
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md), 07:20-10:08
- [The Future of MCP - David Soria Parra, Anthropic](../sources/20260419_v3Fr2JR47KA.md), 09:39-11:49
- [Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](../sources/20260608_SKDJo2CopRs.md), 09:44-10:22
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 05:06-05:41
