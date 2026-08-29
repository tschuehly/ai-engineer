# Run One Dormant, Long-Lived Agent Per Account

Summary: For work that unfolds over weeks or months against a single entity, instantiate one persistent agent per entity that is dormant almost all of the time, woken by a trigger or heartbeat, rehydrating its context from the data and orchestration layers on each wake — the agent's identity is the entity, not the session.

Use when:
- Designing agents for a deal cycle, a case, a patient, a project, or any process with a long clock and sparse events.
- Deciding between a per-request agent and a per-entity agent for stateful work.
- Choosing between polling every entity on a schedule and waking only the ones something happened to.
- Working out where a long-horizon agent's state should live.

Details:
- The three properties that make this class hard are named as a set: duration ("agents that run over a course of weeks or months that keep track of the state of an account throughout a deal cycle"), consequence ("a high bar for error because a lot of the results of our GTM work is customer communication and getting that wrong can have disastrous consequences"), and an impedance mismatch ("the agents are often doing unstructured work and pushing that into systems that are highly structured like a CRM. And so the mapping of what the agent is producing is super important"). ([Berry](../sources/20260826_UhCY231d0FQ.md), 10:38-11:21)
- **The architecture in one sentence.** "An agent that exists for each account and maintains a persistent state of that account. It's always going to execute, and because it's executing over [a course] of weeks or months, it's often going to be dormant for most of the time that it's available. So, we need to use smart triggers or a heartbeat or something to wake it up." (11:21-11:40)
- **State is rehydrated, not carried.** "When it wakes up, it needs to ingest the current context of the account from our data layer and our orchestration layer." The agent does not hold a months-long conversation; each wake is a fresh read against the shared substrate, which is what keeps it consistent with humans looking at the same record and bounds the context it must carry. This is the per-entity form of [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md) — the millisecond keyed profile exists precisely so a waking agent can reload in one shot.
- Feedback is part of the loop because the agent decides unsupervised: "because the agent is making decisions for us in many cases automatically, we need to allow for feedback on the agent as well." (11:40-11:47)
- Wakes can be time-based as well as event-based, and the delay can itself be the policy. The worked example is a closed-lost re-awaken agent reading Gong, email, CRM, and the warehouse, "triggered on a time basis. So, if we lose an account, we're not going to immediately go after that account again. We're going to wait for a little bit of time in order to attack it again." (12:43-13:03)
- **The learning half is explicitly unbuilt.** "The cutting edge of doing this is the learning phase where as the agent works on an account or a series of accounts, it updates its own view of what's working. Today in GTM, this is not fully solved yet. And in fact, the continual learning effort and the next best action suggestions are kind of one of the cutting edge problems that we're working on." Read the architecture as trigger-plus-rehydrate-plus-act; the improvement loop is aspiration in this source, and the wiki's other GTM sources report the same gap ([Thread Every Outcome Back to the Decision That Caused It](thread-every-outcome-back-to-the-decision-that-caused-it.md)). (11:47-12:10)
- The per-entity fan-out is the cost model. One agent per account means the population, not the traffic, sets the upper bound on concurrent state, which is why dormancy is load-bearing rather than incidental — and why the heartbeat interval is a spend decision across the whole book of accounts.
- **Limit.** No implementation is given: no state store, no wake latency, no heartbeat interval, no cost per account, no bound on how many agents run, and no account of what happens when two accounts merge or an entity is de-duplicated mid-cycle. The "high bar for error" is asserted and never measured, and no evaluation method for a months-long trajectory is offered. (10:38-13:03)

Related topics:
- [Agents](../topics/agents.md)
- [Go To Market](../topics/go-to-market.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Give Agents Their Own Fields in the System of Record](give-agents-their-own-fields-in-the-system-of-record.md)
- [Treat Long-Horizon Agents as Asynchronous Workers With Evolving Interfaces](treat-long-horizon-agents-as-asynchronous-workers-with-evolving-interfaces.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Alert on Account Change Events, Including the Ones That Are Absences](alert-on-account-change-events-including-absences.md)
- [Emit Owner-Assigned Tasks From Signals, With a Marketing Default When None Fire](emit-owner-assigned-tasks-from-signals-with-a-marketing-default-when-none-fire.md)
- [Thread Every Outcome Back to the Decision That Caused It](thread-every-outcome-back-to-the-decision-that-caused-it.md)
- [Resolve Entities Across Vendors Before the Agent Reads the Record](resolve-entities-across-vendors-before-the-agent-reads-the-record.md)
- [Use Durable Execution for Production Agent Loops](use-durable-execution-for-production-agent-loops.md)
- [Size Agent Quality Against the Channel's Reply Rate](size-agent-quality-against-the-channel-reply-rate.md)
- [The Human-Agent Handoff Is the Hard Part Once Agents Are the Decision Layer](the-human-agent-handoff-is-the-hard-part-once-agents-are-the-decision-layer.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 09:59-13:03
