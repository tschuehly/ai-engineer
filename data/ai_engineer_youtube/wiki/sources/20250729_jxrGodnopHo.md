# [Full Workshop] Building Metrics that actually work - David Karam, Pi Labs (fmr Google Search)

Source: [[Full Workshop] Building Metrics that actually work - David Karam, Pi Labs (fmr Google Search)](https://www.youtube.com/watch?v=jxrGodnopHo)
Uploaded: 2025-07-29
Transcript: `raw/20250729_jxrGodnopHo/jxrGodnopHo.en-orig.vtt`

## Summary

David Karam and the Pi Labs team frame AI evaluation as an evolving scoring system rather than a one-time test suite. The workshop argues that durable eval work decomposes subjective product quality into many inspectable signals, calibrates those signals against human and user behavior, and then uses the scorer both offline for development and online for generation-time selection.

## Extracted Concepts

- [Treat Evals as the Home of Domain Knowledge](../concepts/treat-evals-as-the-home-of-domain-knowledge.md) - this source argues that AI product judgment increasingly lives in evals because prompts, synthetic data filtering, fine-tuning, and online selection depend on the scoring system.
- [Build Scoring Systems From Inspectable Quality Signals](../concepts/build-scoring-systems-from-inspectable-quality-signals.md) - this source describes breaking subjective quality into many objective or semi-objective signals that combine into a more useful score.
- [Use Online Candidate Scoring to Lift Generation Quality](../concepts/use-online-candidate-scoring-to-lift-generation-quality.md) - this source presents best-of-N generation with online scoring as a simple high-leverage use of a good scorer.

## Topic Links

- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

## Notes

- The workshop distinguishes synthetic data from metrics: synthetic data tests the system, while metrics check outputs against the desired behavior, 04:37-04:51.
- The presenters describe eval work as methodology: set up benchmarks, find metrics that work, calibrate metrics with humans and user data, and treat evals as part of development rather than a one-off testing activity, 06:43-07:18.
- They recommend layering evaluation methods by maturity and ROI: vibe testing and trace inspection can get early systems moving, then teams add human evals, code-based evals, and LLM judges as scale and risk demand more sophistication, 09:27-12:22.
- The source warns that generic helpfulness, harmlessness, and hallucination checks are guardrails, not enough to measure nuanced product quality such as whether a travel plan is actually interesting, 14:10-15:11.
- A scoring system is compared to search ranking: many understandable signals such as relevance, popularity, spam, feasibility, or content quality are combined into a final score, with lower-level signals remaining inspectable, 16:23-17:47.
- Decomposed signals lower variance and improve diagnosis because teams can slice failure data by finer-grained metrics and add new signals as they discover what matters, 18:40-19:14.
