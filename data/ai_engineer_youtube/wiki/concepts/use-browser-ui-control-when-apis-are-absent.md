# Use Browser UI Control When APIs Are Absent

Summary: Browser-based computer use is a practical agent tool surface when useful websites expose visual interfaces but no suitable APIs. It trades clean machine contracts for broad reach, so reliability work shifts into UI perception, action grounding, and workflow-level guardrails.

Use when:
- A target workflow spans websites or tools that do not expose enough API coverage.
- Comparing API, MCP, CLI, and browser-control surfaces for an agent product.

Details:
- Perszyk says the future atomic unit of digital interaction may be an agent call, but the obstacle is that most infrastructure still assumes APIs while many websites are built for visual UIs. (07:48-08:09)
- Nova Act is presented as a specialized Amazon Nova computer-use model plus SDK where an `act` call translates natural language into screen actions. (08:09-08:31)
- The talk notes that current models still cannot reliably click, type, and scroll, making UI-control reliability a prerequisite before broad computer-use agents can be trusted. (03:17-03:27)
- Browser control complements, rather than replaces, machine-readable APIs and CLIs: it reaches existing human-facing workflows but inherits visual ambiguity, latency, and safety constraints. (08:00-08:31)
- **The API can exist and still be unavailable to you.** A second source sharpens "APIs are absent" into a permissions argument: in corporate environments the Office 365 tenant API "requires an app registration, and it also requires admin approval, which as an employee you can't often get," while the web login the employee already has is enough to drive the same actions. "In this pattern the web UI itself kind of becomes a universal API… a permissionless API." Batch personalized email from the Outlook web client needs no human-likeness at all — a synthetic click opens compose, fields are filled programmatically, a synthetic click sends, and the captured sequence loops for 20 or 200 messages. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 08:48-10:43)
- **The cost of that reach is a hostility gradient.** Sites that resist automation escalate the work from a scripted sequence to trusted browser input to human-like motion and vision, which is the escalation discipline in [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md); the immediate trap is that resistance often presents as silence rather than an error ([Chrome Stamps Every Input Trusted or Untrusted](chrome-stamps-every-input-trusted-or-untrusted.md)). Driving the UI in place of a sanctioned API also inherits the account's terms of service, and terms-of-service risk is real: the same speaker was threatened with an account ban for the work. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 00:01-01:09, 10:43-12:41)

- **"Absent" is the steady state for most of the web, not a transitional gap.** Dhruv Batra's version of this page's premise is a distribution claim: "the head of the distribution, the most popular websites perhaps, will give you the API, but the long tail will not," against roughly 200 million active sites whose owners — school district offices that answer a purchasing question with a Freedom of Information Act request and a scan of your own email — will not publish an endpoint even after generating one becomes technically trivial. That converts UI control from a fallback into the default path for a majority of targets; see [The Long Tail of the Web Will Not Ship APIs](the-long-tail-of-the-web-will-not-ship-apis.md). The same source is explicit about the other direction too: where an aggregator or API already exists, clicking through the UI "is bizarre." ([Dhruv Batra](../sources/20260814_Ki980nV0__0.md), 01:12-08:33)
- **The cheap substitute does not work either.** The natural reaction — skip both the API and the pixels and have a coding agent read the HTML — fails on pages whose displayed state is computed rather than stored, which includes ordinary e-commerce and sports pages. See [Rendered State Is Not in the HTML](rendered-state-is-not-in-the-html.md). ([Dhruv Batra](../sources/20260814_Ki980nV0__0.md), 08:33-12:24)
- **How the control surface itself is changing, from the API side.** OpenAI's original computer-use tool "only allowed you to do one action at a time," and required the harness author to implement each exposed action type; recent models and API shapes let the agent script the environment instead — Codex drives Playwright against a persistent Node REPL, so the action vocabulary becomes whatever the library exposes and page handles survive across turns ([Drive Computer Use Through a Persistent Scripting Session](drive-computer-use-through-a-persistent-scripting-session.md)). This changes the economics of the fallback path on this page in a specific way: the agent can inspect one page by hand and then write a loop for the remaining hundred, so the per-page cost of UI control stops being flat. It does not touch the perception problem — the script still has to name the right element — nor the terms-of-service exposure. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 08:12-10:07)
- **In commerce the counterparty actively defends against it, and the failure lands at the step that matters.** The usual account of browser-agent brittleness is client-side; Prio supplies the other half from inside a retailer: "any engineering department of that merchant will tell you an AI impersonating your browser is just firing up all the alarm bells. So, a lot of times, you will probably be even stuck on the payment flow." Anti-fraud tooling is built to detect exactly the signature a browsing agent produces, so the agent gets furthest through the cheap steps — search, browse, add to cart — and fails at checkout. Where the site has an adversarial stake in identifying automation, "no API available" understates the problem. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 03:08-03:49)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [The Long Tail of the Web Will Not Ship APIs](the-long-tail-of-the-web-will-not-ship-apis.md)
- [Rendered State Is Not in the HTML](rendered-state-is-not-in-the-html.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)
- [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md)
- [Chrome Stamps Every Input Trusted or Untrusted](chrome-stamps-every-input-trusted-or-untrusted.md)
- [Drive Computer Use Through a Persistent Scripting Session](drive-computer-use-through-a-persistent-scripting-session.md)
- [Agent Protocols Must Encode the Distinctions the User Interface Collapses](agent-protocols-must-encode-the-distinctions-the-ui-collapses.md)

Sources:
- [Useful General Intelligence - Danielle Perszyk, Amazon AGI](../sources/20250802_Dj0b_cEBHBI.md), 03:17-03:27, 07:48-08:31
- [The Dark Arts of Web Automation — Corey Gallon, Rexmore](../sources/20260814_26RtyAm9y_Q.md), 00:01-01:09, 08:48-12:41
- [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../sources/20260814_Ki980nV0__0.md), 01:12-12:24
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 08:12-10:07
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 03:08-03:49
