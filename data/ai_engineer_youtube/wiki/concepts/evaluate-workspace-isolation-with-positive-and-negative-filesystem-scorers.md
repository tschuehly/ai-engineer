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

- **A field failure that motivates the negative scorer and then argues past it.** AIDAChip ran role-scoped agents and found "an analog agent that's specifically for analog design actually overstepping and doing RTL agent work… Even we tried to enforce it, but it was a difficult problem" — a prompt-enforced boundary failing exactly as this page anticipates. Separately, an agent told not to write spec files did it through bash, then `sed`, then `cat`. Their conclusion is that the eval was never going to be the fix: they moved to "a spec hierarchy with agent scope and file isolation" and to blocking "from system level, not tool by tool." The negative scorer keeps its value as *verification* of an enforced boundary rather than as a substitute for one — and it is the natural test to run against a substrate-level block, which this source asserts and never verifies. ([Mohamed](../sources/20260822_0I6aoPSRzVc.md), 12:49-13:14, 13:36-14:25)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Evaluate agent skills with task scenarios and comparative conditions](evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Scope Role Agents With a Spec Hierarchy and File Isolation](scope-role-agents-with-a-spec-hierarchy-and-file-isolation.md)
- [Block the Capability at the Substrate, Because Denying a Tool Only Denies a Name](block-the-capability-at-the-substrate-because-denying-a-tool-only-denies-a-name.md)
- [Grade the Alignment, Not the Agents](grade-the-alignment-not-the-agents.md)

Sources:
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md), 12:33-17:05
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 12:49-13:14, 13:36-14:25
