# Move Production MCP From API Keys to Scoped OAuth Token Flows

Summary: Local MCP API keys are a development convenience, not a production authorization model. Shared remote MCP servers should use streamable HTTP plus OAuth 2.1 patterns such as PKCE, short-lived scoped tokens, token exchange, and client identity metadata instead of long-lived unscoped credentials.

Use when:
- Moving an MCP server from local stdio usage to shared remote deployment.
- Comparing API-key, DCR, and CIMD approaches for MCP client authorization.

Details:
- Scaling the common MCP setup of long-lived, broadly scoped API keys in config files or environment variables to hundreds or thousands of agents creates a serious security problem. 01:21-01:46
- Stdio MCP is a local, single-user, no-network setup; production use needs streamable HTTP so multiple clients and agent fleets can reach a horizontally scalable, governable server. 08:11-09:18
- Crossing from local stdio to production remote MCP brings OAuth, token management, CORS, TLS, rate limiting, and governance concerns all at once. 09:19-10:03
- API-key setups leave users provisioning, storing, and maintaining long-lived credentials that are rarely rotated, often unscoped, sometimes shared, and stored in client config or environment variables. 10:51-13:04
- Passing an API key through to an upstream API can create a confused-deputy vulnerability; mapping many users to one shared upstream credential makes revocation and compromise response worse. 13:04-13:32
- OAuth 2.1 with PKCE lets the authorization server validate the code challenge, send users through SSO and consent, and mint an access token for the MCP client. 16:26-17:48
- OAuth's authorization-code flow is the right mental model for end-user delegation to agent clients, while refresh tokens let access tokens stay short-lived and rotate without dropping the authorized connection. 02:57-03:18, 10:54-11:07
- Token exchange lets the MCP server trade a delegation token for a session token for the upstream API, so upstream calls do not depend on forwarding the original authorization header. 17:58-18:55
- Dynamic Client Registration handles unbounded client registration, but creates non-portable registrations and phishing risk because clients self-assert metadata at `/register`. 18:55-19:54
- CIMD uses a client-ID metadata document hosted at a client-controlled URL; this avoids a growing registration database, binds redirect URIs to client metadata, and lets authorization servers selectively allow or deny clients. 20:00-22:35
- **A third option that precedes both, available only to products that already ship a desktop client.** Rather than choosing between API keys and OAuth, Figma inherited an existing authenticated session: the Electron desktop app runs figma.com in its front end, an IPC bridge reaches a Node process with the user's file permissions, and a local server-events endpoint lets clients connect on the machine. "We punted so until [the March 2025 spec revision] there wasn't this [auth] spec to to build from and we could easily relay [auth] from our web app to our desktop app." This buys time on authorization and pays for it in reach — nothing running in CI, a cloud sandbox, or on a phone can connect. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 13:28-14:12)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Short-lived IdP-derived tokens reduce standing MCP access](short-lived-idp-derived-tokens-reduce-standing-mcp-access.md)
- [Cross-app access centralizes MCP authentication through the identity provider](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md)
- [Cross-app access does not replace authorization policy](cross-app-access-does-not-replace-authorization-policy.md)
- [Stateless remote MCP servers rebuild allowed tools per request](stateless-remote-mcp-servers-rebuild-allowed-tools-per-request.md)
- [Model MCP Servers as OAuth Resource Servers](model-mcp-servers-as-oauth-resource-servers.md)
- [An Installed Desktop App Is an Auth and Filesystem Beachhead](an-installed-desktop-app-is-an-auth-and-filesystem-beachhead.md)

Sources:
- [How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)](../sources/20250730_blmAkayzE8M.md), 01:21-03:18, 10:54-11:07
- [Your Insecure MCP Server Won't Survive Production - Tun Shwe, Lenses](../sources/20260408_BurJvbqFr4c.md), 08:11-22:35
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 13:28-14:12
