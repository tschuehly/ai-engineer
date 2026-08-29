# Keep Human Review on High-Risk Agent Operations

Summary: Human review should remain on sensitive agent actions, dependency changes, and final diffs. LLM monitors and review tools can help triage, but they are not yet substitutes for deterministic controls and accountable human approval.

Use when:
- Designing approval policies for code-executing agents.
- Deciding which agent commands, dependency changes, or generated diffs need human inspection.

Details:
- The talk says code review, approvals, and confirmations are important because they keep humans in control, but approving every trivial command is impractical. 05:34-06:04
- LLM-based PR review and code-review tools are useful, but they do not replace a human reviewing operations the model is about to perform. 09:49-10:16
- Dependency additions deserve scrutiny because a model may install a lesser-known, vulnerable, malicious, or typo-squatted package that later runs in a privileged environment. 10:16-10:33
- Dependency-security tools such as Socket's MCP server can be exposed to the agent or run as a post-rollout system check before dependency changes are trusted. 11:47-12:15
- LLM-based monitors in the loop are valuable but not as certain as deterministic controls, so review design should combine monitors with system-level enforcement. 13:02-13:17
- **Scope can do the work of review, and often does in year one.** Cloudflare's entire go-to-market agent surface is read-only by construction — every named use case is a query or a generated artifact — so no approval gate exists because no agent can change a record. The asymmetry that justifies the sequencing is failure visibility: a wrong answer is caught by the person who asked for it, while a wrong CRM write propagates into forecasts, routing, and compensation before anyone reads it. Quoting and approvals are named as the harder class precisely because they already have human authorization chains an agent would have to enter rather than precede. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 12:36-14:28, 17:51-18:04)
- **Where review is unaffordable, containment substitutes for it — partially.** Berry's agents write to the system of record without a per-write gate, and the control is structural: agent-owned columns kept separate from human- and pipeline-owned ones, so a bad value cannot overwrite a good one. This is the option for write paths whose volume rules out review, and its boundary is consumption — once a routing rule or another agent reads the agent-owned column, the error is loose again. Containment bounds the damage; only review bounds the error. ([Berry](../sources/20260826_UhCY231d0FQ.md), 12:23-12:43)
- **Pause-and-resume as a substrate feature rather than a per-workflow build.** In a Temporal-backed agent stack, "human-in-the-loop tooling to just pause execution, get input, resume" is listed alongside config-scoped tool calls as something that arrives with durable execution. That matters for adoption: if suspending a run for approval requires bespoke state handling, teams under delivery pressure skip the gate; if the workflow engine already suspends and resumes, the cheap path and the safe path are the same path. ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 10:49-11:13)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)

Related concepts:
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Human approval can hide tool-description and parameter risk](human-approval-can-hide-tool-description-and-parameter-risk.md)
- [Read-Side Agents Scale First Because the Write Side Needs Approvals](read-side-agents-scale-first-because-the-write-side-needs-approvals.md)
- [Give Agents Their Own Fields in the System of Record](give-agents-their-own-fields-in-the-system-of-record.md)
- [Gate a Generated Multi-Channel Campaign on the Channel Owner](gate-a-generated-multi-channel-campaign-on-the-channel-owner.md)

Sources:
- [OpenAI on Securing Code-Executing AI Agents - Fouad Matin (Codex, Agent Robustness)](../sources/20250730_w7IMuYsBNr8.md), 05:34-06:04, 09:49-13:17
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 12:36-14:28, 17:51-18:04
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 12:23-12:43
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 10:49-11:13
