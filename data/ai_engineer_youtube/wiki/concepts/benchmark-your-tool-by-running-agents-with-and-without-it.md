# Benchmark Your Own Tool by Running Agents With and Without It

Summary: The way to find out whether your MCP server or API actually helps an agent is to build a task set representative of the work your users do, run agents through it in both conditions, and then read the traces — not to check that the tool returns correct results. Sourcegraph built CodeScaleBench this way: hundreds of software-lifecycle tasks, agents run with and without the code-navigation tool, thousands of traces retained as the fix list.

Use when:
- You ship an agent-facing surface (MCP server, CLI, API) and cannot say what it changes about an agent's behavior.
- Deciding what evidence a prospective buyer should be given about a tool's value.
- Choosing between "does the tool work" tests and "does the tool help" evaluation.

Details:
- **The construction.** "One of my first projects when I… became an agent advocate was to build a benchmark called CodeScaleBench. And so I developed hundreds of tasks that were reflective of the software development life cycle. And I basically unleashed these agents with and without our product tooling." The product under test is Sourcegraph's code-navigation MCP tool. ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 05:36-06:17)
- **The A/B is the whole design.** The without-tool arm is a control in the same sense as a do-nothing baseline in a context-management bake-off: without it, a passing run only shows the agent completed the task, not that your surface contributed. See [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md) for the same discipline applied to context techniques, where the control beat every technique.
- **Two questions, and the second is the one that pays.** The stated purpose is "how is our tool helping the agent do the work that it's going to be doing" *and* "when it isn't working well, why isn't it working well? So that we can then go in and actually fix that." A pass/fail rate answers only the first. The repair work comes from the traces. (06:06-06:33)
- **The traces are the deliverable, not the score.** "I have thousands and thousands of these traces… now we have these amazing logs of data for like these really tight feedback loops where you can see exactly where it's breaking down and then go in and fix it." The one narrated example — a parameter name the model guessed from training priors — is a tool-description fix that no aggregate metric would have surfaced. See [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md). (06:17-07:20)
- **Task set shape: representative of the lifecycle, not of the tool.** The tasks were written to reflect the software development lifecycle, so the without-tool arm is a plausible baseline workflow rather than a strawman that the tool trivially wins. A task set built from your tool's capabilities guarantees a favorable result and teaches nothing.
- **You can run this population at a scale you cannot run on humans.** The same source names the general version: "you can basically spin up like thousands of these agents to perform experiments on them and experiments that you can't really do as easily with the developers who don't want to maybe talk to you that much." Agent-user research is cheap in the way human-user research is not, which changes the economics of instrumenting an agent surface. (16:08-16:20)
- **The output metrics buyers want are operational, not just correctness.** "How many tokens is the agent dealing with to work with your tool? And how fast is it?" — so the benchmark should report per-task token consumption and latency in both arms alongside completion, which is the same metric set as [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md). (07:23-07:38)
- **Limit.** No aggregate with-versus-without result is reported in the talk — only that the benchmark and traces exist, plus one narrated trace. The pattern is well specified; the effect size for this particular tool is not. ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), Provenance and Limits)
- **The cheapest version of this design measures token cost rather than task success.** Burns compares the same agents working on his library with and without bundled docs in `node_modules`, and reports "almost 50% token saving" against the alternative of searching the web for the same information, observed "between many different models." No task-success axis is reported, which is the weakness — a with/without comparison on cost alone cannot distinguish a cheaper run from a shallower one. The complementary standing check is an external agent-readiness grader, with the caveat that its rubric moves under you. See [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md) and [Score Agent-Readiness Against a Moving Baseline](score-agent-readiness-against-a-moving-baseline.md). ([Burns](../sources/20260826_V_5bn4q-vAI.md), 11:16-11:45, 12:48-13:33)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Trace agent tool use to improve prompts and tools](trace-agent-tool-use-to-improve-prompts-and-tools.md)
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)
- [Evaluate Retrieval and MCP Layers by Task Value](evaluate-retrieval-and-mcp-layers-by-task-value.md)
- [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md)
- [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)
- [Score Agent-Readiness Against a Moving Baseline](score-agent-readiness-against-a-moving-baseline.md)

Sources:
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 05:36-07:38, 16:08-16:20
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 11:16-11:45, 12:48-13:33
