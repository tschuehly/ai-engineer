# Amend a Recurring Agent Task by Replying to Its Output

Summary: When a standing agent job produces output you do not like, the cheapest place to correct it is the thread the output arrived in. A reply such as "this is too verbose, make it shorter" should edit the job's persistent specification, not just this run — so the next firing is already different and nobody has to find a settings page.

Use when:
- Recurring agent reports are ignored because tuning them means leaving the channel where they land.
- Deciding whether feedback on an agent's output applies to the current run or to the standing task.
- Designing the create-and-refine loop for scheduled agents that non-specialists will own.

Details:
- The amendment happens in the report's own thread: "you can always just come back in this thread and… 'this is too verbose. Verbose. Make it shorter'" (20:26-20:40).
- The effect is on the stored task, not the delivered message: "the agent is able to update its task underneath, and able to sort of give you the answer like update so that the next time it fires, it's not going to be as verbose. And I can tell it explicitly what I want" (20:44-20:58). The distinction is the whole idea — a one-shot correction leaves the same report arriving tomorrow.
- The job being tuned is the on-call handoff report, containing "a summarization of all of the work that was done over the last day… a bunch of different sort of investigation summaries that we did, some notable changes, work completed," plus a critical open item (19:59-20:26). Verbosity is exactly the kind of preference that is invisible until the first output lands, which is why it should be correctable at the point of delivery.
- Creation works the same way and includes a clarification round: "this is me sort of saying, 'Hey, I want to do a new recurring health summary for my team.' So the agent's going to take a look at my environment, it's going to explore my environment a little bit, and eventually likely come back and ask me a couple questions about what I want to see, what kind of reports do I want, how verbose do I want it, etc… and it's going to set up that sort of initial thing for me so that I can test it out, make sure it's working, and then share it with the rest of my team" (22:17-22:47). The agent surveys the environment before asking, so its questions are about a real system rather than a blank form; the output is a testable draft, then a shared job.
- The surface choice follows from the same reasoning. A UI exists — "you can always go down and inspect all the different tasks that you have and view their reports, view previous runs. You can see all the work that the agent has done underneath" (21:40-21:56) — but it is deliberately secondary: "we think the surface area being where you live, right? So, Slack… or MS Teams if you're on MS Teams, as this kind of first party experience" (21:56-22:11), and "you open resolve just to kind of see what the top findings are, but ideally a lot of your interaction is kind of in the places that you're already kind of doing work" (24:20-24:31).
- The pattern implies a task record with a durable, editable specification and an audit trail of runs — otherwise "update its task underneath" has nowhere to write, and a review of prior runs cannot explain why the report changed shape.
- Caveats: this segment was not shown completing on stage — "no time to watch this actually go, but this works" — so the audience saw the posted instruction and prior output, not the round trip, and the demo Slack workspace is explicitly synthetic. Nothing is said about who may amend a task shared with a team, whether amendments are versioned or reversible, or how an ambiguous reply in a thread is distinguished from ordinary discussion of the report.

Related topics:
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Map External Conversation Threads to Agent Task IDs](map-external-conversation-threads-to-agent-task-ids.md)
- [Make One Agent Session Reachable From Every Interface](make-one-agent-session-reachable-from-every-interface.md)
- [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md)
- [Keep Humans Aligned With Proactive Agent Work](keep-humans-aligned-with-proactive-agent-work.md)
- [Answer Unaddressed Questions Behind a Confidence Gate](answer-unaddressed-questions-behind-a-confidence-gate.md)

Sources:
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 19:59-20:58, 21:40-22:47, 24:20-24:31
