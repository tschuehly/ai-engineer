# Routing Savings Compound Across an Agent Session

Summary: Per-request pricing understates model routing, because one user prompt to a coding agent becomes many heterogeneous model calls — planning, edits, tests, docs, tool follow-ups — and only some of them need the frontier tier. The measurable unit is the session, where the gap widens with every turn: 8 cents against 25 after one feature request, 14 against 44 after three.

Use when:
- Estimating what a router or a cheaper default would actually save on an agentic workload.
- A routing evaluation is being run on single-shot prompts and the result looks marginal.
- Explaining why an always-premium coding agent's bill grows faster than its usage.
- Deciding what to instrument in an agent harness to make model spend legible.

Details:
- **The measurement, taken twice on the same running session.** Two OpenCode terminals, one configured with Claude Opus and one pointed at a per-task router, both given "build me a spinning wheel app." After the feature: "the software engineering router has only spent 8 cents on the session while Opus directly has spent 25 cents. So we have about a 3x in cost and very very similar quality so far." After two further prompts (unit tests, then a README): "the total session cost for the router was 14 while the total session cost for Opus was 44." ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 09:36-13:25)
- **Why the gap compounds rather than staying flat.** The structural difference is stated plainly: "on the left we'll see every single request that I write goes to the same premium model. Cost and latency is going to stay high for pretty much every single task. On the right the router is selecting models based on the task" (10:47-11:18). Each additional user prompt adds another burst of internal calls whose task mix is different from the last, so the always-premium arm pays its worst-case rate on every one while the routed arm pays the tier each call needs. The saving is not a per-call discount, it is the *fraction of calls that did not need the frontier tier*, multiplied by the length of the session.
- **The consequence for evaluation design.** A routing eval on isolated prompts measures the discount; a routing eval on a session measures the policy. This is the routing instance of the pressure named in [Agentic Workloads Turn Token Price Into Unit-Economics Pressure](agentic-workloads-turn-token-price-into-unit-economics-pressure.md) — one user action triggering many model calls is exactly what makes the compounding real — and it argues for session totals in the report alongside per-request numbers, as in [Evaluate a Router Against the Always-Frontier Arm](evaluate-a-router-against-the-always-frontier-arm.md).
- **The instrumentation that makes it visible.** The demo runs on a custom harness panel showing "token usage in real time, which models are being selected, what tasks those map to, and the cost accumulating live" (10:04-10:16). Live cumulative session cost, broken down by selected model and matched task, is the view that turns routing from an assertion into something an engineer can watch; a per-request log does not surface the compounding at all.
- **The cheaper version of the same finding.** Coinbase's blanket-default approach reaches the same place with no router: defaulting an internal gateway to GLM and Kimi "cut their AI spend by nearly half while their token usage continues to grow" ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 10:27-10:55). Both observations are about aggregate spend over a long stream of agentic calls rather than about any single request's price — which suggests the compounding, not the per-call tier gap, is where most of the money is.
- **Caveats.** These are two readings from one live demo of one small app, not a distribution. The control arm is impure — "OpenCode sometimes routes to haiku by itself" (10:37-10:47) — which pushes the reported ratio *down*, not up, so the direction survives but the 3x does not. Quality across the session is assessed by inspection on stage. Nothing is said about a session where the routing goes wrong: a mis-matched task that sends a hard edit to a cheap model can cost more than it saves once the agent spends extra turns repairing the result, and that failure mode is exactly the one a session-level metric would catch and a per-request metric would not.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Evaluate a Router Against the Always-Frontier Arm](evaluate-a-router-against-the-always-frontier-arm.md)
- [Give Each Task a Model Pool With an Explicit Selection Policy](give-each-task-a-model-pool-with-an-explicit-selection-policy.md)
- [Agentic Workloads Turn Token Price Into Unit-Economics Pressure](agentic-workloads-turn-token-price-into-unit-economics-pressure.md)
- [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md)
- [Treat Token Spend as a Strategic Axis](treat-token-spend-as-a-strategic-axis.md)
- [Measure Agent Interface Efficiency With Tokens per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)

Sources:
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 09:36-13:25
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 10:27-10:55
