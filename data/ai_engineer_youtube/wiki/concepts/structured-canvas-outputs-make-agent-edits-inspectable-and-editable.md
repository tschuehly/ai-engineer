# Structured canvas outputs make agent edits inspectable and editable

Summary: Canvas agents become more useful when they create structured app objects rather than flat images. Structured outputs let humans inspect, select, edit, annotate, and iterate on the generated artifact using the same primitives available to the agent.

Use when:
- Building agents that generate diagrams, mockups, whiteboard content, or UI sketches.
- Deciding whether a visual agent should produce pixels, code, or structured scene/editor objects.

Details:
- Ruiz distinguishes the tldraw drawing agent from diffusion image generation: the agent uses text structured outputs to make the same canvas shapes and objects a human could make (05:18-05:32).
- Structured spatial generation has model and prompt-engineering hazards because visual and language priors conflict; the example is y-axis direction, where Cartesian graphs increase upward but web coordinates increase downward from the top-left origin (06:31-07:34).
- The benefit is iterative editability: a generated UI or diagram can be annotated, recolored, modified, and used as the next prompt context rather than treated as a final bitmap (03:48-04:25).
- A Postman talk frames the same idea as the endgame of generative UI: "beyond components" toward human-agent collaboration on a shared artifact. The Excalidraw MCP app is cited not just as diagram output/visualization but as a shared canvas where a human and an agent collaborate — going back and forth with the agent ("change this") while the user can also click around and directly modify the UI the way they're used to — so generative UI becomes personalized *and* collaborative rather than one-shot output ("don't just use agents as an orchestrator and delivery mechanism to show me some visualizations"). ([Casas/Postman] 14:46-16:16)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Canvas-native agents turn spatial work surfaces into prompt context](canvas-native-agents-turn-spatial-work-surfaces-into-prompt-context.md)
- [Non-technical collaborators can steer agents with natural work artifacts](non-technical-collaborators-can-steer-agents-with-natural-work-artifacts.md)
- [Place Agent UI Generation on a Static–Declarative–Generative Spectrum](place-agent-ui-on-the-static-declarative-generative-spectrum.md)

Sources:
- [Agents on the Canvas in tldraw - Steve Ruiz, tldraw](../sources/20260501_sPUjIBH5Cwg.md), 03:48-04:25, 05:18-07:34
- [Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman](../sources/20260603_hCMrEfPG2Yg.md), 14:46-16:16
