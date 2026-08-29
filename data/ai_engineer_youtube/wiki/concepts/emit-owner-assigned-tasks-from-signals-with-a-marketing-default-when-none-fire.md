# Emit Owner-Assigned Tasks From Signals, With a Marketing Default When None Fire

Summary: Make the unit of the decision layer a signal — one customer event important enough to change what should happen next — and have the service that watches for it decide three things: whether an action is available, who owns that action, and what concrete task to emit. Then handle the common case the design forgets: when no signal fires, route the customer to an automated default rather than dropping them.

Use when:
- Turning a customer or usage data model into work that humans and agents actually pick up.
- Deciding whether an event system should notify, recommend, or assign.
- Covering the silent majority of entities that never trigger anything.

Details:
- The unit is defined tightly: "a signal is a single customer event that's important enough to change what should happen next for a customer." Importance is defined by consequence, which is what keeps the signal set from becoming a metric feed. ([Liu](../sources/20260826_L4I7WgiEquo.md), 11:26-11:35)
- Signals split by initiator. User-driven ones are things the customer did — "hitting their AI limit," reaching out through contact sales — while external ones are "not user initiated at all": a company raising funding, hiring signals, a shift in their tech stack. "Those external signals are what allowed us to be proactive instead of reactive." (11:35-11:59)
- **The service assigns an owner, which is the step that separates this from an alerting system.** It "watches the customer profile, decides whether a single action is available, decides who should own that action, and then it emits a concrete task" — and "this task could be for a human or an agent," with a rep's task landing "in their Notion database" where they can act on it. (12:00-12:27)
- The output is a task in the assignee's existing work surface, not a notification: a rep "starts their day with an already prioritized task box" where the outbound draft is "already pre-researched and available for them to review." (16:14-16:41)
- **The no-signal branch is a designed path, not a gap.** "If there is no signal about a customer, the marketing component of our system kicks in. We have a predictive engine that will recommend product features most relevant for that customer and it will send out lifecycle emails and in-app nudges or multichannel communication to drive a customer towards adoption automatically." Signal-driven sales work and predictive lifecycle marketing are the two halves of one router rather than two programs. (12:29-12:53)
- The single-classifier routing primitive is what stops the two halves from both firing at the same customer — centralizing the decision is credited with preventing double sends. (08:26-08:37)
- The strongest reported number belongs to the default branch, not the signal branch: "users who received context-aware recommendations were 63% more likely to take the next step," with no absolute rates, control description, sample size, or definition of the step. (19:07-19:14)
- **Limit.** No signal taxonomy, volume, precision, or threshold definition is given; the predictive engine is named only by its output; and how a signal's owner is chosen is not described. (11:20-12:53)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Alert on Account Change Events, Including the Ones That Are Absences](alert-on-account-change-events-including-absences.md)
- [Make Routing and Eligibility a Shared First-Class Primitive](make-routing-and-eligibility-a-shared-first-class-primitive.md)
- [Reduce Every Workflow to Know, Decide, Act, and Learn](reduce-every-workflow-to-know-decide-act-and-learn.md)
- [Proactive Agent Systems Need Observation, Personalization, Timing, and Workflow Embedding](proactive-agent-systems-need-observation-personalization-timing-and-workflow-embedding.md)
- [Repo-Local Markdown Tasks Give Agents Durable Scoped Work Units](repo-local-markdown-tasks-give-agents-durable-scoped-work-units.md)
- [Run a Signal Layer to Triage Comms and Protect Focus](run-a-signal-layer-to-triage-comms-and-protect-focus.md)

Sources:
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 08:26-08:37, 11:20-12:53, 16:14-16:41, 19:07-19:14
