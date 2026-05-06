# Optimize LLM Programs With Metrics and Teacher Feedback

Summary: DSPy optimizers use datasets and metrics to produce an improved module, turning prompt improvement into a measurable optimization loop instead of a manual editing exercise.

Use when:
- Building an LLM task with known examples, expected outputs, and a metric that reflects real task quality.
- Trying to transfer an LLM workflow to a smaller or cheaper model while preserving useful performance.

Details:
- The optimizer workflow starts with a dataset, task signatures, and metrics; it evaluates a base program and iteratively proposes prompt changes using the metric signal. 47:24-48:39
- Teacher feedback can give textual reasons for failures, not just labels, so the optimizer can tighten the prompt based on what was wrong and what the answer should have been. 48:42-49:28
- The source suggests useful optimization can happen with tens to hundreds of input-output examples when the metrics accurately describe the desired behavior. 61:56-62:14
- Metric-level analysis after optimization can reveal whether to tune a metric, split a metric, adjust the dataset, or restructure the program. 62:20-63:22
- Optimizer output is a reusable compiled module that can be saved, loaded, and called later like another DSPy module. 63:29-63:49
- Optimization is most plausible for relatively well-defined LLM tasks with known inputs and outputs; the speaker cautions that ordinary classification may be a poor example for replacing classical ML, while optimization can still help transfer an LLM task to a smaller model at lower cost. 70:14-70:52

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build AI app benchmarks before optimization](build-ai-app-benchmarks-before-optimization.md)
- [Optimize Judge Prompts With Diagnostic Feedback](optimize-judge-prompts-with-diagnostic-feedback.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)

Sources:
- [DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](../sources/20260108_-cKUW6n8hBU.md), 47:24-49:28, 61:56-63:49, 70:14-70:52
