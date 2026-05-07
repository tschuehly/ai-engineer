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

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Treat environments as eval, data, and training substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Measure AI ROI with primary output and guardrails](measure-ai-roi-with-primary-output-and-guardrails.md)

Sources:
- [Efficient Reinforcement Learning - Rhythm Garg & Linden Li, Applied Compute](../sources/20251209_o15AaYl7Wu0.md), 00:43-04:03
