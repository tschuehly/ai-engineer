# Track User Dissatisfaction Alongside Pairwise Model Preference

Summary: Pairwise model battles should preserve a way for users to say both answers are bad. That dissatisfaction signal exposes residual failure rates that a winner-only leaderboard can hide.

Use when:
- Designing model evaluation UIs, human preference collection, or production feedback mechanisms.
- Measuring whether top models are becoming acceptable in absolute terms, not only better than each other.

Details:
- Arena's text battle mode shows two anonymous model responses, asks users which is better, and reveals model names only after the vote. (09:31-09:56)
- The "both bad" option creates a dissatisfaction rate: a direct signal that neither model met the user's expectation. (11:05-11:50)
- Gostev analyzes battles among top-25 models to avoid low-quality model matchups dominating the metric. (11:50-12:09)
- The reported top-model dissatisfaction rate fell from roughly 17-20% before reasoning models to about 9%, but the source argues that 9% is still meaningful because it means users reject both answers from strong models. (12:09-12:55)
- Dissatisfaction rates can move because models improve and because user expectations or prompt difficulty shift over time, so the metric should be interpreted with the prompt distribution, not as a static benchmark score. (14:51-15:13)

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)

Sources:
- [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench](../sources/20260424_R7A8rX-09Zw.md), 09:31-15:13
