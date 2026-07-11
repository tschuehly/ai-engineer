# Agentic Workloads Turn Token Price Into Unit-Economics Pressure

Summary: Agentic products can multiply inference volume because one user action may trigger many model calls. That makes per-token hosted pricing feel different from earlier single-call applications and can push teams toward owned compute or open-model serving for ROI.

Use when:
- Estimating AI product unit economics for agentic workflows.
- Explaining why falling token prices do not automatically solve cost once agent call volume grows.

Details:
- The speaker says ballooning cost was less visible in the prior year because enterprises expected falling price per token to solve it. (05:51-06:10)
- Agentic use cases changed the calculus: one user action can produce roughly 50 inference calls, so costs can balloon even as per-token prices fall. (09:07-09:34)
- To show ROI and economic viability, enterprises may compare per-token API pricing with running models themselves and paying directly for compute. (09:36-10:07)
- The cost decision is tied to control: the talk frames owned compute as a way to move from being a price taker to controlling the price shape. (09:53-10:07)
- The "cost of intelligence keeps falling" assumption is not safe: StandardAgents reports the trend *reversed* in 2026, with per-token cost up ~29–30% adjusted for IQ and ~76% unadjusted at mid-year (partly a memory crunch). That makes per-task efficiency — cheaper models and smaller contexts on narrow tasks — a first-order lever, especially for customer-facing AI where a premium model like Fable is uneconomical unless the customer has a massive lifetime value. ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 22:37-24:13)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Prevent AI billing surprises with caps, notifications, and rate limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Domain-specific agents unlock small models and tight permissions](domain-specific-agents-unlock-small-models-and-tight-permissions.md)

Sources:
- [The Rise of Open Models in the Enterprise — Amir Haghighat, Baseten](../sources/20250724_3WV1vT0B0cg.md), 05:51-06:10, 09:07-10:07
- [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](../sources/20260629_spNAUEgq_A8.md), 22:37-24:13
