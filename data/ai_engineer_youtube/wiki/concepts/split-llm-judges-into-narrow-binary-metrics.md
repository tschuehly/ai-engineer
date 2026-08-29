# Split LLM Judges Into Narrow Binary Metrics

Summary: LLM-as-judge evaluations are easier to calibrate when each judge checks one specific failure mode as a binary decision. Broad "success" judges and one-to-five scores add ambiguity that can hide which behavior is actually broken.

Use when:
- Designing evaluators for agent traces, support conversations, policy adherence, tool use, or response style.
- Replacing a vague judge prompt with a calibrated set of measurable eval dimensions.

Details:
- The workshop starts from trace error analysis: subject-matter experts inspect trajectories, comment on what worked or failed, and cluster failures into error types such as policy adherence, response style, information delivery, and tool-call correctness. 09:20-10:31
- A single "success" judge is discouraged because judging all error types together makes the evaluator too complex to learn and calibrate. 10:31-11:04
- The recommended shape is one specific binary metric per failure mode, such as whether the agent adhered to policy, with reasoning attached to the label. 11:04-11:29
- Numeric one-to-five scores or percentages are harder to calibrate because even human annotators may not agree on the same scalar score. 11:07-11:41
- **A second, orthogonal axis: narrow the question, and also specify the reference.** Splitting a judge into small binary checks makes each *question* answerable; it does not tell the judge what counts as a violation in this particular case. Fox's failure case survives both: two notes drop the same kind of holiday detail, France in one and Lake Malawi in the other, and only the second is the diagnosis — a binary "did the note omit something important?" is as unanswerable in the abstract as a holistic quality score. His remedy is to assemble the reference per output from similar previously judged cases, the expert corrections that apply, and the guidelines in force. The two techniques compose rather than compete: keep the metric binary, and make its reference case-specific. See [Assemble the Judging Standard Per Output From Retrieved Precedent](assemble-the-judging-standard-per-output-from-retrieved-precedent.md). ([Fox](../sources/20260822_yqF6XhzbWBk.md), 11:56-12:36, 15:18-15:39)

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Use Golden Data Sets and Mixed Scoring Functions for AI Application Confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Assemble the Judging Standard Per Output From Retrieved Precedent](assemble-the-judging-standard-per-output-from-retrieved-precedent.md)

Sources:
- [Judge the Judge: Building LLM Evaluators That Actually Work with GEPA - Mahmoud Mabrouk, Agenta AI](../sources/20260410_X4dEHRzBLmc.md), 09:20-11:41
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 11:56-12:36, 15:18-15:39
