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
- **A cheap structural pre-screen, and the second axis a task-scenario suite misses.** Touil reports skill evaluation as still unsettled ("there's still kind of like a discussion on what is the right approach to evaluate skills") and uses a static check as the interim: evaluate the skill against Anthropic's published best practices, because "if the skill is not invoked properly, if the skill is not structured properly, there's a high chance that it's not going to be high quality." ([Touil](../sources/20260828_M05vON8i0aI.md), 19:13-19:37) That is an admission gate, not a quality measure — a well-formed skill can be confidently wrong. He also names the axis a fixed scenario suite silently holds constant: skills must be validated "not against your task but also against the latest models that comes," or "the quality starts degrading over time" (11:43-11:55), which makes the with-skill/without-skill comparison something to re-run per model rather than once.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Evaluate workspace isolation with positive and negative filesystem scorers](evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md)
- [Auto-Evolving Skills Multiply Whatever Governance You Already Have](auto-evolving-skills-multiply-whatever-governance-you-already-have.md)

Sources:
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md), 10:34-14:24, 01:03:12-01:07:18, 01:13:19-01:13:38
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md), 15:18-16:10
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 11:43-11:55, 19:13-19:37
