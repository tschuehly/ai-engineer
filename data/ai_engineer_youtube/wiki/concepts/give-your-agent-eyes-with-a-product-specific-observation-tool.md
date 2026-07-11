# Give Your Agent Eyes With a Product-Specific Observation Tool

Summary: A coding agent is "blindfolded" when it can write code but cannot see the running product it changed. Generic screenshot/browser tooling only fits web apps, so build a bespoke observe-and-control surface tailored to your product's runtime — delivered as a CLI, skill, or MCP — that lets the agent drive the app and read back what actually happened.

Use when:
- Your product is not a plain web page (a VS Code extension, desktop app, game engine, CLI) and off-the-shelf browser/screenshot tools do not reach it.
- Deciding what runtime signals and actions an agent needs to verify its own work instead of relying on a human to click and read logs.

Details:
- Poolside's product is a VS Code extension, not a web page, so generic screenshot/snapshot tooling "takes an extra step to get there"; they built an internal CLI so "our AI can interface with it just like it would with a normal web page. But we take it further." (03:45-04:30)
- The bespoke surface exposes both observation and actuation: take screenshots, produce a "very token-compressed" snapshot of the UI, extract logs from front-end and back-end services, restart services, and stackable high-level commands — open a specific menu, navigate to a page, send a message to the agent, wait for the reply, upload an image. (04:00-04:53)
- The tool itself is not the point — "it's to build your own"; it can be a CLI, a skill, or an MCP, and "it's going to be different from people to people and problem to problem" (he chose a CLI "cuz I like things simple"). (05:43-06:23)
- Tailor the representation to the product: for "a game in Unity, do you want an ASCII representation of your 3D world for your AI?"; for an app with many permissions and logins, make it easy for the AI to take those. (09:17-09:38)
- Finding what to build: refuse to hand-correct the AI ("the button is a bit to the left") and instead ask how to make the AI realize the problem by itself, then run a retrospective loop asking the AI to review its own logs for "stinks" (e.g. `sleep(15)` everywhere signals a missing wait-for). (08:30-09:17)
- This is a distinct move from generic web verification: the categories of signal (visual, log, interaction, state) overlap with multisensory/browser verification, but the emphasis is that non-web products need a *custom-built* surface, not a reused one.

Related topics:
- [Tools](../topics/tools.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Use Multisensory Feedback Loops for Coding-Agent Validation](use-multisensory-feedback-loops-for-coding-agent-validation.md)
- [Autonomous browser verification finds painted-door failures](autonomous-browser-verification-finds-painted-door-failures.md)
- [Expose Observability As Agent-Readable Feedback](expose-observability-as-agent-readable-feedback.md)
- [Reproduce the Bug Before Fixing to Earn Agent Trust](reproduce-the-bug-before-fixing-to-earn-agent-trust.md)
- [Agent Experience Means Autonomous Access, Understanding, and Operation](agent-experience-means-autonomous-access-understanding-and-operation.md)

Sources:
- [Your agent is blindfolded — Johan Lajili, Poolside AI](../sources/20260708_iRcX54EO5g8.md), 03:45-04:53, 05:43-06:23, 08:30-09:38
