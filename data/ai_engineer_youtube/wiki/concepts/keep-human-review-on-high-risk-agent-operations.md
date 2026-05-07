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

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)

Related concepts:
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Human approval can hide tool-description and parameter risk](human-approval-can-hide-tool-description-and-parameter-risk.md)

Sources:
- [OpenAI on Securing Code-Executing AI Agents - Fouad Matin (Codex, Agent Robustness)](../sources/20250730_w7IMuYsBNr8.md), 05:34-06:04, 09:49-13:17
