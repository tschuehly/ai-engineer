# Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model

Summary: When a browser agent fails on ordinary multi-step workflows, the bottleneck is usually the runtime interface — what the model sees, what it can do, and what it learns from — not the model. Rebuilding those three levers can take the *same or a cheaper* model from confusion to correct execution on hostile pages.

Use when:
- A browser or computer-use agent stalls, loops, or is slow on tasks that look simple, and the instinct is to swap in a bigger/smarter model.
- Designing or debugging a browser-agent runtime (observation representation, action layer, feedback loop).

Details:
- Thesis, stated directly: "models are pretty smart, but it's the infra around them that sucks." Most browser-agent progress over the past year has been model upgrades (better vision, longer context, smarter planning), yet agents still fail on basic workflows because the interface to the browser is the limiting factor. (00:56-01:09)
- Three levers, each a design surface distinct from the weights:
  - **What it sees** — a compact whole-page representation (markdown) instead of a raw DOM dump or a single screenshot, so the model can see the entire page in few tokens. See [Give Browser Agents a Compact Whole-Page Representation](give-browser-agents-a-compact-whole-page-representation.md). (01:09-01:26, 03:33-03:50)
  - **What it can do** — fast actions with stable handles instead of one click per model call, so the agent can plan and execute long sequences rather than round-tripping the model per interaction. (01:09-01:18)
  - **What it learns from** — step-by-step delta feedback (what popped up, what is gone, that a click did not register) from tracking the full end-to-end page, instead of only a pass/fail at the end. (03:50-04:08)
- Evidence the split is real: a baseline agent spent 10-20 seconds just to click a Start button on a 30-step challenge; Claude with default computer-use took ~2 minutes and got stuck screenshot-scroll-screenshot downloading an Aadhaar document and could not pick a date on an unfamiliar booking site — the same tasks completed quickly on the rebuilt runtime using a *cheaper* model. (00:30-02:41)
- This complements the general principle that observation and action spaces are explicit design choices ([Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)) and the parallel finding for tool-using agents that failures are often interface/discipline, not raw capability ([Fix Tool Discipline Before Reaching for a Bigger Model](fix-tool-discipline-before-reaching-for-a-bigger-model.md)).
- Contrast with the site-side approach: WebMCP and agent-readable web surfaces ask *sites* to publish clean action surfaces; this is the *agent-side* runtime that works on unmodified, hostile pages when no such surface exists.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Give Browser Agents a Compact Whole-Page Representation](give-browser-agents-a-compact-whole-page-representation.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)
- [Fix Tool Discipline Before Reaching for a Bigger Model](fix-tool-discipline-before-reaching-for-a-bigger-model.md)
- [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)

Sources:
- [Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, ARK](../sources/20260628_JnubYCYunk8.md), 00:30-04:23
