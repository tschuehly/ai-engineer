# Agent-readable web surfaces guide browsing agents

Summary: Web applications should expose agent-readable maps and action surfaces so agents can find relevant content and call intended operations instead of imitating human browsing through screenshots, DOM inspection, and coordinates.

Use when:
- Preparing documentation or product sites for AI coding agents and browser agents.
- Deciding whether a web app should publish `llms.txt`, `llms-full.txt`, or agent-callable tools.

Details:
- The talk argues that web apps now need to optimize not only for human usability and SEO but also for how agents consume and use the application. (36:03-36:41)
- `llms.txt` is framed as a Markdown map, analogous to a mix of `robots.txt` and sitemap conventions, that points agents to the website information they need. (36:47-38:20)
- The Angular example uses `llms.txt` to link agents directly to documentation areas such as animation docs instead of making them crawl every page. (37:36-38:20)
- `llms-full.txt` is described as a variant that can bring a site's content into a single file for agent consumption. (38:23-38:36)
- WebMCP is presented as a proposal for web apps to expose MCP-like tools directly from the application, so agents can call explicit operations such as add-to-cart instead of guessing buttons from screenshots, DOM text, or coordinates. (40:49-42:57)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [MCP applications ship UI and tools together](mcp-applications-ship-ui-and-tools-together.md)
- [Discover large API tool surfaces progressively](discover-large-api-tool-surfaces-progressively.md)

Sources:
- [AI Didn't Kill the Web, It Moved in! - Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)](../sources/20260410_XZ0boOjtbNo.md), 36:03-42:57
