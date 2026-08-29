# An Installed Desktop App Is an Auth and Filesystem Beachhead

Summary: If your product already ships a desktop app that holds an authenticated session and can reach the file system, that process is a place to put a local MCP server — which lets you ship before the protocol has an auth story, before you have solved remote hosting, and with a data-residency answer enterprises already want. Figma took exactly this route and only built the remote server afterwards.

Use when:
- Deciding between a local (stdio or loopback) MCP server and a remote HTTP one for a first release.
- The protocol's authorization story is immature, contested, or newer than your ship date.
- Enterprise customers are raising data-egress objections to a hosted integration.

Details:
- Four requirements shaped the beta and they are worth copying as a checklist: "we wanted to launch quickly. Um we wanted to have the highest possible bar for our security. We wanted to respect file permissions. And we wanted to respect our pricing [and] packaging so we didn't have abuse vectors." The last is unusual to see stated and is a real design constraint — an agent-accessible surface can become a way to obtain a paid capability outside its packaging. 13:13-13:28
- The decision point: "after the spec changed and introduced O[Auth] in March 2025, we had to decide whether to keep our MCP server local or sort of switch to the new remote server using streamable HTTP and kind of like work on all the [auth] problems." They chose local — "we punted so until [then] there wasn't this [auth] spec to to build from and we could easily relay [auth] from our web app to our desktop app." 13:28-13:49
- The architecture, concretely: "the Figma desktop app is Electron and so the front end of it is a web app and we basically just run figma.com in that and then we have an IPC bridge between the two and that sends it to our node process that allows us to talk to the user's file system. Um we then sort of expose a server events server in node and that way clients could talk directly locally." 13:49-14:12
- What the desktop app supplies for free, and why this generalizes: an already-authenticated session (so no OAuth), a process with the user's own file permissions (so file access inherits the OS model rather than needing one), and a distribution channel that is already installed. A web-only product has none of these and has to build all three before it can ship anything.
- The enterprise angle is a side effect rather than a design goal: "The local story was also really great with enterprises because they kind of like the idea of our data not being sent anywhere." 14:12-14:18
- The stated primary reason is learning speed, not architecture quality: "this architecture was our fastest path to getting something into the hands of users to understand product market fit and what kind of tools and use cases folks had." Local was scoped to a population that could tolerate it — the server "was heavily designed for developer use cases. You kind of had to know what you were doing a little bit" — and developers were targeted "because they were the first to adopt AI workflows." 02:50-03:12, 14:18-14:25
- Local is a first step, not an end state, and the sequence is short: the local server launched, work on remote began "as soon as we launched," remote shipped in September, "we G[A]'d both servers in October 2025," and read and write capabilities followed. Both servers are maintained, not one replacing the other. 14:44-15:18
- **The generalizable trade.** Local buys time on authorization and data residency and pays for it in reach — it requires an install, it constrains the client to the same machine, and it cannot serve agents running in CI, in a cloud sandbox, or on a phone. Everything in this wiki's remote-MCP material, from [Deploy Remote MCP Servers on Serverless Cloud Infrastructure](deploy-remote-mcp-servers-on-serverless-cloud-infrastructure.md) to [Move Production MCP From API Keys to Scoped OAuth Token Flows](move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md), is the bill that comes due when reach starts to matter. The claim here is about ordering, not about which is correct.
- Outcome caveat: the only result reported is "one of the fastest growing products that they've ever had, which was not something we expected," with no figure, rate, or comparison product, and it is attributed to the local server, the remote server, and read/write capabilities combined rather than to this architecture.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Deploy Remote MCP Servers on Serverless Cloud Infrastructure](deploy-remote-mcp-servers-on-serverless-cloud-infrastructure.md)
- [Move Production MCP From API Keys to Scoped OAuth Token Flows](move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md)
- [Carry MCP JSON-RPC Over Internal Transports](carry-mcp-json-rpc-over-internal-transports.md)
- [Enterprise MCP Requires SaaS Security Controls](enterprise-mcp-requires-saas-security-controls.md)
- [Tools Are the Only Primitive Every Client Implements](tools-are-the-only-primitive-every-client-implements.md)

Sources:
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 02:50-03:12, 13:13-15:18
