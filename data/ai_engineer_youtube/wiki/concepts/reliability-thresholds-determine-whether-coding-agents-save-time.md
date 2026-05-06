# Reliability Thresholds Determine Whether Coding Agents Save Time

Summary: Coding agents can be impressive on benchmarks while still slowing expert developers if their output is not reliable enough to accept cheaply. Productivity depends on whether the agent reduces total work after prompting, review, correction, and context handoff are counted.

Use when:
- Evaluating whether a coding agent will speed up expert maintainers on mature repositories.
- Explaining why a model can pass benchmark tasks but fail to improve real engineering throughput.

Details:
- The METR field study found that experienced developers on mature open-source repositories took 19% more time when AI was allowed, despite expert forecasts of about 40% savings and participant forecasts around 24-25%. (12:29-13:24)
- The talk identifies overoptimism as a failure mode: if developers expect AI to help, they may spend time invoking it even on tasks where direct implementation would be faster. (14:14-14:30)
- High-context maintainers may already know the solution and be limited mostly by typing or mechanical implementation, so prompting and supervising an agent can be slower than doing the work directly. (14:30-14:59)
- Reliability needs to be high enough that developers can accept output without costly verification; the speaker suggests that something like 95-99% correctness may be needed for "tab tab tab" productivity on these tasks. (18:22-18:46)
- Unit-test-style or SWE-bench-like scoring can miss mergeability, maintainability, and quality constraints that matter to future collaborators and repository owners. (18:47-19:16)
- Task interdependence can erase apparent subtask speedups: if humans need the context and rationale from task A to complete task B, delegating task A may make the overall sequence slower or less reliable. (19:55-20:22)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Measure AI developer productivity with field experiments, not benchmark extrapolation alone](measure-ai-developer-productivity-with-field-experiments-not-benchmark-extrapolation-alone.md)

Sources:
- [Why Agent Hype can fall short of reality - Joel Becker, METR](../sources/20251224_RhfqQKe22ZA.md), 12:29-20:22
