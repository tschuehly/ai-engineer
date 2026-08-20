# Separate Execution From the Production Context That Judges It

Summary: A production task decomposes into execution — knowing the steps and having the tools to run them — and the environment-specific context that decides whether the result matters. The two are different capabilities with different sources, and the second is the scarce one, because it is what turns a retrieved number into a decision to escalate or stop.

Use when:
- Scoping an operations agent and trying to decide whether the gap is tool access or judgment.
- Evaluating a monitoring or on-call agent that can reach every dashboard and still produces output nobody acts on.
- Deciding what a per-company knowledge layer has to hold that a general model cannot supply.

Details:
- The definition is deliberately minimal: "a task is just execution and the context to understand how to actually execute the task." Execution is "understanding what to do and being able to execute that. Maybe having access to the tools" (10:17-10:36).
- The split is illustrated on one action: "it's one thing to go check a dashboard. It's another thing to say that metric smells off. And the execution is can load the dashboard. It's the production context that's going to say, this feels wrong. And I don't know if I can even explain why it feels wrong. It just feels wrong and I want to dig into the next layer of sort of understanding of that" (10:37-11:00).
- What the context half produces is a prioritization verdict, not a fact: "you need the execution engine, that's great, but you really need that production context that tells you is this important or not important" (11:00-11:12). An agent with tools but no context returns readings; an agent with both returns a decision.
- The claim is positioned against model progress rather than alongside it. Smith grants that "models have gotten incredibly capable over the last year, but especially over the last like 6 months or so," and locates the difficulty elsewhere: "truly understanding your environment and the way that your services interact and where the hotspots are, keeping track of all of that sort of understanding is incredibly difficult. But it's incredibly important for any model to be successful at the task that it needs to do" (06:36-07:11).
- The context is a moving target, which is what makes it a system rather than a document: "how do we have systems that not just can understand your environment at any one point, but grow as your system evolves? Because again, your system is evolving faster and faster. We need to keep up with learning about what's the current state, what's the current sort of causal chains that we need to be keeping an eye on" (07:14-07:32).
- The generalized version of the argument: "we need full stack AI. It's not just about the models anymore, it's about the context around the models and what the models can do inside of a specific domain" (03:00-03:12), restated as a cost claim in the closing — "cost of operational work… it's not just in the task execution, it's in the environment complexity. That's where the biggest issue is going to happen" (23:58-24:18).
- If the split holds, an operations agent is not portable between companies the way a coding agent is: the execution half transfers and the context half has to be rebuilt, which is the stated reason "we spend so much time on our knowledge system. Truly understanding your, you know, what your environment looks like, what your needs are" (23:09-23:28).
- Caveat: this is a vendor talk, and the learning system that supplies the context half is named repeatedly as the hard part but never described. No storage model, retrieval mechanism, staleness policy, or evaluation of the learned knowledge appears anywhere, and nothing in the talk is measured — there is no comparison between an agent with the context layer and one without it.

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Analyze Operational Health Over Time Slices Before Invoking Repair Agents](analyze-operational-health-over-time-slices-before-invoking-repair-agents.md)
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Last-Mile Domain Context Beats Model Chasing](last-mile-domain-context-beats-model-chasing.md)
- [Derive the Post-Deploy Check Plan From What Actually Changed](derive-the-post-deploy-check-plan-from-what-changed.md)
- [Expose Observability As Agent-Readable Feedback](expose-observability-as-agent-readable-feedback.md)

Sources:
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 03:00-03:12, 06:36-07:32, 10:17-11:12, 23:09-23:28, 23:58-24:18
