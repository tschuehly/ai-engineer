# Trace Agent Tool Use To Improve Prompts And Tools

Summary: Coding-agent observability should expose prompts, available tools, tool calls, and environment state so failures can be converted into better tool descriptions, tool behavior, or prompts.

Use when:
- Debugging why an agent selected the wrong tool or failed inside a workflow.
- Designing observability for agent runs that execute code, tests, and repository operations.

Details:
- The workshop presents Dagger Cloud as a visualization layer for understanding what an agent is doing, what tools it sees, and how it interacts with those tools. (16:05-16:34)
- Inspecting traces can reveal repeated tool misuse; the suggested fix is to improve the tool description or change how the tool works, not only to rerun the agent. (16:36-16:54)
- During the demo run, the trace shows prompts, model responses, available workspace functions, file reads, and tool calls as the agent edits a Vue app. (45:54-46:23)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Dynamic Artifacts Make Agent Work Reviewable and Reusable](dynamic-artifacts-make-agent-work-reviewable-and-reusable.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)

Sources:
- [Ship Agents that Ship: A Hands-On Workshop - Kyle Penfound, Jeremy Adams, Dagger](../sources/20250727_Fzb1a24hF-o.md), 16:05-46:23
