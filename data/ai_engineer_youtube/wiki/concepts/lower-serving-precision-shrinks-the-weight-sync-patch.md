# Lower Serving Precision Shrinks the Weight-Sync Patch

Summary: For a fixed float format the visibility floor is roughly θ/2^(mantissa+1), so a coarser serving dtype has a *higher* rounding boundary and absorbs more of the optimizer's motion. Serving rollouts in FP8 or FP4 therefore produces fewer changed weights per training step than BF16 — quantization, usually chosen for memory and bandwidth, doubles as a weight-synchronization lever. Group-scaled formats need separate treatment because a shared scale can move many elements at once.

Use when:
- Choosing a rollout serving dtype in a system that syncs weights by patch.
- Estimating how a precision change will affect cross-region weight-sync volume.
- Reasoning about MXFP4, INT4, or NVFP4 serving in a training loop.
- Separating training precision from serving precision in an RL stack.

Details:
- The formula and its direction: "for [a] fixed [size] float format the visibility floor is roughly theta over two to the mantissa plus one. So as you can see the FP4 will be higher and FP8 also will be between BF16 and FP4, which means in even lower precision there will be less weight changed." Fewer mantissa bits, wider gaps between representable values, more of the optimizer's step absorbed. ([Modal](../sources/20260810_maRzp4kImJ4.md), 13:25-13:42)
- **Training and serving precision are separate choices here.** "Rollout [is] often serving even lower precision such as MXFP4, FP8 and NVFP4, and we can see many many model providers doing this in the rollout. This is not a training precision — the training is just like in the normal BF16, although people can do QAT on that." The absorption argument compares the master weights' step against the *serving* format's floor, so lowering serving precision alone shrinks the patch without touching the training numerics. (13:06-13:25)
- **The counterintuitive consequence.** Quantization is normally reasoned about as a cost with an accuracy price — see [Treat Quantization as a Memory-Bandwidth Lever](treat-quantization-as-a-memory-bandwidth-lever.md). In a patch-synced RL loop it acquires a second, independent benefit on the *training* side: the coarser the served view, the less of it changes per step, and the cheaper the trainer→rollout link becomes. The accuracy cost is unchanged and unaddressed by this argument; the talk offers no reward or quality comparison across serving dtypes.
- **Group-scaled formats do not follow the same per-element reasoning.** "Plain floats are easy to reason about — each element has its own rounding… [in] group scale[d formats] such [as] INT4 they're a bit different. This is the regime where many low precision serving systems are moving towards right now. For INT4 each weight is quantized against a shared group scale, and we can apply the same rationale… [for] NVFP4 [there are] hierarchical scales, and we can see there are different encoding and the [decoding] mechanism." The rationale is asserted to carry over; the mechanics differ, and the talk does not work through them. (13:42-14:16)
- The unstated risk in that last point: with a shared group scale, a single scale-factor change re-encodes every element in its group, so a format that usually produces the smallest patches can also produce correlated bursts of change. Nothing in the talk measures patch size for group-scaled formats — the only measured run uses FP8. *This implication is derived from the mechanism as described, not stated by the speaker.*
- The one first-party measurement is at FP8: GLM 4.7 Air changed 0.15% of served weights on the first, high-learning-rate step and settled near 0.05% per step. No BF16 or FP4 comparison run is shown, so the monotone claim across formats rests on the formula rather than on data. (14:16-14:43)
- Practical framing: precision choice in a patch-synced RL loop now trades across three axes at once — serving memory and bandwidth, output quality, and weight-sync volume. The first two were already coupled; this source adds the third.

Related topics:
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Adam Absorption Hides Most Weight Updates From the Served Model](adam-absorption-hides-most-weight-updates-from-the-served-model.md)
- [Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md)
- [A Sparse Served-Weight Delta Is Not Gradient Sparsity](a-sparse-served-weight-delta-is-not-gradient-sparsity.md)
- [Treat Quantization as a Memory-Bandwidth Lever](treat-quantization-as-a-memory-bandwidth-lever.md)
- [Use hybrid RL system design for agent trajectories](use-hybrid-rl-system-design-for-agent-trajectories.md)

Sources:
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 13:06-14:43
