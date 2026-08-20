# Answer Unaddressed Questions Behind a Confidence Gate

Summary: An agent can watch a chat channel it was never addressed in, decide per message whether it has enough confidence to help, stay silent when it does not, and — when it is unsure but not hopeless — ask the person privately before answering in public. The cost this removes is interruption, not difficulty.

Use when:
- Engineers lose focus to questions that are easy for them and expensive to context-switch into.
- Deploying an agent into a channel where a confidently wrong answer would be acted on by colleagues.
- Designing an escalation path for an agent whose confidence sits between "answer" and "ignore."

Details:
- The cost being removed is explicitly interruption rather than effort: "I can be sort of heads down trying to build something, and then the eventual Slack notification comes in that like this channel somebody asked this kind of important question, and I just need to jump in there and try to provide context. It's not hard work. It's not hard for me to go answer questions, but it's disrupting me and if I don't go answer it, they won't get an answer for a while" (15:57-16:36). Both halves matter: the interruption is real and so is the latency if nobody takes it.
- The precondition is coverage of what people actually ask about: "our agent actually has access to a lot of information that people ask questions about. At least this is true internally" (16:36-16:44) — a scope qualification the speaker makes himself.
- The gate is per message and self-assessed: an agent watching "all of these sort of critical channels" that will "determine whether it has enough sort of confidence to answer the question or not" (16:44-16:52).
- No addressing is required, which is the point: "I'm not having to know that resolve exists. I don't have to like at mention resolve, whatever. I've set up this agent to sort of passively watch this channel" (21:01-21:14). Requiring an at-mention would put the burden back on the asker to know an agent exists and to judge whether it can help.
- The instruction is written so silence is the default: "if you see something that you think you have an answer for that somebody's kind of digging into, go ahead and respond. Otherwise don't." The demo shows the negative case as a result, not a failure — "here's a message that I posted that it's decided I don't need to respond to this" (21:14-21:28).
- The middle band gets a private escalation, which appeared without being designed: because "our agents have access to like Slack DMs and things like that… you can have an agent that basically will DM you to say, 'I think I know the answer to this, but I'm not sure. Can you confirm this for me before I, you know, respond back?'" (16:52-17:09). This converts an uncertain public answer into a one-line private check — a wrong guess costs one DM to one person rather than a wrong answer standing in a channel where others will act on it.
- The trigger type here is an event stream of chat messages rather than a schedule, which is what lets the same background-agent machinery cover a workload with no fixed cadence (11:49-12:13).
- Caveats: the confidence gate has no threshold, calibration method, or error rate anywhere in the talk — one declined message is shown, and no false-answer or false-silence rate is given. There is no discussion of what happens when a confident answer is wrong, of channel scoping or data boundaries for an agent reading critical channels and holding DM access, or of prompt injection, despite arbitrary chat messages being a trigger. Smith describes the DM behavior as "emergent," which is an honest description and also means it is not a guaranteed control.
- **The same "say nothing" option, reached from configuration rather than from a confidence score.** Gazit's agentic-workflow manifest declares outputs the run may produce and then adds: "I explicitly said you're allowed to do nothing… the last thing I want is noise. I don't want the agents denial of servicing me." The contrast is instructive. A confidence gate decides silence *per instance*, from the model's own estimate; a declared safe-output list makes silence a *permitted terminal state* for the whole job, so it holds even when the model is confidently wrong or has been injected. The two compose: the gate picks when to speak, the manifest bounds what speaking can consist of and caps how much of it there can be. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 08:26-08:48)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep Humans Aligned With Proactive Agent Work](keep-humans-aligned-with-proactive-agent-work.md)
- [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md)
- [Amend a Recurring Agent Task by Replying to Its Output](amend-a-recurring-agent-task-by-replying-to-its-output.md)
- [Plan Asynchronous Authorization for Background Agents](plan-asynchronous-authorization-for-background-agents.md)
- [Turn Unfiled Conversation Into Concrete Prototypes](turn-unfiled-conversation-into-concrete-prototypes.md)
- [Bound What an Unattended Automation May Emit, Including Emitting Nothing](bound-what-an-unattended-automation-may-emit.md)

Sources:
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 11:49-12:13, 15:57-17:09, 21:01-21:28
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 08:26-08:48
