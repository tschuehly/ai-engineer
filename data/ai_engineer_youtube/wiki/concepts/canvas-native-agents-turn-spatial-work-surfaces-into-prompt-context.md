# Canvas-native agents turn spatial work surfaces into prompt context

Summary: A canvas-native agent can use drawings, annotations, selected objects, forms, and layout relationships as task context instead of relying only on a chat transcript. This makes the work surface itself part of the prompt and lets non-technical collaborators steer technical generation through spatial artifacts.

Use when:
- Designing an agent interface for diagrams, prototypes, whiteboards, UI mockups, or mixed visual/text artifacts.
- Comparing sidebar chat agents with agents that operate directly inside the user's work surface.

Details:
- tldraw's Make Real pattern let users draw on a canvas and send that visual/spatial artifact to a model to produce a working prototype, which Ruiz frames as a way for non-technical users to make technical things without looking at code (02:34-03:02).
- Canvas context can include the old generated result plus markup layered on top of it: the user can annotate an object, point at color swatches, and ask the agent to revise the prior output from that combined context (03:48-04:25).
- Ruiz describes the goal as moving the agent out of the sidebar and into the canvas so it behaves more like a collaborator than a remote operator borrowing the user's keyboard (08:41-09:46).

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Non-technical collaborators can steer agents with natural work artifacts](non-technical-collaborators-can-steer-agents-with-natural-work-artifacts.md)
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)

Sources:
- [Agents on the Canvas in tldraw - Steve Ruiz, tldraw](../sources/20260501_sPUjIBH5Cwg.md), 02:34-04:25, 08:41-09:46
