# Preserve rollout trajectory context for agent RFT grading

Summary: Agent RFT needs rollout-level traceability: every tool call in a sampled trajectory should be tied to the same rollout context so the final answer can be graded with the evidence of how the agent got there.

Use when:
- Designing tool endpoints or reward endpoints for agent reinforcement fine-tuning.
- Building graders for multi-step agents where final-answer scoring depends on tool behavior.

Details:
- The talk describes Agent RFT training that can call customer-hosted public tool endpoints and then invoke a custom customer-hosted reward endpoint after each rollout. (02:57-03:18)
- Each agent rollout receives a unique identifier, and all tool calls into the customer's system are associated with that ID so the trajectory can be tracked as it evolves. (05:12-05:31)
- The final answer can be associated with the maintained context and passed as a holistic grading context into the grader, rather than grading only the final text in isolation. (05:31-05:44)
- For coding workflows, this trace context can include repository inspection, shell commands, file reads, tool-call counts, test output, lint output, and whether the agent validated its own work before claiming success. (06:54-08:53, 10:32-12:12)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Evaluate agent trajectories with backtests and smell metrics](evaluate-agent-trajectories-with-backtests-and-smell-metrics.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)

Sources:
- [Agent Reinforcement Fine Tuning - Will Hang & Cathy Zhou, OpenAI](../sources/20251209_p1CmPZ2j6Lk.md), 02:57-12:12
