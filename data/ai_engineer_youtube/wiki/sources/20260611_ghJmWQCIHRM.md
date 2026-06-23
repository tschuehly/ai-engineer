# The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google

Source: [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](https://www.youtube.com/watch?v=ghJmWQCIHRM)
Uploaded: 2026-06-11
Transcript: `raw/20260611_ghJmWQCIHRM/ghJmWQCIHRM.en-orig.vtt`

## Summary

Tara Agyemang, a developer relations engineer on the Google Chrome team, introduces WebMCP (Web Model Context Protocol), a proposed web standard that lets a site declare its capabilities as structured tools that in-browser AI agents can call directly, instead of forcing agents to scrape the entire DOM, the accessibility tree, and screenshots and then compute pixel coordinates for a click that may miss when an ad shifts the layout. She frames WebMCP as the client-side implementation of the "tools" part of MCP — analogous to how JavaScript was inspired by Java — distinct from server-side MCP because the tools live in the browser and the page must be open. The talk gives the two implementation paths (a declarative API that adds attributes to existing HTML forms so the browser auto-generates a JSON schema, and an imperative `registerTool` API with an `execute` block of normal JavaScript for complex multi-step flows), shows page-scoped tools through a maze-game demo, and completes a concert-ticket purchase in three tool calls. It stresses a foundations-first prerequisite (good semantic HTML, accessibility, and performance get a site halfway to agent-ready) and keeping the UI in sync with tool calls, with manual checkout for real money. WebMCP is experimental early-preview (Chrome 146+), with a Model Context Tool Inspector extension and an eval CLI available now.

## Extracted Concepts

- [Expose Site Capabilities to In-Browser Agents With WebMCP](../concepts/expose-site-capabilities-to-in-browser-agents-with-webmcp.md) - the talk is the dedicated WebMCP walkthrough: declarative vs imperative APIs, page-scoped tools, and the client-side tools-only relationship to MCP.
- [Make Web Foundations Agent-Ready Before Adopting WebMCP](../concepts/make-web-foundations-agent-ready-before-adopting-webmcp.md) - accessible, semantic, fast sites are already most of the way to agent-ready before any new standard is added.
- [Agent-readable web surfaces guide browsing agents](../concepts/agent-readable-web-surfaces-guide-browsing-agents.md) - strengthens the existing surface-design concept with a dedicated WebMCP source.

## Topic Links

- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

## Notes

- The motivating failure: agents usually pass the entire DOM to understand the page, then read the accessibility tree for structure, then take a screenshot to catch elements not in the HTML/a11y tree, then measure how far to click — a long, brittle, token-heavy process that can still miss when an ad loads and pushes content down. (02:08-03:00)
- Foundations first: making a site accessible for everyone makes it accessible to AI agents by default; improving semantic HTML, robust accessibility, page performance (core web vitals), and good UX flows gets you "halfway to an agent-ready website," and only then does WebMCP make sense. (03:02-03:49)
- WebMCP is a proposed web standard that lets you define your site's capabilities as structured tools for AI agents — "the USB-C of AI agent interactions" — giving the agent a menu of named actions instead of guessing what the site does, which "significantly improves the performance and the reliability of agents navigating your website." (03:53-04:42)
- Tools are page-scoped: in the maze demo the landing page exposed only a `start maze game` tool, and after starting, the maze page exposed a new set (move north/south/east/west, look, pick up / drop / use items). The agent maps a natural-language prompt ("down then right", "complete the maze") to the registered tools and can repeat tool calls until it judges the task done; prompt quality affects efficiency. (04:47-08:59)
- The Model Context Tool Inspector is a standard Chrome extension (in the Chrome Web Store) that lives in the side panel, lists every tool it finds on the page, and lets you interact via a prompt or call tools directly. The maze demo could only be played through the AI tooling, not by clicking the UI. (04:53-05:54, 09:08-09:26)
- WebMCP vs MCP are complementary: MCP connects agents to applications server-side (you set up your own service; the agent can access it anywhere, anytime), while WebMCP is "the implementation of the tools part of the MCP," client-side, with all tools living in the browser and requiring the browser window to be open. (09:58-11:23)
- Use cases are complex multi-step sites: booking a flight, filtering products on a shopping site, filling complicated medical or financial forms, triggering fixes hidden on a page, or letting a user ask the agent to apply filters instead of clicking each input and checkbox. (11:23-12:35)
- Declarative API: add a few attributes (tool name, tool description) to a normal HTML form and the browser auto-generates a JSON schema using the form fields as parameters; other attributes exist, e.g. an `agent-invoked` boolean to record whether the form was filled by an agent or a human. Use it when you have a standard form element. (12:35-13:35)
- Imperative API: call `registerTool` with an object — manually author the schema, give it a descriptive name and description (so the agent knows when to call it), and an `execute` block of normal JavaScript (wrap existing functions, validate/trim input, create and append DOM nodes) that returns information to the agent on success for its next steps. It is the more-used path because flows are usually complex. (13:41-15:13)
- Concert demo completed a purchase in three tool calls: `search concerts` (by name → returns concert info including an ID), `open concert page` (with the ID → loads a page that exposes its own tools), and `purchase ticket` (quantity and section). Each step updated the UI so the user can see what is happening — "always make sure your UI is in sync with the tool calls" — and the speaker notes you'd want the user to do the final checkout manually so they know they're spending real money. (15:16-17:43)
- Status and setup: early preview, very experimental, the API has been changing weekly. Enabled in Chrome 146+ (Chrome Canary recommended; otherwise enable an experimental flag via the URL), plus the Model Context Tool Inspector extension. Resources: the early-preview blog/program (docs, best practices, API info) and a GitHub repo with the inspector, ~6-7 demos (maze code is live), and an eval CLI for testing WebMCP tools on your own sites. (17:46-20:01)
- Closing framing: agents already use the web, so we don't have to settle for token-heavy, brittle screen-scraping; WebMCP can turn every website into a high-performance API for agents while still building good UX for human users. (20:29-21:11)
