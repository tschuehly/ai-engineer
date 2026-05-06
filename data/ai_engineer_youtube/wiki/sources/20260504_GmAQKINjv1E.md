# Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase

Source: [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](https://www.youtube.com/watch?v=GmAQKINjv1E)
Uploaded: 2026-05-04
Transcript: `raw/20260504_GmAQKINjv1E/GmAQKINjv1E.en-orig.vtt`

## Summary

Pedro Rodrigues presents agent skills as structured context packages for improving product-specific agent behavior, then demonstrates a Supabase workflow where skills, MCP tools, and evals are used together to guide an agent toward safer database changes. The talk emphasizes progressive disclosure, a clear split between contextual guidance and integration tools, eval-driven skill development, and the need to validate the evaluator itself.

## Extracted Concepts

- [Agent skills package progressive-disclosure context for repeatable workflows](../concepts/agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) - this source explains skills as folders with `SKILL.md`, optional references, and scripts that expose only enough context for an agent to decide when to load more.
- [Use skills for workflow guidance and MCP for integrations](../concepts/use-skills-for-workflow-guidance-and-mcp-for-integrations.md) - this source distinguishes MCP as the integration/tool layer and skills as the context layer that explains how and when to use those tools.
- [Evaluate agent skills with task scenarios and comparative conditions](../concepts/evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md) - this source lays out an eval-driven loop for defining success metrics, running with and without a skill, and comparing results.
- [Validate eval harnesses before trusting skill scores](../concepts/validate-eval-harnesses-before-trusting-skill-scores.md) - this source shows that a bad assertion or judge can misreport whether a skill helped.

## Topic Links

- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

## Notes

- Skills are described as folders containing instructions, files for repeated workflows, custom information, and optional script-backed tools; `SKILL.md` carries front matter with at least a name and description. 03:17-04:22
- Progressive disclosure is framed as the main advantage: the agent initially sees the skill description and loads deeper files only when needed. 04:25-05:24
- Reference files can act like chapters behind the `SKILL.md` index, and references can point to other references, creating a graph of contextual material. 05:21-06:24
- The talk recommends using MCP for integrations and remote/service-backed actions, while skills provide the instructions and workflows that do not fit in MCP tool descriptions. 07:19-08:36
- Script-backed skills run in the local environment, so they inherit operating-system, dependency, and credential constraints that remote MCP tools can avoid. 07:56-08:36
- Eval-driven skill development starts by defining metrics, then creating the skill, running manual or automated evaluations, grading behavior, and iterating. 11:32-14:24
- A useful skill eval can inspect inputs, expected outputs, tool calls, reasoning steps, and deterministic assertions rather than only matching exact natural-language output. 10:34-11:07, 13:37-14:14
- In the Supabase demo, the skill guides the agent to create a SQL view with `security_invoker`; the evaluation setup compares conditions with and without the skill. 01:05:13-01:07:18
- The live eval produced misleading results because the harness checked the wrong thing, showing that skill scores depend on evaluator correctness. 01:09:24-01:12:46
- For production skills, the talk recommends checking whether skills are still used and whether they still describe a current workflow. 01:17:04-01:17:41
