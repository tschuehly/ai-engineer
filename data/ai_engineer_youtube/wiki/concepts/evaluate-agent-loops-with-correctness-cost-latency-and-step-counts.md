# Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts

Summary: Agent-loop evals should combine outcome correctness with operational metrics such as cost, latency, and number of tool or question steps. Fast or cheap runs can be misleading when the model reaches an answer by guessing.

Use when:
- Comparing models or prompts for multi-turn tool-using agent loops.
- Reviewing eval dashboards where speed, cost, or step count might hide correctness failures.

Details:
- Pydantic Evals is used to compare GPT-4.1, Gemini, and Claude Sonnet 4.5 on a toy agent loop with pass/fail assertions, average cost, latency, and question-count metrics, 11:05-11:45.
- The speaker later found that Gemini's apparently faster, cheaper performance was partly because it invented wrong answers that were not being checked, showing that operational metrics need correctness validation before ranking models, 11:45-12:13.
- The same toy loop can take dozens of steps and still fail to infer the target object, which makes step count useful as an efficiency signal but insufficient as a quality measure, 02:55-03:24, 12:13-12:20.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Compare Models by Task, Thinking Budget, Cost, and Latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Evaluate Agent Trajectories With Backtests and Smell Metrics](evaluate-agent-trajectories-with-backtests-and-smell-metrics.md)

Sources:
- [From Stateless Nightmares to Durable Agents - Samuel Colvin, Pydantic](../sources/20251124_flf_IKnFYnE.md), 02:55-03:24, 11:05-12:20
