# Short-Lived IdP-Derived Tokens Reduce Standing MCP Access

Summary: XAA can improve MCP security by exchanging an active SSO session for short-lived access tokens, so revoked or locked identity-provider sessions stop new MCP access after token expiry.

Use when:
- Evaluating MCP credential lifetime and revocation behavior.
- Designing agent access after employee offboarding, device compromise, or suspicious activity.

Details:
- The talk warns that ordinary MCP OAuth flows can leave access and refresh tokens on local machines, outside the identity provider's direct revocation path, for days, weeks, or months. 05:17-06:14
- In the XAA flow, the user signs into the IdP once, the client obtains an IdP-backed identity JWT authorization grant token, and the MCP server's authorization server exchanges it for a normal OAuth access token. 10:04-11:49
- Because the downstream access token can be short lived, the client can rerun the IdP-backed exchange only while the user's SSO session is still valid. 12:20-12:50
- If the user's access is removed or the IdP session is locked, the client cannot obtain a fresh MCP token after the existing short-lived token expires. 12:50-13:06

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Cross-app access centralizes MCP authentication through the identity provider](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md)
- [Constrain sensitive file access with purpose-built tools](constrain-sensitive-file-access-with-purpose-built-tools.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)

Sources:
- [One Login to Rule Them All: Cross-App Access for MCP - Garrett Galow, WorkOS](../sources/20260428_EmhRyw6xeT0.md), 05:17-06:14, 10:04-11:49, 12:20-13:06
