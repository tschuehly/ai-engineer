# Collaborate With Complex Agents Through High-Bandwidth Artifacts

Summary: Chat is a flexible input channel, but it is a poor primary collaboration surface for complex agent work. Persistent artifacts such as documents, tables, comments, tagged agents, and domain-specific review primitives let humans steer and inspect the exact part of the work that matters.

Use when:
- Designing UX for long-running or vertical-domain agents.
- Deciding whether chat should be the main agent interface or only an input layer.
- Building review surfaces for agent-produced documents, tables, reports, or plans.

Details:
- Linear chat collapses a large work tree into one low-bandwidth sequence, which makes it hard to answer many questions, inspect local context, or correct only the affected node. 11:15-11:39
- The talk recommends persistent high-bandwidth artifacts that differ by industry and task. For legal work, a document can support highlighting a clause, changing only that clause, adding comments, tagging agents or collaborators, and handing off parts of the document to specialist agents. 11:43-12:18
- A tabular review is presented as a known legal primitive: the agent reviews many contracts, flags a few items needing a human take, and gives the reviewer a fast way to inject judgment before the agent continues. 12:18-12:53
- Chat boxes remain useful as flexible input, but should not be the main collaboration mode for complex agents; agents are not humans and should not be constrained to human-only language interfaces. 12:56-14:02

- Matt Dailey (Ref) reaches the same conclusion from the engineering-team side rather than the vertical-domain side, and adds a second charge against chat. Chats are "the relic of building for implementation… default isolated and ephemeral and… brain off," so decisions made inside one "are not shared with my team [and] are going to disappear," leaving only the code behind. Where the Legora argument is that chat is *low-bandwidth* for steering complex work, this one is that chat is *lossy*: the reasoning is deleted at session end. His replacement is a durable shared document holding the state of the work — "your core atom of your work is a doc rather than a chat." ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 10:38-11:35, 14:23-14:30)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Purpose-built agent workspaces make orchestration visible](purpose-built-agent-workspaces-make-orchestration-visible.md)
- [Canvas-native agents turn spatial work surfaces into prompt context](canvas-native-agents-turn-spatial-work-surfaces-into-prompt-context.md)
- [Make the Doc the State and the Agent the Action](make-the-doc-the-state-and-the-agent-the-action.md)

Sources:
- [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../sources/20260422_XNtkiQJ49Ps.md), 11:15-14:02
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 10:38-11:35, 14:23-14:30
