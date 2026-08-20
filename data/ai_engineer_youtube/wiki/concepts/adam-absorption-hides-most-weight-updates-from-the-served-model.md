# Adam Absorption Hides Most Weight Updates From the Served Model

Summary: During RL post-training, an Adam step is roughly the learning rate in magnitude, while the serving format's rounding boundary is roughly half a ULP — about θ/256 for BF16. At typical RL learning rates the step is a thousand times smaller than the boundary, so the master weight moves and the value the rollout engine would serve does not. The master update stays dense; the *served* update becomes sparse, and that gap is what makes cheap weight synchronization possible.

Use when:
- Explaining why consecutive rollout weight versions are ~99% bit-identical.
- Deciding whether a weight-sync scheme built on served-view sparsity will hold for your optimizer and learning rate.
- Reasoning about what quantized serving hides from a training loop.
- Auditing a claim that "only 1% of weights change per step."

Details:
- The quantity that matters is not the weight but the **rollout-visible weight**: "the weights in the served rollout checkpoint — not the FP32 optimizer states, not the Adam moments — the weights the rollout engine will actually use to serve, maybe let's say the FP8 or maybe NVFP4 format." ([Modal](../sources/20260810_maRzp4kImJ4.md), 06:10-06:33)
- **Ingredient one, the floor.** "The optimizer may keep very high precision master weights but the next forward pass really [reads] a BF16 visible view. That view has finite resolution around a value of magnitude theta. BF16 spacing is roughly theta over 128… people call it ULP… the distance between the adjacent representable BF16 value. But the update only needs to cross the near[est] rounding boundary to be visible. That boundary is about half of the ULP. So roughly theta over 256 for weight around one." For θ = 1: ULP ≈ 0.0078, boundary ≈ 0.0039. Below that, "the BF16 visible value will [round] back, so you will not see any change from the rollout weight perspective." (07:10-08:21)
- **Ingredient two, the push.** "For Adam… we ignore the weight decay term, the per-parameter update is the learning rate times a normalized direction. The raw gradient can be dense and can have very different magnitudes across parameters, and Adam divides by running gradient statistics. So the per-weight push is usually on the order of learning rate." A cited paper "prove[s] a bound: the Adam step is at most B times the learning rate… the important note is Adam makes the push small and very controlled." Normalization is doing the work: the update magnitude is decoupled from the gradient magnitude. (08:21-09:11)
- **The comparison.** "The value changes only if the push clears the floor… take theta equal one, the BF16 boundary is about 0.0039, a typical Adam step here is around 3 millionths, so the update is more than a thousand [times] smaller than the boundary." The careful restatement matters: "this is not saying the master weights [are] frozen forever. It is saying the value that [the] rollout engine would serve does not change on this part." (09:11-09:52)
- **Where the effect lives on the weight distribution.** Plotted with weight magnitude on the x-axis and update magnitude on the y-axis, the floor is a diagonal (it scales with θ) while the push is roughly flat (it scales with the learning rate). "The red floor is above the green push. Those updates exist in the master weights but they are not visible in the served BF16 view… small weights on the left can move. Large weight on the right, they will just stay the same. They will be absorbed. This is the Adam absorption. This is why the served update become[s] very sparse." Large-magnitude weights are the ones that freeze, because their rounding boundary is proportionally larger. (09:56-10:41)
- Reported measurement: casting weights to BF16 and comparing consecutive versions bitwise gives "around 99% of the time is bit identical per step" across a model family, and "it also survives staleness — even when the rollout lags, the changed set remain very small." The one first-party run — GLM 4.7 Air served in FP8 — changed 0.15% of weights on the first, high-learning-rate step and settled near 0.05% per step "when the Adam is going relatively stable." (12:05-12:34, 14:16-14:43)
- **The effect is a statement about learning rate, and its own numbers show the sensitivity.** The quoted margin is ~1000× (3e-6 against 3.9e-3), and the GLM run's high-learning-rate first step changed three times as many weights as its stable regime. So a scheme built on absorption is cheapest exactly when training has settled and most expensive during warmup or aggressive-learning-rate phases, and a learning rate raised by three orders of magnitude would erase the margin entirely. *This reading is derived from the numbers as stated; Jiang does not draw it.*
- **Scope is explicitly Adam-only, and explicitly at risk.** Jiang raises it himself as an open question: "a lot of model providers such as Moonshot and also DeepSeek, they're adopting Muon in their post training. Does the sparsity still hold for Muon, because a lot of thing[s] we discussed previously [are] only for Adam[?]" No analysis of Muon's step-size distribution is offered. (18:48-19:02)
- Provenance: the Adam bound, the ~99% bit-identical measurement, and the cross-family scope are all attributed to a paper the talk never names, so none of the supporting evidence is checkable from the source. The single first-party data point is one internal run on one model at one precision.
- Do not read this as sparsity of the update itself — see [A Sparse Served-Weight Delta Is Not Gradient Sparsity](a-sparse-served-weight-delta-is-not-gradient-sparsity.md), which is the misreading Jiang stops to correct on stage.

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [A Sparse Served-Weight Delta Is Not Gradient Sparsity](a-sparse-served-weight-delta-is-not-gradient-sparsity.md)
- [Lower Serving Precision Shrinks the Weight-Sync Patch](lower-serving-precision-shrinks-the-weight-sync-patch.md)
- [Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md)
- [Treat Quantization as a Memory-Bandwidth Lever](treat-quantization-as-a-memory-bandwidth-lever.md)
- [Score a Post-Training Algorithm on Four Properties](score-post-training-algorithms-on-four-properties.md)

Sources:
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 06:10-10:41, 12:05-12:34, 14:16-14:43, 18:48-19:02
