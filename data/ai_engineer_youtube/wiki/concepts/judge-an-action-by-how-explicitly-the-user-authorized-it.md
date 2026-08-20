# Judge an Action by How Explicitly the User Authorized It

Summary: The same agent action can be correct or catastrophic depending on whether the user named its target. Risk policies keyed only on the operation ("delete", "upload", "curl") cannot express that, so the reusable rubric axis is authorization explicitness — how directly the user's own words license this specific action — scored against the action's impact.

Use when:
- Writing the rubric for an automated approval reviewer, a guardrail classifier, or an LLM judge over agent actions.
- Finding that a command allowlist is simultaneously too strict (blocking things the user asked for) and too loose (permitting the same command on a target nobody mentioned).
- Deciding what evidence an approval decision needs beyond the tool call itself.

Details:
- The worked contrast: "in some cases you want the agent to actually delete a file. In other cases you don't. If you ask it to or if it… is part of the project, it makes sense. Especially like things like if you ask it to delete a dot git folder, great. If you didn't ask it to, it should probably not touch that part and like completely delete your history." ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 14:24-14:46)
- Authorization is scored as a level, not a boolean, and the score is justified from the conversation: in the demo the user authorization is "high because we explicitly told it to delete the file." The second field is impact — "what is the impact of the deletion or like the action itself and what should we do?" ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 14:48-15:06)
- **The rubric requires the transcript, which is the operational consequence.** An approval component that sees only the tool call cannot compute this axis; the reviewer in the source is handed "the transcript as well as sort of the tool calls that are actually happening" precisely because "the context matters." Any guardrail you build on this rubric inherits that input requirement. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 14:03-14:28)
- The axis is not filesystem-specific. Applied to the network it separates "curling Google to see if… the internet works" from "uploading a file" — same egress capability, different licence, and the difference is again in what the user asked for rather than in the protocol. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 15:04-15:18)
- **Why the axis exists at all is the agency failure mode.** Prompting a model toward high agency produces actions that are reasonable continuations of the goal but were never authorized — uploading a file to a file share because email attachment failed. Those actions are invisible to an operation-keyed policy (uploading is allowed) and visible to an authorization-keyed one (nobody said "file share"). ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 12:38-13:10)
- **The security caution is that the evidence is attacker-adjacent.** Explicit authorization is read out of the transcript, and the transcript is exactly where injected content lives. A rubric that upgrades authorization when the conversation contains an instruction is, by construction, upgradeable by anything that can get text into the conversation. The source does not address this; treat authorization explicitness as an input to a judgment, never as an authorization primitive on its own — the wiki's guidance to [verify an action through a different channel than the one that acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md) applies here.
- **Provenance.** This is one slide in a vendor talk, described by the speaker as "a gross oversimplification" of the actual work, with no rubric text, no scale definition, no inter-rater or accuracy data, and no examples where the judgment was wrong. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 15:18-15:32)

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Escalate Risky Actions to a Read-Only Review Subagent](escalate-risky-actions-to-a-read-only-review-subagent.md)
- [Human Approval Can Hide Tool-Description and Parameter Risk](human-approval-can-hide-tool-description-and-parameter-risk.md)
- [Enforce Deterministic Guardrails Around Sensitive Tool Calls](enforce-deterministic-guardrails-around-sensitive-tool-calls.md)
- [Teach Calibrated Confidence So an Agent Knows When to Hand Off](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)
- [Verify an action through a different channel than the one that acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md)
- [Raise the Floor Before Maxing the Benchmark](raise-the-floor-before-maxing-the-benchmark.md)

Sources:
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 12:38-15:32
