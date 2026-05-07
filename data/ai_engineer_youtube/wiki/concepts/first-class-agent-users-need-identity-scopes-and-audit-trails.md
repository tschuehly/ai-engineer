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

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Identify the human subject behind agent actions](identify-the-human-subject-behind-agent-actions.md)
- [Treat Agents As Users For Authorization](treat-agents-as-users-for-authorization.md)
- [Record Workflow History for Agent Debugging and Compliance](record-workflow-history-for-agent-debugging-and-compliance.md)

Sources:
- [Building the platform for agent coordination - Tom Moor, Linear](../sources/20250728_UG9IAdmi2Dg.md), 14:39-15:40
