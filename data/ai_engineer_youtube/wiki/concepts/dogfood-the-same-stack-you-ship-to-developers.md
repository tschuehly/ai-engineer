# Dogfood the Same Stack You Ship to Developers

Summary: Build your own agent product on the exact primitives you sell — same API, same open-source harness, same file format, same app server — rather than a privileged internal path plus a simplified external one. When a new internal need appears, bake it into the public primitive first so external developers inherit it, and the platform improves every time someone forks or stress-tests it.

Use when:
- Deciding whether to expose a real developer platform or ship a closed product with a separate, richer internal stack.
- Designing the layering (model API → harness → app server → app/plugins) of an agent product meant to be built on by others.
- Explaining why an open harness and a shared instruction-file format are strategic, not just goodwill.

Details:
- The claim, stated as the section's one takeaway: "we're not building one system for OpenAI and a second system that's simplified for developers. At every layer, we actually use the thing that we give to you." (13:39-13:56)
- Layer 1, model API: developers use the models through the responses API, "and this is how we built the Codex app" — same models, same API. When Codex needed a new capability (compaction, to keep long-running tasks inside the context window), it was "baked into the API first so you can benefit as well," so external agents get the same primitives OpenAI built for itself. (09:44-10:33)
- Layer 2, harness: the Codex harness is open source to inspect/fork/adapt; the OpenAI models are the *default* but "not hard coded," so you can swap in an open model and keep the same agent loop; the same harness is used in model post-training so the models learn to call tools in an environment that is itself open source. The instruction file was named `AGENTS.md` deliberately so "other agents can actually use it as well" instead of inventing a Codex-only format. (10:37-11:16)
- A reference implementation beats reverse-engineering: the Open Code team could read how OpenAI implemented ChatGPT sign-in, reuse the parts that fit, and replace the rest — "better than having developers reverse engineering how it builds." (11:17-11:43)
- Layer 3, app server: made open source because OpenAI itself needed one unified way to control the harness across a VS Code extension and the Codex app — "not kind of a community adapter, it's really the path that we use for our own products." Evidence it is real: "Toma" built native Codex Monitor and later Codex for iOS on the app server before the official app shipped. (11:44-12:33)
- Layer 4, app/plugins: the in-app browser and plugins are extension points, and browser-use / computer-use were "built as plugins using the exact same extension points" developers get; role-specific plugins (data science, design) are open source too. The subscription works across Open Code, Pi, Droids, Open Claw, Xcode, and JetBrains. (12:37-13:33)
- The compounding payoff of the single stack: "every time you fork the harness, every time you find the edge of capabilities of the models, it means we get to learn and improve" — external usage is a feedback source, not a support cost. (13:56-14:07)
- Related contrast: this extends [Use stable agent harnesses as model-evolution boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md) (also OpenAI) — that concept treats the harness as the abstraction that survives model churn; this concept adds that the *same* harness/API/format should be the one you also ship, closing the gap between your product and your platform.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Use stable agent harnesses as model-evolution boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md)
- [Build Product Primitives Before Feature Surfaces](build-product-primitives-before-feature-surfaces.md)
- [Let agent harnesses extend through ordinary code packages](let-agent-harnesses-extend-through-ordinary-code-packages.md)
- [Agent harnesses combine model, tools, prompts, filesystem, skills, hooks, and memory](agent-harnesses-combine-model-tools-prompts-filesystem-skills-hooks-and-memory.md)

Sources:
- [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](../sources/20260709_pMggiOb18tc.md), 09:44-14:07
