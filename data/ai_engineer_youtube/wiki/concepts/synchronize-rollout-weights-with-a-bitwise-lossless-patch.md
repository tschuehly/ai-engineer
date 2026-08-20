# Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint

Summary: A full checkpoint is the wrong unit of synchronization between an RL trainer and its rollout fleet: at frontier scale it is around 500 GB and takes minutes to hours, while even fully async training wants weight-update latency within seconds. Ship instead a patch against the *served view* — changed positions plus replacement bits — encoded so the engine reconstructs the target version bit-for-bit rather than by adding a numeric delta.

Use when:
- Deciding what object crosses the wire between trainer and rollout workers.
- Diagnosing weight-sync latency as the thing keeping rollout inside the trainer's cluster.
- Designing an update format that must be safe to apply repeatedly over many versions.
- Evaluating a "delta sync" scheme for numerical soundness.

Details:
- **The reframe.** "The problem is not whether rollout can leave the cluster; the problem is the full checkpoint is a wrong unit of synchronization." The placement question and the transfer question look like one problem and are not. ([Modal](../sources/20260810_maRzp4kImJ4.md), 05:53-06:02)
- The numbers that make the checkpoint unusable off-cluster: "at this scale the checkpoint is very huge… you have like 500 gigabytes, normally take multiple minutes to hours to just do the [weight sync]. So moving that over commodity link might not be the smartest choice, because when you're doing async, maybe even fully async training, you still want weight update latency to be as low as possible, like within seconds." Async training relaxes *synchronization*, not *freshness* — the reason to want low sync latency survives the move to async. (05:25-05:53)
- **What the patch is a diff of matters more than the diff.** The comparison is made in the rollout's own dtype: "we first look at the rollout view: the weight cast or projected to the dtype that the rollout engine will be serving. Then we compare the version t minus one and the version t… the patch is the change position plus replacement bits and also some metadata." Diffing the master weights would produce a dense object; diffing the served view is what produces a sparse one, for reasons on [Adam Absorption Hides Most Weight Updates From the Served Model](adam-absorption-hides-most-weight-updates-from-the-served-model.md). (10:41-11:06)
- **Replacement, not addition — this is the correctness argument.** "There are multiple lossless encodings. People can do selective overrides. They can also do XOR. The important part is there are bit-level equivalent[s]. So it's not a floating point addition. So there's no additive delta drift. If a rollout engine applied the patch correctly, it reconstruct[s] the sync[ed] server version bitwise." A patch that added a numeric delta in low precision would accumulate rounding error across hundreds of versions and slowly separate the served policy from the trainer's; overwriting bits cannot. (11:06-11:30)
- The equivalence this buys is what makes the whole architecture safe to reason about: "the rollout engine gets the same served version you would have gotten [by] syncing to the full checkpoint." Correctness becomes an identity claim about the artifact rather than a tolerance claim about numerics — the engine is not running an approximation of the policy, it is running the policy. (06:42-06:53)
- Reported effect: "the link shrinks from hundreds of gigabytes to maybe hundreds of megabytes," quantified later as "from like 500 gigabytes to 500 megabytes. So it will be like extremely fast, in seconds." (06:53-07:00, 17:26-17:41)
- Related but distinct mechanism: LoRA also ships a small object, for an unrelated reason. "The base model is frozen and the adapter is small enough by construction. So you do not need to have the push versus floor arguments here. So full parameter delta is small by absorption and the LoRA updates are small by construction." A small-payload sync is not evidence of the absorption effect; check which mechanism a given system relies on. (11:36-12:03)
- **Costs the talk does not price.** Building the patch requires casting the full parameter set to the serving dtype and diffing against the previous version at every step, and the bulletin board must retain prior versions so a lagging engine can replay missing transitions. No overhead figure, no storage figure, and no measured cross-region transfer latency appear anywhere — "extremely fast, in seconds" is derived from the size ratio. Nor is the reverse traffic considered: for long agentic rollouts the trajectories flowing back may exceed the weight patch flowing out.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Adam Absorption Hides Most Weight Updates From the Served Model](adam-absorption-hides-most-weight-updates-from-the-served-model.md)
- [A Sparse Served-Weight Delta Is Not Gradient Sparsity](a-sparse-served-weight-delta-is-not-gradient-sparsity.md)
- [Lower Serving Precision Shrinks the Weight-Sync Patch](lower-serving-precision-shrinks-the-weight-sync-patch.md)
- [Publish Immutable Weight Versions to a Bulletin Board](publish-immutable-weight-versions-to-a-bulletin-board.md)
- [The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)
- [Let Training Crash and Checkpoint Against a Fast Filesystem](let-training-crash-and-checkpoint-against-a-fast-filesystem.md)

Sources:
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 05:03-07:00, 10:41-12:03, 17:26-17:41
