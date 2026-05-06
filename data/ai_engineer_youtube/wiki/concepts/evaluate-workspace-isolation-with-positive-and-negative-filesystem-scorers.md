# Evaluate workspace isolation with positive and negative filesystem scorers

Summary: Agent workspace isolation should be evaluated with both a positive check for intended edits in the isolated workspace and a negative check for forbidden edits in the primary checkout. This catches a key failure mode of prompt-enforced worktree workflows: the agent silently escapes its assigned directory.

Use when:
- Testing a coding agent that should operate only inside a Git worktree, branch, sandbox, or temporary checkout.
- Replacing hard workspace constraints with prompt or skill instructions.

Details:
- Cursor's prompt-coded worktree workflow depends on instructing the model to stay inside its assigned checkout, which can fail in long sessions or with weaker models that forget or hallucinate the operating boundary. 12:33-13:18
- The described eval runs Cursor CLI headlessly and uses two scorers: one checks whether expected work happened in the worktree, while the other checks whether any work happened in the primary checkout where edits are forbidden. 15:18-16:10
- Early simple evals already exposed model differences: Haiku often deviated into the primary checkout, while Composer and Grok performed better in the tested cases. 16:20-16:42
- Evaluation results are meant to drive prompt updates, stronger system reminders, and eventually model training tasks that teach the workflow directly. 14:17-15:15, 16:42-17:05

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Evaluate agent skills with task scenarios and comparative conditions](evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)

Sources:
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md), 12:33-17:05
