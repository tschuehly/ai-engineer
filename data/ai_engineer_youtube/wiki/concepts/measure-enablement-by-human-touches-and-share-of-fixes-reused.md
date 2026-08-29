# Measure Enablement by Human Touches and Share of Fixes Reused

Summary: Two metrics for agent enablement that a team can move and a VP can defend: how many human touches it takes before the agent produces the right result, which should fall as the harness and context improve, and how much of each fix is shared, because a fix that lands in a common harness multiplies across everyone rather than making one person faster.

Use when:
- Choosing what to report on an agent-enablement program when token spend and seat counts are the only numbers on hand.
- A VP of Engineering has to justify agent spend and cannot prove "faster delivery" or "better quality."
- Deciding whether an improvement should be made locally or pushed into a shared surface.
- Distinguishing a team that is genuinely improving its system from one that is simply prompting more.

Details:
- **Metric one: human touches to a correct result.** "There's a lot of metrics that people are saying like, 'is your tokens spend and all that stuff?' I started to believe in these two metrics… One is you start measuring how many human touches you still do to have the agent do the right thing. That's supposed to go down the better your harness is, the better your context is, the better your guidelines are." ([Debois](../sources/20260822_zCJtYuqwm7E.md), 09:09-09:52) The definition is deliberately end-to-end — it counts interventions to a *right* result, so it cannot be gamed by shipping wrong output faster.
- **Metric two: reuse share, and the reframing inside it.** "If you're going from solo to shared system, that becomes a multiplier. You fix something once, everybody gets the benefit. This is not the multiplier from the one person becoming the 10x person, but the one change that optimized the agents has an impact on all the people." (09:52-10:19) The 10x-engineer frame is being explicitly rejected: the unit of leverage is the shared artifact, not the individual.
- **Why these two and not velocity or quality: attribution.** For the VP, "we have faster delivery, maybe they can promise, but hard to prove. We have quality that improved, again, hard to say. But… you can show how much turns and how much improvement you're making on that journey. And same thing, how much there is reuse. So, it's an easier way to show metrics than comparing productivity with and without agent[ic] coding." (17:32-18:19) The argument is not that touches and reuse matter more than delivery speed — it is that they are causally attributable to the enablement work, while a delivery-speed comparison needs a counterfactual nobody has.
- **The pair is complementary, not redundant.** Touch count is a per-task efficiency measure that a single engineer can improve by tuning their personal setup. Reuse share is the check that the improvement left that person's machine. A program where touches fall and reuse stays flat has produced power users, not a platform — which is exactly the failure [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md) describes structurally and this pair makes visible.
- **Touch count doubles as a cost metric, which is why it survives a budget conversation.** "If I can reduce the number of iterations the agent has to run through, that is an optimization that I can run." (13:38-13:47) Fewer turns to the right answer is simultaneously less human attention and fewer tokens, so the same number answers the enablement question and the spend question — see [Ship a Catalog of Paved Roads, Not One Standard](ship-a-catalog-of-paved-roads-not-one-standard.md) for the cost-visibility half.
- **Where it sits against the wiki's other measurement advice.** [Measure AI Transformation by Outcomes Instead of Adoption](measure-ai-transformation-by-outcomes-instead-of-adoption.md) warns that adoption breadth proves nothing, and [Stage Agentic-Engineering Adoption With a Delegation Maturity Model](stage-agentic-engineering-adoption-with-a-delegation-maturity-model.md) supplies a capability axis for the same reason. Human touches is neither: it is a *process* metric that moves within one rung of the ladder, so it is the number you watch between quarterly outcome reviews. Its weakness is the mirror of its strength — a falling touch count on a stable task mix says nothing about whether the org is shipping better software.
- **Caveats, and they are substantial.**
  - Neither metric is defined operationally. What counts as a touch — a chat turn, a manual edit, a re-run, a review comment — is left open, and the answer changes the number by a lot. Nothing is said about how to collect either without self-reporting.
  - Debois reports no measured value for either metric in any team, including his own. These are proposals.
  - Touch count is only comparable within a stable task mix. A team that starts routing harder work to agents will see touches rise while improving, and there is no normalization offered.
  - "How much of each fix is shared" has no denominator. Share of what — fixes, engineers reached, repos touched? The intent is clear and the instrument is not.

Related topics:
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Measure AI Transformation by Outcomes Instead of Adoption](measure-ai-transformation-by-outcomes-instead-of-adoption.md)
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Stage Agentic-Engineering Adoption With a Delegation Maturity Model](stage-agentic-engineering-adoption-with-a-delegation-maturity-model.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Ship a Catalog of Paved Roads, Not One Standard](ship-a-catalog-of-paved-roads-not-one-standard.md)
- [Run the Retro Against the System and Split Planning by Scopedness](run-the-retro-against-the-system-and-split-planning-by-scopedness.md)
- [Measure AI Coding Adoption With PR Telemetry and Guardrails](measure-ai-coding-adoption-with-pr-telemetry-and-guardrails.md)

Sources:
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 09:09-10:19, 13:38-13:47, 17:32-18:19
