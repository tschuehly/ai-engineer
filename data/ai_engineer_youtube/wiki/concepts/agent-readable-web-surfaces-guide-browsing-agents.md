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
- A dedicated WebMCP talk from the Google Chrome team frames the same surface concretely: tools are page-scoped (each page advertises its own action set), they can be added declaratively by annotating existing HTML forms (the browser auto-generates the JSON schema) or imperatively via `registerTool` with an `execute` block of JavaScript, and a live demo bought concert tickets in three tool calls (search, open page, purchase). ([Agyemang/Google] 04:47-17:28)
- Surface design has a prerequisite: solid web foundations (semantic HTML, accessibility, page performance, good UX) already make a site usable by agents and get it "halfway to agent-ready" before any explicit agent tooling is added. See [Make Web Foundations Agent-Ready Before Adopting WebMCP](make-web-foundations-agent-ready-before-adopting-webmcp.md). ([Agyemang/Google] 03:02-03:49)

- What best-in-class agents actually consume today sits between the raw page and a published tool surface: "they're not just consuming the raw DOM and HTML of the page anymore. They're looking at subsections of that like the accessibility tree, the ARIA tags. These are labeled components of a page that can help show your agent where it needs to click and why." Accessibility markup is the one agent-readable surface that already exists on many sites without anyone adding it for agents — which makes ordinary accessibility work the cheapest agent-readability investment available. ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 10:26-10:46)
- The file-convention family is broader than `llms.txt` alone: "we've seen things like `llms.txt`, `skills.md`, `agents.md` all being published alongside our websites. We need to see more of that to build the agent-first web." The same source names the missing member of the family — a published convention for how an agent *signs up and logs in*, see [Design an Agent-First Signup and Login Flow](design-an-agent-first-signup-and-login-flow.md). ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 11:05-11:45)
- Caveat on adoption, from the same source: this half of the problem is the harder one because it is not self-serve. "We're not just engineering on our own systems anymore. We have to be evangelists to the web and to the broader world that, hey, you want agents to come to your website." Any design that depends on site cooperation excludes the sites least likely to cooperate — see [Computer Use Diffuses AI Into the Form-Filling Economy](computer-use-diffuses-ai-into-the-form-filling-economy.md). ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 10:09-10:26)

- Scope limit worth stating on this page, from a source that rejects the premise for most of the web: every surface here requires the site's owner to publish something, and Dhruv Batra argues that only the head of the distribution will — "the head of the distribution, the most popular websites perhaps, will give you the API, but the long tail will not," where the tail is ~200 million active sites including institutions that answer questions by fax and Freedom of Information Act request. He also reads the growing convention list as evidence of churn rather than progress: "it was initially supposed to be MCP servers, then WebMCP, and for payments there are 20 different competing protocols." Treat this page as the playbook for sites that *choose* to participate, and [The Long Tail of the Web Will Not Ship APIs](the-long-tail-of-the-web-will-not-ship-apis.md) for coverage of the rest. ([Dhruv Batra](../sources/20260814_Ki980nV0__0.md), 00:57-08:33)
- The DOM-adjacent surfaces also inherit a limit that is not about adoption: an affordance the page renders rather than states — a grayed-out, unclickable "sold out" driven by a fetched `quantity` of zero — has no text for any of these formats to carry. See [Rendered State Is Not in the HTML](rendered-state-is-not-in-the-html.md). ([Dhruv Batra](../sources/20260814_Ki980nV0__0.md), 10:14-11:33)
- **Commerce went past agent-readable pages to a separate protocol plane, and the reason was the payment step.** The screenshot-and-DOM generation failed twice over — "really clunky and slow and brittle," and detected as automation by the merchant's own fraud stack — so the shape that replaced it removes the page from the loop entirely: "the AI surfaces the product. Agent calls the merchant checkout API. No browser." For high-value transactional flows this suggests page-level affordances are a bridge rather than the destination; they help an agent understand a site, but the transaction wants a server-to-server contract. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 03:08-03:49, 05:26-06:05)
- **The precondition that makes `llms.txt` inert when it is missing, plus two format preferences.** Jarmak names `llms.txt`-style pages as the response to assistants repeating stale claims about a product — "more authoritative sources of truth that you're hoping to direct the agent to" — and immediately qualifies it: "they still need to be using the tools and using real-time information and provenance to be able to give accurate answers about your product." Against a model answering from weights, a published file does nothing. Two format notes from the same passage: assistants "really really like charts and FAQs," and you should "give the agent something to quote… they want to bring something that they can really sell to the user," so the unit that travels is an extractable, citable claim rather than a paragraph. And refresh unconditionally — "even if your stuff hasn't changed in 2 years… keep everything up-to-date and fresh because that is how they have their relevance algorithm." ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 11:27-12:12)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [The Long Tail of the Web Will Not Ship APIs](the-long-tail-of-the-web-will-not-ship-apis.md)
- [Rendered State Is Not in the HTML](rendered-state-is-not-in-the-html.md)
- [Expose Site Capabilities to In-Browser Agents With WebMCP](expose-site-capabilities-to-in-browser-agents-with-webmcp.md)
- [Make Web Foundations Agent-Ready Before Adopting WebMCP](make-web-foundations-agent-ready-before-adopting-webmcp.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [MCP applications ship UI and tools together](mcp-applications-ship-ui-and-tools-together.md)
- [Discover large API tool surfaces progressively](discover-large-api-tool-surfaces-progressively.md)
- [Design an Agent-First Signup and Login Flow](design-an-agent-first-signup-and-login-flow.md)
- [Publish Per-Site Skills So Agents Do Not Rediscover a Website](publish-per-site-skills-so-agents-do-not-rediscover-a-website.md)
- [Agent Protocols Must Encode the Distinctions the User Interface Collapses](agent-protocols-must-encode-the-distinctions-the-ui-collapses.md)
- [Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md)
- [Human and Agent Credibility Reward Opposite Writing Styles](human-and-agent-credibility-reward-opposite-writing-styles.md)
- [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md)

Sources:
- [AI Didn't Kill the Web, It Moved in! - Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)](../sources/20260410_XZ0boOjtbNo.md), 36:03-42:57
- [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](../sources/20260611_ghJmWQCIHRM.md), 03:02-17:28
- [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../sources/20260814_GqoNrUz8hEU.md), 10:09-11:45
- [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../sources/20260814_Ki980nV0__0.md), 00:57-11:33
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 03:08-03:49, 05:26-06:05
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 11:27-12:12
