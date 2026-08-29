# The Human-Agent Handoff Is the Hard Part Once Agents Are the Decision Layer

Summary: When an agent takes over the reasoning and deciding for work a person used to do end to end, but a person still has to execute the last step, the binding problem stops being model quality and becomes coordination: the human may disagree with what the agent decided, or not know it happened at all.

Use when:
- Deploying agents into a workflow that still terminates in a human action — a call, a visit, a signature, a conversation.
- A technically working agent system is producing friction with the people it was built for.
- Deciding what an agent owes a human besides the outcome — notification, rationale, override.
- Prioritizing between improving the agent and improving what the human sees of it.

Details:
- Asked for the hardest problem across the whole stack, the speaker names none of the four he had just presented: "I think one of the harder problems is probably the interface between the human and the agent." ([Berry](../sources/20260826_UhCY231d0FQ.md), 16:51-17:12)
- **The role assignment that creates the problem.** "The most powerful use of agents within GTM is to act as the reasoning and decision layer for a lot of tasks that a sales rep was previously doing." Putting the agent at the decision layer rather than at the execution layer is what splits one person's job across two actors. (17:12-17:26)
- **Two distinct failure shapes, and they need different fixes.** "The rep might think that they should do something different" is a disagreement — it needs an override path and a way to see the agent's reasoning. "The rep might not know that the agent did something" is an awareness gap — it needs notification and a shared record, and it is the one that shows up in front of the customer. (17:26-17:38)
- The reason it cannot be designed away: "ultimately a human still needs to get on a call with a prospect, [so] coordinating the connection between what the automated systems are doing and what the human sales rep is doing and making that work well, I think is probably one of the hardest problems." As long as the terminal step is human, the handoff exists. (17:38-17:47)
- **The wiki's architectural answer to this is a substrate, and it is a partial answer.** [Put Humans and Agents on the Same Substrate Instead of an AI Layer on Top](put-humans-and-agents-on-the-same-substrate-instead-of-an-ai-layer-on-top.md) makes what the agent did *readable* by the same person, which addresses the awareness gap in principle. It does not address the disagreement, and it does not make anyone actually read — the second failure here is attentional, not architectural. A shared record the rep never opens before the call is indistinguishable from no record.
- The structural mitigation in the same talk is narrower and worth pairing: [Give Agents Their Own Fields in the System of Record](give-agents-their-own-fields-in-the-system-of-record.md) at least makes agent decisions identifiable as such when the human does look, which is a precondition for both disagreeing with one and noticing one.
- This is the counterpart of the rubber-stamp failure in [Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md). There the human nominally reviews and defers; here the human is not in the loop at all and finds out afterward. A system can have both, on different actions, and neither is fixed by better model output.
- **Limit.** This is an unelaborated opinion in a 90-second Q&A: no mechanism, no interface design, no incident, no measurement, and no claim that Clay has solved it. It is worth recording because of *where* it lands — the vendor's own ranking puts it above the four technical problems the talk was built around — not because of what it demonstrates. (16:51-17:47)
- **A design that attacks the disagreement half without naming the problem.** Ramp's answer to "the rep might think that they should do something different" is to put the sign-off with whoever owns the surface — the rep approves the CRM opportunity, the channel owner approves the campaign artifact — so the agent's decision is never final over someone else's territory. That addresses disagreement structurally; it says nothing about the unawareness half, since a rep who never opens the approval queue is exactly as uninformed as before. ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 13:25-13:28, 17:02-17:10)

Related topics:
- [Agents](../topics/agents.md)
- [Go To Market](../topics/go-to-market.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Put Humans and Agents on the Same Substrate Instead of an AI Layer on Top](put-humans-and-agents-on-the-same-substrate-instead-of-an-ai-layer-on-top.md)
- [Give Agents Their Own Fields in the System of Record](give-agents-their-own-fields-in-the-system-of-record.md)
- [Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md)
- [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md)
- [Shadow Your Best Human Before Encoding the Workflow](shadow-your-best-human-before-encoding-the-workflow.md)
- [Design Agent Presence With Visual Alignment and Handoff](design-agent-presence-with-visual-alignment-and-handoff.md)
- [Separate the Context Gap From the Expert Gap](separate-the-context-gap-from-the-expert-gap.md)
- [Gate a Generated Multi-Channel Campaign on the Channel Owner](gate-a-generated-multi-channel-campaign-on-the-channel-owner.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 16:51-17:47
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 13:25-13:28, 17:02-17:10
