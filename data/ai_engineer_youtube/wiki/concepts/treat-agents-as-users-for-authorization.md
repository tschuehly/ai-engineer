# Treat Agents As Users For Authorization

Summary: Agent backends should authorize every tool and data access as if an end user made the request. Running the agent on a server does not justify service-level authority or LLM-decided authorization.

Use when:
- Designing multi-tenant tools, databases, or document access for an agent.
- Reviewing whether an agent backend is using service tokens where user-scoped checks are required.

Details:
- Casco found cross-user data access by inspecting leaked tool definitions such as user-by-ID and document-by-ID lookup, then using an ID from a product demo to retrieve another user's personal information. 04:20-05:18
- The failure mode is an insecure direct object reference: the system validated that a token existed, but did not also verify that the requester was authorized for the referenced object. 04:45-04:59
- Interconnected user IDs, chat IDs, and document IDs can let an attacker traverse more of the system once one object reference leaks. 05:20-05:38
- The fix is to separate authentication from authorization and enforce an access-control matrix or row-level security check against the requester for each object. 05:41-06:11
- Developers may pattern-match server-hosted agents as services and grant service-level permissions, but agent actions should be treated like user actions; the LLM should not decide authorization. 06:29-07:15

Related topics:
- [Agents](../topics/agents.md)
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Identify the human subject behind agent actions](identify-the-human-subject-behind-agent-actions.md)
- [Authorize High-Impact Agent Actions Transactionally](authorize-high-impact-agent-actions-transactionally.md)

Sources:
- [How we hacked YC Spring 2025 batch's AI agents - Rene Brandel, Casco](../sources/20250730_kv-QAuKWllQ.md), 04:20-07:15
