# Rewrite Agent Memory in a Periodic Batch Pass Over Session Logs

Summary: "Dreaming" — feed the day's session transcripts plus the current memory state into a periodic batch process that extracts "new insights and new organized structures that essentially feed back and edit the memory," so tomorrow's sessions start smarter. It is the *manage* phase of the write–manage–read memory loop pulled out of the request path and run offline, which is what lets it be expensive, cross-session, and willing to delete.

Use when:
- An agent accumulates memories that are individually correct but collectively unstructured, contradictory, or stale.
- Inline memory consolidation is adding latency to user-facing turns.
- Deciding what a memory system should be allowed to do that a per-turn writer cannot.

Details:
- **The mechanism as described.** Inputs are the session transcripts and the *current memory state*; the output is edits to memory. Running it "as a periodic batch process" is the whole point — the pass sees many sessions at once, so it can notice patterns no single session could, and it is off the latency budget, so it can afford a large model and multiple passes. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 27:28-28:44)
- **Why it is the "manage" phase, not another "write" phase.** In the [write–manage–read loop](treat-memory-as-a-write-manage-read-control-loop.md), writing appends what just happened and reading retrieves it; managing is the phase that reorganizes, merges, and discards. A per-turn writer structurally cannot manage well: it sees one session, it is under latency pressure, and it has no basis for deciding that an older memory is now wrong. A batch pass has all three. Naming dreaming as *this* phase is what makes it evaluable — the question to ask of it is a management question ("did the reorganization improve retrieval?"), not a capture question.
- **The organizational tier.** Alongside per-agent memory, the talk describes an organization-scale memory holding "the team's runbooks and details," so the batch pass has a shared target as well as a private one. That raises a question the source does not answer: whose sessions may edit shared memory, and what stops one agent's mistaken conclusion from becoming everyone's premise. (28:20-28:44)
- **It is framed as newly feasible rather than newly invented.** The presenters attribute the feature's viability to model progress — enabled "as models have evolved and become more capable." Read that as an instance of the same dynamic as [harness fixes going stale](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md), running the other direction: capabilities that were previously too unreliable to hand to an unsupervised batch job become available, and the harness should be revisited for additions as well as removals. (27:28-27:45)
- **The unaddressed hazards, which are the reason to keep this page skeptical.** A process that edits memory can corrupt it, and the source gives no conflict-resolution rule, no rollback path, no versioning of memory state, and no statement of what happens when the rewrite is wrong. Nor is there any evaluation that rewritten memory produces better outcomes, or any cost figure for a nightly pass over all transcripts. Before adopting the pattern, decide those four things — resolution, rollback, evaluation, cost — because the source decided none of them in public.
- Provenance: an Anthropic vendor talk, where dreaming appears on a frontier/coming-soon list alongside scheduled deployments, self-hosted sandboxes, multi-agent orchestration, and outcomes. It is announced, not evaluated: no benchmark, no ablation, no user study, no cost. Record the shape of the idea; do not record it as a validated technique.

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Treat Memory as a Write–Manage–Read Control Loop, Not a Store](treat-memory-as-a-write-manage-read-control-loop.md)
- [Keep the Session Log Separate From the Context Window](keep-the-session-log-separate-from-the-context-window.md)
- [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md)
- [Do Not Outsource the Memory System](do-not-outsource-the-memory-system.md)
- [Incident Agents Turn Alerts Into RCA and Operational Memory](incident-agents-turn-alerts-into-rca-and-operational-memory.md)

Sources:
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 27:17-28:44
