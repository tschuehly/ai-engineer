# Use Online Candidate Scoring to Lift Generation Quality

Summary: A reliable scorer can be used at generation time: sample multiple candidate responses, score them immediately, and return the best one. This can improve quality without changing the model or prompt, but it depends on a scorer aligned with the product's definition of goodness.

Use when:
- Considering best-of-N generation, reranking, or online response selection for an AI feature.
- Reusing offline eval metrics as runtime control logic.

Details:
- The workshop describes raising temperature, generating several responses, scoring them online, and selecting the best candidate as a simple technique used by large labs, 13:21-13:40.
- The presenters frame this as an online reinforcement-learning-like pattern because the scorer supplies immediate feedback over candidate generations, 13:30-13:38.
- The lift comes from scorer-guided selection rather than prompt or model changes, so the approach is only as good as the scoring system it leans on, 13:39-13:51.
- Online scoring is part of a broader lifecycle: the same scoring system can support offline experiments, prompt optimization, synthetic-data filtering, fine-tuning, reinforcement learning, and production control, 12:54-13:19.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use eval agents to improve prompts, datasets, and scorers](use-eval-agents-to-improve-prompts-datasets-and-scorers.md)
- [Optimize LLM programs with metrics and teacher feedback](optimize-llm-programs-with-metrics-and-teacher-feedback.md)
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)

Sources:
- [[Full Workshop] Building Metrics that actually work - David Karam, Pi Labs (fmr Google Search)](../sources/20250729_jxrGodnopHo.md), 12:54-13:51
