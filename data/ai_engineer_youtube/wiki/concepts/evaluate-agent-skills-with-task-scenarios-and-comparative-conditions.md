# Evaluate agent skills with task scenarios and comparative conditions

Summary: Skill evaluation should use concrete task scenarios, expected behavior, and condition comparisons so teams can measure whether a skill changes agent behavior in the intended direction.

Use when:
- Building an eval loop for an agent skill or workflow prompt.
- Testing whether a skill improves a product-specific agent task.

Details:
- The proposed eval-driven loop starts by defining metrics and what "good" means, then creating the skill, running manual or automated evaluations, grading results, and iterating. 11:32-14:24
- Evaluations can check inputs, expected outputs, reasoning steps, tool calls, deterministic assertions, and LLM-graded behavior rather than exact natural-language output alone. 10:34-11:07, 13:37-14:14, 01:04:32-01:05:08
- For skill impact, the demo compares two conditions: with the skill loaded and without it, then compares outputs from the same task. 01:06:52-01:07:18, 01:13:19-01:13:38
- Braintrust and Langfuse are named as tools that can support structured eval runs and observability over agent behavior. 12:37-13:34, 01:03:12-01:03:18
- Prompt-coded coding workflows need task-specific behavioral scorers, such as checking that an agent edited its assigned worktree and did not edit the primary checkout. 15:18-16:10

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Evaluate workspace isolation with positive and negative filesystem scorers](evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md)

Sources:
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md), 10:34-14:24, 01:03:12-01:07:18, 01:13:19-01:13:38
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md), 15:18-16:10
