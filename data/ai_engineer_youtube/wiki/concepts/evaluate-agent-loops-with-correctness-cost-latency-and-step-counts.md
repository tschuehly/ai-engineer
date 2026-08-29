# Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts

Summary: Agent-loop evals should combine outcome correctness with operational metrics such as cost, latency, and number of tool or question steps. Fast or cheap runs can be misleading when the model reaches an answer by guessing.

Use when:
- Comparing models or prompts for multi-turn tool-using agent loops.
- Reviewing eval dashboards where speed, cost, or step count might hide correctness failures.

Details:
- Pydantic Evals is used to compare GPT-4.1, Gemini, and Claude Sonnet 4.5 on a toy agent loop with pass/fail assertions, average cost, latency, and question-count metrics, 11:05-11:45.
- The speaker later found that Gemini's apparently faster, cheaper performance was partly because it invented wrong answers that were not being checked, showing that operational metrics need correctness validation before ranking models, 11:45-12:13.
- The same toy loop can take dozens of steps and still fail to infer the target object, which makes step count useful as an efficiency signal but insufficient as a quality measure, 02:55-03:24, 12:13-12:20.
- Report distributions, not a single mean. SWE-rebench publishes tokens per problem and tries per problem alongside the resolved rate, runs each task five times for confidence intervals, and separates pass@5 (solved at least once = the model's *potential*) from pass-all-5 (solved in every run = *reliability*) so a flattering average does not hide an unreliable model. ([SWE-rebench](../sources/20260604_wcUJWP6WpGM.md), 12:53-13:27)
- **The inverse of the Gemini failure: fewer steps can mean skipped verification, not efficiency.** Cline ran GLM and Opus on one real bug in their own repository. Opus "finished faster. It used half as many tool calls" — and "left a bunch of type errors and it broke the production build," while GLM spent twice the tokens, "cleaned up dead code and verified that the build compiled before completing." Every operational metric on that run ranked the wrong model first: fewer tool calls, lower latency, fewer tokens. The reason is that in an agentic loop the extra steps *are* the verification, so step count penalizes exactly the behavior you want, and cost and step count also decouple — GLM's double token spend cost half as much in dollars. Rank on delivered correctness (does the build still compile, do the types check) and read the operational metrics only within the set of runs that passed. ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 09:28-10:17)

- **A negative turn budget, motivated by a deadline rather than by cost.** "We also realized that we need to have guardrails for the agent. So we need to tell the agent what not to waste turns doing. Like code review is something that has to happen in like a specific time span. And then if it starts spending time doing things that it should not be doing, uh leads to a bad quality code review." Two things worth separating: the constraint is latency, because a review that arrives after the author has moved on is worthless regardless of content; and the instrument is a prohibition list rather than a step cap, which fails differently — a step cap truncates the good path along with the bad, while a prohibition list only helps for the wasteful behaviours you already know to name. Uber reports no measurement of either. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 07:01-07:20)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Compare Models by Task, Thinking Budget, Cost, and Latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Evaluate Agent Trajectories With Backtests and Smell Metrics](evaluate-agent-trajectories-with-backtests-and-smell-metrics.md)
- [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)
- [Run Agentic Coding Evals as an Infrastructure-Reliability Problem](run-agentic-coding-evals-as-an-infrastructure-problem.md)
- [Verification Guardrails Let You Downshift to Cheaper Models](verification-guardrails-let-you-downshift-to-cheaper-models.md)
- [Comment Volume Is a Property of the Review Pipeline, Not the Model](comment-volume-is-a-property-of-the-review-pipeline.md)

Sources:
- [From Stateless Nightmares to Durable Agents - Samuel Colvin, Pydantic](../sources/20251124_flf_IKnFYnE.md), 02:55-03:24, 11:05-12:20
- [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](../sources/20260604_wcUJWP6WpGM.md), 12:53-13:27
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 09:28-10:17
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 07:01-07:20
