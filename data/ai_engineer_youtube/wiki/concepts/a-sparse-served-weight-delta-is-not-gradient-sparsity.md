# A Sparse Served-Weight Delta Is Not Gradient Sparsity

Summary: When ~99% of a served model's weights are bit-identical between consecutive training versions, the natural reading — that the gradients are sparse — is wrong. Gradients are dense (about 99% of parameters receive a non-zero gradient) and the FP32 master update is dense too. It is just small, and small dense updates disappear under quantization. Sparsity is a property of the observation, not of the learning signal.

Use when:
- Interpreting a measurement that most weights did not change between checkpoints.
- Evaluating a claim that a training method produces sparse updates.
- Deciding whether a sparsity-exploiting optimization is safe to build on.
- Explaining to a team why the trainer cannot skip work that the sync layer skips.

Details:
- **The misconception, named on stage.** "A common misconception there is like it works because all our gradients are sparse. They are not. The paper reports the gradients are dense. About 99% of the parameter gets non-zero gradients. The FP32 master update is also dense. It's just small. The main thing is like the rollout weight change is just 1% from the perspective of rollout engine." ([Modal](../sources/20260810_maRzp4kImJ4.md), 12:44-13:05)
- The measurement is deliberately narrow about what it is measuring: "the measurement is not [about] gradient sparsity. It's not optimizer state sparsity. They cast weights to BF16, compare consecutive version[s]… bitwise and they count what did not change over time." The result — around 99% bit-identical per step across a model family — describes the *quantized view* of the weights and nothing else. (12:05-12:28)
- **Why the distinction is load-bearing rather than pedantic.** Real gradient sparsity would license skipping computation: sparse backward passes, sparse optimizer state, sparse all-reduce. Served-view sparsity licenses none of that. The trainer must compute, store, and communicate the full dense update; only the *published artifact* compresses. Building trainer-side optimizations on the observed 99% figure would be building on the wrong mechanism.
- It also tells you where the effect can be destroyed. Gradient sparsity would be a property of the data and the model; served-view sparsity is a property of the *ratio* between the optimizer's step size and the serving format's rounding boundary — see [Adam Absorption Hides Most Weight Updates From the Served Model](adam-absorption-hides-most-weight-updates-from-the-served-model.md). Change the learning rate, the optimizer, or the serving dtype and the number moves; change the dataset and it does not.
- A second small-payload mechanism worth keeping separate for the same reason: "the base model is frozen and the adapter is small enough by construction. So you do not need to have the push versus floor arguments here. So full parameter delta is small by absorption and the LoRA updates are small by construction." Three distinct reasons a weight update can be cheap to ship — sparse gradients, absorption, and low-rank construction — with different preconditions and different failure modes. (11:36-12:03)
- **The general lesson.** A quantity measured through a lossy view can look structured when the underlying quantity is not. Before optimizing against an observed sparsity, establish whether it lives in the signal or in the instrument: here the instrument is a BF16 (or FP8, or FP4) cast, and the entire effect is an artifact of it — a productive artifact, but an artifact.
- Provenance: the dense-gradient counter-claim and the ~99% bit-identical figure both come from a paper the talk never names, and no model, size, task, or step count is given for the cross-family measurement. The correction is therefore reported rather than independently checkable.

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Adam Absorption Hides Most Weight Updates From the Served Model](adam-absorption-hides-most-weight-updates-from-the-served-model.md)
- [Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md)
- [Lower Serving Precision Shrinks the Weight-Sync Patch](lower-serving-precision-shrinks-the-weight-sync-patch.md)
- [Optimize the Whole Vocabulary, Not the Token You Sampled](optimize-the-whole-vocabulary-not-the-sampled-token.md)

Sources:
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 11:36-13:05
