# Fan Out a Scheduled Per-Entity Agent Instead of Waiting for a Trigger

Summary: When the deliverable is due at a known time rather than caused by an event, run the per-entity agent on a schedule: fan out one agent per account nightly, each composing the same four inputs — the served context store, the vector index, system-owned skills, and that user's own instructions — and have the artifact waiting when the person starts their day.

Use when:
- The output has a natural deadline (a meeting, a shift, a weekly review) rather than a triggering event.
- Choosing between a heartbeat, an event wake, and a batch schedule for a per-account agent.
- Designing the input set a background agent should assemble, and deciding which parts are owned by the platform and which by the user.

Details:
- **The shape.** "Putting all this together, you get an operational background agent. You have like every night we're going to go and generate these things, fan out a set of agents that are going to go and compute per account meeting prep." ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 12:33-12:44)
- **Four inputs, two of them not owned by the platform.** The agents "use some set of tools giving them access to that online CDP in Postgres I mentioned, the vector database, meeting prep skills that we own at the system level, as well as custom instructions that users are providing themselves." Splitting system-owned skills from user-owned instructions is what lets one nightly job produce differently-shaped output per person ([Let Users Author the Output Format as a Skill](let-users-author-the-output-format-as-a-skill.md)). (12:44-13:00)
- **The schedule is derived from the consumer, not from the data.** The brief exists because account managers are "in back-to-back-to-back meetings all day"; a nightly batch puts the artifact in place before the first one. There is no event to wait for — the meeting is already on the calendar, so the fan-out set is knowable in advance. (09:26-09:33)
- **Three scheduling disciplines now sit side by side in this wiki, and they answer different questions.** [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md) wakes on a smart trigger or heartbeat because the work is sparse and unpredictable over a deal cycle. [Emit Owner-Assigned Tasks From Signals, With a Marketing Default When None Fire](emit-owner-assigned-tasks-from-signals-with-a-marketing-default-when-none-fire.md) fires when a customer event changes what should happen next. A scheduled fan-out ignores both and computes for every entity in scope on a clock. Pick by whether the *demand* is scheduled: a meeting brief is, a churn intervention is not.
- **Cost scales with the population, not with activity.** A nightly fan-out spends on every account whether or not anything changed, which is the opposite of the dormancy argument. It is affordable here because the fan-out set is bounded by tomorrow's meetings rather than by the book of accounts — worth stating explicitly, because fanning the same pattern over every account is a materially different bill.
- **The retrieval each agent does is scoped, not global.** Agents run "some combination of vector search, attribute search, keyword search in order to pull information scoped to a specific account… without having to pull in the full raw corpus into agent context, which would also be very inefficient, very expensive." The attribute filter is what makes the per-entity scope enforceable rather than hoped for. (11:52-12:09)
- **Limit.** No run count, per-run cost, runtime, failure rate, or accuracy for the produced briefs is given, and no policy is described for a meeting that is added or cancelled after the nightly run. (12:33-13:00)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md)
- [Emit Owner-Assigned Tasks From Signals, With a Marketing Default When None Fire](emit-owner-assigned-tasks-from-signals-with-a-marketing-default-when-none-fire.md)
- [Let Users Author the Output Format as a Skill](let-users-author-the-output-format-as-a-skill.md)
- [Hydrate a Trigger Event to Its Entity Once and Persist the Mapping](hydrate-a-trigger-event-to-its-entity-once-and-persist-the-mapping.md)
- [Back the Served Context Layer With a Transactional Store for Referential Integrity](back-the-served-context-layer-with-a-transactional-store-for-referential-integrity.md)
- [Use Durable Execution for Production Agent Loops](use-durable-execution-for-production-agent-loops.md)
- [Push the Narrative Because Dashboard Adoption Is Always Uneven](push-the-narrative-because-dashboard-adoption-is-always-uneven.md)
- [Model LLM Calls and Tools as Durable Activities](model-llm-calls-and-tools-as-durable-activities.md)
- [Hybrid Retrieval Combines Lexical, Sparse, Dense, and Reranking Signals](hybrid-retrieval-combines-lexical-sparse-dense-and-reranking-signals.md)

Sources:
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 09:26-09:33, 11:52-13:00
