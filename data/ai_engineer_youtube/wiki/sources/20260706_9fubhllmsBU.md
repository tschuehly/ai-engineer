# Field Guide to Fable — Thariq Shihipar, Anthropic

Source: [Field Guide to Fable — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=9fubhllmsBU)
Uploaded: 2026-07-06
Transcript: `raw/20260706_9fubhllmsBU/9fubhllmsBU.en-orig.vtt`

## Summary

Thariq Shihipar (works on Claude Code at Anthropic) gives a "field guide" to working with Fable, Anthropic's newest model, structured as four moves: unhobble Claude, find your unknowns, deal with the grief, and be unreasonable. The through-line is **capability overhang** — models get smarter in *spiky* ways, and the tools/harness you give them decide which spikes you can reach: a chat model can't name the Pokémon whose names end in "aw" though it knows all of them, but Claude Code writes a script, fetches the list, and filters in seconds. Because "the models are grown, not designed," what contains a model is *us* — the harness and prompt are a function of our understanding of it — so unhobbling means understanding the model better to unleash it, treated "closer to biology than physics." Concretely, the newest model class wants a *smaller* system prompt: Claude Code cut 80% of its system prompt because examples now constrain a model that is more imaginative than the examples, and the guidance shifted to "give context, not constraints" (avoid "do not do this"). The same tools ratchet in capability across generations (the ask-user-question tool went from barely callable under Opus 4, to 40-question interviews under Opus 4.5, to embedded HTML questionnaires under Opus 4.8/Fable; output progressed Markdown → plan-mode Markdown for the human → in-depth HTML reports). The second half is a human-side workflow: the map (your plan/prompt/spec) is not the territory (the real codebase), and anything Claude hits that isn't in the map is an *unknown* — an unspecified decision point — so at high model capability *your ability to match map to territory becomes the bottleneck*. He gives concrete techniques to use the model to surface your own unknowns (blind-spot pass, brainstorm/prototype variants, interview-me, reference-as-map, implementation-note logging, quiz-me). The close is a mindset: Anthropic's "tradeoffs are not real" — stop picking two of good/fast/cheap and demand all three, "force reality to show you the tradeoff," rescope ambition up (he built a full keynote deck in 4 hours with Fable) — with the caveat that "building is easier, but generating value is still hard."

## Extracted Concepts

- [Capability Overhang: Tools Decide Which Model Spikes You Reach](../concepts/capability-overhang-tools-decide-which-model-spikes-you-reach.md) - the Pokémon-"aw" example and "grown, not designed / what contains them is us" framing anchor the concept that latent capability is unlocked by the harness, not just the weights.
- [Shrink the System Prompt and Drop Examples as Models Improve](../concepts/shrink-the-system-prompt-and-drop-examples-as-models-improve.md) - Claude Code's 80% system-prompt cut, "examples constrain a more imaginative model," "give context not constraints," and the ask-user-question tool ratchet are direct evidence.
- [Use the Agent to Surface Your Own Unknowns](../concepts/use-the-agent-to-surface-your-own-unknowns.md) - the map/territory + knowns matrix and the blind-spot-pass / interview / reference / implementation-note / quiz techniques are the concept's core.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)

## Notes

- Framing: "the models are grown, not designed… what contains them is us" — the harness and prompt are a function of our understanding of the model; unhobbling = understand it better to unleash it, "still very early." (02:37-03:39)
- Capability overhang, spiky progress: chat model can't answer which Pokémon end in "aw" (Croconaw, Drednaw) though it knows all ~1000; Claude Code fetches every Pokémon, writes a script, filters — "Claude gets smarter in spiky ways." (03:40-04:50)
- Give it arms, not a bigger window: instead of a 100M-token context to paste your whole codebase, give it the bash tool so it "can build and search its own context" — the insight behind Claude Code; each such jump is spiky/new. (04:50-05:37)
- Claude Tag (a recent multiplayer/proactive product) is "unlocked" by Claude's ability to "wake itself up and do work" rather than needing a prompt each time. (05:37-05:58)
- System prompt shrinking: Claude Code "removed 80% of the system prompt." Best-practice arc: 3.5-new = small prompt, few tools, lots of examples → smarter models = larger prompt, many tools, lots of examples → newest class = *smaller* prompt, fewer examples ("examples tend to constrain it cuz it's actually more imaginative than the examples we give it"), "give it context and not just constraints," avoid "do not do this." (05:58-07:02)
- Tool-capability ratchet: ask-user-question tool — Opus 4 "could barely call it," Opus 4.5 could run a 40-question spec interview, Opus 4.8/Fable can "build a whole HTML report with the questions embedded." Output progression: Markdown (rich output) → plan-mode Markdown (for the human) → in-depth HTML reports. (07:02-08:27)
- "Closer to a biology than a physics… still very empirical, very organic; we don't know all the rules but there is some intuition to build." Recommends Anthropic's "Biology of a Large Language Model" paper. (08:27-09:04)
- Unhobble yourself: "the map is not the territory." The plan/prompt/spec in your mind is the map; the real codebase/constraints are the territory; anything Claude hits that's not in the map is an *unknown* — "a decision point I haven't specified." Fable "traverses such a large area" it hits many unknowns, so "Fable bottlenecked my ability… to match the map and the territory to find my unknowns." (09:04-10:09)
- Knowns matrix: known knowns (what you write in the prompt), known unknowns, unknown knowns (obvious, "know it when I see it," so you wouldn't write it), unknown unknowns (haven't considered). Use Fable to find them. (10:12-10:48)
- Blind-spot pass: e.g. "I'm working on a new auth provider I know nothing about in this codebase — do a blind-spot pass to help me figure out my relevant unknown-unknowns and prompt better," pointing it at the module, git diff, or Slack for gotchas; also works to learn new fields (he used it for color grading in video editing). "The model knows more about almost everything than I do; I just need to get it out of it." (10:48-11:52)
- Brainstorm/prototype for unknown knowns: "I have no visual taste — make me an HTML page with four widely different design decisions so I can react to them" (know-it-when-you-see-it for design). (11:52-12:28)
- Interview-me: ask Claude to interview you, giving context about you/the work/the stage; "prioritize questions that would change the architecture" is extremely helpful. (12:28-12:58)
- References: "one of the best ways to give Claude a map is to give it another map" — pass reference code (even a different system/language) or an HTML mock-up as the spec instead of writing the spec in words; "Fable is really incredible at it." (12:58-13:35)
- Implementation notes: while Fable runs and hits an unknown, "ask it to log it" so you can see where deviations happened and why. (13:35-13:57)
- Quiz-me: get Fable to quiz you about what happened so you understand the work and can represent it in a PR/merge — "one of the most important parts… is staying in the loop." (13:57-14:23)
- Grief: coding before LLMs "feels like a foreign country"; work that took weeks now takes hours; loss of hand-coding craft but "the only way out is through." (14:23-16:28)
- Being unreasonable: Anthropic believes "tradeoffs are not real" — instead of prioritizing X against Y, "just do all of it… force reality to show you the tradeoff." Good/fast/cheap becomes "pick three." Reframe to be more ambitious; "the only way to prove that agents work is to do the best work of our lives faster than ever." He built the talk's deck "last night in about 4 hours with Fable." (16:28-18:00)
- Caveat: "building is easier, but generating value is still hard" — engineers over-focus on the process of building/their setup, but "the point is to generate value," which takes many swings/tries. Close: "go explore, make it real, and be less reasonable." (18:00-19:05)
