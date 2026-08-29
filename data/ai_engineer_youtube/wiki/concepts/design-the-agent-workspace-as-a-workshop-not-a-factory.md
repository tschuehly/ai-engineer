# Design the Agent Workspace as a Workshop, Not a Factory

Summary: "Software factory" is the usual name for an agent-driven development system, and Abdalla rejects it — not as a style objection but because the metaphor loses the people in it and imports the wrong properties. Her replacement is a potter's workshop, which is an equally serious production system (dozens of apprentices, hundreds of handcrafted mugs a day) with four properties a factory framing does not emphasize: it reacts to events, it is inspectable, it modifies itself, and its owner watches how people work in it and changes the process accordingly.

Use when:
- Naming or scoping an internal agent-driven development system, and the default word on the slide is "factory."
- Deciding what to build after the pipeline works — where the next investment goes.
- Justifying observability spend on an agent system that already produces output.
- Explaining why a fixed, fully automated pipeline stops improving.

Details:
- **The objection.** "You might have heard this term of the software factory… I kind of want to push back on this term a little bit. I kind of actually hate it cuz I don't think it gets the point across and it feels a little — Where's the people in this?" ([Abdalla](../sources/20260822_L173Z8DpaJg.md), 14:21-15:04)
- **The workshop is presented as a system, not as craft nostalgia, and that is the load-bearing part.** The potter had "set up different stations for different components of the mug," "a specific process for sourcing clay and preparing ahead of time," and verification per component with named restart points — "If the dimple wasn't the right size, what would you do? What part of the process would you restart?" — at a scale of "dozens of apprentices in his shop and hundreds of mugs handcrafted per day." Stations, sourcing, and staged verification are factory concepts; the argument is not that the workshop has fewer of them. "Some people might think workshops are this quaint thing where it's like a workspace for a single individual, but… they're actually heavy-duty systems for doing work." (15:04-17:14)
- **Property one — automations that react to events.** "We expose things like the ability for these agents to implement automations that react to events in the real world the same way that a human in a workspace might need to react to a real event of a kiln being astray or a handle being broken." The examples are both failures rather than schedule ticks, which is the distinction from a cron-driven pipeline. (17:50-18:31)
- **Property two — inspectability, with its cost stated.** "My potter friend talked about how he actually watched the way people worked in his space and refined the process over time. That doesn't come for free. Your system has to actually be something that you can inspect and look into." The sequence matters: watching how the work is done is the input to refining the process, so observability is not a reporting feature but the precondition for property three. (18:31-18:49)
- **Property three — self-modification.** "The workspace is not the static component that doesn't change ever. It needs to react to what's going on and modify itself to amend to the goals of the people that are working in it and the product that it's producing." (18:49-19:08)
- **Property four — cost, stated as a joint constraint rather than a separate goal.** "You want to reduce the amount of buggy software that comes out of the other end of your factory… and you want to do this without compromising on cost, without spending too many tokens." Defect rate and token spend are named together, which is the same unit the wiki insists on elsewhere: quality per token, not either alone. (19:08-19:29)
- **What this adds to the wiki's existing factory page.** [Automation Loops Convert Repeated Review and Triage Into Factory Improvements](automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md) already holds the improvement loop, and this is the same claim with the ordering made explicit — you cannot run that loop without inspectability, and the thing you inspect is how people work in the system, not only what it output. The disagreement is narrow and worth keeping: that page's frame is a factory that automates stages while staying visible enough for humans to improve; this one says the visibility and the humans are the system, and the stages are the easy part.
- **Where the metaphor is doing real work versus decoration.** The wiki's [complicated-versus-complex diagnostic](match-the-harness-to-complicated-vs-complex-problems.md) already argues that a fixed factory harness fits decomposable problems and fails on interacting adaptive ones. Read against that, the workshop is a claim about which regime a development organization is in — a system with people who react to signals in it is complex by that definition, which is why a static pipeline stops improving. That is the version of this page worth acting on. The mug details are a talk device.
- **The stated purpose of the whole thing, and its scope.** "Building systems that remove toil and drudgery from our software process so that more people have the ability to build," with reproducing a bug and monitoring a production system as the named toil. The expansion is deliberate: "the definition of who a builder is is expanding to non-developers." (17:31-17:50, 19:29-19:47)
- **Evidence.** None. This is a framing argument with no measurement attached — no comparison of a workshop-shaped system against a factory-shaped one, no defect or token figures behind property four, and no description of what Warp's own event-reactive automations or self-modification mechanisms actually are.

Related topics:
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Automation Loops Convert Repeated Review and Triage Into Factory Improvements](automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md)
- [Match the Harness to Complicated vs Complex Problems](match-the-harness-to-complicated-vs-complex-problems.md)
- [Let the Agent Harness Emerge at Runtime (Adaptive Engineering)](let-the-agent-harness-emerge-at-runtime-adaptive-engineering.md)
- [Purpose-Built Agent Workspaces Make Orchestration Visible](purpose-built-agent-workspaces-make-orchestration-visible.md)
- [Put an Agent Approval Gate in Front of Maintainer Attention](put-an-agent-approval-gate-in-front-of-maintainer-attention.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)

Sources:
- [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../sources/20260822_L173Z8DpaJg.md), 14:21-19:47
