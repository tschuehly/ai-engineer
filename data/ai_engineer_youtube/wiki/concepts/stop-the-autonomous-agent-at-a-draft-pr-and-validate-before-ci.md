# Stop the Autonomous Agent at a Draft PR and Validate Before CI

Summary: Uber's cloud coding agent deliberately halts at a draft pull request without pushing to CI, for two reasons that are usually conflated: end-to-end features need feature-level validation that CI does not perform, and a fleet of agents pushing every attempt to CI is a load problem. The consequence is that visual and integration checks move into the inner loop — a simulator screenshot compared against the Figma spec, and a staged backend brought up against the new front end — before any build queue is touched.

Use when:
- Autonomous coding agents are saturating the build queue with attempts.
- Agent output is correct-compiling and wrong-looking, and CI has no opinion about that.
- Deciding what an agent must prove before a human or a pipeline sees its work.
- Extending a coding agent from toil tasks to user-visible features and finding the loop no longer holds.

Details:
- **The stopping point and its two reasons.** "It's going to stop at just creating a draft PR and it's not going to push it to CI yet. The reason being is that we were seeing that this was great for doing like toil sort of workloads, but to build more advanced end-to-end features we really need to be able to validate the feature first, and we want to prevent a lot of extra load coming on to CI. So if we can validate sooner before we push to CI, that would be a big benefit." ([Huda](../sources/20260821_17-YSUHo6Lk.md), 13:42-14:07) The load reason is the one usually left out of shift-left arguments, and at fleet scale it may be the binding one.
- **The task-class boundary is explicit.** The unchanged pattern was fine for toil; features are what broke it. That is a more precise statement of the wiki's staging advice than "start with maintenance" — it names *what* stops working, namely that a toil diff's correctness is legible in the diff and a feature's is not.
- **What moves into the inner loop.** Static analysis, with automatic repair of what it finds; then "visual validation — we can launch a simulator with a skill, grab a screenshot from the simulator, compare it to the Figma specs"; then "bring up the service and our backend staging environment and compare the front end and the backend integration together." Note that the design artifact is the oracle for the visual check, which only works because the same upstream flow produced the Figma mock-ups. (14:07-14:56)
- **The outer loop is not emptied, it is made recoverable.** "Errors can still happen on CI, so self-healing CI is something that we've implemented here where we can fix a lot of the issues that you hit on CI." Shifting checks left reduces arrivals at CI; it does not make CI failures stop happening, so the outer loop still needs its own repair path. (14:56-15:10)
- **The reviewer gets the evidence, not just the diff.** "If this is an autonomous diff coming from Minion, we want to give a human reviewer some confidence that this diff has gone through a lot of self-improvement already… on the PR you will have a table attached that says all these different checks that it went through, including the screenshots." The screenshots matter disproportionately: they are the only element a reviewer can judge without re-deriving the agent's reasoning. See [Make Intent and Evidence the Review Surface](make-intent-and-evidence-the-review-surface.md). (15:21-15:54)
- **The precondition is an environment that can run the checks.** A simulator launch, a service bring-up, and a staging comparison all happen inside the agent's environment, which is why this pattern depends on the pre-provisioned cross-repo pod described in [Pre-Provision Agent Environments With Snapshots and Prebuilt Indexes](pre-provision-agent-environments-with-snapshots-and-prebuilt-indexes.md). An agent that can only edit text cannot validate a feature.
- **Caveat.** No numbers: no CI load before and after, no rate at which visual validation catches something, no false-positive rate on the screenshot comparison, and no statement of how the Figma-versus-screenshot comparison is actually judged. The talk also does not say what happens to a draft PR that never passes inner-loop validation — whether it is discarded, retried, or handed to a human as-is.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Split Code Review Across the Loops and Size the Model to Each](split-code-review-across-the-loops-and-size-the-model-to-each.md)
- [Make Intent and Evidence the Review Surface](make-intent-and-evidence-the-review-surface.md)
- [Local-First Platform Workflows Shorten Agent Feedback Loops](local-first-platform-workflows-shorten-agent-feedback-loops.md)
- [Pre-Provision Agent Environments With Snapshots and Prebuilt Indexes](pre-provision-agent-environments-with-snapshots-and-prebuilt-indexes.md)
- [Treat CI and Experiment Capacity as the Scarce Resource Agent Throughput Consumes](treat-ci-and-experiment-capacity-as-the-scarce-resource-agent-throughput-consumes.md)
- [Run Verify-Fix-Review Loops for Agentic Refactors](run-verify-fix-review-loops-for-agentic-refactors.md)
- [Human Ownership Keeps Agent Pull Requests From Bypassing Review](human-ownership-keeps-agent-pull-requests-from-bypassing-review.md)
- [Stage Proactive Coding Agents From Maintenance to System Awareness](stage-proactive-coding-agents-from-maintenance-to-system-awareness.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 13:18-15:54
