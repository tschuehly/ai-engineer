# Author Visual Artifacts as HTML and Decouple the Editing Format from Delivery

Summary: Use HTML/CSS as the universal *editing* substrate for agent-authored visual artifacts (slides, docs, and even video), and treat the delivery/presentation format (a PowerPoint deck, a PDF) as a separate render step. The editing format is arbitrary and separable from how the artifact is finally presented, so pick the one agents are already good at.

Use when:
- Building agent-driven generation of slide decks, board/sales decks, reports, docs, or short videos.
- Choosing whether an agent should author directly in the delivery tool's format (PPTX, Figma files) or in an intermediate format that renders to the delivery format.
- Deciding how to combine "make it look good" with "fill it with the right content" in an artifact-generation pipeline.

Details:
- The core reframe: a delivery tool is not the artifact. "PowerPoint is a tool that you use to make slide decks. The deck itself, that's just the presentation mode… the editing format is totally arbitrary." So you can "just pick the editing format that the agents are already good at, HTML," and "if you need to render to a different format like PDF later on," do that as a downstream step. 04:34-05:10
- Why HTML is the right editing substrate: HTML tags carry semantic meaning (heading, chart, grid) and the browser renders them to pixels, giving charts, layouts, fonts, and motion "for free" while keeping the artifact fully readable, themeable, and editable line-by-line — the properties that make agent iteration and human review tractable. See [Match the agent's output medium to its native representation](match-agent-output-medium-to-its-native-representation.md). 03:57-04:34
- Breadth of the pattern in production: Nori builds all its slide decks, board decks, and sales decks in HTML, uses it for docs (adding color and vibrancy on-brand), and even rendered the talk's own video from it — "just HTML and CSS… literally just divs all the way down." The same editing substrate spans multiple artifact types and multiple delivery formats. 05:11-05:40
- Content is separate from format: "a beautiful deck on its own is generally not worth anything" — you still have to populate it. The complementary move is to give the model access to your data (call transcripts, emails) and have it "build the deck end to end," letting agents do the grunt work while humans "focus on vision and story." 05:53-06:22
- Operational payoff: because the editing format is text/structure that agents handle well, artifact creation becomes portable and low-friction (Kapoor reports building entire board decks from his phone during his commute); the leverage comes from the editing substrate matching the agent, not from a bespoke canvas tool.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Match the agent's output medium to its native representation](match-agent-output-medium-to-its-native-representation.md)
- [Dynamic Artifacts Make Agent Work Reviewable and Reusable](dynamic-artifacts-make-agent-work-reviewable-and-reusable.md)
- [Place Agent UI Generation on a Static–Declarative–Generative Spectrum](place-agent-ui-on-the-static-declarative-generative-spectrum.md)

Sources:
- [HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](../sources/20260628_JRTAtZ5iBkU.md), 04:34-06:22
