# Design LLM-Native Interactive Experiences Around Narrative State, Not Numeric Mechanics

Summary: When an LLM is the runtime engine for an interactive experience (a game, simulation, or agentic session), represent state as narrative/qualitative context the model reasons over — mood, characters, memory, world — rather than a numeric state machine of HP, dice, and stats. "Try narrative; context matters, and in general not numbers."

Use when:
- Building an LLM-driven game, RPG, or interactive fiction where the model directs play at runtime.
- Deciding whether to encode experience state as numbers/rules or as free-form narrative context.
- Designing any stateful LLM loop (simulation, companion, tutor) where qualitative state is what the model is actually good at tracking.

Details:
- The device's RPG deliberately drops the traditional tabletop machinery (HP, dice rolls, numeric stats) and instead has the LLM track and advance narrative state: an NPC with memory, a world "mood" (e.g. "ominous"), and generated content. (13:22-14:30)
- Generated worlds, characters, personalities, maps, and skills are all produced by the model, then converted to one-bit matrices for the constrained displays — the model owns the *state and content*, the device only renders it. (13:55-14:30)
- Explicit closing takeaway: "try narrative, the context matters, and in general not numbers" — a design principle, not just a game detail: LLMs reason over context, so make the durable state the context. (17:46)
- Complements runtime-LLM game direction: where the runtime-NPC concept covers *the LLM acting as a live game master*, this concept covers *how to represent the state it acts on* — qualitative narrative rather than a numeric rules engine.
- Reusable beyond games: any long-running LLM experience benefits from keeping the authoritative state as legible narrative context (world, memory, mood) rather than a hidden numeric model the LLM must translate to and from.

Related topics:
- [Agents](../topics/agents.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Drive Game NPCs and Difficulty With Runtime LLMs](drive-game-npcs-and-difficulty-with-runtime-llms.md)
- [Keep inference off the microcontroller: build the AI-native device as a thin client over a backend](keep-inference-off-the-microcontroller-thin-device-over-a-backend.md)

Sources:
- [OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack](../sources/20260628_akk6KRlcwW4.md), 13:22-17:46
