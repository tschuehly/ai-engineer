# Give Browser Agents a Compact Whole-Page Representation

Summary: Represent a web page for a browser agent as a compact markdown-like structure that captures the whole page in a few thousand tokens, rather than dumping the raw DOM or relying on screenshots. A screenshot shows only one viewport snippet; the raw DOM is huge; the compressed representation lets the model see and reason over the entire page cheaply.

Use when:
- Choosing the observation format for a browser or computer-use agent.
- A browser agent scrolls, re-screenshots, or loses track of off-screen elements, or its DOM-based context is blowing up token cost.

Details:
- Observation-cost comparison for one page: the full DOM ≈ 20,000 tokens; a screenshot ≈ 1,100 tokens but reveals only the single visible snippet; a compressed markdown representation ≈ 1,800 tokens yet represents the *entire* page. (03:33-03:50)
- The compressed representation "compresses the website and lets the agent see the entire page in very few tokens," so the model can plan long action sequences instead of navigating blind through partial screenshots. (01:18-01:26)
- Pair the markdown with a screenshot: together they stay cheap token-wise while giving the model both structure (whole-page layout, all actionable elements) and pixels (visual grounding), which lets it reason well and construct a long sequence of tasks. (04:08-04:23)
- Augment the static representation with change feedback: track the full end-to-end page and report deltas (elements that appeared, elements now gone, a blocker that was removed) so the model does not have to re-screenshot to discover what changed. (03:50-04:08)
- This is the observation lever of the broader thesis that the browser-agent bottleneck is the interface, not the model — see [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md).
- **Caveat on what the compressed representation cannot carry.** Any document-derived format inherits the fact that a page's displayed state is often computed rather than written: a variant that is grayed out and unclickable because a fetched `quantity` is zero has no text saying "sold out" anywhere in the source, and a score that arrives in a later asynchronous fetch is absent from the initial HTML entirely. "It is calculated. It is rendered." That is an argument for keeping the screenshot in the pair for the specific facts being extracted, not just for visual grounding of clicks — see [Rendered State Is Not in the HTML](rendered-state-is-not-in-the-html.md). ([Dhruv Batra](../sources/20260814_Ki980nV0__0.md), 09:01-11:33)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)
- [Rendered State Is Not in the HTML](rendered-state-is-not-in-the-html.md)

Sources:
- [Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, ARK](../sources/20260628_JnubYCYunk8.md), 01:18-04:23
- [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../sources/20260814_Ki980nV0__0.md), 09:01-11:33
