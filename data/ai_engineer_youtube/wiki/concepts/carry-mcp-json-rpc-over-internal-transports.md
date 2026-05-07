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

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Deploy Remote MCP Servers on Serverless Cloud Infrastructure](deploy-remote-mcp-servers-on-serverless-cloud-infrastructure.md)
- [MCP Gateways Create an Enterprise Root of Trust](mcp-gateways-create-an-enterprise-root-of-trust.md)

Sources:
- [Remote MCPs: What we learned from shipping - John Welsh, Anthropic](../sources/20250619_0NHCyq8bBcM.md), 02:43-04:21, 09:44-11:18
