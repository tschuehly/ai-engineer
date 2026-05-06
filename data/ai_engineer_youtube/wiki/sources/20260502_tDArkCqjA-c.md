# Human-in-the-Loop Automation with n8n - Liam McGarrigle

Source: [Human-in-the-Loop Automation with n8n - Liam McGarrigle](https://www.youtube.com/watch?v=tDArkCqjA-c)
Uploaded: 2026-05-02
Transcript: `raw/20260502_tDArkCqjA-c/tDArkCqjA-c.en-orig.vtt`

## Summary

Liam McGarrigle demonstrates a visible n8n automation pattern for a Gmail and Google Calendar agent: start from a chat or Slack trigger, attach a model and memory, expose service nodes as tools, keep credentials scoped by project, tune tool names and descriptions as prompt surface, and add human approval gates for sensitive actions.

## Extracted Concepts

- [Visual Agent Workflows Make Tool Use Observable and Adjustable](../concepts/visual-agent-workflows-make-tool-use-observable-and-adjustable.md) - supports visible agent orchestration with triggers, memory, tools, execution state, and auditability.
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](../concepts/route-high-impact-agent-actions-through-explicit-human-approval-gates.md) - supports human review for sensitive tool actions and approval routing.
- [Use Tool Names and Descriptions as Operational Prompts](../concepts/use-tool-names-and-descriptions-as-operational-prompts.md) - shows that tool metadata is prompt context that affects tool selection.
- [Split Large Automation Surfaces Into Specialized Subagents and Subworkflows](../concepts/split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md) - supports decomposing broad automations into subagents and reusable subworkflows.

## Topic Links

- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- n8n projects can separate credentials and collaborators so teams do not accidentally use the wrong credentials across unrelated workflows. 09:06-09:34
- n8n's visual interface still allows field-level JavaScript when the workflow needs a small amount of code inside a mostly visual automation. 02:00-02:23
- Service nodes such as Gmail and Google Contacts can be exposed as tools for the agent to call at its discretion. 22:06-22:27
- Node names and descriptions are passed to the LLM as tool names and descriptions, so vague or stale tool metadata becomes an agent behavior problem. 29:06-30:00
- Human approval should be a hard control boundary rather than another model decision, especially for actions that change calendars, send messages, or affect business process state. 01:10:41-01:16:08
