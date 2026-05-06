# Validate eval harnesses before trusting skill scores

Summary: A skill evaluation can fail for harness reasons rather than agent reasons, so teams should inspect assertions, judge prompts, and raw outputs before trusting aggregate pass/fail scores.

Use when:
- An eval result contradicts manual inspection or task behavior.
- Adding LLM-as-judge grading to agent or skill evaluation.

Details:
- The Supabase demo produced a misleading pass/fail outcome because the evaluation checked the wrong metadata path for the `security_invoker` property instead of directly inspecting the view. 01:09:24-01:12:16
- The speaker notes that evals are code: if they evaluate the wrong expected behavior, the results are wrong even if the underlying agent behavior is acceptable. 01:10:50-01:11:21
- LLM-as-judge grading can automate nondeterministic evaluation, but the judging model can also hallucinate, so deterministic checks and raw-output inspection remain important. 01:04:32-01:05:08, 01:12:24-01:12:46
- A stronger setup can run skills in a fresh Docker or sandbox environment with only the skill under test, reducing contamination from local state or other skills. 01:13:03-01:13:18

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Evaluate agent skills with task scenarios and comparative conditions](evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)

Sources:
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md), 01:04:32-01:05:08, 01:09:24-01:13:18
