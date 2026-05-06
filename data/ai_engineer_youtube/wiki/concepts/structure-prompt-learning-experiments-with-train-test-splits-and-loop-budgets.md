# Structure Prompt-Learning Experiments With Train/Test Splits and Loop Budgets

Summary: Prompt-learning runs should make their experimental scope explicit: sample size, train/test split, evaluation prompt or rule count, and optimization loop count all affect speed, representativeness, and confidence.

Use when:
- Turning prompt iteration into a repeatable experiment instead of one-off prompt editing.
- Choosing whether to run a fast small-sample loop or a more representative validation pass.

Details:
- The workshop starts from a dataset with feedback and routes that data into an optimizer, which generates candidates, evaluates them, and refines the prompt, 28:24-28:57.
- Sample count controls how many rows are used; zero can mean all data, while a positive number can limit the run for faster experimentation, 29:13-29:26.
- A train/test split separates data used to optimize from data used to evaluate the new prompt, 29:42-29:59.
- Evaluation rule or prompt count controls how many candidate prompts are used during evaluation, while the optimization-loop count controls how many generate/evaluate/refine iterations run per experiment, 30:02-30:34.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build AI app benchmarks before optimization](build-ai-app-benchmarks-before-optimization.md)
- [Optimize LLM programs with metrics and teacher feedback](optimize-llm-programs-with-metrics-and-teacher-feedback.md)
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md)

Sources:
- [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](../sources/20260106_SbcQYbrvAfI.md), 28:24-30:39
