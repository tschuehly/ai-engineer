# Run a Signal Layer to Triage Comms and Protect Focus

Summary: A "signal layer" is an agent loop that reads your communication and tracking tools (Slack, Linear) on your behalf, deduplicates the asks, and surfaces only the real high-priority work. It acts as an attention facade so the human never opens those apps directly and gets pulled off task.

Use when:
- A developer loses focus to Slack threads, DMs, and ticket noise during agent-assisted work.
- Designing which integrations to wire into a personal coding-agent setup first.
- Deciding how an agent should mediate inbound asks rather than route them straight to the human.

Details:
- The motivating failure: combing Slack yourself is roughly 80% likely to get you distracted by another thread or a new ask, pulling you off the task you meant to do. (06:01-06:23)
- The pattern: give the agent read (and write) access to Slack and have it run on a loop to detect @-mentions, DMs, and genuinely high-priority asks that need action, while it also has Linear access via MCP so it can deduplicate asks and find the real tickets. (06:23-06:49)
- The goal is a facade, not full automation: it surfaces just enough signal for the human to keep attention on the work only they can do, instead of monitoring every channel. (06:42-06:49)
- Practical starting advice: pick the single highest-cost context switch for you (often Slack or Linear) and plug it into your preferred pane of glass first, rather than wiring every integration. (16:50-17:02)
- This is the inbound counterpart to delegating outbound work: the same Claude Code session that triages comms can act on the deduplicated ticket (e.g. fix a bug and verify its own work) and fire status back into the originating Slack channel via its MCP connection. (01:09-02:49)
- **The same pattern pointed at accounts rather than at messages.** Request Lens is a signal layer over customer state: it watches a joined model of internal and external data and surfaces only transitions — signup, surge, stop, watchlist arrival — so the team reads events rather than dashboards. The reusable structure is identical to comms triage (a noisy stream, a definition of significance, a human queue), applied to a domain where the most valuable signal is something ceasing to happen. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 03:53-04:42, 07:02-07:27)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Treat Human Attention as the Bottleneck for Agentic Work](treat-human-attention-as-the-agentic-bottleneck.md)
- [Drive Agents Remotely and by Voice to Decouple Work From the Desk](drive-agents-remotely-and-by-voice-to-decouple-work-from-the-desk.md)
- [Proactive agent systems need observation, personalization, timing, and workflow embedding](proactive-agent-systems-need-observation-personalization-timing-and-workflow-embedding.md)
- [Embed agent tools in existing work surfaces](embed-agent-tools-in-existing-work-surfaces.md)
- [Alert on Account Change Events, Including the Ones That Are Absences](alert-on-account-change-events-including-absences.md)

Sources:
- [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](../sources/20260611_so9l_MwS2yg.md), 01:09-02:49, 06:01-06:49, 16:50-17:02
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 03:53-04:42, 07:02-07:27
