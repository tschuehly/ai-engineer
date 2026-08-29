# Discover Failure Modes From Production Outputs, Not Synthetic Cases

Summary: The failure-mode ontology is found, not designed. Put the system in production, cluster what actually goes wrong, and name the clusters — because the ways a real system fails are effectively unbounded and a synthetic test set can only contain the failures someone already imagined.

Use when:
- Starting an eval taxonomy and tempted to enumerate failure modes in a planning meeting.
- Deciding whether to invest in synthetic eval data or in production output review.
- You have a failure-mode list and want to know what it is for beyond being a checklist.
- Explaining why a suite that passes keeps being surprised by incidents.

Details:
- **The instruction.** "You don't write that rubric in a vacuum. You have to put the system in production and look at the real outputs. Cluster what goes wrong and the failure modes surface on their own. You name them. This is your failure mode ontology. Discover from your data, not guess on a whiteboard." ([Fox](../sources/20260822_yqF6XhzbWBk.md), 14:01-14:19)
- **Why it cannot be shortcut, stated as a coverage argument rather than a quality one.** "The ways that a real system goes wrong are effectively unbounded, and synthetic test cases only cover the failures you already imagined. The ones that hurt you are often the ones that you didn't. And you'll only find those in real outputs." Synthetic data is not accused of being unrealistic; it is accused of being a projection of the author's hypothesis space. (14:19-14:39)
- **What the ontology is used for.** Two jobs, both indirect: "this ontology is your map — what to capture judgment on, what to retrieve against, including the failures that you never thought to check for." It decides which outputs go in front of experts and how judged cases are indexed for retrieval. (14:19-14:39)
- **What it is explicitly not.** "Those discovered modes, they're not a checklist that the judge runs, but they organize everything." This is the distinction that separates this page from a conventional taxonomy: running the list at judge time reintroduces the frozen standard the whole method exists to avoid, because the list can only name modes discovered so far. (14:39-14:59)
- **A worked discovery, at small scale.** Fox's own catalogue came from generating notes across three leading ambient scribes and mapping every error found, plotted with consequence on one axis and automated-check detectability on the other. The finding that motivated everything downstream is a distribution rather than a case: "a handful up top get caught. But almost everything sits below the line," concentrated in "the high stakes and missed ones." Charting detectability against consequence — rather than counting errors by type — is what makes a discovery pass actionable. (03:29-04:36)
- **The loop closes back here.** "When a brand new failure mode appears, discovery surfaces it and it flows straight back in," which is why discovery is a standing activity rather than a project phase, and why the ontology is expected to keep growing rather than to converge. (15:39-15:59)
- **How this sharpens the wiki's existing ontology page.** [Failure-Mode Ontologies Prioritize Domain AI Work](failure-mode-ontologies-prioritize-domain-ai-work.md) records Anterior's use — label reviewed errors, chart which labels drive the north-star metric, rank the backlog — which is the ontology as a *prioritization* index over engineering work. This source adds a second use with a different consumer: the same labels index the retrieval corpus a judge reads at scoring time. A team that builds the ontology only for the backlog will have built the artifact and not connected it to the judge.
- **Relation to the coverage limit already recorded here.** [Evals Only Cover Known AI Product Failures](evals-only-cover-known-ai-product-failures.md) states the problem — suites cover named failures, and the unnamed ones are what hurt. This is a proposed procedure for narrowing that gap continuously, and it does not close it: discovery still only names what appeared in outputs somebody looked at, so the unbounded-failure argument applies to the discovery pass itself.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Failure-Mode Ontologies Prioritize Domain AI Work](failure-mode-ontologies-prioritize-domain-ai-work.md)
- [Evals Only Cover Known AI Product Failures](evals-only-cover-known-ai-product-failures.md)
- [Capture Expert Reasoning and Corrections, Not Just a Score](capture-expert-reasoning-and-corrections-not-just-a-score.md)
- [Assemble the Judging Standard Per Output From Retrieved Precedent](assemble-the-judging-standard-per-output-from-retrieved-precedent.md)
- [Connect Production Observability to Offline Eval Loops](connect-production-observability-to-offline-eval-loops.md)
- [Continuously Reconcile Eval Datasets With User Reality](continuously-reconcile-eval-datasets-with-user-reality.md)

Sources:
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 03:29-04:36, 14:01-14:59, 15:39-15:59
