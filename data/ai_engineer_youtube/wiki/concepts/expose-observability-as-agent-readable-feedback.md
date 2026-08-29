# Expose Observability As Agent-Readable Feedback

Summary: Logs, metrics, traces, and deployment health signals should be available through machine-friendly surfaces so agents can verify outcomes and iterate without relying on human dashboards. Taken further, the observability platform itself can ship an agent that reads its own telemetry and drives the eval/improvement loop.

Use when:
- Designing observability for platforms or applications that coding agents need to debug.
- Defining success criteria for agent-executed deployment or provisioning work.
- Deciding how a coding agent (Claude Code, Codex) should drive an observability/eval platform instead of a human clicking dashboards.

Details:
- The talk emphasizes that agents need precise instructions and explicit success criteria, including how they know they have completed the task. (11:14-11:32)
- Humans may verify deployments by reading graphical observability dashboards, but agents are unlikely to use those interfaces reliably as their primary feedback channel. (11:32-12:03)
- Platform teams should expose logs, metrics, traces, and other verification signals through APIs, CLIs, MCP servers, or similar machine-friendly surfaces so the agent can close the loop. (12:03-12:20)
- Platform-readiness changes should be measured before and after with delivery, reliability, support-load, or developer-experience metrics rather than assumed from AI adoption alone. (17:12-19:19)
- Arize generalizes this from "agents verify their own work" to "agents operate the observability platform": because most people do not want to live in dashboards or buttons, it exposes all primitives (observability, evals, experiments) via a CLI plus a set of tools and skills so a coding agent can run them programmatically. (Arize, 13:11-13:53)
- The platform also ships its own agent ("Alex") with access to all the trace data and hooks; an external coding agent or a user can ask "do you see any issues with my application?" and Alex plans and runs tasks, surfacing high latency and detected errors. (Arize, 13:53-15:23)
- The end goal is to "automate you out of" the whole flywheel: the AI should already have context of the traces, create evals on the fly, and know when something changed and a new eval is needed — "you shouldn't even have to choose your evals." (Arize, 14:33-15:12)

- Browser agents give the pattern a concrete signal list. Because the agent acts on someone else's site, the telemetry that matters is what a human debugger would want: "you need screen recordings, logs, network activity. And you need to feed that back into your agent so it can self-improve. Every agent you run should get better every single time." Browserbase's "Auto Browse" (as spoken) is described as this loop — "how is my agent able to improve itself over multiple loops" with observability data as the input. The precondition is that the substrate is pinned first, or the recordings capture variance the agent cannot act on ([Hold the Browser Environment Constant Across Runs](hold-the-browser-environment-constant-across-runs.md)). ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 14:35-15:10)

- LangChain runs the same pattern on its own tracing product and adds the part of the loop that stays human-facing. Traces are centralized into a tracing project — per agent or across all agents — and then "we send agents to read traces from other agents," with the mining product reading the corpus, finding issues, "agentically searching over it," and preparing datasets. But one of the three named outputs is content for people, not machines: "humans are still in the loop. Like, I need to know that customers are happy… I just don't have the bandwidth to read a bunch of traces," which matters most "in like high-trust domains like legal and medical. Like, some human needs to review this, but they can't read it all." Agent-readable observability and human-readable summarization are two outputs of the same mining pass, not competing designs. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 04:40-05:09, 10:39-11:08, 12:15-12:46)

- **Machine-readable telemetry is the floor, not the goal.** Resolve AI accepts the premise — its agents read dashboards, telemetry, and change events, and everything it does is reachable "through kind of MCP servers" so another harness can "pull production context a bit more efficiently" — and then argues the remaining gap is interpretive: "the execution is can load the dashboard. It's the production context that's going to say, this feels wrong." Exposing signals is what lets an agent look; it is not what tells it whether the reading is important. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 10:37-11:12, 23:28-23:58)
- **Coverage is the precondition, and it has to be bought before the incident.** Whatever an agent can read is bounded by what was instrumented, and Krieger's rule for that boundary is deliberately over-inclusive: "pre-measure everything that you think you might even remotely need," because the alternative is a number with no history and therefore no interpretation. The same argument extends the surface an agent can act on: first-class flags, ramps, and dynamic config "changed in a matter of seconds" are the knobs a remediation has to reach for, and "having that kind of runtime configuration is super key" for AI systems specifically because so many of their tradeoffs are settings. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 07:08-07:52)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Choose Eval Scope Across Span, Multispan, Trajectory, and Session](choose-eval-scope-across-span-multispan-trajectory-and-session.md)
- [Catalog Eval Signal Sources Across Judge, Human, Golden, Deterministic, and Business](catalog-eval-signal-sources-judge-human-golden-deterministic-business.md)
- [Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)
- [Separate Execution From the Production Context That Judges It](separate-execution-from-the-production-context-that-judges-it.md)
- [Pre-Measure Everything and Build Runtime Knobs Before You Need Them](pre-measure-everything-and-build-runtime-knobs-before-you-need-them.md)

Sources:
- [Platforms for Humans and Machines: Engineering for the Age of Agents - Juan Herreros Elorza](../sources/20260408_cCRO3ChaYhM.md), 11:14-12:20, 17:12-19:19
- [LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](../sources/20260607_JsCCrBF7F1g.md), 13:11-15:23
- [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../sources/20260814_GqoNrUz8hEU.md), 14:35-15:10
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 04:40-05:09, 10:39-11:08, 12:15-12:46
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 10:37-11:12, 23:28-23:58
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 07:08-07:52
