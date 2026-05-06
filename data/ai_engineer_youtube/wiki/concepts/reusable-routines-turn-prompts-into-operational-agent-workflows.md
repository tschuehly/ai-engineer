# Reusable Routines Turn Prompts Into Operational Agent Workflows

Summary: Repeated agent work should become reusable routines with schedules, manual triggers, template variables, and skill references instead of staying as copied prompts in a folder.

Use when:
- A team repeats the same agent prompt for releases, PR handling, reports, or operational updates.
- Deciding whether to encode a workflow as a routine, skill, or both.

Details:
- Paperclip routines can run on a schedule or manually, can be grouped by project or agent, and can expose template variables such as the branch for a PR workflow.
- Example routines include summarizing merged PRs into a Discord message, writing a release changelog, creating a PR from a branch, and using a Greptile review skill after PR submission.
- Routines can call skills, creating overlap with skill systems: skills package how to do specialized work, while routines encode when and with what variables the work should run.
- Reports are treated as intermediate work products that can later grow action buttons for creating issues, plans, or feature integrations.

Related topics:
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Package reusable context as skills, libraries, and registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Automation loops convert repeated review and triage into factory improvements](automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md)

Sources:
- [Paperclip: Open Source Human Control Plane for AI Labor - Dotta Bippa](../sources/20260415_h403btjldDQ.md), 11:05-14:22
