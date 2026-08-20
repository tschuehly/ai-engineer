# Blend a Partial-Hint Teacher to Bound the Distribution Shift (Residual Guidance)

Summary: Run the teacher twice — once with half the hint and once with all of it — and distill toward a linear combination of the two. The gap between them measures how strong the hint was and how far out of the student's distribution it pushes, and mixing them keeps the update from landing somewhere the student has no path to.

Use when:
- Hints vary in strength and you have no way to grade them before training.
- A self-distillation run installs a behavior the model cannot reproduce without the hint.
- Looking for a mitigation for hint leakage that does not depend on an LLM redacting the hint correctly.

Details:
- The premise: "in a hint, most of the time you need to actually get through the entire hint in order to get the full information. So what if you cut it in half? Then you have a partial hint." Truncation is a cheap strength dial precisely because hints are usually cumulative. ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 17:51-18:07)
- The construction: "this is the partial teacher, we're able to get the log props of a slightly smart[er] teacher, and then we have the full teacher as well, and that's with the full hint. Now what we can do is actually take the linear combination of both of these, and this gives us a good idea of how strong the hint is and how out of distribution it is for the original model." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 18:07-18:30)
- **It does two jobs at once, and they are worth separating.** As a *measurement*, the divergence between half-hint and full-hint teachers is an unsupervised estimate of hint strength — computable per example, needing no labels. As a *clamp*, the mixture is what actually gets distilled into. A team could adopt only the first and use it to filter or sort hints before training.
- What it prevents: "on the left you have normal OP[S]D where you might be entirely shifting distributions and there's almost no overlap between your model and the original solution… to this kind of cool world where let's say half the hint is actually quite close to your distribution but the full hint is very off and you take a linear combination and so then you're not shifting the model into unknown territory." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 18:30-18:52)
- **The underlying rule generalizes past this method.** A target the student has no probability mass near is not a lesson, it is a jump — and a training signal that demands the jump gets satisfied by whatever shortcut is available, which is the [hint leakage](hint-leakage-is-the-reward-hacking-of-self-distillation.md) pathology. Interpolating toward a reachable intermediate is the same instinct as the [step-level divergence weighting](weight-distillation-steps-by-student-teacher-divergence.md) in the same talk: both refuse to train hard toward a target the student is far from, one along the trajectory axis and one along the hint-strength axis.
- Contrast with the wiki's other answer to over-broad distillation targets. Applied Compute narrows *where* the update applies — [judge-placed hints](let-a-judge-place-the-hint-and-distill-only-nearby-steps.md), short windows, [token masking](mask-irrelevant-teacher-tokens-before-learning-from-them.md) — while this narrows *how far* it moves. They are orthogonal, and nothing in either talk reports combining them.
- **What is unspecified, and it is most of the method.** The mixing coefficient, whether it is fixed or derived from the measured divergence, whether "half" means half the tokens or half the reasoning steps, and how the mixture is computed (over logits or probabilities) are all left out, as is any comparison against plain OPSD. What survives without those details is the design idea and the measurement trick.
- Provenance: named as "some more satisfying algorithmic approaches" after the LLM hint filter, illustrated with two distribution sketches, no numbers, and no reference to a paper or post.

Related topics:
- [Models](../topics/models.md)

Related concepts:
- [Hint Leakage Is the Reward Hacking of Self-Distillation](hint-leakage-is-the-reward-hacking-of-self-distillation.md)
- [Weight Distillation Steps by Student/Teacher Divergence](weight-distillation-steps-by-student-teacher-divergence.md)
- [Distill Without a Golden Answer by Giving the Teacher Privileged Information](distill-without-a-golden-answer-using-privileged-information.md)
- [Let a Judge Place the Hint and Distill Only the Steps Near It](let-a-judge-place-the-hint-and-distill-only-nearby-steps.md)
- [Mask Irrelevant Teacher Tokens Before Learning From Them](mask-irrelevant-teacher-tokens-before-learning-from-them.md)
- [Optimize the Whole Vocabulary, Not the Token You Sampled](optimize-the-whole-vocabulary-not-the-sampled-token.md)

Sources:
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 17:47-18:52
