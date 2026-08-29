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
- **The internal-tooling version of the pressure, with a measured relief valve.** Coinbase "defaulted to using GLM and Kimi in their internal LLM gateway and… this has cut their AI spend by nearly half while their token usage continues to grow" — the volume kept climbing and the bill halved anyway, because the swap happened at the gateway rather than in every calling application. Rizwan's projection is that this becomes the default enterprise shape: "businesses building their own internal tooling and routing to work with these agents in the most dollar efficient way for them. Even if it means not having access to the latest new feature in something like Claude Code." The demand-side figures he stacks against it show why the pressure is now visible where it previously was not: an anonymous CFO report of $500 million on Claude in a single month with no per-user limits set, and Uber's CTO reporting $2,000 per user per month and the entire 2026 budget spent in four months. All four figures are relayed second-hand from slides. ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 05:46-06:27, 10:27-10:55)


- **A measured instance of the multiplication, taken at two points in the same session.** Two coding-agent terminals given identical prompts — one always calling Claude Opus, one behind a per-task router — diverge as the session lengthens: 8 cents against 25 after one feature request, 14 against 44 after three ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 09:36-13:25). The reason is exactly this page's premise: one user action becomes many model calls with different requirements, so an always-premium policy pays its worst-case rate on every internal call while a routed policy pays each call's own tier. The pressure this page describes is therefore not evenly distributed across a product — it concentrates in whichever surfaces have the longest agent loops. See [Routing Savings Compound Across an Agent Session](routing-savings-compound-across-an-agent-session.md). Single live demo of one small app, with an impure baseline (the harness sometimes chose a cheap model on its own), so the direction is sound and the 3x ratio is one sample.

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Prevent AI billing surprises with caps, notifications, and rate limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Domain-specific agents unlock small models and tight permissions](domain-specific-agents-unlock-small-models-and-tight-permissions.md)
- [A Subsidized Coding-Agent Subscription Is a Lock-In Ramp](a-subsidized-coding-agent-subscription-is-a-lock-in-ramp.md)
- [Routing Savings Compound Across an Agent Session](routing-savings-compound-across-an-agent-session.md)

Sources:
- [The Rise of Open Models in the Enterprise — Amir Haghighat, Baseten](../sources/20250724_3WV1vT0B0cg.md), 05:51-06:10, 09:07-10:07
- [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](../sources/20260629_spNAUEgq_A8.md), 22:37-24:13
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 05:46-06:27, 10:27-10:55
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 09:36-13:25
