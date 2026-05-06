# Judge the Judge: Building LLM Evaluators That Actually Work with GEPA - Mahmoud Mabrouk, Agenta AI

Source: [Judge the Judge: Building LLM Evaluators That Actually Work with GEPA - Mahmoud Mabrouk, Agenta AI](https://www.youtube.com/watch?v=X4dEHRzBLmc)
Uploaded: 2026-04-10
Transcript: `raw/20260410_X4dEHRzBLmc/X4dEHRzBLmc.en-orig.vtt`

## Summary

Mahmoud Mabrouk presents LLM-as-judge evaluation as a calibration problem: unreliable judges can create fast but useless feedback loops, so teams should ground judges in human annotations, split broad success judgments into narrow binary metrics, inspect labeled trace distributions, and use GEPA-style prompt optimization with diagnostic feedback to improve judge rubrics.

## Extracted Concepts

- [Calibrate LLM Judges Like Binary Classifiers](../concepts/calibrate-llm-judges-like-binary-classifiers.md) - reinforces that judge reliability means agreement with human annotations, not generic judge confidence.
- [Split LLM Judges Into Narrow Binary Metrics](../concepts/split-llm-judges-into-narrow-binary-metrics.md) - supports decomposing broad success evals into one binary judge per failure mode.
- [Optimize Judge Prompts With Diagnostic Feedback](../concepts/optimize-judge-prompts-with-diagnostic-feedback.md) - shows how GEPA optimization benefits from verdicts, ground truth, reasoning, and domain priors.

## Topic Links

- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- A judge that does not correlate with human annotations can make evaluation loops fast but directionless; calibrated judges are useful for both offline prompt iteration and online production monitoring. 01:18-03:15
- Mabrouk frames a data flywheel as optimizing the harness, observing traces, adding evals from edge cases and annotations, and repeating. 03:18-03:56
- Error analysis should have experts inspect traces, comment on what worked or failed, and cluster failures before building judge metrics. 09:20-10:31
- Broad "success" judges are discouraged; the talk recommends specific binary metrics with reasoning because scalar scores are hard even for humans to agree on. 10:31-11:41
- Data and annotation quality remain the hard part: inspect the distribution, check that annotations contain enough information for learning, and be skeptical of small, uneven, or AI-generated annotation sets. 13:21-14:29
- GEPA's `optimize_anything` can optimize judge prompts or richer configurations, while the evaluator logs outputs, errors, and reasoning for the optimizer. 19:55-21:36
- In the demo, a custom reflection template that included the judge verdict, ground-truth annotation, and policy-learning prior improved the optimized rubric from 69% to 74% accuracy and reduced a compliance-label bias. 29:13-33:07
