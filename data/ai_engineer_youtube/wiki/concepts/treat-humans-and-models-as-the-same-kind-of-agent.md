# Treat Humans and Models as the Same Kind of Agent

Summary: Escalation is hard to hardcode because you cannot predict where it will happen. Widening the platform's definition of "agent" to cover both LLMs and humans — so any action either can take, the other can take too — turns escalation into a property of every step rather than a branch you had to anticipate, and leaves downstream steps indifferent to who acted.

Use when:
- An agent must be able to hand a decision to a human at an unpredictable point in its chain of actions.
- Regulated or clinical workflows require named human approval for some outcomes but not all of them.
- You are about to write per-step escalation branches, or a separate human path that reimplements the agent's actions.
- The same context must be presented to a model and to a person without maintaining two representations.

Details:
- **The two difficulties escalation actually poses.** First, it is dynamic: "you don't know in advance when exactly perhaps the agent's going to escalate. It could be that you're asking the AI to escalate when it's not sure … it could be that you define some sort of rules in your system, maybe in a medical context, the treatments going above a certain threshold means that it needs to be escalated … for an approval." Second, "humans and LLMs ultimately process context differently. You know, LLMs will have no problem if you give them massive massive amounts of text, but humans that's not the case." ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 12:57-13:47)
- **The primitive.** "If in your platform you enforce … a wider definition of agent which encompasses both LLMs and humans, then you can make it such that any action that can be taken by an LLM could also be taken by a human." ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 13:47-14:03)
- **What that buys is composability, not just an off-ramp.** "At any point in the kind of chain of actions that your agent is taking, it can escalate to a human, the human could perform that action, and then any step downstream doesn't care about whether it was a human or an LLM that did those actions upstream." Escalation stops being a terminal state that drops the run and becomes a substitution inside a run that continues. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 14:03-14:16)
- **One context definition, two renderings.** "You can define methods that take the context, which has some kind of shared definition of context, which is irrespective of whether it's a human or an LLM that's going to be accessing it. And you can take those methods to then map into something that's agent friendly, like a prompt, or into something that's more human friendly, for example, a UI." This is the concrete answer to the second difficulty: the divergence in how humans and models absorb context is handled at the presentation layer, not by keeping two systems. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 14:19-14:41)
- **It also produces an eval for free.** Because both kinds of agent can perform the same task, "for any task, you could get both the agent, the LLM agent, and the human to perform it, and your difference is your eval." See [let evals emerge from your architectural primitives](let-evals-emerge-from-your-architectural-primitives.md). ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 16:16-16:29)
- **Distinguish it from an approval gate.** [Routing high-impact actions through explicit human approval](route-high-impact-agent-actions-through-explicit-human-approval-gates.md) puts a human *in front of* a specific action the designer flagged in advance; equivalency makes the human an *alternative executor* of any action, which is what covers the escalation triggers you did not enumerate. The two compose: a gate decides that a human is required, equivalency decides what the human can then do.
- **Caveat carried in from elsewhere in this wiki.** Making the human path frictionless does not make the human attentive; [automation bias turns human-in-the-loop into a rubber stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md) when a person is handed a confident model's output to approve. Equivalency helps by letting the human act rather than merely ratify, but the review-quality problem is not solved by the primitive.

Related topics:
- [Agents](../topics/agents.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Let Evals Emerge From Your Architectural Primitives](let-evals-emerge-from-your-architectural-primitives.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md)
- [Keep the Expert as the Decider With AI in Their Loop](keep-the-expert-as-decider-with-ai-in-their-loop.md)
- [An Audit Trail Is a Chain of Evidence, Not a Developer Log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md)

Sources:
- [Why Your Enterprise Tech Stack Isn't Ready for AI Agents — Christopher Lovejoy & Saul Howard](../sources/20260819_mav15aW9lLM.md), 12:57-14:41, 16:16-16:29
