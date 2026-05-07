# Build Scoring Systems From Inspectable Quality Signals

Summary: A useful AI eval can decompose subjective quality into many inspectable signals that are easier to understand, debug, calibrate, and combine than one broad judge prompt. The signal set should grow as failures reveal missing dimensions of quality.

Use when:
- Designing metrics for outputs where "good" is subjective or multi-dimensional.
- Debugging why a broad LLM judge or human rating is noisy, unstable, or hard to act on.

Details:
- Pi Labs compares AI scoring to search ranking: score each candidate with many signals, then combine those signals into a final score used for selection or evaluation, 16:23-16:54.
- Lower-level signals should be easy to inspect and often objective or deterministic; they may start as simple code checks and become more subjective only as they are composed upward, 17:17-17:47.
- Breaking a broad quality judgment into smaller signals reduces variance, improves precision, and lets teams slice failures by fine-grained dimensions instead of arguing over one opaque score, 18:28-19:01.
- The scoring system does not need to be complete upfront. Start with five to ten correlated signals, debug against real examples, and add signals over time as the team discovers what matters, 10:33-11:15, 19:03-19:14.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Prefer Simple Debuggable Eval Scores](prefer-simple-debuggable-eval-scores.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Write custom scorers as product specifications](write-custom-scorers-as-product-specifications.md)

Sources:
- [[Full Workshop] Building Metrics that actually work - David Karam, Pi Labs (fmr Google Search)](../sources/20250729_jxrGodnopHo.md), 10:33-11:15, 16:23-19:14
