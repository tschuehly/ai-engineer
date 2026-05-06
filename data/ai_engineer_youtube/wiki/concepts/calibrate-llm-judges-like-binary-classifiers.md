# Calibrate LLM Judges Like Binary Classifiers

Summary: LLM judges should be treated as evaluators that need their own validation. For pass/fail rubrics, align the judge with domain-expert labels, tune it on a development split, and validate it on a held-out test split with precision/recall-aware metrics.

Use when:
- Building an LLM-as-judge evaluator for generated content, workflow outputs, or agent traces.
- Deciding whether a judge prompt is reliable enough to gate workflow changes.

Details:
- The workshop treats an LLM judge as a binary classifier that outputs pass/fail labels rather than as an inherently trustworthy oracle. 01:43:43-01:44:15
- Judge reliability is defined as alignment with a domain expert, measured against labeled dev/test data splits. 01:44:15-01:44:33
- The development loop runs the judge on the dev split, computes F1 score, adjusts the judge prompt and examples, and repeats until performance converges. 01:44:44-01:45:28
- The held-out test split is used only after calibration as the final validation step, analogous to ordinary binary-classifier evaluation. 01:45:31-01:45:45
- F1 is used because it combines precision and recall, which matters for pass/fail judges where both false approvals and false rejections can distort workflow quality. 01:44:47-01:44:58
- A miscalibrated judge can make prompt and harness iterations faster without making them better; the useful signal is whether the judge correlates with human annotations and business goals. 01:18-03:15
- Judge calibration starts before prompt optimization: inspect trace distributions and annotation quality, because small, uneven, or AI-generated labels can make the optimized judge learn the wrong rubric. 13:21-14:29
- For PM-facing product evals, the judge prompt should produce categorical labels that can be mapped to scores, rather than raw numeric ratings, because numeric prompts produce unreliable model behavior. 10:38-11:28

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Validate eval harnesses before trusting skill scores](validate-eval-harnesses-before-trusting-skill-scores.md)
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Optimize Judge Prompts With Diagnostic Feedback](optimize-judge-prompts-with-diagnostic-feedback.md)
- [Label LLM Judge Outputs Before Mapping Them to Scores](label-llm-judge-outputs-before-mapping-them-to-scores.md)

Sources:
- [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../sources/20260420_mYSRn6PC1mc.md), 01:43:43-01:45:45
- [Judge the Judge: Building LLM Evaluators That Actually Work with GEPA - Mahmoud Mabrouk, Agenta AI](../sources/20260410_X4dEHRzBLmc.md), 01:18-03:15, 13:21-14:29
- [Shipping AI That Works: An Evaluation Framework for PMs - Aman Khan, Arize](../sources/20251226_2HNSG990Ew8.md), 09:19-11:28
