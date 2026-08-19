# Expose the Domain's Vocabulary to Agents, Not the Platform's Primitives

Summary: When an agent has to express an intent through a platform's implementation primitives, it re-derives the same solution from scratch on every request, slightly differently each time. The fix is a layering change rather than a better model or prompt: raise the surface the agent talks to so that common domain intents are first-class nouns the agent selects, and let the platform's primitives stay below that line.

Use when:
- A coding agent keeps rebuilding the same well-known behavior on your platform and producing a different implementation each time.
- Deciding whether the next reliability investment is a better model, a bigger prompt, or a new API layer between the agent and an existing SDK.
- Choosing the words for a tool surface, and deciding whose vocabulary — the implementers' or the users' — those words should be drawn from.

Details:
- The symptom that starts Arturo Nunez's diagnosis is stability, not failure: "if I say, 'I want a camera that follows this character,' I've seen the demos, and the LLM reinvents the wheel every single time. Well, when the result is going to be essentially the same" (07:28-07:41). Every game already has this camera; nothing in the engine names it.
- His account of the cause is a layering error, and he states it as the thesis of the talk: "by default, the context is on the game engine rather than on the game design part, and I think we should flip that idea" (07:41-07:50). Powerful engines and powerful agents exist, but connecting them is "just building a bridge between two worlds, and it's not optimal, and you still need to know kind of like what to ask in vocabulary of an engine, in the vocabulary of code. Otherwise… the LLM goes rogue and does stuff, and reinvents the wheel over and over" (06:55-07:28).
- The cost is measurable in how much of the intent is boilerplate. To control a character in a conventional engine you import a mesh and then assemble "a renderer, an animator, a rigid body, and collider for physics, an audio source, and then you add your movement logic and your game rules" — almost all of which "every single character in every single game out there has," while the human or agent must still read component descriptions and "what the hundreds of sliders do" (07:50-08:27). The actual intent is one line at the end of a stack of ceremony.
- The replacement vocabulary is chosen from an existing source rather than invented: the words already used to *teach* the domain. Nereu's intents are "character," "animated," "double jump," and event rules like "when you collect a coin, I want you to increase the score," and Nunez grounds the choice in tutorials — "the tutorial tells you, 'Oh, press A to jump and press A again while you're in the air to do a double jump.' That's the language that we should be using" (08:28-09:16). Any domain with a teaching literature has this vocabulary already written down.
- The precondition is that a domain-level noun must have one obvious meaning at the platform level. Nunez's is "everything is just an asset. Everything has to be rendered on screen. Everything has physics most of the time" (08:28-08:45) — because the boilerplate is universal, it can move under the line without loss.
- Where this does *not* remove work, by his own account: the hard part becomes composing the domain's own concepts into the vocabulary. "There are a lot of genres, there are a lot of ways to describe the same game, there are things like the mood of the game. Like I want to make a platformer but that feels like scary. Well, that also touches on… the post-processing effects and… the lighting" (12:09-12:45). Building the intent layer moves the difficulty from the agent's context into the platform designer's decomposition problem; it does not delete it.
- Caveat: the source is a closed-alpha product demo by its builder (13:50-14:04), with no measurement of agent reliability before and after the vocabulary change. The mechanism is argued from ten years of watching Unity users, not from an eval.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Make Agent Edits Declarative Tags Instead of Generated Code](make-agent-edits-declarative-tags-instead-of-generated-code.md)
- [Encode Agent Intent Into Server-Side Tools](encode-agent-intent-into-server-side-tools.md)
- [Maintain ubiquitous language for AI coding](maintain-ubiquitous-language-for-ai-coding.md)
- [Evaluate tool definitions and outputs as context](evaluate-tool-definitions-and-outputs-as-context.md)
- [Scope the Assistant to Getting the User Unstuck, Not One-Shotting the Artifact](scope-the-assistant-to-getting-users-unstuck-not-one-shotting.md)

Sources:
- [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../sources/20260818_VBCDhRrvlYo.md), 06:55-09:16, 12:09-12:45
