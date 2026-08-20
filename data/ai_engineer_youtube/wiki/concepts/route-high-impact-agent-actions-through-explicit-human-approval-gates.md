# Route High-Impact Agent Actions Through Explicit Human Approval Gates

Summary: Agent workflows should route sensitive or high-impact actions through explicit approval steps that the model cannot bypass.

Use when:
- Giving an agent access to email, calendar, HR, finance, or other state-changing tools.
- Designing approval flows for chat, Slack, webhooks, or subworkflows.
- Deciding when a coding agent should pause before privileged filesystem, server, or network exposure actions.

Details:
- The workshop adds human-in-the-loop control to a Gmail and Google Calendar management agent so useful automation remains observable and controllable. 01:10-01:25
- Approval routing can use the trigger's user or channel metadata for ordinary replies, but should send sensitive requests such as vacation-day actions to the relevant decision maker or channel for approve/deny handling. 01:10:41-01:11:07
- The approval step is described as a hard human-review boundary: letting the LLM decide whether approval occurred would defeat the purpose of the control. 01:13:56-01:15:00
- When the built-in approval surface does not fit, confirmation logic can be implemented as a subworkflow with an if-node branch and exposed back to the agent as a tool. 01:15:30-01:16:08
- Guardian approvals are presented as a safer alternative to all-access coding-agent operation: privileged actions such as deleting directories, running servers, or exposing files should trigger review logic instead of being granted by default. 49:50-51:40
- Carpentero adds a caveat for approval UX: a human may approve a simplified operation while the model reads a fuller tool description or hidden parameter that changes the actual action. 10:53-12:04, 15:28-15:39
- Auth0 describes an async approval pattern for long-running agents: the agent initiates an authorization request for a risky operation, the user receives structured transaction details, and approval returns as an access token containing the exact approved details. 09:02-10:40
- BlackRock's regulated financial-app framing argues for designing human-in-the-loop review first because compliance and four-eyes checks remain necessary even when agentic automation is tempting. 13:44-14:05
- Kozlov's Cloudflare/Knock example wraps an `issueCard` tool in required human input, defers execution until approval, routes the approval webhook back to the correct durable object, and stores status so the same card cannot be provisioned twice. 15:58-18:44
- Kyle Jaejun Lee (KRAFTON) runs a fleet-wide **review gateway** to catch plan drift as plans flow down an agent hierarchy: any layer that wants to act submits its plan and then blocks — "Nothing runs until I approve. And the second I approve, a hook fires the work off automatically." This collapses per-pane inspection into "One web inbox, one control point, I never walk into the work windows anymore," and as the fleet grows every machine sends its review requests over SSH into one main gateway hosted on an always-on box, "because… Your one point of control can't be a thing that falls asleep." ([I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](../sources/20260708_4kYl2_mqmnQ.md), 03:20-04:11, 07:04-07:27)

- Amazon AGI Lab adds a second, model-side layer under the same gate. Their computer-use agents are *trained* to judge whether an action is authorized, irreversible, visible to the user, and impactful, and to escalate on their own ([calibrated confidence](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)); the harness then keeps a hard override — "wherever the confidence calibration of the model is not correct, we let the harness override the model and force it to give control back to the user." The learned estimate generalizes to actions no policy author enumerated; the enforced gate covers the case where the estimate is wrong. Neither replaces the other. ([From RL to IRL](../sources/20260814_Cc0_nyxROBA.md), 10:09-10:34, 13:44-13:55)

- **The gate has a failure mode of its own: users turn it off.** OpenAI reports that Codex's approval prompts produced measurable fatigue — "in our own testing… we saw people would just start clicking yes" and "in polls that we did… people started to just use full access mode more" — so the approval count is itself a metric to watch, not just a safety dial to turn up. Their response was not a better prompt but a different reviewer: an automatic [read-only review subagent](escalate-risky-actions-to-a-read-only-review-subagent.md) that judges the action and only escalates to the human when it disagrees, with the criterion being [how explicitly the user authorized it](judge-an-action-by-how-explicitly-the-user-authorized-it.md). That inverts this page's default — the human gate stops being per-action and becomes the exception path — and it moves the risk from "human approves without reading" to "model approves wrongly," for which the source offers no false-approval rate. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 11:59-12:22, 13:15-15:32)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Grow personal-agent permissions incrementally from recurring pain](grow-personal-agent-permissions-incrementally-from-recurring-pain.md)
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Human approval can hide tool-description and parameter risk](human-approval-can-hide-tool-description-and-parameter-risk.md)
- [Vault and exchange tokens for scoped upstream agent access](vault-and-exchange-tokens-for-scoped-upstream-agent-access.md)
- [Teach Calibrated Confidence So an Agent Knows When to Hand Off](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)
- [Escalate Risky Actions to a Read-Only Review Subagent](escalate-risky-actions-to-a-read-only-review-subagent.md)
- [Judge an Action by How Explicitly the User Authorized It](judge-an-action-by-how-explicitly-the-user-authorized-it.md)

Sources:
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md), 01:10-01:25, 01:10:41-01:11:07, 01:13:56-01:16:08
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md), 49:50-51:40
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md), 10:53-12:04, 15:28-15:39
- [Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0](../sources/20260114_VSdV-AdSlis.md), 09:02-10:40
- [How BlackRock Builds Custom Knowledge Apps at Scale — Vaibhav Page & Infant Vasanth, BlackRock](../sources/20250823_08mH36_NVos.md), 13:44-14:05
- [Building Agents (the hard parts!) - Rita Kozlov, Cloudflare](../sources/20250723_j_TKDweOsYE.md), 15:58-18:44
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](../sources/20260708_4kYl2_mqmnQ.md), 03:20-04:11, 07:04-07:27
- [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../sources/20260814_Cc0_nyxROBA.md), 10:09-10:34, 13:44-13:55
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 11:59-12:22, 13:15-15:32
