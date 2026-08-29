# Expose Site Capabilities to In-Browser Agents With WebMCP

Summary: WebMCP is a proposed web standard that lets a site declare its capabilities as named, typed, described tools for in-browser AI agents, replacing the scrape-the-DOM-then-guess-coordinates pattern with direct, page-scoped tool calls. It is the client-side implementation of the tools part of MCP, so the browser must be open and the tools live in the page.

Use when:
- Building a complex multi-step site (booking, filtering, medical/financial forms, hidden actions) where you want browser agents to act reliably instead of inferring buttons from screenshots and DOM text.
- Deciding how a web app should publish agent-callable actions, and where WebMCP fits relative to server-side MCP, `llms.txt`, and pixel-level browser control.

Details:
- Motivating failure: agents typically pass the entire DOM, then read the accessibility tree, then take a screenshot to catch missing elements, then compute how far to click — a long, brittle, token-heavy chain that can still miss when an ad loads and shifts the layout. WebMCP replaces guessing with a "menu" of explicit actions, framed as "the USB-C of AI agent interactions," which the talk says significantly improves agent performance and reliability on a site. (02:08-04:42)
- Relationship to MCP: WebMCP is "the implementation of the tools part of the MCP" — inspired by MCP "like JavaScript is inspired by Java." It is complementary, not a replacement: MCP connects agents to applications server-side (you host a service the agent can reach anywhere, anytime), while WebMCP is client-side — all tools live in the browser and the browser window must be open for it to work. (09:58-11:23)
- Tools are page-scoped. In the maze demo the landing page exposed only `start maze game`; after starting, the maze page exposed a new tool set (move N/S/E/W, look, pick up / drop / use items). The agent maps natural language ("down then right", "complete the maze") onto the registered tools and can repeat calls until it judges the task done; prompt quality affects efficiency. (04:47-08:59)
- Declarative API: add a few attributes (tool name, tool description) to a normal HTML form and the browser auto-generates a JSON schema using the form fields as parameters. Additional attributes exist, e.g. an `agent-invoked` boolean to record whether a form was filled by an agent or a human. Use it for standard form elements. (12:35-13:35)
- Imperative API: call `registerTool` with an object — manually author the schema, give a descriptive name and description so the agent knows when to call it, and an `execute` block of normal JavaScript (wrap existing functions, validate/trim input, create and append DOM nodes) that returns information to the agent on success for its next steps. It is the more-used path because real flows are usually complex/multi-step. (13:41-15:13)
- End-to-end shape: the concert demo bought tickets in three tool calls — `search concerts` (by name → returns info including an ID), `open concert page` (with the ID → loads a page exposing its own tools), and `purchase ticket` (quantity, section). Keep the UI in sync with each tool call so the user sees what is happening, and leave the final checkout for the user to do manually so they know they are spending real money. (15:16-17:43)
- Status and tooling (as of the talk): experimental early preview, API changing weekly; enabled in Chrome 146+ (Chrome Canary recommended, else an experimental URL flag). The Model Context Tool Inspector is a Chrome Web Store extension that lists every tool found on a page and lets you prompt or call tools directly for debugging; a GitHub repo ships ~6-7 demos and an eval CLI for testing WebMCP tools on your own sites. (04:53-05:54, 17:46-20:01)

- **The agent-side reading of the same feature**, from a browser-agent platform: "Chrome just added WebMCP… Websites can now publish MCP servers within their page that your agent can take advantage of without pre-installing the actual MCP. It can now issue tool calls to a website like submit the registration form in a way that's not only context-efficient, but is website approved and blessed." Two things in that sentence matter beyond the Chrome-team framing above — no client-side installation step (the tool surface arrives with the page, so an agent visiting an unfamiliar site gets it for free), and *blessed*, meaning the action is one the site chose to expose rather than one the agent inferred. Klein also treats WebMCP as a supply of pre-visit site knowledge, which is the same job as a [per-site skill](publish-per-site-skills-so-agents-do-not-rediscover-a-website.md): "your agent doesn't have to discover something in the first place if it's done it before." ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 08:18-08:26, 10:46-11:25)
- **A commerce data point about where in-page tools stop being enough.** Agentic shopping reached the same conclusion WebMCP does — stop guessing at the DOM, declare capabilities as tools — and then went one step further by moving the transaction off the page: "agent calls the merchant checkout API. No browser." The reason is specific to money rather than to ergonomics: an in-page tool still executes inside a browser session the merchant's fraud stack is actively trying to identify, and that is where browsing agents died, "stuck on the payment flow." Page-scoped tools serve discovery and interaction; the checkout leg still wants a server-to-server protocol. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 03:30-03:49, 05:26-06:05)

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Make Web Foundations Agent-Ready Before Adopting WebMCP](make-web-foundations-agent-ready-before-adopting-webmcp.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [MCP applications ship UI and tools together](mcp-applications-ship-ui-and-tools-together.md)
- [Group Agent Tools by Human-Facing Actions](group-agent-tools-by-human-facing-actions.md)
- [Publish Per-Site Skills So Agents Do Not Rediscover a Website](publish-per-site-skills-so-agents-do-not-rediscover-a-website.md)
- [Map the Agentic Commerce Protocol Stack by Layer](map-the-agentic-commerce-protocol-stack-by-layer.md)

Sources:
- [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](../sources/20260611_ghJmWQCIHRM.md), 02:08-20:01
- [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../sources/20260814_GqoNrUz8hEU.md), 08:18-08:26, 10:46-11:25
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 03:30-03:49, 05:26-06:05
