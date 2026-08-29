# Tools Are the Only Primitive Every Client Implements

Summary: A protocol spec is not the interface you build against — the intersection of what your clients have actually shipped is. Figma maintained a client compatibility matrix as a real artifact, and reimplemented three spec features that clients had not built (server instructions, elicitation, sampling) by expressing them through tool results, the one primitive everybody supports.

Use when:
- Building an MCP server, or any protocol server, against clients that ship on independent timelines.
- A spec feature you designed around turns out to be unimplemented, partially implemented, experimental, or deprecated.
- Deciding whether to wait for client support, degrade the feature, or emulate it through a primitive that already works.

Details:
- The constraint, stated plainly: "the MCP spec had a lot of great pieces in it, but some features weren't quite fleshed out within clients, and other features we really wish existed. Many clients only implemented a subset of the spec, and many features were very experimental." A client compatibility matrix "from March 2025" was a maintained artifact, not a slide. 09:06-09:28
- How uneven it was in practice: Claude Desktop had early support while Claude Code "wasn't really supported uh with all the complete set of features"; OpenAI and VS Code had none until a spec update; VS Code — "truly like the golden client," the one that eventually supported every piece — did not reach general availability until July. "In many cases only tools were supported," and "it was hard to kind of understand what you were building towards because clients supported so many different things." 01:58-02:37
- The ground moves under you too. "A few weeks later after we started getting our initial architecture sorted a new version of the spec dropped uh deprecating the support type that we were going to use which was server events." Sampling was later deprecated outright. Building against the current spec revision is a bet with a known decay rate. 01:46-01:56, 10:40-10:44
- Emulation one, server instructions. The feature "was in the spec, but no clients implemented it. Um, and it wasn't really highlighted in the docs until Anthropic added a nice blog post uh to sort of talk about it and then some clients started adding it." Figma's substitute was to put "additional instructions into each tool call. Basically instructing the LLM how to use our server." Every tool result carries a slice of what a server description would have carried once. 09:48-10:14
- Emulation two, elicitation and sampling as a pair. The intended workflow was to ask the user "can we map out your code base for code connections so that our MCP server can link them," then have the client's model scan the repository and return matches. Neither primitive was reliably available, so both became tool results: when a design node is a component and is not code-connected, return "a prompt to ask the user if they'd want to map the unlink[ed] component… Kind of mimicking elicitation"; on yes, return "another prompt to have the agent scan the code for potential matches, mimicking sampling," surfaced "in a specified format… in bulk to make a bunch of code connections." 10:16-12:03
- **A primitive can be present and still useless if it does not carry the host's context.** "For sampling even when VS code supported it you could only really query it as a general agent not specific to the codebase" — the server could reach a model, but not the model that could see the repository, which was the entire value of the workflow. Check what a primitive is connected to, not only whether it exists. 11:23-11:33
- The cost of emulation is that you give up the guarantee the primitive existed to provide. Real elicitation is a client-rendered prompt with a typed response; a returned string asking the agent to ask the user is a request the agent may reword, ignore, or answer itself, and the "specified format" for bulk results is a convention with nothing enforcing it. You trade a protocol contract for model compliance, which is the same trade described in the two-audience filtering problem on [Review Comments Have Two Audiences With Inverted Error Costs](review-comments-have-two-audiences-with-inverted-error-costs.md) — the agent obeys instructions it should have questioned, and questions instructions it should have obeyed.
- A related reason to prefer proactive surfaces over reactive ones: Figma now exposes resources describing how to use the server plus Figma help articles, "whereas before we would send that information down with like an [error]… and the agent would have to call uh wasting inference and sort of reasoning to sort of figure out what is actually going wrong." Error-driven discovery is paid in extra round trips; the same information placed where the agent already looks is paid once. 09:28-09:47
- Development aid named in passing: the open-source MCP Inspector — "if you haven't used it and you're developing an MCP server, you're doing yourself a disservice." 12:04-12:13
- Time-scoping caveat: all client-support facts here are a snapshot dated March-July 2025, the SSE and sampling deprecations are tied to specific spec revisions, and the speaker's own closing point is that "the MCP spec is only two years old and we're still figuring out the best way to do things." The durable claim is the method — build against the client intersection and emulate upward — not the particular matrix.

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)
- [Expose task workflow guidance through MCP resources and tools](expose-task-workflow-guidance-through-mcp-resources-and-tools.md)
- [Use Tool Names and Descriptions as Operational Prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Standardize the Editor–Agent Boundary With a Client-Agent Protocol](standardize-the-editor-agent-boundary-with-a-client-agent-protocol.md)
- [Return a Pointer to the Reader's Own Component Instead of a Faithful Copy](return-a-pointer-to-the-readers-own-component-instead-of-a-copy.md)
- [An Installed Desktop App Is an Auth and Filesystem Beachhead](an-installed-desktop-app-is-an-auth-and-filesystem-beachhead.md)

Sources:
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 01:46-02:37, 09:06-12:13
