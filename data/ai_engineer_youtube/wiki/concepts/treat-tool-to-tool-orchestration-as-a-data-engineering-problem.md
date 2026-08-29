# Treat Tool-to-Tool Orchestration as a Data Engineering Problem

Summary: Keeping ten to thirty operational tools in agreement is not integration work — it is a distributed data engineering problem with heterogeneous refresh cadences, per-field volatility, fan-out to many destinations, and continuous partial failure, and staffing or tooling it as "connect the APIs" is what makes agent systems act on a world view none of the tools actually holds.

Use when:
- An agent program is blocked on data being wrong in one system and right in another.
- Scoping the work between "we have the data" and "the agent can act on it."
- Deciding whether to buy an orchestration product or build one, and what it must cover.
- Estimating why an apparently simple sync keeps breaking.

Details:
- The definition is maintenance across disagreeing views: "in most cases, the view of the world that those tools have is different depending on where you look. And so, orchestration, in my view, is really the act of keeping all of that up to date." ([Berry](../sources/20260826_UhCY231d0FQ.md), 06:36-06:47)
- **The tool count is the scale claim.** The named base stack is "CRM, data warehouse, sequencer, a dialer, a note taker for call recording, and some chat interface like Slack" — six systems — but "I usually see like 10 or 20 or 30 tools that actually these teams are interfacing with." (06:57-07:26)
- Four properties turn it into data engineering rather than plumbing, and they are listed together. Heterogeneous cadence: "some systems need kind of like real-time updates one record at a time. Other systems are going to need hundreds of thousands of records, maybe updated once a day… monthly or weekly." Per-field volatility: "employee count change[s] all the time. Other data points like headquarters location change very rarely." Partial writes: "I'm not going to be making updates to all the fields at the same time. So I need logic within these systems that helps with that." Fan-out: "take a single system that I'm working with and actually fan its information out to multiple different systems." (07:19-08:08)
- **The fifth property is the operational one: failure is the steady state, not the exception.** "Because I end up with this kind of distributed setup, I also have failures that are happening all the time. So this turns into a fairly complex data engineering problem that we need to resolve." A system designed around a happy path will spend its life outside it. (08:08-08:18)
- The specific race this creates has its own page: your tools sync to each other outside your orchestrator, so a record you just wrote is not yet actionable elsewhere. See [Wait for the Background Sync Before Acting on a Record You Just Created](wait-for-the-background-sync-before-acting-on-a-record-you-just-created.md).
- The problem is symmetric across motion: asked whether this is outbound-only, the answer is that "the orchestration problem is pretty acute in inbound. You have to get the routing right. You have to qualify the account properly. There's usually historical context on inbound that comes in that needs to be understood." (18:14-18:33)
- **This is the tool-sprawl problem from the other side of the buy decision.** Snowflake's reps "using 15 different tools… and then they end up stitching all of that together in spreadsheets" describes the human paying the orchestration cost manually; the response there was consolidation into one governed store ([Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)). Berry assumes the tools stay put and the orchestrator absorbs the difference, which is the realistic assumption when the tools belong to other departments. Both accounts agree the disagreement is the problem; they disagree about whether you are allowed to delete it. ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 01:46-02:29)
- **Limit.** No numbers of any kind: no failure rate, no volume, no latency, no cost, and no description of how failures are detected, retried, or reconciled. The claim that this is "a fairly complex data engineering problem" is argued by enumeration, and the enumerated list comes from a vendor whose product sells against it. (06:19-08:18)
- **The consequence stated from the campaign side rather than the pipeline side.** Disagreeing tools are not merely untidy: "everybody's operating off of a different source of truth, and that makes it effectively impossible to go and distribute some coordinated action across these different go-to-market teams and channels." A multi-channel action cannot be defined over audiences that four systems compute differently, which is why the reconciliation work has to land before any orchestration layer above it is meaningful. ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 02:41-03:04)

Related topics:
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Wait for the Background Sync Before Acting on a Record You Just Created](wait-for-the-background-sync-before-acting-on-a-record-you-just-created.md)
- [Build Orchestration From a Few General-Purpose Node Types](build-orchestration-from-a-few-general-purpose-node-types.md)
- [Refresh Record Fields Selectively by Volatility and Price](refresh-record-fields-selectively-by-volatility-and-price.md)
- [Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Use Durable Execution for Production Agent Loops](use-durable-execution-for-production-agent-loops.md)
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Protect Sender Reputation by Splitting Domains and Routing Replies Home](protect-sender-reputation-by-splitting-domains-and-routing-replies-home.md)
- [Ship Go-to-Market Changes on an Engineering Release Cadence](ship-go-to-market-changes-on-an-engineering-release-cadence.md)
- [Distribution Is the Bottleneck, Not the Idea](distribution-is-the-bottleneck-not-the-idea.md)
- [Back the Served Context Layer With a Transactional Store for Referential Integrity](back-the-served-context-layer-with-a-transactional-store-for-referential-integrity.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 06:19-08:18, 18:14-18:33
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 01:46-02:29
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 02:41-03:04
