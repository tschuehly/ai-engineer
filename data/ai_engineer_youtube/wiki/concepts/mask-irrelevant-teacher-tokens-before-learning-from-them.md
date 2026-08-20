# Mask Irrelevant Teacher Tokens Before Learning From Them

Summary: A teacher's output carries its stylistic preferences alongside the lesson you meant to teach. Relevance-masked self-distillation puts an LLM judge between teacher and student to select which tokens are learned from, which Applied Compute reports both improves learning of a very out-of-distribution behavior and reduces catastrophic degradation.

Use when:
- Self-distillation installs the target behavior but also drifts the model's voice or general capability.
- A narrow behavior change must not cost base-task performance.
- Deciding what granularity to intervene at once trajectory- and step-level selection are already in place.

Details:
- The technique, named: "something called relevance mask self-distillation… we use an LLM judge to sample and choose which tokens we actually learn from from our teacher model." A blog post on Applied Compute's site is cited but not walked through in the talk. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 16:57-17:36)
- The failure it targets is specific and easy to overlook: "often, we'll see that the teacher model has preferences of certain connector words that are not really relevant to actually what we're trying to teach the student." The teacher is not wrong at those tokens — it simply has opinions there that carry no lesson, and an unmasked KL objective charges the student for every one of them. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 17:12-17:27)
- The reported effect is two-sided: "we're able to increase our ability to learn a very, very out of distribution behavior, while also being better about avoiding catastrophic degradation." Both directions matter — masking is not only a safety measure, it is claimed to concentrate the signal and speed the intended learning. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 17:27-17:36)
- **Why this belongs in the same family as the other localization tricks.** The talk applies three nested filters: a judge picks *where in the rollout* the hint goes, distillation runs on *that step and a few after*, and masking picks *which tokens in those steps* to learn from ([Let a Judge Place the Hint and Distill Only the Steps Near It](let-a-judge-place-the-hint-and-distill-only-nearby-steps.md)). Each narrows the update toward the intended lesson. Read together they say the same thing at three scales: the default distillation objective is far too broad for a targeted behavior change.
- The most useful way to hold this without the vendor's numbers: catastrophic degradation from self-distillation is at least partly an *aperture* problem rather than a fundamental capability/behavior tradeoff. Two approaches that could not narrow their aperture — a format reward and SFT on correct traces — degraded the base model on a comparable task ([When Rewards and SFT Both Degrade the Base Model](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)).
- **What is missing before you could reimplement it.** The judge prompt, the masking policy, the fraction of tokens typically masked, whether masking is binary or weighted, and any ablation against unmasked self-distillation are all unstated. The talk names the technique and its motivation; the mechanism is left to a blog post.
- The judge dependency is real and unvalidated here — a judge that masks the wrong tokens silently removes the lesson. The wiki's judge-validation guidance applies: [check the judge before changing the agent](check-the-judge-before-changing-the-agent.md).
- Provenance: a vendor's in-house technique presented in the "tips and tricks" segment of a talk that closes on hiring, with charts referenced but no numbers spoken.

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Let a Judge Place the Hint and Distill Only the Steps Near It](let-a-judge-place-the-hint-and-distill-only-nearby-steps.md)
- [When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)
- [Distill Without a Golden Answer by Giving the Teacher Privileged Information](distill-without-a-golden-answer-using-privileged-information.md)
- [Distill reasoning traces into small models](distill-reasoning-traces-into-small-models.md)
- [Check the judge before changing the agent](check-the-judge-before-changing-the-agent.md)
- [Preserve long-context ability with single-stage RL](preserve-long-context-ability-with-single-stage-rl.md)
- [Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)

Sources:
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 16:57-17:36
