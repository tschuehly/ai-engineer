# Distill Without a Golden Answer by Giving the Teacher Privileged Information

Summary: Most distillation methods assume a correct answer exists to distill toward, which enterprise agent work rarely has. The alternative is to build the teacher out of *privileged information* the student did not have — a behavior prior, a known rubric, or an observation about the rollout that just happened — so the teacher is better than the student without anyone knowing what the right output was.

Use when:
- A post-training proposal stalls because nobody can produce ground-truth outputs for production tasks.
- Choosing between RL with a reward function and distillation for a behavior you can describe but not score.
- Auditing a distillation pipeline for a hidden dependency on labels you will not have in production.

Details:
- The constraint, stated as a complaint about the field: "we want to do this without having access to some golden answer… a lot of distillation work is done assuming you have some kind of golden answer that you can distill into the model. And this is often not the case… we want to think about how we can do continual learning and distillation without having some beautifully golden rubric to accompany every task." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 09:49-10:36)
- The substitute for the answer is an asymmetry, not a label: "the whole point of distillation is we have some kind of information that allows us to create a teacher model, which is smarter than the student model or the on-policy model. Um in order to create a teacher that's smarter than this on-policy model, we need to create some kind of hint or have some kind of privileged information." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 03:43-04:07)
- **The teacher and the student can be the same model.** Nothing in the setup requires a larger teacher; the teacher is the same policy with the hint in its context, which is why the technique is called self-distillation. What the student learns is how to behave as if it had seen the hint. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 03:43-04:07, 16:57-17:36)
- What counts as privileged information, from the talk's own examples: a general behavior prior ("a customer support agent that is too willing to give refunds"), an aggregate production observation ("the model tends to miss on questions like this"), a known rubric for a single task, a budget fact the model does not track ("you are near your 40-turn limit. There's only about three turns left"), or an observation about the rollout just produced ("in your prior rollout, you'd formatted hyperlinks like this"). ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 04:07-04:42, 12:04-12:22, 15:09-15:36)
- **Why this is a different tool than a reward function.** A reward says how good an output was and needs a scorer; a hint says something the model did not know and needs only that you know it. On a formatting task where the correct format *was* known well enough to reward, rewarding it still degraded the base model while hinting did not ([When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)). The absence of a golden answer is the common case; the hint approach also happened to win where an answer existed.
- **How this relates to the wiki's other no-teacher construction.** For a private corpus, on-policy distillation manufactures a teacher by putting the documents in the context window and cloning the resulting answers ([Distill Behaving as if the Corpus Were in Context](distill-behaving-as-if-the-corpus-were-in-context.md)). That is the same move with different privileged information: there the asymmetry is *knowledge in the window*, here it is *a statement about what the model should have done*. Both dodge the missing-teacher problem by constructing the asymmetry rather than finding a stronger model.
- Contrast with the same company's earlier position. Applied Compute's 2025-12 talk describes a loop that "samples many reasoning trajectories per problem, grades final answers, reinforces correct traces" ([Efficient Reinforcement Learning](../sources/20251209_o15AaYl7Wu0.md), 01:44-02:53) — a grading step this talk explicitly designs around. The two are complementary tools for the same customers, not a reversal, but the eight-month shift in emphasis is a signal about which enterprise tasks turned out to be gradeable.
- Provenance: a vendor talk with unpublished results. The claim that golden answers are "often not the case" in enterprise work is asserted from their customer base, not measured.

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Place a Continual-Learning Setup on Two Axes: Trace Policyness and Hint Provenance](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)
- [Distill Behaving as if the Corpus Were in Context, Not the Documents](distill-behaving-as-if-the-corpus-were-in-context.md)
- [When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Specialize Models Against Private Benchmarks With RL](specialize-models-against-private-benchmarks-with-rl.md)
- [Run a Jury of Analysts and a Consensus Judge for No-Ground-Truth Questions](run-a-jury-of-analysts-and-a-consensus-judge-for-no-ground-truth-questions.md)
- [Distill reasoning traces into small models](distill-reasoning-traces-into-small-models.md)

Sources:
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 03:43-04:42, 09:49-10:36, 12:04-12:22, 15:09-15:36
- [Efficient Reinforcement Learning - Rhythm Garg & Linden Li, Applied Compute](../sources/20251209_o15AaYl7Wu0.md), 01:44-02:53
