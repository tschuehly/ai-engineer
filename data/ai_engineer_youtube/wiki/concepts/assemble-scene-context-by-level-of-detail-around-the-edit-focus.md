# Assemble Scene Context by Level of Detail Around the Edit Focus

Summary: When an agent operates on a large live state (a scene, a canvas, a document, a map), do not serialize all of it. Borrow level of detail from real-time rendering: send full attribute values for the objects near whatever the user is currently editing, degrade to an identity and a position for objects further out, and drop the ones that will never be referred to — then recompute the grading as the user's focus moves.

Use when:
- An agent's context is dominated by a serialization of application state that grows with the size of the user's document or world.
- The state has a distance metric — spatial proximity, selection adjacency, call-graph distance, document section — that predicts what the next instruction will refer to.
- Choosing between "send everything," "retrieve on demand," and a graded middle for a stateful editing agent.

Details:
- The problem is stated concretely: "if we feed the entire scene to the LLM, the context grows a lot. Let's say in this scene I think I had like 100 assets… But, most of them are like grass that we could ignore. It doesn't really make sense" (14:48-15:07). The waste is not just volume — most of the objects are of a class no instruction will ever name.
- The analogy is taken from a solved problem in the same industry. In rendering, a near object gets "a higher quality texture… material… model," while "something that's too far away from the camera, I'm just going to maybe just put a cube and the user won't be able to tell because it's so far away" (15:07-15:44). Level of detail already encodes the judgment that fidelity should be spent where attention is.
- Applied to prompt assembly, the grading is anchored on the user's current selection rather than on the camera. With the user clicking on the knight, "the things that are around it might have a higher priority, so we feed them information about the tags that they have and the values of the settings on those tags. Things that are nearby, we just say, 'Okay, there's something that's a player here at this position, but I'm not going to send you the entire context'" (15:44-16:18). Three tiers, then: full attribute values, identity plus position, and omitted.
- The middle tier is what makes the technique different from filtering. A degraded entry still lets the model *refer* to an object ("the player over there") and ask for it, so the omission is recoverable; a filtered-out object is invisible. The cheap position-and-type stub is the analogue of the distant cube.
- The grading is recomputed continuously rather than fixed per session: "as a user keeps moving around and modifies things, then we update that and feed the assistant with more relevant information about the game" (16:18-16:33). The context is a function of current focus, not of session history.
- Nereu pairs the spatial grading with two non-spatial context inputs: a summary of what *type* of assets the game contains ("if you're using robots, if you're using something like medieval") and a user-written description of the game being made (10:54-11:35). Global character comes from a cheap summary; local detail comes from proximity.
- Caveat: the source reports no measurement — no token counts before and after, and no failure analysis of instructions that referred to something demoted or dropped. The scene demonstrated held about 100 assets, so the technique is described at a scale where sending everything is expensive but not impossible.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Give Browser Agents a Compact Whole-Page Representation](give-browser-agents-a-compact-whole-page-representation.md)
- [Curate Context Strategically Because Models Drop the Middle](curate-context-strategically-because-models-drop-the-middle.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Canvas-native agents turn spatial work surfaces into prompt context](canvas-native-agents-turn-spatial-work-surfaces-into-prompt-context.md)
- [Make Agent Edits Declarative Tags Instead of Generated Code](make-agent-edits-declarative-tags-instead-of-generated-code.md)

Sources:
- [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../sources/20260818_VBCDhRrvlYo.md), 10:54-11:35, 14:48-16:33
