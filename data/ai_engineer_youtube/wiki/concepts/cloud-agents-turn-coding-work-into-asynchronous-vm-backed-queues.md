# Cloud Agents Turn Coding Work Into Asynchronous VM-Backed Queues

Summary: Cloud coding agents let humans plan synchronously, then hand execution to isolated background environments that can run in parallel. This increases throughput only when context, setup, cost, and review handoffs are managed.

Use when:
- Designing parallel coding-agent execution beyond a local single-agent session.
- Choosing between local agent runs, cloud VMs, and queue-based coding workflows.

Details:
- Jules is presented as an asynchronous coding agent that runs background work in parallel, with remote cloud agents better suited to this mode than IDE-local agents because they are not constrained by the user's laptop and can be used from any device. 01:12-02:16, 03:33-03:49
- In the Jules demo, the agent gets its own cloud VM, clones the whole codebase, runs the same commands as the developer, integrates with GitHub, and uses tests to validate later feature work. 07:53-08:24
- Cloud agents are described as running on separate VMs with their own development environment, allowing multiple tasks to proceed in parallel without requiring the human to keep the local workspace active (15:26-17:24).
- A practical workflow is to plan synchronously, write or refine a spec, dispatch execution asynchronously, and later review the finished cloud-agent output (01:01:30-01:02:14).
- VM-backed execution depends on the same factory primitives as local work: agents need runnable setup, accessible context, and enough environment capability to start the project and run checks (09:00-09:24, 15:26-21:52).
- The talk notes cost and wrong-context risks around cloud agents; spawning them in the wrong repo or without the right setup wastes work, and cloud agents can be expensive enough to require intentional routing (01:11:27-01:11:29, 01:21:03-01:21:47).
- Cursor's cloud-agent VMs also illustrate a training-infrastructure reuse pattern: secure sandboxes that load user code, run tools, and edit files can double as production-matched RL environments for coding models. 08:31-09:05
- **The two things this pattern is actually built on, and neither is about coding agents.** Shenoy's version of the same claim — "you take the exact same coding agent, you wrap it in a sandbox, and you just let it go run… it can provide the code in the form of a PR" — is followed by the observation that makes it a warning: "we've figured out what the async and forking mechanism for code is… What does that look like for the rest of the world?" The sandbox-and-PR loop is a *forking substrate*, and the reason engineers accept it is a second, separate property: they "launch 10 jobs and be comfortable with the fact that job seven might finish before job three." Both are inherited from software practice, not from the agent. See [Async Agents Need a Forking Substrate and a User Who Tolerates Out-of-Order Completion](async-agents-need-a-forking-substrate-and-a-tolerant-user.md). ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 07:59-09:24)

- **What the setup and handoff costs look like when a platform team has removed them.** Uber's cloud coding agent, Minion, runs interactive or autonomous on a pre-provisioned Kubernetes "balloon pod" that already holds every repository snapshotted with "the search index already built," so "the agents can start working within a matter of seconds" and a single run makes "backend changes and the front end changes here too as well" ([Medisetty and Huda](../sources/20260821_17-YSUHo6Lk.md), 06:09-07:03, 13:18-13:42). That addresses two of the three costs this page names — setup and context — by pre-paying them at the pool rather than per run. The third, review handoff, is answered differently: the run deliberately stops at a draft PR without pushing to CI, so validation happens before either a queue or a human sees it. See [Pre-Provision Agent Environments With Snapshots and Prebuilt Indexes](pre-provision-agent-environments-with-snapshots-and-prebuilt-indexes.md) and [Stop the Autonomous Agent at a Draft PR and Validate Before CI](stop-the-autonomous-agent-at-a-draft-pr-and-validate-before-ci.md).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Parallel Coding Agents Support Multitasking and Variation Search](parallel-coding-agents-support-multitasking-and-variation-search.md)
- [Verification-First Prompts Make Parallel Agent Work Reviewable](verification-first-prompts-make-parallel-agent-work-reviewable.md)
- [Isolate parallel coding work with project worktrees](isolate-parallel-coding-work-with-project-worktrees.md)
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)
- [Production-Matched RL Environments Train Coding Agents on Real Tool Surfaces](production-matched-rl-environments-train-coding-agents-on-real-tool-surfaces.md)
- [Async Agents Need a Forking Substrate and a User Who Tolerates Out-of-Order Completion](async-agents-need-a-forking-substrate-and-a-tolerant-user.md)
- [Pre-Provision Agent Environments With Snapshots and Prebuilt Indexes](pre-provision-agent-environments-with-snapshots-and-prebuilt-indexes.md)

Sources:
- [Your Coding Agent Just Got Cloned And Your Brain Isn't Ready - Rustin Banks, Google Jules](../sources/20250725_X4BwOu0GWb8.md), 01:12-08:24
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md), 15:26-21:52, 01:01:30-01:02:14
- [Building Cursor Composer - Lee Robinson, Cursor](../sources/20251202_fL1iJHtl51Q.md), 08:31-09:05
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 07:59-09:24
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 06:09-07:03, 13:18-14:07
