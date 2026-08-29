# Return a Pointer to the Reader's Own Component Instead of a Faithful Copy

Summary: When a tool can generate a perfect standalone rendering of something the consumer already has a better version of, return a reference to their version instead. Figma's MCP server stops emitting React and Tailwind markup for any design element that Code Connect maps to a real codebase component and returns "use button component" instead — which raises fidelity and cuts context in the same move, rather than trading one for the other.

Use when:
- A tool or MCP server produces generated artifacts (markup, SQL, config, client code) that a mature consumer codebase already has canonical, hardened versions of.
- Output is correct in isolation but wrong in context: it ignores the design system, the internal SDK, the shared helper, the approved query.
- You are trimming tool output for token cost and looking for compression that does not lose information.

Details:
- The reframe: "having an agent translate a pixel uh, perfect version of code isn't enough… That's really only half the story." Correctness against the design and correctness against the codebase are two different bars, and only the first is visible to the generating system. 06:58-07:10
- Why the second bar dominates for enterprises: "An enterprise doesn't care if it's pixel perfect if it's not using its like battle tested accessible and internationalized components." The generated markup is not merely redundant, it is a regression — the real component carries accessibility and internationalization properties the copy silently drops. 07:10-07:50
- The two costs of emitting a copy are named together: "if you had a primary button in your codebase, you wouldn't be referencing it. And that's not ideal if it has accessibility properties or internationalization properties. And then second… you'd eat up the context window." 07:36-07:50
- The mechanism: Code Connect "allows you to link design components to components in your codebase," and the server uses those links to "pass back effectively what is a pointer which allows the agent to use the code component leading to our higher fidelity implementation" — "you go from like this big old thing of uh react [tailwind] to the small react component that just says use button component." 07:17-08:37
- Why this is unusual: fidelity and token cost normally trade against each other, and most context-budget advice is about choosing what to drop. A pointer wins on both because it exploits information the reader already holds. The compression ratio is a property of the *reader's* library, not of the summarizer.
- The precondition is coverage, and it is the page's real limit. The pointer strategy only fires for elements that have a Code Connect mapping; everything unmapped falls back to full markup with all of its costs. That is why Figma wanted to ask the user "can we map out your code base for code connections so that our MCP server can link them so that the output would be better and reduce the amount of context we send" — the bulk-mapping workflow described in [Tools Are the Only Primitive Every Client Implements](tools-are-the-only-primitive-every-client-implements.md) exists to raise this coverage rate. 10:55-11:16
- Generalization: the same shape applies wherever a server can name something in the client's own namespace instead of reproducing it — reference the internal SDK call rather than the raw HTTP request, the shared fixture rather than an inline literal, the existing migration rather than regenerated DDL. The requirement is a mapping between your vocabulary and theirs, which is the expensive part and usually has to be authored, not inferred.
- Nothing on this page is measured. The talk reports no fidelity metric, no token reduction figure, and no eval delta for Code Connect versus raw markup; the "pixel perfect" claim is asserted with a bug-report escalation rather than a number, and the argument for pointers is made from the enterprise objection rather than from data.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Tell the Agent Only What Is Not Recoverable From the Code](tell-the-agent-only-what-is-not-recoverable-from-the-code.md)
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Pick the Serialization the Models Have Seen Most, Not the One Native to Your System](pick-the-serialization-the-models-have-seen-most.md)
- [Tools Are the Only Primitive Every Client Implements](tools-are-the-only-primitive-every-client-implements.md)
- [Agent-Legible Codebases Reduce Generated-Code Entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [Specs and Style Guides Steer Coding Agents Toward Maintainable Code](specs-and-style-guides-steer-coding-agents-toward-maintainable-code.md)

Sources:
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 06:58-08:37, 10:55-11:16
