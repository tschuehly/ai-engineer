# Choose a skill's trigger by trading context load against cognitive load

Summary: A skill can be user-invoked (the human points the agent at it) or model-invoked (its description sits in the agent's context so the agent can decide to load it); the choice trades context load on the agent against cognitive load on the pilot, and both have real costs, so neither is a default.

Use when:
- Deciding whether a new skill should advertise a model-readable description or stay user-only.
- Auditing why an agent isn't firing a skill, or why an agent's per-request token cost keeps growing as skills accumulate.

Details:
- Every skill can always be user-invoked: the file sits on the filesystem and the human points the agent at it (e.g. a `/` command, depending on the harness). A skill becomes *model-invoked* only when its description is placed in the agent's context — the description acts as a "context pointer" the agent may choose to follow to read `SKILL.md`. 03:16-05:30
- The switch is explicit: `disable model invocation: true` keeps a skill's description out of the agent's context so it shows only to the user (Matt Pocock's `grill me` is user-only; his `codebase design` is model-invocable). 05:00-06:00
- Context load (the model-invoked cost): each model-invoked skill adds a description that costs tokens on *every* request and "a different thing for the agent to think about" — 100 model-invoked skills means 100 descriptions permanently in context. 06:00-06:45
- Unpredictability (a second model-invoked cost): even a perfectly-matched skill may just not be invoked; that unpredictability is what forces teams to *eval their skills* to confirm they fire at the right time — "a really nasty problem I prefer to avoid." 06:30-07:10
- Cognitive load (the user-invoked cost): pure user-invoked skills are deterministic and keep the agent's context small, but the pilot must remember and deeply understand the skills to use them — the load shifts onto the human. 06:20-07:25
- The tradeoff is symmetric, not a default: superpowers is primarily model-invoked ("gives the agent superpowers"); Matt Pocock's own repo prefers user-invoked to stay in full control. "Model invoke skills and user invoke skills both have their same costs." 07:00-07:28
- Related discipline: complex or numerous model-invoked skills are exactly what needs eval harnesses that check whether the agent loads and triggers a skill for the right task.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Evaluate agent skills with task scenarios and comparative conditions](evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Prune skills with single source of truth, sediment removal, and no-op deletion tests](prune-skills-with-single-source-of-truth-sediment-and-no-op-deletion-tests.md)

Sources:
- [Building Great Agent Skills: The Missing Manual - Matt Pocock](../sources/20260629_UNzCG3lw6O0.md), 03:16-07:28
