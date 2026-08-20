# Keep the Harness Thick Early and Thin It as the Model Improves

Summary: Treat the guardrail layer around a computer-use agent as deliberately temporary scaffolding. Early on it must be strong enough to make the model fail gracefully in front of real users and to capture those failures as training data; as the model absorbs those jobs, the harness gets thinner.

Use when:
- Deciding how much guardrail logic to build around an agent whose model you (or your vendor) are still improving.
- Planning a staged rollout with design partners or internal users before general availability.
- Arguing about whether a fix belongs in the harness or in the model.

Details:
- Definition used: "harness is a very overloaded term, but I think of the harness as… the interface between the model and the world" — context management, the tools available, tool execution — "and we can put an additional layer of guardrails in the harness to prevent the model from doing something bad, and then also nudge it in the right direction when needed." ([From RL to IRL](../sources/20260814_Cc0_nyxROBA.md), 12:24-12:51)
- The six controls in this lab's harness (12:51-14:00):
  - **Checkpointing and rollback when possible** — before a risky state or action, checkpoint so a bad action can be undone if the surface allows it.
  - **Action risk classifier** — inspect the model's *proposed* actions and judge whether they are safe or risky before execution.
  - **Credential guardrails** — "it's easy to detect if the credentials are active, if we've been signed out, and then nudge the model in the right direction based on that." The cheap deterministic check for the failure that locked an account.
  - **Execution monitor** — watch for loops, repeated clicks, and unproductive behavior, and nudge.
  - **Audit logs** — "maintaining evidence of all the actions and effects so that we can always go back and see what was the trail, what happened, and what was the effect."
  - **Human handoff** — the harness can override the model and force it to return control when [its confidence calibration is wrong](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md).
- The trajectory rule that makes this a strategy rather than a feature list: "early on, our harness is really strong. So [the] harness has to detect all the gaps in the model and make it fail gracefully so that we are able to capture the failure modes and train on them, but we also are not causing any harm to the users that are actually using the models. And over time, the model becomes better and better, and the harness becomes thinner and thinner." (16:49-17:12)
- The harness therefore has two jobs at once — *contain* the failure so no user is harmed, and *record* it so it becomes training data. A guardrail that silently prevents a bad action without logging what the model tried to do satisfies the first job and starves the second.
- Design consequence: build harness controls so they can be removed. Each one is an implicit bet about a model gap, and the audit log is what tells you whether that gap has closed.
- **Tension with the runtime-first sources.** The wiki's browser-agent material argues that the interface, not the model, is the bottleneck and that rebuilding what the agent sees, does, and learns from lets a *cheaper* model succeed ([Fix the Browser-Agent Runtime Interface](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)). Both can hold and they are aimed at different readers: if you cannot change the weights, runtime engineering is the only lever you have; if you are training the model, the same runtime work is scaffolding you expect to delete. Which posture applies depends on whether the model is yours.
- Related but different claim already in the wiki: [use stable agent harnesses as model-evolution boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md) treats the harness as the durable part while models change underneath. Mishra's version is narrower — the *guardrail* layer is what shrinks, not the interface itself.
- **A worked instance of the thinning, with the cost of not doing it.** Anthropic's Applied AI team reports adding context-reset machinery to compensate for Sonnet 4.5 "literally [getting] anxious as it approached its context window limit" and wrapping up tasks early, then finding that on Opus 4.5 — which "no longer exhibited context anxiety" — the same machinery "became dead weight. In fact, it became pure overhead, adding things like latency and causing issues with the cache being discarded incorrectly at times." That supplies the concrete answer to "what happens if we just leave the scaffolding up": a guardrail that fires on a schedule or a threshold keeps *executing*, so staleness is a running cost rather than dead code. Recorded separately as [a harness fix becomes overhead when the model outgrows it](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md). ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 07:58-08:57)
- **Where the thinning goes when the lab owns both halves: into the model's training, and then behind the API.** OpenAI describes Codex features that started as harness logic and ended up as model behavior — the diff format, the search tool, and most pointedly compaction, which now runs server-side because "the model has been trained with the auto compaction" ([Match Agent Tooling to the Model's Training Distribution](match-agent-tooling-to-the-models-training-distribution.md)). That is Mishra's trajectory rule observed at a second lab and carried one step further: the guardrail does not merely shrink, it crosses the API boundary and stops being the harness author's code at all. The consequence for a reader who does *not* own the weights is the uncomfortable one — the thinning happens on the provider's schedule, and what you get back is a behavior you can no longer tune. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 10:15-10:56, 18:51-19:35)

Related topics:
- [Agents](../topics/agents.md)

Related concepts:
- [Map RL Assumptions to Deployment Realities for Computer-Use Agents](map-rl-assumptions-to-deployment-realities-for-computer-use-agents.md)
- [Teach Calibrated Confidence So an Agent Knows When to Hand Off](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)
- [Use stable agent harnesses as model-evolution boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md)
- [An Audit Trail Is a Chain of Evidence, Not a Developer Log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md)
- [Train Computer-Use Agents in a Flight Simulator, Not on Exams](train-computer-use-agents-in-a-flight-simulator-not-on-exams.md)
- [Product harnesses can become model customization environments](product-harnesses-can-become-model-customization-environments.md)
- [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)
- [Match Agent Tooling to the Model's Training Distribution](match-agent-tooling-to-the-models-training-distribution.md)

Sources:
- [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../sources/20260814_Cc0_nyxROBA.md), 12:24-14:00, 16:49-17:12
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 07:58-08:57
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 10:15-10:56, 18:51-19:35
