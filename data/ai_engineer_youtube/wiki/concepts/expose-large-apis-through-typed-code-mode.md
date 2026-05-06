# Expose Large APIs Through Typed Code Mode

Summary: Typed code mode lets an agent access a broad API by writing code against generated SDK types instead of loading every endpoint as a separate tool schema. Types become a compact interface contract that the model can reason over.

Use when:
- A full API surface is too large to expose as MCP tools, but partial product-specific servers lose important coverage.
- The agent can generate code and the runtime can execute it with controlled credentials and policy.

Details:
- Cloudflare's code-mode pattern generates TypeScript or SDK types from API specifications and asks the model to write code against those types. (07:20-08:20)
- The talk frames types as a concise representation of inputs and outputs that can make an entire API accessible in far fewer tokens than endpoint-by-endpoint tool descriptions. (07:42-08:20)
- Generated code can compose operations such as listing workers, deploying a worker, and adding Cloudflare Access protection while keeping the API spec as the source of truth. (08:20-09:06)
- The approach depends on MCP clients or agent runtimes supporting code execution; Cloudflare found client support lagged because running untrusted model-written code is an obvious security concern. (09:06-10:08)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Discover Large API Tool Surfaces Progressively](discover-large-api-tool-surfaces-progressively.md)
- [Run Agent-Written API Code Inside Programmable Sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)

Sources:
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md), 07:20-10:08
