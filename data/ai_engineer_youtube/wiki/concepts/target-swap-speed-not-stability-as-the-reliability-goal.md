# Target Swap Speed, Not Stability, as the Reliability Goal

Summary: Once agents write and rewrite parts of the system, the useful reliability objective inverts. The question is not how reliable you can make the system, but how much of it you can change while holding reliability constant — which makes how fast you can swap a component in and out the thing to optimize, and makes captured knowledge, not the current implementation, the durable asset.

Use when:
- Setting a reliability or platform objective for a team whose components are increasingly agent-generated.
- Deciding whether to harden the current implementation or reduce the cost of replacing it.
- Arguing that a model, skill, or harness component should be treated as swappable by default.
- Framing what an AI transformation is actually accumulating, when the code itself is cheap to regenerate.

Details:
- **The inversion, in one sentence.** "If you ask the question of how fast can we swap in, swap out something new, that's your reactive mode. And if you can improve that, ultimately it's not about making the whole system more reliable, but can I keep it reliable while changing more of the system." ([Debois](../sources/20260822_zCJtYuqwm7E.md), 20:43-21:07)
- **The lineage he draws it from.** "That brings continuous delivery actually to continuous learning." (20:38-20:43) The analogy is load-bearing and worth unpacking: continuous delivery's insight was that deploy frequency and stability are not a trade-off once the deployment pipeline is good enough, so you optimize the pipeline rather than the release. The claim here is the same shape one level up — optimize the swap, not the component.
- **What the asset is, if the components are replaceable.** "I think your moat is capturing the knowledge. The knowledge you're putting now into skills, in your context, and maybe in your harness, the way you restrain this, your business context." (20:24-20:43) The knowledge persists across swaps precisely because it is separate from any implementation — the same reason [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md) treats skills as the place organizational know-how ends up.
- **A concrete reading for the model layer.** The wiki records repeatedly that a model or harness change invalidates the assumptions built around it — [A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md) reports roughly 80% of a suite voided by one switch. Under this page's objective, that number *is* the metric: it measures how expensive your next swap will be, and driving it down is the work. That reframes an eval suite tied to one harness from a completed asset into a swap cost.
- **The risk posture that goes with it: a dim factory, not a dark one.** "The dark factory, which is probably a dim factory. You have to see what risk you're willing to take for what features. So, not all features will become autonomous, but you can invest more in auditing like problems — who changed the code — verifiers that check whether that code was useful, and when it fails, you invest in situational awareness as well. So, there's a whole spectrum from being a micromanager to being on autonomous approval that everything is correct, but you make the decision on what your risk level is." (19:46-20:24) The three named investments — audit trail, verifier, situational awareness — are what let you keep reliability while changing more, so they are the concrete version of the objective rather than a separate topic. See [Choose Autonomy Level by Task Uncertainty and Control Needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md) for the wiki's slider, to which this adds that the level is chosen per feature by risk appetite rather than per system.
- **Why "dim" rather than "dark" is the substantive word.** A dark factory has no humans in it at all. Debois's position is that the fully autonomous end of the spectrum is reachable for some features and not chosen for others, and that the choice is a risk decision an organization makes rather than a capability it waits for — which is the same reading he applies to "it will not work here" at the start of the talk (00:24-00:56).
- **Caveats.**
  - Entirely unmeasured and unimplemented. No swap-time figure, no example of a component swapped, and no method for measuring "how much of the system you can change."
  - The objective is stated at a level of abstraction that resists operationalization. Continuous delivery had lead time and change-failure rate; nothing equivalent is proposed here.
  - Treating knowledge as the moat needs an argument the talk does not make about why context files and skills are more defensible than code, given they are equally copyable and equally portable when people leave.

Related topics:
- [Workflows](../topics/workflows.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Assume the Harness Commoditizes and Differentiate on the Organization](assume-the-harness-commoditizes-and-differentiate-on-the-organization.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)
- [A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)
- [Choose Autonomy Level by Task Uncertainty and Control Needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md)
- [An Audit Trail Is a Chain of Evidence, Not a Developer Log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md)
- [Keep the Harness Thick Early and Thin It as the Model Improves](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md)
- [Institutionalize Knowledge Infrastructure for AI Adoption](institutionalize-knowledge-infrastructure-for-ai-adoption.md)

Sources:
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 19:46-21:07
