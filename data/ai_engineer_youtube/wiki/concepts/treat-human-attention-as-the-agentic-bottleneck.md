# Treat Human Attention as the Bottleneck for Agentic Work

Summary: As coding agents scale toward infinite parallelism, the binding constraint shifts from agent capability to human attention, which degrades under load and does not scale. Workflows should be designed to conserve and protect attention, not just to maximize agent throughput, or the default outcome is faster burnout.

Use when:
- Designing personal or team coding-agent workflows that run many parallel or long-running agents.
- Explaining why "more agents" stops producing more output past a point.
- Deciding what humans should keep owning when agents do most implementation.

Details:
- The thesis: agents can loop infinitely until they hit the verification criteria you give them, but human attention is still "in meatspace," degrades under load, and is the hard constraint; the symptom is firing up four parallel agents and being wiped out by 11am. (03:36-05:12)
- What stays human is judgment and taste: knowing that something is actually solved and that the criterion is met in terms of human and business needs, not just that the agent reported done. (05:04-05:12)
- Context switching is the most expensive part and is now worse than ever because hyper-charged tools make it faster than ever to burn out, especially if a developer scales work linearly with what the tools can produce. (00:50-01:09, 04:23-04:52)
- Two paths follow: the default mindless path is "burnout turbo" — super fast and easier than ever, enabled by LLMs — while the intentional path delegates the minutiae to agents while the human stays responsible for quality, review, and shipping. (16:18-16:50)
- The recommended starting move is to build one single layer (e.g. plug Slack or Linear into your preferred pane of glass, or add one verification gate) and spend the recovered margin on time away from the desk, rather than reinvesting all gains into more work. (16:50-17:35)
- A holistic-wellbeing extension treats the developer's body as part of the loop: an Oura ring connected via MCP lets the model flag poor sleep and propose stopping early; the human can override it, but at least the tradeoff was considered. (15:31-16:18)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Run a Signal Layer to Triage Comms and Protect Focus](run-a-signal-layer-to-triage-comms-and-protect-focus.md)
- [Drive Agents Remotely and by Voice to Decouple Work From the Desk](drive-agents-remotely-and-by-voice-to-decouple-work-from-the-desk.md)
- [Fractured Attention Becomes Usable With Delegated Agents](fractured-attention-becomes-usable-with-delegated-agents.md)
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)

Sources:
- [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](../sources/20260611_so9l_MwS2yg.md), 00:50-05:12, 15:31-17:35
