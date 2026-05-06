# Agents on the Canvas in tldraw - Steve Ruiz, tldraw

Source: [Agents on the Canvas in tldraw - Steve Ruiz, tldraw](https://www.youtube.com/watch?v=sPUjIBH5Cwg)
Uploaded: 2026-05-01
Transcript: `raw/20260501_sPUjIBH5Cwg/sPUjIBH5Cwg.en-orig.vtt`

## Summary

Steve Ruiz shows how tldraw experiments with agents embedded directly in an infinite canvas rather than confined to a chat sidebar. The useful patterns are canvas objects as prompt context, structured-output drawing instead of image generation, visible multi-agent state on the work surface, leader/follower delegation over shared state, and the safety tradeoff of giving agents executable runtime access to a hackable canvas.

## Extracted Concepts

- [Canvas-native agents turn spatial work surfaces into prompt context](../concepts/canvas-native-agents-turn-spatial-work-surfaces-into-prompt-context.md) - this source shows agents reading drawings, annotations, forms, and selected objects as part of the task context.
- [Structured canvas outputs make agent edits inspectable and editable](../concepts/structured-canvas-outputs-make-agent-edits-inspectable-and-editable.md) - this source contrasts generated images with text/structured outputs that create normal canvas shapes and UI elements.
- [Shared canvases expose multi-agent state and coordination](../concepts/shared-canvases-expose-multi-agent-state-and-coordination.md) - this source demonstrates multiple agents visible on the canvas with leader/follower delegation, shared state, and spatial progress feedback.
- [Hackable agent runtimes need tight safety boundaries](../concepts/hackable-agent-runtimes-need-tight-safety-boundaries.md) - this source highlights the danger of letting agents execute JavaScript against an app runtime, even when it enables richer browser, DOM, and screenshot access.

## Topic Links

- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- tldraw is described as an online whiteboard, startup, and SDK whose canvas is built from React components and is used in products such as Replit's agent canvas and Luma AI's canvas (00:00-01:35).
- Make Real turned a drawing on the canvas into a working prototype, giving non-technical users a way to produce technical artifacts without seeing code (02:34-03:02).
- The canvas prompt can combine generated UI, annotations, and color swatches: the user can mark up a previous result and ask the system to revise it from that spatial context (03:48-04:25).
- The drawing agent uses text structured outputs to create the same shapes a human can create on the canvas, rather than producing a flat image like a diffusion model (05:18-05:32).
- Spatial structured output is hard because model priors can conflict across coordinate systems, such as Cartesian y-up conventions versus web y-down coordinates from the top-left origin (06:31-07:34).
- One-shot canvas generation was useful but did not feel collaborative; Ruiz wanted the agent out of the sidebar and directly in the canvas (07:37-09:46).
- Fairydraw places multiple agents directly on the canvas so users can see state, thinking, action location, and relative work across agents (09:54-10:54).
- Multiple canvas agents can see each other's work, operate on the same objects, and coordinate through a leader that scouts the canvas, creates a to-do list, delegates tasks, observes progress, and judges completion (10:55-12:32).
- Giving agents more canvas access runs into safety limits: tldraw's runtime API makes code-based control possible, but posting arbitrary JavaScript to an endpoint and running it is explicitly called a bad idea except in a constrained local/offline experiment (13:34-14:48).
- Runtime access enables higher-level workflows such as visualizing code, editing the diagram, and updating code to match the revised diagram (15:05-15:22).
