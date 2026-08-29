# Carry MCP JSON-RPC Over Internal Transports

Summary: MCP's message protocol can be reused over organization-specific transports when the client library ultimately receives readable and writable streams. The stable boundary is the JSON-RPC tool/resource/session protocol, while websocket, gRPC, Unix socket, or other internal routing can remain infrastructure choices.

Use when:
- Standardizing model context and tool integrations across internal products.
- Deciding whether custom transport requirements should block MCP adoption.

Details:
- The talk separates MCP's JSON-RPC message specification from the global transport standard around streamable HTTP, OAuth 2.1, and session management; most of the agent-integration value is in the message protocol and server interaction shape. 02:43-03:35
- Anthropic standardized on MCP internally for model context even when the stream traveled within one process, across data centers, or through enterprise networking, because the calling code still receives an MCP client session with tools and methods. 03:35-04:21
- Internal transports can be chosen to fit local infrastructure: the example uses websockets carrying JSON-RPC blobs into an MCP SDK client session, and notes that gRPC, Unix sockets, or even unusual message carriers can work if they provide the read/write stream boundary. 09:44-11:18
- Treating transport as an implementation detail lets teams keep external MCP compatibility while adapting internal routing, multiplexing, and network constraints to their own platform. 09:44-11:18
- **A consumer-product instance of transport as an implementation detail, and a reminder that transport choices decay.** Figma's local server rides an Electron IPC bridge from the web front end to a Node process, which exposes a server-events endpoint that MCP clients connect to directly on the machine — chosen because it was the fastest path to the user's file system with an authenticated session already in hand. The cautionary half: "a few weeks later after we started getting our initial architecture sorted a new version of the spec dropped uh deprecating the support type that we were going to use which was server events." Treating transport as replaceable is not only an architectural preference, it is insurance against the spec moving under a running build. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 01:46-01:56, 13:49-14:12)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Deploy Remote MCP Servers on Serverless Cloud Infrastructure](deploy-remote-mcp-servers-on-serverless-cloud-infrastructure.md)
- [MCP Gateways Create an Enterprise Root of Trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [An Installed Desktop App Is an Auth and Filesystem Beachhead](an-installed-desktop-app-is-an-auth-and-filesystem-beachhead.md)

Sources:
- [Remote MCPs: What we learned from shipping - John Welsh, Anthropic](../sources/20250619_0NHCyq8bBcM.md), 02:43-04:21, 09:44-11:18
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 01:46-01:56, 13:49-14:12
