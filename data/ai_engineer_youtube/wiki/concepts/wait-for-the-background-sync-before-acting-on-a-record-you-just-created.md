# Wait for the Background Sync Before Acting on a Record You Just Created

Summary: In a stack of pre-integrated SaaS tools, the tools sync to each other on their own schedule, outside your orchestrator — so a record you write to system A is not yet addressable in system B, and any workflow that writes then immediately acts has to poll for readiness instead of assuming it.

Use when:
- An automation intermittently fails with "record not found" on a system you just wrote to.
- Designing a workflow whose steps cross two vendors that also have a native integration with each other.
- Reviewing an agent plan that creates an object and then operates on it in the next step.

Details:
- The structural cause is that your orchestrator is not the only writer: "usually they are not fully orchestrated, which means that one system is talking to each other while I'm trying to talk to both of those systems at the same time." ([Berry](../sources/20260826_UhCY231d0FQ.md), 08:18-08:31)
- **The worked example is a two-vendor pair most GTM stacks have.** "If you have a Salesforce connected to Outreach or a sequencer, usually that CRM [and] sequencer are syncing independently of your orchestration system. And so if you create contacts in your CRM, you actually need to wait for that contact to sync to the sequencer before you can then take action on it." (08:31-08:47)
- The remedy named is explicit polling, not retry-on-error: "this creates some difficult problems where you actually need to introduce things like [waits] and loops to check if information is ready." The check is for *presence*, and it belongs in the workflow graph as a step rather than in an exception handler. (08:47-08:55)
- **Why this is not just a retry.** A retry assumes the operation failed; here the operation succeeded and the *view* has not caught up, so the failure surface is whatever the downstream system does with an unknown ID — often a silent no-op or a newly created duplicate rather than an error. That is also why the bug is intermittent: it depends on where in the vendor's sync interval your write landed.
- The latency is unbounded from your side. You do not own the sync schedule, cannot observe its queue depth, and get no completion event, which makes the wait a poll with a timeout rather than a barrier — and makes the timeout a business decision (drop the task, escalate, or proceed degraded) rather than a constant.
- **This is a concrete instance of the general orchestration diagnosis.** [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md) lists constant partial failure as a defining property of the distributed setup; this is the failure that most looks like a bug in your code and is not. It is also an argument for durable execution: a workflow that can suspend, poll, and resume from where it left off handles this natively, which is the shape [Use Durable Execution for Production Agent Loops](use-durable-execution-for-production-agent-loops.md) and Notion's Temporal workflows describe.
- The hazard compounds when an agent, rather than a fixed workflow, is doing the acting. A model that reads "contact not found" will often decide to create the contact — producing exactly the duplicate the sync was about to deliver.
- **Limit.** One example, no measurement: no observed sync latency, no failure rate, no timeout guidance, and no description of how Clay detects readiness beyond "waits and loops." Whether the check is a poll on the destination record, a webhook, or a fixed delay is not stated. (08:18-08:55)

Related topics:
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)
- [Build Orchestration From a Few General-Purpose Node Types](build-orchestration-from-a-few-general-purpose-node-types.md)
- [Use Durable Execution for Production Agent Loops](use-durable-execution-for-production-agent-loops.md)
- [Keep Workflow Orchestration Deterministic and Put Side Effects in Steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md)
- [Resolve Entities Across Vendors Before the Agent Reads the Record](resolve-entities-across-vendors-before-the-agent-reads-the-record.md)
- [Treat Every External System of Record as Non-Authoritative](treat-every-external-system-of-record-as-non-authoritative.md)
- [Protect Sender Reputation by Splitting Domains and Routing Replies Home](protect-sender-reputation-by-splitting-domains-and-routing-replies-home.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 08:18-08:55
