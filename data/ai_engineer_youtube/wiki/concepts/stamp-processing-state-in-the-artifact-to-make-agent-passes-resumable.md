# Stamp Processing State in the Artifact to Make Agent Passes Resumable

Summary: Write a processing marker — a timestamp, a version, a done flag — into each artifact the agent touches, and a repeated batch pass becomes incremental and resumable with no job queue, database, or state service: the corpus is its own checkpoint store.

Use when:
- Running an agent repeatedly over a growing folder of files, tickets, records, or documents where reprocessing everything each time is wasteful or destructive.
- Designing a scheduled or overnight agent job that must survive being interrupted, rate-limited, or run twice.
- Choosing between an external work-tracking store and in-artifact state for a batch enrichment pipeline.

Details:
- The instruction is one line in the skill: "Put a little time stamp on there so if we ask the agent to do another pass it remembers that some other agent did it in the past." The stamp is written by the same pass that does the work, so the record cannot drift from reality. ([LLM Knowledge Bases](../sources/20260812_I3bpdgFJCUY.md), 06:48-06:57)
- What it buys on the next run is the entire selection step: the automation "will go ahead and find any notes that weren't enriched in the past. So remember that at the top here we gave it a little timestamp every time it gets enriched. So the next time we ask an agent to do it, it was look for anything that's not tagged yet. It'll go through, run that whole flow across all those notes." (08:38-09:04)
- The scheduled cloud version depends on this and nothing else for work selection: the daily prompt tells the agent to "run enriched note across [n] notes that are not enriched yet." No queue survives between sandbox runs — the sandbox is torn down — so the only thing carrying state across days is the marker inside the synced Markdown. See [Run Recurring Knowledge Jobs in a Cloud Sandbox With Sync-Down/Sync-Back](run-recurring-knowledge-jobs-in-a-cloud-sandbox-with-sync-down-sync-back.md). (15:44-16:35)
- Why the marker belongs *in* the artifact rather than beside it: the artifacts are synced between machines by a tool that knows nothing about the pipeline (the Obsidian headless CLI, or a git clone). State stored in the file travels with the file for free; state stored in a sidecar database would have to be synced, reconciled, and kept consistent with files edited by hand in between runs.
- The general form is stronger than the timestamp instance. A stamp that records *what version of the pass* ran, not just that one did, lets you re-enrich everything when the skill changes — the talk uses only a timestamp, so a rewritten `enrich note` skill has no way to invalidate already-stamped notes. That gap is not addressed in the source and is the first thing to add when adopting this.
- Related failure to watch: because the marker is what makes the pass skip work, anything that strips or reformats frontmatter silently causes full reprocessing, and anything that stamps before completing causes silent skipping of half-done artifacts. Stamp last.
- The same idea appears elsewhere in the wiki as durable file-based work units — see [Repo-local Markdown tasks give agents durable scoped work units](repo-local-markdown-tasks-give-agents-durable-scoped-work-units.md) — but there the file *is* the task; here the file is the subject and the state is a field on it.

Related topics:
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Run Recurring Knowledge Jobs in a Cloud Sandbox With Sync-Down/Sync-Back](run-recurring-knowledge-jobs-in-a-cloud-sandbox-with-sync-down-sync-back.md)
- [Constrain Agent-Generated Tags to a Reference Vocabulary](constrain-agent-generated-tags-to-a-reference-vocabulary.md)
- [Repo-local Markdown tasks give agents durable scoped work units](repo-local-markdown-tasks-give-agents-durable-scoped-work-units.md)
- [Ambient Agents Need Self-Maintenance and Memory Hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)

Sources:
- [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../sources/20260812_I3bpdgFJCUY.md), 06:48-06:57, 08:38-09:04, 15:44-16:35
