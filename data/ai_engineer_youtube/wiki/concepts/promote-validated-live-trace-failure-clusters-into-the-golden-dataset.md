# Promote Validated Live-Trace Failure Clusters Into the Golden Dataset

Summary: Close the live-data feedback loop by mining production traces (with user thumbs and subject-matter-expert annotations) into clustered failure modes, root-causing and triaging each with an SME, and then folding every *validated* cluster back into the golden dataset and scorers — so a fixed failure becomes a permanent regression test ("self-healing evals") rather than a one-off patch.

Use when:
- Real users/beta testers/SMEs are exercising an agent and its live-data behavior is wider and messier than your eval set.
- You have accumulated traces + feedback and need a repeatable way to turn them into durable fixes and eval coverage.
- You want production failures to stop recurring instead of being re-discovered next sprint.

Details:
- Collect the raw material: every production run captures a **trace** (user interaction, tool usage, latency, tokens burned), and users give a thumbs up/down plus a comment on what went well/wrong and the expected behavior; when a real-user signal is missing, an **SME annotates the trace** — inspecting input, output, tools called, and agent behavior, and recording how it performed vs how it should have. 21:00-26:00
- When enough traces accumulate, download them locally (e.g. 114 traces as JSON) and run an **agent workflow packaged as a skill** that instructs the coding agent to read the JSON, cluster the failures (focusing on negative feedback), do an **adversarial review** of the clusters, and — because the coding agent has access to the agent's actual code plus per-trace detail — trace each cluster down to a **root cause** and propose fixes. 22:00-24:00
- Output is a full markdown report: positive/negative feedback, negative rate, each failure cluster (with linked trace IDs, the user feedback, possible root causes, and a suggested fix). Example cluster: "markdown formatting failure — URLs not hyperlinked, formatting inconsistencies." 24:00-25:19
- The report is not the end: **triage and validate with SMEs**, then prioritize fix-now / fix-later / don't-fix. Fix with the coding agent (hand it the failure mode + traces) or **discard** — a cluster can be a false positive, an intended behavior, or feedback that isn't useful right now, so human judgment is required. 25:19-26:15
- The durable move: every validated failure mode **becomes part of the golden dataset and the eval suite is updated to catch it**, so if the failure is ever reintroduced later it's spotted fast (it now lives in the golden dataset and scorers) — the traces double as regression tests for the fix. 26:15-26:32
- Cadence is use-case dependent: generating the report ~once per sprint is reasonable; with 10,000+ feedback traces, one report is too much, so split into several. 26:40-27:30
- Given enough context and the ability to test its changes against those regression traces, a coding agent has fixed an entire suite of issues with a single prompt; complex clusters can be handed to the [branch-per-hypothesis optimization loop](optimize-an-agent-with-a-branch-per-hypothesis-coding-agent-loop.md) to build draft PRs. 27:00-27:51

- **The promotion step is what makes this survive the standing objection to clustering.** Ben Hylak argues that clusters cannot function as issues — you do not control their boundaries, "it's very, very hard to reliably track over time," and "what you consider to be like the same issue or not is actually very, very unique to every company" ([Clusters Are Not Issues](clusters-are-not-issues.md)). This pipeline escapes all three because the cluster is not the artifact: an SME validates it, names it, and it becomes a golden-dataset entry and a scorer with a stable identity that can be re-run and trended. Stated as a rule, a cluster is a discovery output that has to be promoted into something you named before anything can be tracked against it — and the corollary is that the SME triage step is load-bearing, not administrative overhead to automate away. ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 17:03-18:08)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Optimize an Agent With a Branch-per-Hypothesis Coding-Agent Loop](optimize-an-agent-with-a-branch-per-hypothesis-coding-agent-loop.md)
- [Diagnose Agent Failures With Code-Checkable Indicators and Sampling](diagnose-agent-failures-with-code-checkable-indicators-and-sampling.md)
- [Portfolio-Allocate Eval Failures With a Triage Agent](portfolio-allocate-eval-failures-with-a-triage-agent.md)
- [Replay Production Failures Before Promoting Prompt Fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Clusters Are Not Issues](clusters-are-not-issues.md)

Sources:
- [Agents Building Agents - Alfonso Graziano, Nearform](../sources/20260628_aHhB3sjGjkI.md), 21:00-27:51
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 17:03-18:08
