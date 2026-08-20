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

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)
- [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md)
- [Chrome Stamps Every Input Trusted or Untrusted](chrome-stamps-every-input-trusted-or-untrusted.md)

Sources:
- [Useful General Intelligence - Danielle Perszyk, Amazon AGI](../sources/20250802_Dj0b_cEBHBI.md), 03:17-03:27, 07:48-08:31
- [The Dark Arts of Web Automation — Corey Gallon, Rexmore](../sources/20260814_26RtyAm9y_Q.md), 00:01-01:09, 08:48-12:41
