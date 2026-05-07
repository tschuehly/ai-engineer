# Authenticate Agents With URL-Based PKI Identities

Summary: Agent clients need verifiable identities when they request credentials or communicate on their own behalf. URL-based identifiers paired with public-key infrastructure, signed JWT assertions, or HTTP message signatures can make agent identity more trustworthy than anonymous dynamic registration.

Use when:
- Designing agent-to-agent or agent-to-MCP communication without a human delegation flow.
- Evaluating dynamic client registration for agent ecosystems.

Details:
- Client-credentials style OAuth flows matter when agents communicate with other agents or MCP servers on their own behalf rather than on behalf of a user. 10:54-11:21
- Manual developer-portal registration creates too much friction for open MCP ecosystems where tools and agents may not know about each other ahead of time. 11:24-11:58
- Dynamic client registration lets agents request client credentials at runtime, but the registration request is uncredentialed, which makes agents anonymous and weakens trust. 12:02-12:45
- URL identifiers can reuse the identity users already associate with an app or agent, while PKI lets the agent prove control by signing JWT assertions or HTTP message signatures that verifiers check against public keys. 12:49-14:02

Related topics:
- [Agents](../topics/agents.md)
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Identify the Human Subject Behind Agent Actions](identify-the-human-subject-behind-agent-actions.md)
- [Cross-App Access Centralizes MCP Authentication Through the Identity Provider](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md)
- [Preserve Authorization Chain of Custody Across Agent Hops](preserve-authorization-chain-of-custody-across-agent-hops.md)

Sources:
- [How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)](../sources/20250730_blmAkayzE8M.md), 10:54-14:02
