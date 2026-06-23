# Build Agents on Addressable Stateful-Serverless Instances

Summary: Running each agent session as one addressable, persistent, hibernating compute instance (one per ID) makes resumable streaming, multi-client sync, and background scheduling emergent properties of the runtime instead of distributed-systems plumbing you build in userland.

Use when:
- Choosing the runtime/compute model for a stateful agent, chat, or coding-agent product.
- Deciding whether to build resumability, cross-device sync, and scheduling yourself or inherit them from the platform.
- Evaluating "stateful serverless" runtimes (Cloudflare Durable Objects-style) against stateless function-per-request hosting plus an external database.

Details:
- Cloudflare's Durable Objects model: for a given ID, a class spins up once and every future request and websocket connection lands in the same instance, so state lives in the compute unit rather than an external database. A naive serverless `let counter = 0; counter++` fails because each invocation spins up, runs, and disappears with no state; the single-instance-per-ID model fixes that. This is "stateful serverless." (02:20-03:24)
- The instance is addressable, persistent, hibernates/sleeps, can run long-running and background work even with no inbound requests, and connects out to other services. (03:56-04:15)
- Edge placement gives ~15ms latency (London), just under the 16ms of a 60fps animation frame, which is why the same primitive powers real-time collaborative sync such as TLDraw's shared canvas across many phones. (03:27-03:52)
- Resumable streaming becomes free: ask an LLM for a long story and refresh mid-stream — in a stateless serverless world this needs a database, replication, and sticky sessions, but here the client reconnects to the instance, which replays the start of the stream and continues sending bytes. (13:34-14:05)
- Multi-tab and multi-browser/device sync come out of the box (phone and laptop on the same session); the original killer use case for the primitive was real-time collaborative sync. (14:05-14:19)
- Background scheduling is built in — an agent can schedule recurring work (e.g., "every Friday at 9pm, compile my git history, wiki, and Notion and send it to my manager"). (04:57-05:13)
- Cloudflare's Agents SDK builds these properties on the model and behaves as an execution environment more than a library, so LangChain, the Vercel AI SDK, or other agent libraries can run inside it; it ships React hooks plus plain-JS clients and is a first-class, production-ready backend for the Vercel AI SDK (tool calls, synchronize, resumability, cross-tab state). (04:32-05:55)
- A persistent agent loop on this model becomes a coding-agent backend reachable from any client (terminal, chat, phone, iOS, web) where everything is synced, resumable, and stateful. (15:39-16:08)
- The architectural payoff: you do not have to patch sync, streaming, and scheduling in userland and become a distributed-systems engineer — the runtime owns the hard parts. The framing is that agent products should be "multiplayer" (shareable, collaborative sessions), which most chat products still lack. (14:22-14:53)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Stateful Remote MCP Servers Persist Agent Memory Across Clients](stateful-remote-mcp-servers-persist-agent-memory-across-clients.md)
- [Use Resumable Streams as the UI Boundary for Durable Agents](use-resumable-streams-as-the-ui-boundary-for-durable-agents.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [Treat long waits as logical workflow state](treat-long-waits-as-logical-workflow-state.md)

Sources:
- [Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](../sources/20260608_SKDJo2CopRs.md), 02:20-05:55, 13:34-16:08
