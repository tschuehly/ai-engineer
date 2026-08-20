# Inject Concept Drift to Test What a System Forgets

Summary: A memory system that only ever accumulates is never tested on the harder half of the job. Deliberately invalidating part of what the system learned — a schema migration, a policy change, a renamed field — turns an accumulation test into a test of whether it can discard stale experience while keeping the rest, which is where humans are quietly good and models are not.

Use when:
- Designing an eval for agent memory, a running profile, a notes file, or a fine-tuning loop that runs against a changing system.
- A memory system works in eval and degrades in production, where the underlying schemas, APIs, or policies keep moving.
- Deciding what to put in an eval sequence beyond "more instances of the same thing."

Details:
- The mechanism, in the database task: "in the real world, there's often concept drift in the things you're doing. In the database example, let's say there's a migration of your database. Columns get dropped. There's new columns with different names added. The data format changes." ([Evaluating Continual Learning](../sources/20260812_iqloyWCGYQQ.md), 12:01-12:18)
- What the drift is testing, and why it is not the same as remembering: "As a human, you reason through all this uncertainty and you're able to update your priors. You know that there's still some information from the past that may be relevant, but from your exploration, you learn what to forget and you learn what's actually relevant to maintain over time." Some past knowledge survives the migration and some does not; sorting the two is the task. (12:18-12:31)
- The stated gap: "You kind of have an innate ability to maintain the stability and plasticity trade-off in your mind. But this isn't native to a lot of language models. And so if we give it a task after the database migration, it might struggle in its ability to detect and discard stale experience and simultaneously update from new experience." (12:31-12:50)
- Design position: drift is added on purpose and repeatedly — "this notion of concept drift is something we try to add a lot to our tasks to further test the limits of what memory and continual learning might look like in language model systems." (12:50-13:00)
- **Placement matters as much as presence.** The drift arrives partway through a sequence, after the system has had time to build up exactly the knowledge the migration invalidates. Injecting the change before the system has learned anything tests nothing; injecting it after is what makes the stale knowledge available to be wrongly reused.
- Realism is validated rather than assumed: instances were checked with domain experts against "is these the sorts of drifts you would expect and things you would expect to remember in an environment." A drift that no real system would produce measures a failure nobody will hit. (13:29-13:52)
- The failure this design catches is [a plasticity failure](classify-continual-learning-failures-as-stability-or-plasticity.md) — a system that keeps applying superseded knowledge, or that over-rotates and discards knowledge that survived. Without drift in the sequence, a memory eval can only detect the stability half.
- **What this adds to memory designs already in this wiki.** Several pages treat conflict as something memory should notice at write time — [Make Memory Notice Conflicts and Seek the Evidence That Settles Them](make-memory-notice-conflicts-and-seek-the-evidence-that-settles-them.md) — and hygiene loops as something ambient agents need. Drift injection is the eval-side counterpart: it manufactures the conflict on a schedule you control, so a conflict-resolution mechanism can be measured instead of argued for.
- Concrete drifts worth injecting, generalizing the schema example: a renamed or removed API field, a changed pricing or eligibility rule, a repository refactor that moves the file an agent memorized, a customer policy update that invalidates a stored preference, an opponent that changes strategy.
- Caveats: no result is reported for how any system performed on the drift instances specifically, only the qualitative epidemiology failure described elsewhere. Frequency, magnitude, and how many drifts per sequence are all unstated.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Classify Continual-Learning Failures as Stability or Plasticity](classify-continual-learning-failures-as-stability-or-plasticity.md)
- [A Learning Benchmark Needs Headroom, Shared Structure, and a Signal](a-learning-benchmark-needs-headroom-shared-structure-and-a-signal.md)
- [Measure Learning as Gain Over a Memory-Wiped Rerun](measure-learning-as-gain-over-a-memory-wiped-rerun.md)
- [Make Memory Notice Conflicts and Seek the Evidence That Settles Them](make-memory-notice-conflicts-and-seek-the-evidence-that-settles-them.md)
- [Ambient Agents Need Self-Maintenance and Memory Hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)
- [Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md)
- [Continuously reconcile eval datasets with user reality](continuously-reconcile-eval-datasets-with-user-reality.md)
- [Treat Memory as a Write-Manage-Read Control Loop](treat-memory-as-a-write-manage-read-control-loop.md)

Sources:
- [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../sources/20260812_iqloyWCGYQQ.md), 12:01-13:00, 13:29-13:52
