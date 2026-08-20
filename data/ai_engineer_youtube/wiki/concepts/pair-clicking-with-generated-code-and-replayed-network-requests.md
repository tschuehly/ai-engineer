# Pair Clicking With Generated Code and Replayed Network Requests

Summary: The most reliable browser agents in production do not drive pixels for every step. They mix modes: click when the page demands it, but watch the network, have the model write a script that replays the underlying requests, and run that script for the repeatable part — and route simple pages to cheaper models rather than paying frontier prices for a form fill.

Use when:
- A browser agent works but is slow, expensive, or flaky on a task that is fundamentally the same every run.
- Deciding what a browser agent's action space should contain — only UI actions, or UI actions plus code execution and network interception.
- Building a repeatable automation (report pull, data extraction, batch submission) where the first successful run could become a script.

Details:
- The core reframe: "automating the web isn't always just clicking the button on the screen. It might be intercepting the network requests and writing a coding agent or having coding write a script to actually replay those network requests." The browser is used to *discover* the request; the script is what runs afterwards. ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 07:21-07:40)
- The production observation, not a proposal: "the most reliable browser agents that we see in production right now are often writing code alongside using the browser to actually automate a task." (07:40-07:50)
- Why it wins on context, with a familiar example: "you might see Claude Code output a script more often than using Claude in Chrome because that's a very context-efficient way to automate a repeatable task." A click sequence costs tokens on every repetition; a script costs tokens once. (07:50-07:59)
- The same talk's other multimodal lever is model routing inside one task: "sometimes you'll use a smarter model for a more complex page. Sometimes a dumber model for a simpler page. And maybe you're using a combination of coding and computer use to actually power your agent." Multimodal here means multiple models and multiple action modes, not just vision plus text. (07:05-07:21)
- This is the browser-agent statement of a pattern the wiki records from the data-collection side, where an agent explores a site, writes a parser, runs it, and repairs it when selectors change — with measured savings of roughly 60-100 tokens to execute a built script versus ~10,000 tokens to walk the same data through the model. See [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md).
- Boundary: replaying requests is the *cheap* path, not the always-available one. It fails where the UI is the only permissionless interface (no API credentials obtainable), where the endpoint is signed or bound to browser-issued tokens, or where the page's own JavaScript must run for the action to count — see [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md) and [Chrome Stamps Every Input Trusted or Untrusted](chrome-stamps-every-input-trusted-or-untrusted.md). The discipline is to try the cheaper mode and keep the expensive one as the fallback, in the same spirit as [letting deterministic code drive the loop and calling the model only for perception](let-code-drive-the-timed-loop-and-call-the-model-only-for-perception.md).

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [Let Deterministic Code Drive the Timed Loop and Call the Model Only for Perception](let-code-drive-the-timed-loop-and-call-the-model-only-for-perception.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)
- [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)

Sources:
- [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../sources/20260814_GqoNrUz8hEU.md), 07:05-07:59
