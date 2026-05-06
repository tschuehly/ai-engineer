# Use Reviewer and Approver Roles To Make Agent Workflows Reliable

Summary: Agent workflows become more reliable when completion routes through explicit reviewer and approver roles instead of relying on one worker agent to remember every validation instruction.

Use when:
- A coding or operational agent often skips requested validation steps.
- Designing multi-agent review loops where quality checks and final acceptance are separate responsibilities.

Details:
- Paperclip's QA example gives a QA agent browser skills for opening sites, filling forms, and clicking buttons, then requires a review when an assignee finishes work.
- The talk separates a reviewer from an approver: a QA agent may iterate with the worker, while a manager or approver decides whether the reviewed work is sufficient for the organization's brand or standards.
- This workflow is positioned as a vendor-neutral alternative to per-agent hooks that behave differently across Claude Code, Codex, and other agents.
- The cited failure mode is prompt-only validation: asking a coding agent to test in the browser before handing work back often fails unless the workflow enforces the review path.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)

Sources:
- [Paperclip: Open Source Human Control Plane for AI Labor - Dotta Bippa](../sources/20260415_h403btjldDQ.md), 08:41-11:03
