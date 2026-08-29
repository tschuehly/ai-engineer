# Serve Markdown Through Three Redundant Paths

Summary: Publish the Markdown version of every page through three independent access paths — a `.md` URL suffix, `Accept`-header content negotiation, and a `?mode=agent` query parameter — plus a `<link>` alternate in the HTML head. The redundancy is not belt-and-braces engineering; it is coverage for agents whose capabilities differ, including ones that cannot set a request header.

Use when:
- Adding agent-readable Markdown to a docs or marketing site and choosing a single mechanism.
- An agent, or a human pasting a URL into one, cannot reach your Markdown even though it exists.
- Auditing whether the agent-readable surface is reachable by the agents you actually care about.

Details:
- **The motivation is cost.** "HTML is expensive, and why can't we just ship markdown to the agents? And we can." The Markdown twin of a documentation page carries the same content without the markup, navigation chrome, and scripts that an agent pays for and discards. ([Burns](../sources/20260826_V_5bn4q-vAI.md), 07:07-07:20)
- **Path 1 — the `.md` suffix.** Append `.md` to any documentation URL and get the Markdown. Its real virtue is that it is *pasteable*: a human handing a page to an agent can type the suffix, with no capability required on the agent's side. (07:20-08:31)
- **Path 2 — content negotiation.** A redirect in the framework config so that "if it detects an agent has the header of accepting markdown, instead of returning the HTML, it will return the markdown." This is the correct-by-the-book mechanism and the one that needs no URL change. (08:31-08:56)
- **Path 3 — the query parameter.** "Not all agents can append header tags. So, there's also a URL query of `mode=agent`." This is the whole argument for redundancy in one sentence: the standards-clean path assumes a client capability that a meaningful share of agents do not have, and a query parameter survives any client that can construct a URL. (08:56-09:06)
- **The discovery hint, and its honest caveat.** A `<link>` alternate in the head declares that a Markdown version exists — "if you look at all the best documentation websites, [Mintlify], Vercel, [c15t]… they all have this in the header. This is saying to the agents whenever they visit the website that there is an alternative version of this in markdown." Support is unverified: "who actually supports it? Don't ask me. Perplexity, some of the agents, it's all up in the air." Publish it, but do not rely on it as the only route. (07:43-08:17)
- **Design reading: three paths span three capability tiers.** Header negotiation assumes a full HTTP client; the query parameter assumes only URL construction; the suffix assumes only that a human or agent can type. Ordering your fallbacks by required client capability is the generalizable version of this list, and it is the same reasoning that makes an in-page tool surface a complement rather than a replacement for a plain file — see [Expose Site Capabilities to In-Browser Agents With WebMCP](expose-site-capabilities-to-in-browser-agents-with-webmcp.md).
- **Scope beyond docs.** The same pipeline runs on the vendor's marketing site, so "every part of our marketing website also has a markdown file," and the Q&A answer for a non-developer-tool site puts per-page Markdown first: "a lot of CMSs are not built in this way," which is presented as the main obstacle rather than any technical difficulty. (12:11-12:48, 14:49-15:27)
- **Limit.** No measurement is given for how much any path is used, by which agents, or what the HTML-versus-Markdown token difference actually is on these pages. The claim that HTML is expensive is uncontroversial; the routing advice is one team's coverage strategy.

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Hand-Write llms.txt and Index the Rest for Fetching](hand-write-llms-txt-and-index-the-rest-for-fetching.md)
- [Generate Agent-Facing Docs Artifacts From One Markdown Source](generate-agent-facing-docs-artifacts-from-one-markdown-source.md)
- [Expose Site Capabilities to In-Browser Agents With WebMCP](expose-site-capabilities-to-in-browser-agents-with-webmcp.md)
- [Make Web Foundations Agent-Ready Before Adopting WebMCP](make-web-foundations-agent-ready-before-adopting-webmcp.md)
- [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)

Sources:
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 07:07-09:06, 12:11-12:48, 14:49-15:27
