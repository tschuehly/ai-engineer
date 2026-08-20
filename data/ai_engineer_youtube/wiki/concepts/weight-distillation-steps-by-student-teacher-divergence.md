# Weight Distillation Steps by Student/Teacher Divergence

Summary: In a long tool-calling trajectory, compute the student/teacher KL at each step and use it as a *weight* on that step's tokens rather than as a penalty on the loss. Steps where the two have already parted contribute little, steps still in distribution train normally, and a trajectory that goes off the rails and recovers is learned from where it is recoverable.

Use when:
- A self-distillation run over 50-100 tool calls is producing hedging or unstable evals.
- Deciding what to do with the KL you are already computing.
- Choosing a granularity for a corrective update: the trajectory, the step, or the token.

Details:
- The construction: "in a tool calling trajectory, let's say you have a 100 tool calls going on. Well, what we can do is start to look at the KL divergence of the student model and the teacher model as time goes on. And now we can use this as a waiting [weighting] factor. So not just like normal KL where we use that as a KL penalty, but instead we're actually multiplying the token weight of every single step based on this divergence property." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 14:31-15:03)
- **The distinction from a KL penalty is the whole idea.** A KL penalty is a term added to the objective that pulls the student toward a reference everywhere. Here KL is not in the objective at all — it is a per-step scalar multiplying how much that step's tokens count, so divergence *removes* gradient rather than adding a pull. One says "stay close"; the other says "if you are already far, this step has nothing to teach you."
- The three cases walked through: an in-distribution trajectory where "everything is a weight of one"; a heavily divergent one where "we're only going to modify W1 as the first step… train that, get that right, and then move on"; and the case the per-step independence exists for — "the model might go off tracks. We don't want to heavily weight that in, but then later on in the trajectory, it might get back on track again, and we're fine with that and we'll mildly shift the distribution." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 15:03-15:49)
- The middle case is effectively curriculum by fix-the-first-divergence: on a trajectory that went wrong early, learning concentrates at the first point of departure, because everything after it is conditioned on a prefix the teacher would never have written. That is a defensible ordering even if the weighting function were crude.
- It is presented specifically as the answer to [the "but wait" collapse](long-horizon-self-distillation-collapses-into-hedging.md): "this is one way that we've been able to overcome this for long horizon tool calling." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 15:49-15:53)
- **Compare with the other KL-based localization in the wiki, which reaches a compatible conclusion from the opposite direction.** Applied Compute measures that "this KL learning signal basically goes down as you get further and further away from the hint" and responds by hard-windowing — distill the hinted step and a few after ([Let a Judge Place the Hint and Distill Only the Steps Near It](let-a-judge-place-the-hint-and-distill-only-nearby-steps.md)). That is a step function on distance from a known intervention point; this is a continuous weight on measured divergence, which needs no intervention point and handles recovery. Two vendors, two products, same quantity, and neither cites the other. Where a hint's location is known, the window is cheaper; where drift is the problem rather than hint placement, the weight is the more general instrument.
- Composes downward with [token-level relevance masking](mask-irrelevant-teacher-tokens-before-learning-from-them.md): divergence weighting selects *which steps* count, masking selects *which tokens inside a step* count. Nothing in either talk reports running both.
- **What you would need before implementing.** The functional form is unstated — whether weight falls linearly, exponentially, or by threshold in KL; whether weights are normalized across a trajectory; whether the KL is computed on the full vocabulary or the sampled token. No ablation against unweighted OPSD is reported, so the claim that it fixes the hedging collapse rests on the vendor's assertion.
- Provenance: an in-house technique from a founder talk, presented with a three-panel diagram and no numbers.

Related topics:
- [Models](../topics/models.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Long-Horizon Self-Distillation Collapses Into Hedging](long-horizon-self-distillation-collapses-into-hedging.md)
- [Let a Judge Place the Hint and Distill Only the Steps Near It](let-a-judge-place-the-hint-and-distill-only-nearby-steps.md)
- [Mask Irrelevant Teacher Tokens Before Learning From Them](mask-irrelevant-teacher-tokens-before-learning-from-them.md)
- [Optimize the Whole Vocabulary, Not the Token You Sampled](optimize-the-whole-vocabulary-not-the-sampled-token.md)
- [Use token-weighted loss for long coding outputs](use-token-weighted-loss-for-long-coding-outputs.md)
- [Penalize dangerous steps with a process reward model](penalize-dangerous-steps-with-a-process-reward-model.md)
- [Interleave reasoning and tool calls for long-horizon agents](interleave-reasoning-and-tool-calls-for-long-horizon-agents.md)

Sources:
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 14:31-15:53
