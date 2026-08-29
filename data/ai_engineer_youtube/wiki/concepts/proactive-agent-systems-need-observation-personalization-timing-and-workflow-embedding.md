# Proactive Agent Systems Need Observation, Personalization, Timing, and Workflow Embedding

Summary: Proactive agents need enough situational awareness to act before an explicit prompt without becoming noisy or detached from the user's real work. The reusable design pattern combines continuous observation, personalization, timely intervention, and integration into existing work surfaces.

Use when:
- Designing agents that should notice work opportunities instead of waiting for a chat prompt.
- Evaluating whether an agent's proactivity will reduce mental load or create more interruption and supervision.

Details:
- The mental-load problem is that async agents can do work while humans still track completion, follow up, and decide what to ask next; useful proactivity should reduce that monitoring burden (00:39-02:21).
- Reactive developer tools are compute-efficient because they only run on explicit prompt or autocomplete request, but that model keeps the human responsible for managing AI work (03:26-03:50).
- A proactive agent needs observation over code changes, workflow patterns, and project context so it can notice friction and candidate work (04:29-04:46).
- Personalization is required because the agent must learn how the user works, what they care about, what they ignore, preferences, and areas of code they do not want touched (04:46-04:56).
- Timing is a product constraint: acting too early interrupts the user, while acting too late misses the useful moment (04:56-05:03).
- Workflow embedding matters because the agent should appear in terminals, repositories, and IDEs where the user already works rather than forcing attention into a separate app (05:03-05:20).
- **A production-operations vendor reports the same four elements with different content in each slot, which is evidence the pattern is not developer-tool-specific.** Observation is over change events, dashboards, and chat channels rather than code edits; personalization is per-environment rather than per-user ("every company is a unique place. That's why we spend so much time on our knowledge system"); timing becomes an explicit agent decision ("none of this is hard-coded in… it could decide, I want to wait for another hour"); and workflow embedding lands in Slack or MS Teams instead of the IDE — "we think the surface area being where you live." ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 19:10-19:45, 21:56-22:11, 23:09-23:28)
- **That source adds a trigger taxonomy this page leaves implicit.** "When does it work?" resolves to a schedule, an event stream, or a message — the three ways observation turns into an actual run — which is the concrete version of "notice work opportunities." See [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md). ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 11:15-12:18)
- **And it supplies a failure mode for the timing slot beyond too-early/too-late: not interrupting at all.** A channel-watching agent decides per message "whether it has enough sort of confidence to answer the question or not," and the instruction makes silence the default — "if you see something that you think you have an answer for… go ahead and respond. Otherwise don't." Proactivity that can decline is a different control surface from proactivity tuned by when it fires. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 16:44-16:52, 21:14-21:28)
- **The observation layer, with an event class that is an absence.** Exa's Request Lens fires "anytime something significant happens with any of our customers": a signup, a usage surge, a usage stop, or the arrival of a watched account. Three of those appear as rows in a log; "someone stopped using searches" does not, so the observation layer has to run over expected activity as well as observed activity. The timing and workflow-embedding halves are thin here — the output is a notification "that our team can act on," with no personalization, batching, or handoff described. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 07:02-07:27)
- **A go-to-market instance where the four elements are separable components.** Observation is a signal service watching the customer profile; personalization comes from a predictive engine that picks the most relevant product features when no signal fires; timing comes from the signal definition itself — "a single customer event that's important enough to change what should happen next"; and workflow embedding is literal, since the emitted task lands in the rep's own task database beside the account view they already open each morning. The proactive half is specifically the external, non-user-initiated signals — funding rounds, hiring, tech-stack shifts — which "allowed us to be proactive instead of reactive." ([Liu](../sources/20260826_L4I7WgiEquo.md), 11:26-12:53, 16:14-16:41)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Local OS agents can invert the prompt flow](local-os-agents-can-invert-the-prompt-flow.md)
- [Purpose-built agent workspaces make orchestration visible](purpose-built-agent-workspaces-make-orchestration-visible.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md)
- [Answer Unaddressed Questions Behind a Confidence Gate](answer-unaddressed-questions-behind-a-confidence-gate.md)
- [Alert on Account Change Events, Including the Ones That Are Absences](alert-on-account-change-events-including-absences.md)
- [Emit Owner-Assigned Tasks From Signals, With a Marketing Default When None Fire](emit-owner-assigned-tasks-from-signals-with-a-marketing-default-when-none-fire.md)

Sources:
- [Proactive Agents - Kath Korevec, Google Labs](../sources/20251213_v3u8xc0zLec.md), 00:39-05:20
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 11:15-12:18, 16:44-16:52, 19:10-19:45, 21:14-22:11, 23:09-23:28
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 07:02-07:27
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 11:26-12:53, 16:14-16:41
