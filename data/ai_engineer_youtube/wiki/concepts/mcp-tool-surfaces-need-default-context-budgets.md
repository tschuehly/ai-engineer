# MCP Tool Surfaces Need Default Context Budgets

Summary: MCP servers with broad platform coverage should treat default tool exposure and output size as a context budget. More tools can make agents worse when all descriptions and schemas are loaded upfront.

Use when:
- Designing MCP defaults for a large product surface such as repos, issues, pull requests, actions, and projects.
- Debugging agents that select the wrong tool, forget available tools, or burn context before useful work begins.

Details:
- GitHub's MCP server exceeded 100 tools after public contribution growth, and agents became worse at using GitHub while context windows filled faster. (02:06-02:24)
- Configurable tool sets and dynamic discovery were not enough because most users stayed on default settings rather than editing JSON configuration. (03:21-04:15)
- GitHub reduced initial context load by focusing defaults for common use cases and grouping CRUD tools; the default configuration still allowed expansion or contraction for users who needed it. (05:10-05:48)
- Output payloads count against the same budget as tool descriptions: tailoring a pull-request listing output cut more than 75% of its output tokens. (05:53-06:13)
- Cloudflare hit the same context-budget wall at API scale: a 2.3 million-token OpenAPI spec became roughly 1.1 million tokens when naively converted into endpoint tools, making progressive discovery necessary. (02:37-03:30)
- Agent discovery is not a one-time human documentation read: every session may enumerate tool names and descriptions during handshake, so tool count and description size become recurring context costs. 06:12-06:56
- A visible tool count above roughly 50 tools per agent is a performance smell unless the team invests in routing, splitting, namespacing, and evaluation; the budget is per agent, not per individual server. 35:32-37:14
- Amp adds a coding-agent-specific version of this failure mode: irrelevant tools increase context confusion, and generic MCP server descriptions may not be tuned to the feedback loops a particular coding agent needs to close. 04:40-05:58
- AWS describes an internal agent with more than 6,000 tools and uses a retrieval step over stored tool descriptions so only relevant tools enter the model context. (10:57-11:30)
- Bright Data's web-access MCP exposes 66-69 tools but the speaker only loads all of them to demo the surface; for a real task he loads just the two needed (for example scrape-markdown plus search), warning that loading everything floods the context with irrelevant data. (13:41-14:03)
- Chrome DevTools shows the budget trade-off from both ends. Too few: its monolithic `debug_webpage` tool failed because agents couldn't compose behaviors, but decomposing into 25 tools only traded the problem — agents then had 25 tools and no reliable way to pick the right one. Too many: "the schema is the UI for the agent," and a cited paper found ~97% of MCP tool descriptions have quality smells, while richer descriptions raise context size and bias smaller models toward calling tools they shouldn't (an "endless quest for minimum viable description"). (Chrome DevTools, 15:28-18:00)
- Chrome DevTools manages the budget with three levers: tool categorization (hide niche tools such as Chrome-extension debugging behind command-line parameters instead of the default context), a "slim mode" that exposes only ~3 tools (select page, navigate page, evaluate script) at the cost of extra turns or a missing capability, and a CLI alongside the MCP server so the agent chains commands and does post-processing locally (grep the accessibility tree, pipe the control ID into a click) to keep tokens off the model. (Chrome DevTools, 11:10-13:12)
- Output payloads are the other half of the budget: a performance-tracing tool that returned a ~50,000-line JSON trace blew through the context window, so it returns markdown plus a semantic summary instead — "point the agent at the right sentence, not the whole book" — while still allowing raw output for separate post-processing. (Chrome DevTools, 03:58-05:20)
- **The client side of the budget, from a harness that enforces one numerically.** Codex treats the growth term explicitly — model instructions "are fairly structured and don't really change in size," while "the tool registry, where especially if you install MCPs… you might have additional context that is like growing as you're installing more MCPs" — and answers it with two different mechanisms for two different surfaces. Tools are [deferred out of the window entirely and retrieved by tool search](defer-tool-definitions-out-of-context-and-let-the-model-search-for-them.md); the skills list gets a hard budget of [2% of the maximum context window with descriptions trimmed as it grows](cap-the-skills-list-as-a-share-of-the-context-window.md). This page's guidance is aimed at server authors who cannot control the client; the mirror finding is that a client can defend its own budget regardless of what servers expose, and that a percentage of the window is a defensible way to express it. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 05:29-06:35)
- **A third lever alongside fewer tools and trimmed payloads: reference what the reader already has.** Figma's MCP server replaces generated React and Tailwind markup with a pointer to the consumer's own component wherever Code Connect supplies a mapping, collapsing "this big old thing of uh react [tailwind]" into "the small react component that just says use button component." This is the rare compression that does not lose information, because the omitted detail lives in the reader's codebase — but the compression ratio is a property of the reader's library rather than of the server, and every unmapped element falls back to full markup. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 07:36-08:37)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Discover large API tool surfaces progressively](discover-large-api-tool-surfaces-progressively.md)
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)
- [Task-tuned tool sets beat generic integration surfaces for core coding loops](task-tuned-tool-sets-beat-generic-integration-surfaces-for-core-coding-loops.md)
- [Retrieve Tool Descriptions Before Loading Large Tool Catalogs](retrieve-tool-descriptions-before-loading-large-tool-catalogs.md)
- [Defer Tool Definitions Out of Context and Let the Model Search for Them](defer-tool-definitions-out-of-context-and-let-the-model-search-for-them.md)
- [Cap the Skills List as a Share of the Context Window](cap-the-skills-list-as-a-share-of-the-context-window.md)
- [Return a Pointer to the Reader's Own Component Instead of a Faithful Copy](return-a-pointer-to-the-readers-own-component-instead-of-a-copy.md)

Sources:
- [Scaling GitHub for your Agents — Sam Morrow, GitHub](../sources/20260427_0n3MKk7r60w.md), 02:06-06:13
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md), 02:37-03:30
- [Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect](../sources/20260112_96G7FLab8xc.md), 06:12-06:56, 28:25-29:24, 35:32-37:14
- [Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code](../sources/20251222_gvIAkmZUEZY.md), 04:40-05:58
- [Building Agents at Cloud Scale - Antje Barth, AWS](../sources/20250802_WJjInLeaJjo.md), 10:57-11:30
- [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](../sources/20260617_btxGmN8RvNU.md), 13:41-14:03
- [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](../sources/20260605__B4Pv9ttFgY.md), 03:58-18:00
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 05:29-06:35
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 07:36-08:37
