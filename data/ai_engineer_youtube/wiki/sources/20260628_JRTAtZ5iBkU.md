# HTML is All You Need (for Agents to Make Graphics)

Source: [HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](https://www.youtube.com/watch?v=JRTAtZ5iBkU)
Uploaded: 2026-06-28
Transcript: `raw/20260628_JRTAtZ5iBkU/JRTAtZ5iBkU.en-orig.vtt`

## Summary

Amol Kapoor (CEO, Nori) argues that coding agents are not actually bad at making visual artifacts (slides, docs, even video) — the failures people blame on the model are really a *medium* problem. Canvas/pixel tools (PowerPoint, Figma, Canva, Figma MCPs, PowerPoint CLIs, screenshot-and-replace loops) and SVG are built for human hands and eyes and force the model to place coordinates in "a wall of numbers," which is as foreign to a model as handwriting SVG is to a person — hence the garbage output that fuels the ARC-AGI / Simon Willison "pelican riding a bicycle" skepticism. The fix is to give the model tools that match how it thinks: not pixels but language — words, tokens, and structure. HTML lets the model reason in semantic structure (a heading, a chart, a grid) while the browser renders to pixels, so the model never places a coordinate and gets charts, layouts, fonts, and motion "for free," and every line stays readable/themeable/editable. The deeper reframe is that the *editing format* is arbitrary and separable from the delivery/presentation format: PowerPoint is just a tool for making decks, the deck is only the presentation mode, so pick the editing format agents are already good at (HTML) and render to PDF or another format later. Nori uses this HTML trick for all its slide, board, and sales decks, its docs, and even the talk's own video ("divs all the way down"), and pairs it with feeding the model company data (call transcripts, emails) so agents build decks end-to-end while humans focus on vision and story.

## Extracted Concepts

- [Match the agent's output medium to its native representation](../concepts/match-agent-output-medium-to-its-native-representation.md) - agents "can't do graphics" is a tooling/medium problem, not a model limitation; give the model language/structure tools (HTML) instead of human pixel/coordinate canvases.
- [Author visual artifacts as HTML and decouple the editing format from delivery](../concepts/author-visual-artifacts-as-html-decoupled-from-delivery-format.md) - HTML/CSS is the universal editing substrate for slides, docs, and video; the delivery format (PowerPoint deck, PDF) is just presentation mode and can be rendered later.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

## Notes

- Framing: most people think coding agents only write code, but "coding agents can do almost anything," including the visual artifacts — slides, docs, even video — agents are assumed to be terrible at. 00:44-00:58
- Economic motive: the world pours ~34,000 human years/day into slide decks, and most of that is *fiddling*, not thinking; a 10-hour deck "should really take about 25 minutes once you remove all the formatting and the branding and the moving things around." 01:01-01:18
- Why canvas tools fail for agents: PowerPoint/Slides/Figma/Canva are built for human hands and eyes — click, drag, drop, resize, snap to grid — a "geospatial view of the world"; there is a data structure underneath but "in a format that only the application can read," so handing them to an agent yields overlap, unreadable text, and no alignment: "just garbage." 01:21-01:58
- The skeptic's claim it corrects: AI skeptics say agents "fundamentally can't reason about space," and benchmarks like ARC-AGI are built on that premise; Simon Willison's "draw a pelican riding a bicycle" (SVG-only) test is a gut check for spatial reasoning, and model outputs on it are "genuinely, deeply, really bad." 01:58-02:38
- Core thesis — "it's not the model, it's the medium": asking a human to handwrite an SVG of a pelican would fail too, because "SVGs are just a wall of numbers" and "you can't go from a wall of numbers to a pelican." Asking an AI to use a canvas is like asking a human to write SVG by hand. 02:39-03:30
- The fix — tools matched to how the model thinks: give the AI tools "not in pixels, in language — words, tokens, structure — that is its native medium," a language incredible at describing layout that models have trained on billions of examples of, that renders to pixels and runs everywhere. "Oh, right — HTML." 03:07-04:02
- Why HTML works: HTML tags have meanings built into the language (heading, chart, grid) and the browser turns it into pixels, "so the model never actually places a coordinate," and you get visual effects, charts, layouts, fonts, and motion "all of it for free"; the same pelican task in HTML lands in a structure the model can reason about and that you "can read and theme and edit every single line of." 03:57-04:34
- The decoupling reframe: PowerPoint is a *tool* to make slide decks; the deck itself is "just the presentation mode," and "the editing format is totally arbitrary," so pick the editing format agents are already good at — HTML — and render to another format like PDF later. 04:34-05:10
- Production use at Nori: the HTML trick builds all their slide decks, board decks, and sales decks, and their docs (color/vibrancy on-brand); the talk's own video is "just HTML and CSS… literally just divs all the way down." 05:11-05:40
- On content vs. format: a beautiful deck alone is worth nothing — you still need content; "think like the model" and give it access to your data (call transcripts, emails) to build the deck end-to-end while you focus on vision and story (Nori Sessions). 05:53-06:22
- Takeaway: "Stop thinking like a user. Think like the model. Give it the right language, and for graphics, all you need is HTML." 06:45-06:56
