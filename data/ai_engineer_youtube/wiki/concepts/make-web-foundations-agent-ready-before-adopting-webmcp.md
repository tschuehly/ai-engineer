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

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Expose Site Capabilities to In-Browser Agents With WebMCP](expose-site-capabilities-to-in-browser-agents-with-webmcp.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)

Sources:
- [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](../sources/20260611_ghJmWQCIHRM.md), 02:08-03:49
