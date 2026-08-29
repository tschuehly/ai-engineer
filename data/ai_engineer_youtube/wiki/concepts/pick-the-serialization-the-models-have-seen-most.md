# Pick the Serialization the Models Have Seen Most, Not the One Native to Your System

Summary: When a system can hand an agent several textual representations of the same internal structure, choose the one with the most pretraining mass rather than the one that models your domain most faithfully. Figma had three serializations of its own C++ scene graph and picked React and Tailwind — a format borrowed from a different product surface — over its purpose-built internal representation, on the explicit bet that models had seen far more of it.

Use when:
- Deciding how an MCP server, API, or tool should serialize an internal data structure for a model.
- You already own a domain-specific representation (a DSL, an internal XML/JSX dialect, a proprietary AST) and are tempted to expose it because it is the truest description of your system.
- Output quality is poor and you are considering a better model, a longer prompt, or fine-tuning before you have tried a different serialization.

Details:
- The three candidates for Figma's scene graph — "a graph of connected nodes, not unlike the HTML DOM" — were an internal representation "kind of akin to JSX or XML," which was "abstract and sparse, but it didn't have super rigorous fidelity"; D2R, "our like way of saying a react tailwind representation," which already existed because Figma Sites converts the scene graph to HTML; and a plain image. 03:33-04:16
- The selection criterion was pretraining exposure, stated as a hunch and not as a measurement: "we had a hunch that this representation would be the best one because lots of the models were sort of [trained] on this React Tailwind type of code… we had a suspicion that it would work really well." 04:30-04:40
- The chosen representation was not the most faithful one available at design time. The internal JSX/XML dialect was purpose-built for the scene graph and lost on fidelity anyway; the borrowed one won on fidelity too, to the point that it carries a bug-reportable invariant — paste the MCP output into a simple HTTP server and "it should be pixel perfect. Um and if it's not, file a bug." 03:47-04:28
- The image is a supplement, not a medium. Alone it converted poorly because "back in early 2025… agents weren't great at converting images directly to HTML or CSS," but "having the code context plus the image actually had better agentic output" — so the screenshot rides along "as an additional piece of context, not as the sole one." The speaker dates this finding to early-2025 models rather than claiming it as a durable property. 04:41-05:39
- How the image travels matters as much as whether it travels. Inlining it was the wrong answer: "Our first attempt was just passing B 64 data into the code and that was just a terrible idea. It it just blew up the context window and was bad all around. um don't do that." Images are instead abstracted out of the scene graph and hoisted to the top level as links. 05:09-05:24
- **The cost of borrowing a representation is a translation layer you own and a framework bias you have to detect.** Figma's output is React and Tailwind regardless of what the consumer writes, and the team said outright that they "didn't know if the react tailwind code would be successful for other types of code bases." That uncertainty is what drove them to add self-reported language and framework arguments to their tools — the bias introduced by this page's choice is what the instrumentation on [Optional Self-Reported Tool Arguments Are Segmentation Signal, Not Ground Truth](optional-self-reported-tool-arguments-are-segmentation-signal.md) exists to find. 12:29-12:53
- Relationship to the medium argument: [Match the Agent's Output Medium to Its Native Representation](match-agent-output-medium-to-its-native-representation.md) chooses text over pixels, and names "Figma MCPs" among the tools that approach the problem "like a human." This source is the Figma MCP's own account, and it does not contradict that rule so much as run one level below it — every option here except the bare image was already structured text, and the deciding variable was *which* text. The distinction matters because the two rules can point different ways: the most structured, most semantically precise text is often the one the models have seen least.
- Practical consequence: the format worth exposing may already exist elsewhere in your product for an unrelated reason. Figma's winning serializer was built for a website builder, not for agents, and reusing it was cheaper than designing an agent-specific one.
- Nothing here is measured in the talk. There is an eval — mixed quantitative and qualitative, later automated behind LLM judges — but no score, pass rate, or before/after comparison between the three representations is reported, and Figma has no visibility into any lab's training mix. Treat the pretraining-mass criterion as a cheap hypothesis to test, not as a demonstrated result.

Related topics:
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Match the Agent's Output Medium to Its Native Representation](match-agent-output-medium-to-its-native-representation.md)
- [Give Browser Agents a Compact Whole-Page Representation](give-browser-agents-a-compact-whole-page-representation.md)
- [Return a Pointer to the Reader's Own Component Instead of a Faithful Copy](return-a-pointer-to-the-readers-own-component-instead-of-a-copy.md)
- [Optional Self-Reported Tool Arguments Are Segmentation Signal, Not Ground Truth](optional-self-reported-tool-arguments-are-segmentation-signal.md)
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)
- [Keep visual inputs at native shape for GUI and video agents](keep-visual-inputs-at-native-shape-for-gui-and-video-agents.md)

Sources:
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 03:33-05:39, 12:29-12:53
