# Scope Personal and Team Agents By Reachable Authority

Summary: Agent safety boundaries should match who can reach the agent and what that audience is allowed to know or do. A personal agent should be reachable only by its owner, while a team agent should be restricted to team-visible data and team-approved actions.

Use when:
- Exposing a powerful agent through chat, browser, email, messaging, or shared team surfaces.
- Deciding whether an agent should run in personal, group, team, or public-access mode.

Details:
- OpenClaw's security guidance is that a personal agent should not be placed in a group chat; if anyone can talk to the agent, they may be able to exfiltrate anything the agent can access, 10:59-11:32.
- A team agent should only know what the team can know and should not hold unrelated secret data, 11:32-11:45.
- Steinberger names the general high-risk combination as access to private data, access to untrusted content, and the ability to communicate; powerful agents with all three need stronger controls, 13:49-14:35.
- Marking website or email input as untrusted can reduce prompt-injection risk, but unlimited access to an agent or weak local models without defenses still leaves risk, 36:12-37:34.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)
- [Capability-based sandboxes start with no authority](capability-based-sandboxes-start-with-no-authority.md)

Sources:
- [State of the Claw - Peter Steinberger](../sources/20260417_zgNvts_2TUE.md), 10:59-11:45, 13:49-14:35, 36:12-37:34
