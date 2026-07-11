# Match the Agent's Output Medium to Its Native Representation

Summary: When an agent produces bad artifacts (garbled slides, broken graphics), the fault is usually the *medium* the tool forces on it, not the model's capability. Pick output tools that match how the model represents the world — language, tokens, and structure — rather than human hands-and-eyes idioms like canvases, pixels, and coordinates.

Use when:
- An agent produces overlapping, misaligned, or "garbage" visual output and you are tempted to conclude the model "can't reason about space."
- Designing the tool an agent uses to author graphics, slides, diagrams, or documents, and choosing between a canvas/pixel tool and a structured-markup tool.
- Deciding whether to invest in a Figma MCP, PowerPoint CLI, or screenshot-and-replace loop versus letting the model emit structured text.

Details:
- Reframe: agents are widely assumed to be terrible at visual artifacts, and skeptics point to ARC-AGI and Simon Willison's SVG-only "pelican riding a bicycle" test as proof that agents "fundamentally can't reason about space." Kapoor's counter is that these tests measure the *medium*, not the model: asking a human to handwrite an SVG of a pelican would fail too, because "SVGs are just a wall of numbers" and "you can't go from a wall of numbers to a pelican." 01:58-03:05
- Why human canvas tools break for agents: PowerPoint, Slides, Figma, and Canva are built for human hands and eyes — click, drag, drop, resize, snap to grid — a "geospatial view of the world." Their underlying data structure is "in a format that only the application can read," so handing them to an agent yields overlap, unreadable text, and no alignment. Figma MCPs, PowerPoint CLIs, and screenshot-and-replace loops all share the flaw of approaching the problem "like a human." 01:29-03:23
- The design rule: "give the AI tools based on how it thinks, not in pixels, in language — words, tokens, structure — that is its native medium." Choose a representation the model has trained on billions of examples of and understands intuitively, that still renders to pixels and runs everywhere. 03:23-04:02
- Why this makes the model competent: in a structured-markup medium the model reasons about semantic structure (a heading, a chart, a grid) and lets the renderer place pixels, so "the model never actually places a coordinate." The same pelican task that fails in SVG lands in "a structure that the model can reason about" when expressed in HTML. 03:57-04:34
- Generalization: this is a special case of the broader tool-design lesson that a text-native surface (CLI, API, structured markup) is usually a better agent tool than a spatial/GUI surface — the model's leverage comes from operating in tokens and structure, and the renderer or execution layer supplies the human-facing pixels. Preferring a CLI/API over browser automation is a sibling instance of the same rule, applied to acting on a system rather than authoring an artifact.
- Takeaway framing: "Stop thinking like a user. Think like the model. Give it the right language." 06:45-06:56

Related topics:
- [Tools](../topics/tools.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Author visual artifacts as HTML and decouple the editing format from delivery](author-visual-artifacts-as-html-decoupled-from-delivery-format.md)
- [Place Agent UI Generation on a Static–Declarative–Generative Spectrum](place-agent-ui-on-the-static-declarative-generative-spectrum.md)
- [Keep visual inputs at native shape for GUI and video agents](keep-visual-inputs-at-native-shape-for-gui-and-video-agents.md)

Sources:
- [HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](../sources/20260628_JRTAtZ5iBkU.md), 01:29-06:56
