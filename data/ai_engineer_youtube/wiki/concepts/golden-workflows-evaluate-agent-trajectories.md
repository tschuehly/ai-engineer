# Golden Workflows Evaluate Agent Trajectories

Summary: Golden workflows can evaluate whether an agent chose the right intermediate steps, not only whether its final answer looks acceptable. This makes enterprise agent evaluation trace-aware and closer to how known business work should proceed.

Use when:
- A team has known task recipes, playbooks, or successful traces that define expected process steps.
- Final-answer grading hides whether the agent skipped required internal checks, sources, approvals, or metrics.

Details:
- An agent execution trace is itself a generated workflow: it receives a task, plans, acts, observes results, and repeats until it responds (05:20-06:16).
- A company can collect golden workflows that map tasks to the steps required to solve them, then compare a new agent trace against those expected steps (06:18-06:55).
- This differs from end-to-end answer grading because the evaluation asks whether the agent did the right work to get the answer, not just whether the response looked good (06:55-07:10).

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Agent Traces Require Specialized Eval Infrastructure](agent-traces-require-specialized-eval-infrastructure.md)

Sources:
- [How to build Enterprise Aware Agents - Chau Tran, Glean](../sources/20250724_hxFpUcvWPcU.md), 05:20-07:10
