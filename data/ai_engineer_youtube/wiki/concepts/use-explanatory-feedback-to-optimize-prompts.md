# Use Explanatory Feedback to Optimize Prompts

Summary: Prompt optimization improves when the loop receives explanations for failures, not just labels or scalar scores. Human and evaluator feedback can point the optimizer at the instruction, context, or rule that needs to change.

Use when:
- Building a prompt-improvement loop from traces, labeled examples, or production failures.
- Deciding what feedback columns to collect before running an optimizer.

Details:
- Arize frames prompt learning as a loop that combines generated outputs, LLM evals, English feedback, subject-matter-expert labels, and prompt rewriting, 06:32-07:15.
- The useful annotation is not only correct or incorrect; subject-matter experts should explain why the output failed, such as missing an instruction, ignoring context, or omitting required information, 07:34-07:53.
- LLM-as-judge explanations can serve the same role when they provide reasoning behind the label and point at the exact instructions to change, 07:55-08:08.
- The talk argues that explanatory text from humans or judges is especially valuable because text carries the reasons and improvement guidance that metric-only prompt optimizers can miss, 08:19-08:27, 13:39-13:54.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Optimize LLM programs with metrics and teacher feedback](optimize-llm-programs-with-metrics-and-teacher-feedback.md)
- [Optimize Judge Prompts With Diagnostic Feedback](optimize-judge-prompts-with-diagnostic-feedback.md)

Sources:
- [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](../sources/20260106_SbcQYbrvAfI.md), 06:32-08:27, 13:39-13:54
