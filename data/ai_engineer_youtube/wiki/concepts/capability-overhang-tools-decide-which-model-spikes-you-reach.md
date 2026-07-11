# Capability Overhang: Tools Decide Which Model Spikes You Reach

Summary: Models get smarter in *spiky*, uneven ways, and a lot of new capability sits latent ("overhang") until the harness lets the model reach it — so a large part of unlocking a new model is discovering which tools and interactions expose its spikes, not just waiting for higher benchmark scores.

Use when:
- Adopting a stronger model and deciding where to invest: better prompts/tools vs. waiting for the next model.
- Explaining why the same model fails one task in chat but solves it trivially with the right tool.
- Framing harness work as capability discovery ("what is now possible?") rather than plumbing.

Details:
- Spiky, not smooth: a chat model can't say which Pokémon names end in "aw" (Croconaw, Drednaw) even though it knows all ~1000 by heart, but Claude Code fetches every Pokémon, writes a filter script, and answers in seconds — "Claude gets smarter in spiky ways… if you give it the code execution tool it can find the two." (03:40-04:50)
- "The models are grown, not designed" — they are cultivated with data, feedback, and compute and understood empirically, so "what contains them is us": the harness and the way we prompt are a function of *our* understanding of the model, and unhobbling means understanding it better to unleash it. Treat a new model "closer to a biology than a physics" — empirical, organic, rules not fully known. (02:37-03:39, 08:27-09:04)
- Give it arms, not a bigger window: the naive path to coding was "paste the whole codebase into a 100M-token window"; the spike that actually worked was the bash tool so the model "can build and search its own context" — the insight behind Claude Code. Reaching a spike is a new interaction pattern, not a scale increase. (04:50-05:37)
- Overhang is a standing discovery task: "part of the challenge with Fable is figuring out this capability overhang — what is now possible?" and "there's a lot more understanding in [the model] to unlock." Related product example: an ability to "wake itself up and do work" (proactive/multiplayer) was the spike behind Claude Tag. (03:06-03:39, 05:37-05:58)
- Companion levers: the same overhang means a stronger model wants a [smaller system prompt with fewer examples](shrink-the-system-prompt-and-drop-examples-as-models-improve.md) and rewards being pointed at [your own unknowns](use-the-agent-to-surface-your-own-unknowns.md); demos are a practical way to surface spikes for others to branch from ([share demos to reveal latent capabilities](share-demos-to-reveal-latent-model-capabilities.md)).

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Share Demos To Reveal Latent Model Capabilities](share-demos-to-reveal-latent-model-capabilities.md)
- [Coding-Agent Capability Tiers Change the Bottleneck](coding-agent-capability-tiers-change-the-bottleneck.md)
- [Invest in the Harness to Run Weaker and Local Models](invest-in-the-harness-to-run-weaker-and-local-models.md)
- [Shrink the System Prompt and Drop Examples as Models Improve](shrink-the-system-prompt-and-drop-examples-as-models-improve.md)

Sources:
- [Field Guide to Fable — Thariq Shihipar, Anthropic](../sources/20260706_9fubhllmsBU.md), 02:37-05:58, 08:27-09:04
