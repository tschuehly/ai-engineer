# First-Class Agent Users Need Identity, Scopes, and Audit Trails

Summary: Agents operating inside team platforms should be modeled as first-class users with identity, history, scoped access, install and admin controls, and audit trails. This makes agent work governable and inspectable instead of treating it as anonymous automation behind a generic integration token.

Use when:
- Building SaaS or collaboration-platform integrations for autonomous agents.
- Reviewing whether an agent platform has enough governance for team work.

Details:
- Linear models agents as first-class users with identity and history, and says users can see what agents do through a full audit trail of events (14:39-14:53).
- Agents are installed through OAuth, then admins can manage the agent and its access after installation (14:53-15:04).
- A mature GraphQL API lets agents do product actions a human could do, while granular scopes constrain that authority (15:07-15:20).
- Agent-specific webhooks notify the agent when it is triggered or receives replies, and additional scopes control whether the agent is mentionable or assignable (15:20-15:40).


- **What makes the identity real at runtime rather than by convention.** Linear's model describes agents as first-class users with their own history and audit trail; Anthropic's CI team describes the enforcement that has to sit under it. If the agent can assert its own identity, a limit is only a suggestion — on hitting one, "it'll just change the header… instead of sachin, sachin2, and voila, you just have a fresh budget." Their answer is a proxy beside every agent session that holds the real credentials and stamps each call with the identity it already knows, "not the one that agent claims," so that ownership, quotas, rate limits, approvals, and trip wires are all "keyed on the same stamp and the agent never got to touch it." The audit-trail half is explicit too: for their skip and unskip operations "the agent itself is not responsible for writing the row… the agent technically never holds the pen on its own provenance." A per-session ID falls out of the same stamping, which is what lets an operator tell which of many concurrent sessions is misbehaving. See [stamp agent identity at the proxy](stamp-agent-identity-at-the-proxy-because-a-claimed-identity-resets-the-budget.md). ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 08:07-08:24, 17:26-18:47)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Identify the human subject behind agent actions](identify-the-human-subject-behind-agent-actions.md)
- [Treat Agents As Users For Authorization](treat-agents-as-users-for-authorization.md)
- [Record Workflow History for Agent Debugging and Compliance](record-workflow-history-for-agent-debugging-and-compliance.md)
- [Automate the Security Review Path Because Deals Stall There](automate-the-security-review-path-because-deals-stall-there.md)
- [Stamp Agent Identity at the Proxy, Because a Claimed Identity Resets the Budget](stamp-agent-identity-at-the-proxy-because-a-claimed-identity-resets-the-budget.md)

Sources:
- [Building the platform for agent coordination - Tom Moor, Linear](../sources/20250728_UG9IAdmi2Dg.md), 14:39-15:40
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 08:07-08:24, 17:26-18:47
