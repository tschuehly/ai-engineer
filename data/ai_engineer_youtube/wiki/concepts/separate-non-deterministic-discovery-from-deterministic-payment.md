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
- **The commerce specs implement this split as a named session state rather than as an integrator convention.** In UCP and ACP "the checkout APIs will have state, and the three different states are not ready for payment, ready for payment, and then completed," with payment-method selection as the transition that arms the session — "it's added to cart, but it's not ready for payment. I have to pick what I want to pay with." The deterministic leg is therefore enforced by an API that refuses to leave a state until its conditions are met, which is a stronger guarantee than asking the planner to stop being creative at the right moment. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 13:04-14:07)

- **The same split arrived at from the access layer, and it lands in the same place for a different reason.** Šteimantas decomposes a shopping agent into discovery, decision, and execution and gives each a different web-access primitive, keeping a real browser only for checkout because "we need to process inputs and the content is highly dynamic." He is optimizing cost and reliability, not blast radius, yet the boundary falls exactly where this page draws it — which is some evidence the seam is structural rather than an artifact of a payments perspective. Two additions for the transaction side. The wrong-amount failure mode above has a concrete cause and a concrete fix: prices and stock vary by visitor location, so pinning the exit location identically at the verification and checkout stages removes a class of price and availability mismatch ([Keep Geolocation Consistent Across Pipeline Stages](keep-geolocation-consistent-across-pipeline-stages.md)). And the "letting the robot operate the browser like a human is finicky, slow, and hard to observe" objection is narrower than it looks — it is an argument against doing so in *every* stage, which is the actual failure Šteimantas diagnoses; a browser confined to the one irreducible stage is a much smaller surface than a browser-driven pipeline. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 03:45-04:47, 11:54-13:20)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Security](../topics/security.md)

Related concepts:
- [Split Discovery and Validation Across Reasoning and Deterministic Models](split-discovery-and-validation-across-reasoning-and-deterministic-models.md)
- [Keep Workflow Orchestration Deterministic and Put Side Effects in Steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md)
- [Move Mandatory Brittle Tool Steps Outside the Agent Loop](move-mandatory-brittle-tool-steps-outside-the-agent-loop.md)
- [Bound Agent Payments With Processor-Enforced Mandate Tokens](bound-agent-payments-with-processor-enforced-mandate-tokens.md)
- [Model Agentic Checkout as an Explicit Session State Machine](model-agentic-checkout-as-an-explicit-session-state-machine.md)
- [Assign a Web-Access Primitive Per Pipeline Stage](assign-a-web-access-primitive-per-pipeline-stage.md)
- [Keep Geolocation Consistent Across Pipeline Stages](keep-geolocation-consistent-across-pipeline-stages.md)

Sources:
- [Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe](../sources/20260606_KLSuFPj2ld0.md), 00:50-04:50, 14:56-15:55
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 13:04-14:07
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 03:45-04:47, 11:54-13:20
