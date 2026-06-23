# Separate Non-Deterministic Discovery From Deterministic Payment Execution

Summary: Agent discovery and exploration benefit from LLM non-determinism, but credentials, payments, and checkout require determinism. Split the system so a non-deterministic planner finds what to buy while a deterministic, constrained path with verifiable parties executes the transaction, shrinking the blast radius of agent error.

Use when:
- Designing agentic purchasing, checkout, procurement, or any workflow where an agent moves money or takes an irreversible high-impact action.
- Deciding which steps an LLM should drive freely and which must be constrained to deterministic, audited execution.

Details:
- Kaliski's one-line takeaway: discovery and exploration *benefit* from non-determinism (LLMs predict and recommend code, products, and businesses), but credentials, payments, and checkout *require* determinism — not just benefit from it. The critical separation is "how do I find things / what should I do" from "how am I going to transact." (00:50-01:22)
- Four agent-payment failure modes motivate the split: wrong place (a look-alike phishing domain such as a fake amazon.*), wrong thing (an item 10× more expensive, or the wrong variant), wrong amount (prices drift across regions, currencies, and taxes, so a number parsed off a page may not be the real charge), and wrong credential (a card pasted to the wrong place; some payment methods are hard or impossible for an agent to relay). (02:42-04:02)
- The naive baselines are both bad: handing over a raw card number gives no spend controls, and letting the robot operate the browser like a human is finicky, slow, and hard to observe — the same monetary-risk problem any web app has, which is why APIs exist ("dashboard is for a human; robots prefer code"). (02:52-04:31)
- The target shape is a non-deterministic planner plus constraints with verifiable parties and structured negotiation, yielding a small radius of risk: bind to a merchant, enforce spend policies, drive it by API, and use verifiable identities. (04:31-04:50, 15:36-15:55)
- Make a business agent-friendly by exposing programmatic deterministic flows rather than only web UIs, because UI-only surfaces increase the non-determinism of agent interactions and the chance of mis-parsed details. (14:56-15:20)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Security](../topics/security.md)

Related concepts:
- [Split Discovery and Validation Across Reasoning and Deterministic Models](split-discovery-and-validation-across-reasoning-and-deterministic-models.md)
- [Keep Workflow Orchestration Deterministic and Put Side Effects in Steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md)
- [Move Mandatory Brittle Tool Steps Outside the Agent Loop](move-mandatory-brittle-tool-steps-outside-the-agent-loop.md)
- [Bound Agent Payments With Processor-Enforced Mandate Tokens](bound-agent-payments-with-processor-enforced-mandate-tokens.md)

Sources:
- [Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe](../sources/20260606_KLSuFPj2ld0.md), 00:50-04:50, 14:56-15:55
