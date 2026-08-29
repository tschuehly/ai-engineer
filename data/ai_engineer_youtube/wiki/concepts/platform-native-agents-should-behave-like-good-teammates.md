# Platform-Native Agents Should Behave Like Good Teammates

Summary: Agents embedded in collaboration platforms should follow the interaction norms of that platform: acknowledge quickly, restate the understood task, update shared state, continue in threads, clarify before acting, and keep comments concise. Good platform behavior is part of agent reliability because it determines whether humans can supervise and trust ongoing work.

Use when:
- Designing agent UX for issue trackers, Slack, support tools, or project-management products.
- Writing behavior guidelines for agents that interact with humans in shared work surfaces.

Details:
- A triggered agent should respond quickly and precisely; even a lightweight reaction can reassure users that the request was received (16:37-16:55).
- The first response should confirm the concrete action the agent understood, such as producing a PR for the requested issue, so users can catch misinterpretation early (17:00-17:18).
- Agents should inhabit the platform's language and conventions rather than forcing users into a separate interaction model (17:21-17:53).
- If an agent is working on an issue, it should update workflow state such as moving the issue to "in progress," because humans expect teammates to keep shared status current (17:57-18:11).
- Thread replies should continue the interaction without requiring another explicit mention, and coding agents should often form and communicate a plan before taking action (18:13-18:55).
- Output should be concise and useful; dumping raw LLM text into comments or issues creates work rather than value (19:00-19:24).
- **The teammate framing as an internal operating default, with the three properties named.** At Anthropic the advanced mode is "thinking of it as a teammate that actually holds context, has memory, and can be proactive," which shifted the company's default from "most people off in their own CLIs" to "multiplayer async proactive." Those three properties are what separate a platform-native agent from a chat-shaped one: without memory it re-onboards, without proactivity it waits, and without shared context its updates are not legible to the humans in the channel. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 08:44-10:00)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Embed agent tools in existing work surfaces](embed-agent-tools-in-existing-work-surfaces.md)
- [Review research and plans before they multiply into code](review-research-and-plans-before-they-multiply-into-code.md)
- [Map external conversation threads to agent task IDs](map-external-conversation-threads-to-agent-task-ids.md)
- [Make Delegation Multiplayer So People See Larger Asks](make-delegation-multiplayer-so-people-see-larger-asks.md)

Sources:
- [Building the platform for agent coordination - Tom Moor, Linear](../sources/20250728_UG9IAdmi2Dg.md), 16:16-19:24
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 08:44-10:00
