# Make Web Foundations Agent-Ready Before Adopting WebMCP

Summary: Good web foundations — semantic HTML, robust accessibility, and fast page performance — make a site usable by AI agents by default, getting it most of the way to agent-ready before any agent-specific standard is added. Exhaust those foundations first; reach for WebMCP only once they are in place.

Use when:
- Prioritizing work to make a site agent-friendly and deciding whether to invest in a new protocol now or improve the existing site.
- Justifying accessibility, semantic-markup, and core-web-vitals work as agent-readiness work, not only human-UX or SEO work.

Details:
- The talk explicitly inserts a foundations step before introducing WebMCP: "you can do so much by improving web foundations first." (03:02-03:14)
- Making a site accessible for everyone makes it accessible to AI agents by default — accessibility and agent-readability share the same structure. (03:14-03:23)
- The concrete foundation list is semantic HTML, robust accessibility standards, page performance (load quickly, mind core web vitals), and good user-experience flows; doing these gets you "halfway to an agent-ready website." (03:23-03:46)
- Only once those are in place does it make sense to start thinking about WebMCP — the new standard is an addition on top of solid foundations, not a substitute for them. (03:46-03:49)
- This is the same reasoning behind the scraping failure WebMCP targets: agents lean on the DOM, the accessibility tree, and screenshots, so a well-structured, accessible, fast page is already easier for an agent to read even without explicit tools. (02:08-03:00)
- **The general form of this page's argument, named.** Jarmak's closing frame is the curb cut: built for wheelchairs, now used by "anybody with wheels, strollers and suitcases," so "by serving the agents, the human path gets cleared, too." This page is one instance running the other direction — foundations built for humans get you halfway to agent-ready — and the two together say the investment is shared rather than duplicated. One caveat the analogy hides: a curb cut is finished when it is poured, while agent readiness is measured against models that change, so it needs a rerun cadence. See [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 16:45-17:21)
- **One more foundation item, and the reason most sites fail it.** Before any in-page tool surface, serve a Markdown representation of each page — via a `.md` URL suffix, `Accept`-header negotiation, and a `?mode=agent` parameter, with a `<link>` alternate in the head announcing it. Asked what an ordinary non-developer-tool website should do first, Burns names exactly this, and identifies the obstacle as tooling rather than difficulty: "a lot of CMSs are not built in this way." The foundations argument therefore extends past semantic HTML and accessibility into the publishing stack's output formats. See [Serve Markdown Through Three Redundant Paths](serve-markdown-through-three-redundant-paths.md). ([Burns](../sources/20260826_V_5bn4q-vAI.md), 07:07-09:06, 14:49-15:27)

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Expose Site Capabilities to In-Browser Agents With WebMCP](expose-site-capabilities-to-in-browser-agents-with-webmcp.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md)
- [Serve Markdown Through Three Redundant Paths](serve-markdown-through-three-redundant-paths.md)
- [Hand-Write llms.txt and Index the Rest for Fetching](hand-write-llms-txt-and-index-the-rest-for-fetching.md)

Sources:
- [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](../sources/20260611_ghJmWQCIHRM.md), 02:08-03:49
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 16:45-17:21
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 07:07-09:06, 14:49-15:27
