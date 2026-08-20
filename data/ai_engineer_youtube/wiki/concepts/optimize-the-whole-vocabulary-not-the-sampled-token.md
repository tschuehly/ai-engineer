# Optimize the Whole Vocabulary, Not the Token You Sampled

Summary: A policy-gradient update can only reweight the tokens the model actually sampled, which sharpens an existing distribution. A distillation loss that matches the teacher's full next-token distribution can move probability mass onto a token the student never produced — the difference between sharpening a distribution and shifting it, and the stated mechanical reason self-distillation is claimed to keep climbing where GRPO plateaus.

Use when:
- Asking why a method that is "just imitation" would beat RL rather than merely be cheaper.
- Deciding between a reward-based and a distribution-matching objective for a behavior change.
- Explaining why token counts go down rather than up when a training method changes.

Details:
- The claim: "it's actually not just the top token that you sampled that you're actually making better, but instead the entire vocabulary. So for every single token, there's a vocabulary of let's say 65k tokens that you're optimizing over." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 10:21-10:34)
- The worked illustration is a Python `for` loop / `range`: at the highlighted positions "the teacher… wasn't the top sample token of the student, but instead we're pushing that distribution to sample a brand new token. And this is really exciting because we're not just taking now a distribution like RL and slightly sharpening it, but we're instead actually shifting entire distributions." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 10:34-11:03)
- The reported consequence, given without values: on LiveCodeBench "gpo saturates around sonnet level performance and doesn't really push the frontier, but because we're actually shifting distributions we're able to get to brand new territory of results with a lot of data sets." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 11:11-11:31)
- **The token-efficiency corollary is the more checkable claim.** "With RL a fundamental limitation… is the models like to think a lot, right — the more tokens that you expend it's just going to do better. But with opsd you don't have that problem and so the actual tokens to solve some of these really difficult challenges actually collapses." That is a testable prediction with a clear direction: a reward-driven run should grow its reasoning budget over training, a distillation run should not. Anyone running either can measure it without the vendor's numbers. ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 11:31-11:53)
- **What is actually being asserted, stripped of the marketing.** Nothing here says distillation exceeds its teacher. The teacher is the same model holding a hint, so the ceiling is "what this policy would have done had it known," and the argument is that a full-distribution target transfers more of that per rollout than a scalar advantage does ([Distill Without a Golden Answer](distill-without-a-golden-answer-using-privileged-information.md)). Read it as a claim about the *rate* at which information moves, which is also how the same talk's [four-property scorecard](score-post-training-algorithms-on-four-properties.md) frames the per-token row.
- **The cost this hides.** A full-vocabulary target means the teacher must be run and its logits kept for every position, so "cheaper because there are no parallel rollouts" is only half a ledger. The talk does not compare total FLOPs against GRPO.
- **The same breadth is what makes the update dangerous.** If every token in every position carries a target, then every teacher preference is learned, including the ones with no lesson in them — which is precisely the failure Applied Compute mitigates by [masking irrelevant teacher tokens](mask-irrelevant-teacher-tokens-before-learning-from-them.md), and which appears at long horizons as [collapse into hedging tokens](long-horizon-self-distillation-collapses-into-hedging.md). The breadth is the feature and the failure mode.
- Provenance: a vendor talk with no numbers attached to either result. The LiveCodeBench comparison names no model, no GRPO configuration, and no score; "sonnet level" is the only reference point offered, and the "brand new territory" claim has no value at all.

Related topics:
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Score a Post-Training Algorithm on Four Properties](score-post-training-algorithms-on-four-properties.md)
- [Distill Without a Golden Answer by Giving the Teacher Privileged Information](distill-without-a-golden-answer-using-privileged-information.md)
- [Mask Irrelevant Teacher Tokens Before Learning From Them](mask-irrelevant-teacher-tokens-before-learning-from-them.md)
- [Long-Horizon Self-Distillation Collapses Into Hedging](long-horizon-self-distillation-collapses-into-hedging.md)
- [Distill reasoning traces into small models](distill-reasoning-traces-into-small-models.md)
- [Use token-weighted loss for long coding outputs](use-token-weighted-loss-for-long-coding-outputs.md)
- [Scale reasoning models with RL and verifiable domains](scale-reasoning-models-with-rl-and-verifiable-domains.md)

Sources:
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 10:21-11:53
