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
- Independent second instance, in video: Reelful's agentic video editor composes with Remotion, "an open-source framework to create videos as code, as React code… just like a file with the order with all your assets and tracks and how they're following each other," and Ekaterina Deyneka gives the same reason Kapoor gives for HTML — "agents are really good at writing code and therefore we can use them to create videos with this remotion framework" ([Reelful](../sources/20260818_pPj_tjlvYjA.md), 07:12-07:45). A video timeline is the canonical human canvas tool, so this is the rule applied to the medium it should be hardest in.
- What the code medium buys beyond authorship, which neither this talk nor the HTML page states: a mechanically checkable failure mode. Because the composition is code, Reelful runs "this verification layer to make sure that all the composition is clean, is well defined, everything will be rendered and if there are some problems then the agent will reiterate on the composition" ([Reelful](../sources/20260818_pPj_tjlvYjA.md), 07:45-08:19) — the compile-or-retry loop of a coding agent, unavailable on a pixel canvas where "wrong" is only visible to a human or a vision model.
- Generalization: this is a special case of the broader tool-design lesson that a text-native surface (CLI, API, structured markup) is usually a better agent tool than a spatial/GUI surface — the model's leverage comes from operating in tokens and structure, and the renderer or execution layer supplies the human-facing pixels. Preferring a CLI/API over browser automation is a sibling instance of the same rule, applied to acting on a system rather than authoring an artifact.
- Takeaway framing: "Stop thinking like a user. Think like the model. Give it the right language." 06:45-06:56
- **The inverse move, offered as an open question rather than a practice: change the representation to match what the model is best at.** Shenoy's proposal is to route non-engineering knowledge work through the medium the models are strongest in — "the models are trained on code, they want to write code, they're incredibly good at writing code… Rather than wait for the models to catch up on doing services knowledge work, what if we just use that code knowledge and represent knowledge work as code?" The side benefit is structural: a task expressed as code inherits diffs, branches, tests, and review, which is the forking substrate that background agents outside software currently lack. No mechanism, example, or result is given — it is posed as a question the speaker is working on. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 09:24-09:44)

Related topics:
- [Tools](../topics/tools.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Author visual artifacts as HTML and decouple the editing format from delivery](author-visual-artifacts-as-html-decoupled-from-delivery-format.md)
- [Place Agent UI Generation on a Static–Declarative–Generative Spectrum](place-agent-ui-on-the-static-declarative-generative-spectrum.md)
- [Keep visual inputs at native shape for GUI and video agents](keep-visual-inputs-at-native-shape-for-gui-and-video-agents.md)
- [Reuse the Agentic App-Builder Architecture for Non-Code Artifacts](reuse-the-agentic-app-builder-shape-for-non-code-artifacts.md)
- [Make Agent Edits Declarative Tags Instead of Generated Code](make-agent-edits-declarative-tags-instead-of-generated-code.md)
- [Async Agents Need a Forking Substrate and a User Who Tolerates Out-of-Order Completion](async-agents-need-a-forking-substrate-and-a-tolerant-user.md)

Sources:
- [HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](../sources/20260628_JRTAtZ5iBkU.md), 01:29-06:56
- [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](../sources/20260818_pPj_tjlvYjA.md), 07:12-08:19
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 09:24-09:44
