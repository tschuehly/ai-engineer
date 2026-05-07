# Route Agent Optimization By Task Profile, Not One Fixed Loop

Summary: Agent optimization should choose a strategy bundle from the task profile rather than applying one context-refinement procedure to every request. Useful profiles include complexity, uncertainty, verifiability, and resource constraints.

Use when:
- Designing an agent runtime that can choose between minimal prompting, extra reasoning samples, memory retrieval, verification, or model adaptation.
- Deciding whether a simple task should avoid a heavy agent pipeline.

Details:
- Meta-ACE is described as a meta-controller that allocates strategies across context, compute, verification, memory, and parameter dimensions after profiling the task (05:08-06:36).
- The profiling layer assesses semantic complexity, uncertainty, verifiability, and resource availability, including context window, compute budget, and time constraints (06:47-07:41).
- The strategy toolbox includes minimal context for simple tasks, AC-style reflection, adaptive compute, hierarchical verification, adaptive structured memory, and selective test-time training for high-stakes tasks (07:45-08:46).
- Uniform processing can waste resources on simple tasks; the talk claims task-adaptive allocation can save compute for simple tasks while routing complex tasks toward heavier test-time compute, multiple attempts, and memory retrieval (12:23-13:26).

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Choose autonomy level by task uncertainty and control needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md)

Sources:
- [The Unbearable Lightness of Agent Optimization - Alberto Romero, Jointly](../sources/20251124_zfvEMNmVlNY.md), 05:08-08:46
