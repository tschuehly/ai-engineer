# Let Deterministic Code Drive the Timed Loop and Call the Model Only for Perception

Summary: When an interaction runs against a deadline, put the whole loop in deterministic code and invoke the model only for the one step that genuinely needs eyes or judgment. A design that round-trips a model per step spends the budget on inference latency and loses to the clock, even though each individual call succeeds.

Use when:
- The environment expires, times out, or re-arms on its own schedule (challenge rounds, session tokens, live streams, market or auction windows).
- An agent is functionally correct but too slow to finish, and the instinct is to make the model faster rather than to call it less.
- Deciding which steps of an automation are model work and which are code work.

Details:
- **The two halves.** Against reCAPTCHA v2, the **solver** is "pure code, no agent, no model": it does the trusted click on the checkbox, pierces into the challenge iframe, screenshots the grid every round, and re-arms itself if a round expires — "deterministic, it's fast, and it's free." The **operator** is the agent, called in for the only step code cannot do — "look at that grid of fuzzy tiles and figure out what it is that's in it… that's vision and thinking, and that needs eyes and a brain." It names the matching tiles, hands the answer back, "and then just hangs out waiting until the next lap." ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 16:30-18:23)
- **The constraint that forces the split.** "This big bad boss is on a clock. Every round expires, and one challenge can be multiple rounds back-to-back. An agent that round-trips a model on every click and on every look burns that clock and loses. The challenge expires well before it ever finishes." The only shape that worked was "deterministic code running at machine speed with one quick AI look per round," and the result is described as repeatable and reliable rather than a lucky run. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 18:23-19:36)
- **Latency is the design driver, not capability.** Both halves of the work were within the model's reach; what the model could not do was be in the loop often enough. This is the same reason the talk argues for a shell CLI over an MCP server — measured at ~83% task success either way, but 7 turns and under a minute versus 71 round trips and 8 minutes, because MCP "hits the model on every single turn." ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 02:22-04:07, 19:14-19:36)
- **How to find the split in your own loop.** Enumerate the steps and ask which ones a program can decide from structured state. Positioning, clicking, iframe traversal, screenshotting, retry, and re-arming are all mechanical; only "which tiles contain a bus" required perception. The model's share of the loop shrinks to one call per round, and everything around it runs at machine speed.
- **Recovery belongs in the deterministic half.** The solver re-arms itself when a round expires instead of asking the model what to do about it — error handling on a timed loop is control flow, and routing it through inference costs another round trip at exactly the moment the budget is already tight. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 17:21-17:40)
- **Relation to the other "code above the model" patterns.** [Run Must-Not-Fail Decisions in a Code Layer Above the Model](run-must-not-fail-decisions-in-code-above-the-model.md) moves decisions into code because the model must not get a vote on irreversible calls; this pattern moves them into code because the model cannot afford a turn. Same structure, different forcing function — safety versus deadline — and they compose.
- **Precondition.** The split only pays off after the path is known: explore by hand, climb only as far as the page forces, and write the working sequence down as code before wrapping a model around it. See [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md). ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 08:01-08:26)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md)
- [Run Must-Not-Fail Decisions in a Code Layer Above the Model](run-must-not-fail-decisions-in-code-above-the-model.md)
- [Agent Connectivity Stack Combines Skills, MCP, CLIs, and Computer Use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)
- [Verify an Action Through a Different Channel Than the One That Acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md)

Sources:
- [The Dark Arts of Web Automation — Corey Gallon, Rexmore](../sources/20260814_26RtyAm9y_Q.md), 02:22-04:07, 08:01-08:26, 16:30-19:36
