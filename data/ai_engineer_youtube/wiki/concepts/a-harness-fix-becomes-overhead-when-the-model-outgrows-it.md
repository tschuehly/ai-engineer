# A Harness Fix Becomes Overhead When the Model Outgrows It

Summary: Every harness workaround is a recorded belief about something the model cannot do. When a later model can do it, the workaround does not become neutral — it becomes a cost, because the machinery still runs. Anthropic's own worked instance is a context-reset layer built for Sonnet 4.5's "context anxiety" that turned into "pure overhead, adding things like latency and causing issues with the cache being discarded incorrectly" once Opus 4.5 stopped needing it.

Use when:
- Auditing a harness before or after a model upgrade and deciding what to remove rather than what to add.
- Justifying the removal of a guardrail that "isn't hurting anything" — this is the argument that it is.
- Explaining why a model upgrade produced a smaller improvement than the model's own benchmarks suggested.

Details:
- **The general claim.** "Harnesses encode assumptions about what Claude cannot do on its own… they have to be questioned frequently because they go stale as models improve." The one-line consequence the presenters draw is the retrieval cue for this page: "when the model moves and the harness doesn't, it degrades the agent." ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 07:36-08:57)
- **The behavior that prompted the fix.** Sonnet 4.5 "literally got anxious as it approached its context window limit. And so it started to wrap up tasks early… even when it actually had room left to spare." The team responded the way a harness team should: they added context resets and related machinery so the agent would not hit the condition that triggered the behavior. (07:58-08:24)
- **What the fix cost after the model changed.** Opus 4.5 "no longer exhibited context anxiety," and the compensating machinery "became dead weight. In fact, it became pure overhead, adding things like latency and causing issues with the cache being discarded incorrectly at times." Both named costs are the kind that do not show up as a failed test: the agent still works, it is just slower and re-pays for prefix tokens it should have hit in cache. (08:24-08:52)
- **Why this shape is worth naming separately from "keep the harness thin."** The strategy pages argue for thinning on principle. This is the mechanism that makes the principle bite: a stale workaround is not inert scaffolding you can leave standing, because the workaround *executes*. A context reset that fires when it is no longer needed spends latency and discards cache every time. Look for staleness where the harness intervenes on a schedule or a threshold rather than where it merely offers a capability.
- **The diagnostic this suggests.** For each intervention in the harness, name the model deficiency it compensates for. If you cannot name one, it is not a compensation and this page does not apply. If you can, that sentence is a test to re-run against every new model — and the intervention's own cost (latency, cache invalidation, extra tokens, forced truncation) is what you save by deleting it.
- Provenance: an Anthropic vendor talk for its managed-agent product. The context-anxiety story is anecdotal — no eval, no frequency, no task distribution for the original behavior, no measurement that the fix helped, and no quantification of the overhead it later imposed. The dynamic is credible and specific; its magnitude is unreported. The captions render the newer model as "Claude Opus 48," most likely 4.5, and nothing here depends on which release it is.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Keep the Harness Thick Early and Thin It as the Model Improves](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md)
- [Use stable agent harnesses as model-evolution boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md)
- [A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)
- [Build Agent Harnesses Incrementally Up a Capability Ladder](build-agent-harnesses-incrementally-up-a-capability-ladder.md)

Sources:
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 07:36-10:13
