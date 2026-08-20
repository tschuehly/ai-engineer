# Specialize Models Against Private Benchmarks With RL

Summary: Enterprise RL can target private operational benchmarks instead of public leaderboard tasks. The useful training target is a business workflow with measurable ROI, repeated use, and a data flywheel that keeps the specialized model aligned with the company's actual work.

Use when:
- Deciding whether RL is justified for a customer- or company-specific automation.
- Framing post-training around private workflow success instead of generic benchmark improvement.

Details:
- Applied Compute frames RL as a way to bring a customer's out-of-distribution tasks in distribution for current models, extending public-benchmark RL toward enterprise-specific private benchmarks. (01:16-01:43)
- The intended deployment is a specialized system for one use case, paired with a data flywheel so repeated use improves the model over time. (00:43-01:13)
- The simplified training loop samples many reasoning trajectories per problem, grades final answers, reinforces correct traces, and discourages incorrect behaviors; the same mechanism is then pointed at tasks the enterprise cares about rather than math alone. (01:44-02:53)
- Fast, cheap, low-variance runs are part of the product requirement because customer delivery and sustainable unit economics depend on predictable turnaround. (02:56-04:03)

- **The same company, eight months later, designs around the grading step this loop depends on.** Sam Denton's 2026-08 talk states the constraint directly: "we want to do this without having access to some golden answer… a lot of distillation work is done assuming you have some kind of golden answer that you can distill into the model. And this is often not the case" ([Distill Without a Golden Answer](distill-without-a-golden-answer-using-privileged-information.md)). Read as a pair, the two talks say enterprise specialization needs two tools — RL where a private benchmark can actually be scored, and hint-based self-distillation where the behavior can be described but not scored. Neither talk retracts the other; the shift in emphasis is the signal. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 09:49-10:36)
- The later talk also sharpens what "meet the customer where they are" means operationally: the entry point is a trace dump rather than an environment, because [offline hints on offline traces need no replayable environment](offline-hints-on-offline-traces-need-no-replayable-environment.md), and the flywheel this page describes is the same company's "raise all ceilings tomorrow" once a model is serving traffic. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 07:44-09:49)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Distill Without a Golden Answer by Giving the Teacher Privileged Information](distill-without-a-golden-answer-using-privileged-information.md)
- [Offline Hints on Offline Traces Need No Replayable Environment](offline-hints-on-offline-traces-need-no-replayable-environment.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Treat environments as eval, data, and training substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Measure AI ROI with primary output and guardrails](measure-ai-roi-with-primary-output-and-guardrails.md)

Sources:
- [Efficient Reinforcement Learning - Rhythm Garg & Linden Li, Applied Compute](../sources/20251209_o15AaYl7Wu0.md), 00:43-04:03
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 07:44-10:36
