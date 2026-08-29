# Measure Agent Interface Efficiency With Tokens Per Successful Outcome

Summary: The fuel efficiency of an agent-facing tool interface should be measured as tokens per successful outcome — token cost conditioned on the agent actually completing the user journey — and compared within a task class rather than globally, so optimization targets the interface, not just the model.

Use when:
- Deciding which tools, descriptions, or output formats to optimize next on an MCP server or agent interface.
- Replacing gut-driven "this tool feels heavy" decisions with a measurable efficiency signal.
- Reviewing an interface whose tools fit the context window but still take many turns to finish a task.

Details:
- Treat the agent as a separate user class with its own non-functional requirements (efficiency, discoverability, security, stability); the interface, not just the model, has a measurable cost. (Chrome DevTools, 05:25-06:05, 21:32-21:50)
- The metric combines two axes: effectiveness (did the agent complete the entire user journey / is the functional intent fulfilled, yes/no) and efficiency (token cost, tool calls, duration). (08:18-08:45)
- It is deliberately "tokens per **successful** outcome," not "tokens per outcome": fuel economy is worthless if the agent can't reach the destination, so always measure effectiveness alongside cost — a cheap run that guesses or fails is not efficient. (08:45-09:03)
- Do not compare globally. Token usage differs enormously by user journey / task class — web scraping is relatively cheap, while debugging why a responsive layout breaks is intricate and uses more tokens, and that's fine — so compare within a journey. (09:10-10:00)
- Operationalize with a per-use-case view (e.g. a bar per tool or journey where shorter bars = less effective for that case); the short bars are where to focus optimization next. Even an imperfect measurement beats gut-driven decisions because it enables data-informed ones. (10:02-11:03)
- This is the design-time counterpart to model-comparison loop metrics: where loop evals rank models by correctness + cost + latency + steps, tokens per successful outcome ranks the *interface* the model is calling, per journey.
- **Two moves from one MCP server that improve both terms of the ratio at once.** Replacing generated markup with a pointer to the consumer's component cuts tokens and raises output quality together, because the referenced component is the accessible, internationalized one. Separately, Figma moved server usage guidance out of error responses and into resources, because with errors "the agent would have to call uh wasting inference and sort of reasoning to sort of figure out what is actually going wrong" — reactive discovery is billed in round trips, and the same information placed where the agent already looks is billed once. Neither change is quantified in the talk. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 08:12-08:37, 09:28-09:47)
- **The largest reported saving came from moving the artifact, not from compressing it.** Burns's bundled-docs change reports "almost 50% token saving" against the baseline of the agent searching the web — and the tokens removed are almost entirely the retrieval subplot (decide to search, choose a tool, fetch, parse HTML), not the documentation itself. When optimizing an interface's ratio, audit what the agent spends *getting to* your content before you rewrite the content. Caveat for this page's own metric: the figure has no effectiveness term attached, so it is tokens-per-outcome rather than tokens-per-*successful*-outcome. See [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md). ([Burns](../sources/20260826_V_5bn4q-vAI.md), 11:16-11:45)

- **A worked instance where the denominator is doing the work.** Šteimantas' arithmetic — ten pages fetched, three valid, all ten sent to the model, "we waste 70% of the tokens" — is exactly what this page's ratio is built to expose, and it is invisible to a tokens-per-*outcome* measure because the outcome is fine. The agent answers, correctly, from the three real pages; the seven blocked ones are billed as input and contribute nothing. Two lessons for anyone instrumenting this metric. The cheapest improvement was not compression of the payload but a validity filter in front of it — "the problem is not the compression. The problem is that the content is not valid" — which is the retrieval-layer analogue of Burns' finding that the largest saving came from moving the artifact rather than shrinking it. And the effectiveness term needs a coverage component here, since the blocked fetches also shrink the choice set the agent decides from: a run that succeeds on a truncated sample scores as a success. See [Validate Retrieved Content Before Spending Tokens on It](validate-retrieved-content-before-spending-tokens-on-it.md). Caveat: the 70% is arithmetic over a hypothetical, not a measured workload. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 08:39-10:29)

- **The clearest demonstration of why the numerator alone is unusable comes from the cost-control side.** Chawla and Koul benchmark a spend governor and refuse to report savings on their own: simple throttling "is going to kill your agent runs no matter what," so they publish average spend down "almost 78%" beside completion up "from 67% to roughly 96%." That is this page's ratio with the denominator made explicit as a competing arm rather than a divisor — and it generalizes the discipline past interface design to any intervention that is allowed to abandon work. Their own gap is instructive too: the steering action injects "make sure that the LM outputs are more succinct," which changes what a completed run produces, and completion is a binary that a thinner answer still satisfies. Even a tokens-per-*successful*-outcome measure needs its success predicate to be sensitive to quality, not just to finishing. See [A Cost Control Must Report Completion Rate or It Is Just Throttling](a-cost-control-must-report-completion-rate-or-it-is-just-throttling.md). ([FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 18:17-18:39, 19:00-19:26)
- **A fleet-scale efficiency number that is missing exactly the denominator this page argues for.** Uber reports that four successive interface changes to the same tool catalog — direct MCP, a single discovery server, a CLI projection, and generated code for the top consumers — "saved more than 40% fleetwide savings" across 1,000-plus tools ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 05:06-05:41). It is the largest interface-efficiency result the wiki records, and it is uninterpretable in the terms this page sets out: raw token reduction with no success rate attached, no per-stage split, no task class, and no window. A 40% token cut that also cut completion rates would look identical in that figure. The practical reading is that the *direction* is strongly supported — interface shape is a large lever — while the magnitude is not something another team can plan against without re-measuring per successful outcome.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md)
- [A Cost Control Must Report Completion Rate or It Is Just Throttling](a-cost-control-must-report-completion-rate-or-it-is-just-throttling.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)
- [Turn Tool Errors Into Agent Self-Healing Recovery](turn-tool-errors-into-agent-self-healing-recovery.md)
- [Return a Pointer to the Reader's Own Component Instead of a Faithful Copy](return-a-pointer-to-the-readers-own-component-instead-of-a-copy.md)
- [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)
- [Serve Markdown Through Three Redundant Paths](serve-markdown-through-three-redundant-paths.md)
- [Score Agent-Readiness Against a Moving Baseline](score-agent-readiness-against-a-moving-baseline.md)
- [Validate Retrieved Content Before Spending Tokens on It](validate-retrieved-content-before-spending-tokens-on-it.md)
- [Routing Savings Compound Across an Agent Session](routing-savings-compound-across-an-agent-session.md)
- [Stage the MCP Token Tax Down: Direct, Omni, CLI, Then Code Mode](stage-the-mcp-token-tax-down-direct-omni-cli-then-code-mode.md)

Sources:
- [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](../sources/20260605__B4Pv9ttFgY.md), 05:25-11:03, 21:32-22:15
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 08:12-08:37, 09:28-09:47
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 11:16-11:45
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 08:39-10:29
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 18:17-18:39, 19:00-19:26
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 05:06-05:41
