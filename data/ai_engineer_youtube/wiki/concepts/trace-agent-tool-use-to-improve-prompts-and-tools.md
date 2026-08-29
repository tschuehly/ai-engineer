# Trace Agent Tool Use To Improve Prompts And Tools

Summary: Coding-agent observability should expose prompts, available tools, tool calls, and environment state so failures can be converted into better tool descriptions, tool behavior, or prompts.

Use when:
- Debugging why an agent selected the wrong tool or failed inside a workflow.
- Designing observability for agent runs that execute code, tests, and repository operations.

Details:
- The workshop presents Dagger Cloud as a visualization layer for understanding what an agent is doing, what tools it sees, and how it interacts with those tools. (16:05-16:34)
- Inspecting traces can reveal repeated tool misuse; the suggested fix is to improve the tool description or change how the tool works, not only to rerun the agent. (16:36-16:54)
- During the demo run, the trace shows prompts, model responses, available workspace functions, file reads, and tool calls as the agent edits a Vue app. (45:54-46:23)
- **Manufacture the trace corpus instead of waiting for production to supply it.** Sourcegraph built a purpose-made task set — hundreds of software-lifecycle tasks run with and without its MCP tool — and got "thousands and thousands of these traces" out of it, described as "amazing logs of data for like these really tight feedback loops where you can see exactly where it's breaking down and then go in and fix it." The economics are the point Jarmak makes elsewhere in the talk: "you can basically spin up like thousands of these agents to perform experiments on them and experiments that you can't really do as easily with the developers who don't want to maybe talk to you that much." Agent-user research scales in a way human-user research does not. See [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 05:36-06:33, 16:08-16:20)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Dynamic Artifacts Make Agent Work Reviewable and Reusable](dynamic-artifacts-make-agent-work-reviewable-and-reusable.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md)
- [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md)

Sources:
- [Ship Agents that Ship: A Hands-On Workshop - Kyle Penfound, Jeremy Adams, Dagger](../sources/20250727_Fzb1a24hF-o.md), 16:05-46:23
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 05:36-06:33, 16:08-16:20
