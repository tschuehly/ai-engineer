# Label LLM Judge Outputs Before Mapping Them to Scores

Summary: LLM-as-judge evaluators should emit explicit text labels such as pass/fail or good/bad before those labels are mapped to numeric scores. Asking the model directly for a numeric rating can make eval results less reliable because language models are weak at consistent numerical scoring.

Use when:
- Designing an LLM judge rubric that needs a score for dashboards or thresholds.
- Choosing between categorical labels and one-to-five style numeric ratings.

Details:
- The eval prompt should define the role, context to inspect, goal, terminology, and output labels so the judge classifies the example instead of inventing an ambiguous score, 09:19-10:18.
- Numeric-only judge prompts are called out as a common failure mode; the recommended pattern is to ask for a text label and map that label to a score in the surrounding system, 10:38-11:28.
- Labels can still feed quantitative workflows, but the score should be a deterministic mapping from the selected label rather than free-form model arithmetic, 11:05-11:12.
- This pattern complements judge calibration: label definitions and examples become the rubric that can later be compared against human annotations.

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)

Sources:
- [Shipping AI That Works: An Evaluation Framework for PMs - Aman Khan, Arize](../sources/20251226_2HNSG990Ew8.md), 09:19-11:28
