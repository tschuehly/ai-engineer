# Evaluator Quality Is a Dependency of Prompt Optimization

Summary: Prompt-learning systems depend on evaluator reliability because the optimizer will amplify whatever signal the evaluator supplies. Teams should treat evaluator prompts, rules, and code checks as first-class artifacts to test and refine.

Use when:
- Using LLM-as-judge output or rule checks to drive prompt changes.
- Debugging a prompt optimizer that appears to improve a metric without improving task quality.

Details:
- Arize argues that prompt learning outperformed metric-focused approaches in part because it used richer text feedback, but also notes that the quality of the eval signal matters, 13:39-15:04.
- The talk explicitly warns that prompt learning only works if the eval itself is working, so eval engineering is part of the optimization loop rather than a side concern, 15:44-16:03.
- The workshop example initializes evaluators that can be swapped for LLM-as-judge, code-based checks, or other domain-specific evaluation methods, 37:12-37:32.
- The example pairs a comprehensive binary evaluator with detailed explanations and a granular rule checker that inspects rule-by-rule compliance; both produce feedback for iterative prompt improvement, 37:34-38:19.
- In the SWE-bench coding-agent experiment, the judge prompt received the problem statement, agent solution, unit tests, and actual result, then produced pass/fail plus explanations that were used to generate new system-prompt rules, 06:32-08:28.
- The talk explicitly attributes the difference versus GEPA-style optimization to iterating on eval prompts so they return better explanations, not merely to using English feedback, 09:07-10:20.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Calibrate LLM judges like binary classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Validate eval harnesses before trusting skill scores](validate-eval-harnesses-before-trusting-skill-scores.md)
- [System prompt learning updates agent rules from eval explanations](system-prompt-learning-updates-agent-rules-from-eval-explanations.md)

Sources:
- [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](../sources/20260106_SbcQYbrvAfI.md), 13:39-16:03, 37:12-38:19
- [The Unreasonable Effectiveness of Prompt Learning - Aparna Dhinakaran, Arize](../sources/20251223_pP_dSNz_EdQ.md), 06:32-08:28, 09:07-10:20
