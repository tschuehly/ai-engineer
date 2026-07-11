# Shrink the System Prompt and Drop Examples as Models Improve

Summary: As a model class gets more capable, the prompting best-practice inverts: shrink the system prompt, remove examples (which now cap a model more imaginative than the examples), and give *context, not constraints* — because heavy "do this / never do that" instructions written for a weaker model constrain a stronger one.

Use when:
- Migrating a harness or agent to a newer, stronger model and its prompt was inherited from an older one.
- A capable model feels boxed-in, unimaginative, or oddly literal, and the prompt is long and example-heavy.
- Revisiting a tool that "barely worked" on a prior model before assuming it's still weak.

Details:
- Claude Code "removed 80% of the system prompt" for the newest model class — a concrete, large cut, not a trim. (05:58-06:07)
- The arc across generations: Sonnet-3.5-new wanted a *small* prompt, few tools, and lots of examples; as models got smarter you could give a *larger* prompt with many tools and lots of examples and they'd follow it; the newest class wants a *smaller* prompt with *fewer* examples because "the examples tend to constrain it — it's actually more imaginative than the examples we give it." (06:07-06:45)
- Direction of the change: "try to give it context and not just constraints… really trying to avoid being like 'do not do this'," which was necessary for previous models but now holds a stronger model back. (06:45-07:02)
- Tools ratchet with the model, so re-test them each generation instead of trusting an old verdict: the ask-user-question tool went from "could barely call it" under Opus 4 (needing heavy tweaking), to running a 40-question spec interview under Opus 4.5, to building "a whole HTML report with the questions embedded" under Opus 4.8/Fable — same tool, rising capability. Output surfaces evolved the same way: Markdown as rich output → plan-mode Markdown *for the human* → in-depth HTML reports. (07:02-08:27)
- This is a specific instance of [capability overhang](capability-overhang-tools-decide-which-model-spikes-you-reach.md) (a spike is unlocked by *removing* constraint) and complements the harder rule that instructions copied across models can overconstrain via *learned habits*, not only capability ([prompt around learned model habits](prompt-coding-agents-around-learned-model-habits.md)) — the practical debugging move there (ask the agent which instruction caused the bad behavior, then delete it) applies here too.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Capability Overhang: Tools Decide Which Model Spikes You Reach](capability-overhang-tools-decide-which-model-spikes-you-reach.md)
- [Prompt coding agents around learned model habits](prompt-coding-agents-around-learned-model-habits.md)
- [Tune Coding-Agent Harnesses Per Model Family](tune-coding-agent-harnesses-per-model-family.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)

Sources:
- [Field Guide to Fable — Thariq Shihipar, Anthropic](../sources/20260706_9fubhllmsBU.md), 05:58-08:27
