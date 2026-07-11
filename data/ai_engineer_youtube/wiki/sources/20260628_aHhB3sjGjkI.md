# Agents Building Agents

Source: [Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI)
Uploaded: 2026-06-28
Transcript: `raw/20260628_aHhB3sjGjkI/aHhB3sjGjkI.en-orig.vtt`

## Summary

Alfonso Graziano (tech lead at Nearform, a services company; O'Reilly author of *Learning AI Native Software Engineering*) presents a production-minded, repeatable workflow for using AI to build AI — a coding agent as the *builder* that writes and changes a *product agent's* codebase — and targets two failure classes: bad performance on evals and bad performance on live data. The eval backbone is a **golden dataset** (input → expected output, where expected output is often "call this tool / with this parameter / in this chain") treated as a test suite for a non-deterministic system, plus **scorers** that produce an accuracy number for baseline/regression tracking. For the evals failure class he built **AutoAgent**: inspired by Karpathy's "auto research" loop (a coding agent that mutates ML code/hyperparameters to improve a model), it points a coding agent (Claude Code, but multiple work) at the product agent, and hill-climbs — each iteration is a fresh git branch testing one hypothesis (one failure class), keeping the branch on eval improvement and rolling back on regression, with a global cross-run memory file, per-iteration `reports.md`, and a full readable/steerable change log of hypotheses. A hard human-in-the-loop guardrail forbids the coding agent from editing the golden dataset/scorers just to pass. Reported lift without cheating: a tool-less Mastra "math agent" 18%→83% in ~10 iterations, a real production agent 67%→86% in ~10 iterations (found edge cases, improved system prompt + tool descriptions, fixed tool logic), and +10% on an already-human-optimized agent. For the live-data failure class he runs a second loop: collect production traces (interaction, tool usage, latency, tokens) plus user thumbs/comments or SME trace annotations, then an agent workflow packaged as a **skill** clusters the failures, does an adversarial review + root-cause analysis (the coding agent has code + trace access), and emits a markdown report (clusters, trace IDs, root causes, fixes). Humans triage/validate with SMEs (fix-now/later/never, discard false positives/intended behavior), and — crucially — every validated failure mode is folded back into the golden dataset and scorers so it becomes a permanent regression test ("self-healing evals"); cadence ~once per sprint. Both loops are enabled by **Harness Engineering**: building the environment around the coding agent (spec-driven env where each failure mode becomes a spec, quality gates like lint/unit tests/evals/LLM code review, context engineering, observability) so it can change code, validate its own changes, and propose new ones reliably.

## Extracted Concepts

- [Optimize an Agent With a Branch-per-Hypothesis Coding-Agent Loop](../concepts/optimize-an-agent-with-a-branch-per-hypothesis-coding-agent-loop.md) - AutoAgent's git-branch-per-hypothesis eval hill-climb with rollback, cross-run memory, change log, and an anti-gaming guardrail.
- [Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](../concepts/promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md) - the live-data loop that clusters/roots-causes/triages production traces and folds validated failures back into the eval suite as regression tests.

## Topic Links

- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

## Notes

- Framing: building an agent for a real team is a systems problem, not a prompt problem; AI agents bring non-determinism, latency, cost, and hallucinations, and since an agent is just one type of software, "we are using AI to build AI." 00:38-01:25
- Agent from first principles: an LLM (the brain) inside an agentic loop, connected to tools and able to retrieve context. 02:37-02:48
- Two failure classes analyzed: (1) bad performance on evals; (2) bad performance on live data, which is wider and messier than eval data. 02:52-03:20
- Golden dataset: a file (or set) developed with subject-matter experts defining the input the system should retrieve/get and the expected output; expected output can be a value, or "call this tool / with this parameter / in this chain." 03:29-04:38
- Golden dataset = a test suite in a non-deterministic scenario; pair it with a scorer / set of scorers that run the dataset with the LLM and return an accuracy number → baseline, regression detection, iterative improvement. 04:45-05:17
- Demo agent: a simple Mastra "mad agent" (math agent) with only a couple of instructions and a model, no tools; a naive evaluator checks whether the LLM output contains the ground-truth output → 18% pass rate (only simple arithmetic answerable from weights). 05:22-06:42
- Eval failure modes: missing the right tools, wrong/incomplete system prompt, poor context retrieval (usually implemented as tools). 06:40-08:00
- Precedent — Karpathy's "auto research": a loop that updates code/hyperparameters/ML Python and shows a coding agent tweaking a deep-learning algorithm improves accuracy / lowers loss over experiments. 08:00-09:30
- AutoAgent applies the same idea to agents: a loop that runs evals, updates code, tries new system prompts, creates new tools autonomously, and rechecks whether things improved. 09:30-10:30
- Results: naive agent 18%→83% in ~10 iterations; +10% on a production agent that was already humanly optimized (the coding agent found improvements humans hadn't). 10:33-11:21
- Mechanics: coding agent (Claude Code) builds the target agent; the target agent returns eval feedback (regressions, failing evals); Claude Code can read the target agent's thinking/full traces to see what broke → self-improvement. 11:30-12:40
- Human-in-the-loop guardrail: structure the initial agent, give context on what it can/can't touch, and explicitly forbid editing the golden dataset/scorers just to make evals pass. 12:40-13:40
- Step 1: create an optimization job as a markdown file (objective, target repository, metrics, context). 13:40-14:20
- Step 2: run evals once for baseline data + a baseline report (cases, summary, what's working/not), then run the optimization loop; observed iterations: regression→roll back, then +5%, then 0%, then +12%; iteration count is a knob. 14:20-16:40
- Per-iteration: new git branch → hypothesis (one failure class) → change the agent → run eval suite → write `reports.md` → update a global memory file across all runs; continue from branch if improved, roll back to the previous branch if regressed; hypotheses are grounded in the memory + reports files. 15:36-18:00
- Output: a full change log of every improvement/regression; each hypothesis builds a report, so humans can reopen a promising-but-failed hypothesis, read what the agent tried, and steer it next time. 17:17-20:00
- Real production result: baseline 67% → 86% in ~10 iterations without cheating — improved system prompt and tool descriptions to catch more edge cases and fixed tool logic; now running in production. 18:17-18:30
- Second loop (live data): data from real users/beta testers/SMEs; simple feedback "was this response helpful?" yes/no + a note, leveraged to optimize agents. 21:00-22:00
- Live-data flow: users use the system → collect all traces → user thumbs up/down + comment (what went well/wrong + expected behavior) OR SME annotates the trace (input/output/tools called/behavior) → collect enough traces → run an agent workflow to cluster failure modes, validate with SMEs, generate + implement a fix via the coding agent, ship, and use the traces as regressions. 22:00-24:00
- Traces captured: user interaction, tool usage, response latency, tokens burned; download traces-with-feedback locally as JSON (114 traces in the demo) for cluster analysis. 24:00-26:00
- Analysis is a skill: instruct the coding agent to read the JSON, run clustering, do an adversarial review, and — with access to the agent's actual code + per-trace detail — do root-cause analysis and propose improvements; output is a full markdown report (positive/negative feedback, negative rate, clusters with trace IDs, root causes, fixes). Example cluster: markdown formatting failure — URLs not hyperlinked. 23:34-25:19
- Triage + validate with SMEs → prioritize fix-now/later/never → fix with the agent (give it the failure mode + traces) or discard (false positive, intended behavior, or unhelpful feedback); human judgment required. 25:19-26:15
- Validated failure modes become part of the golden dataset and the eval suite is updated to spot those regressions, so a reintroduced failure is caught fast. 26:15-26:32
- Cadence: once per sprint is reasonable; with 10,000+ feedback traces, one report is too much → split into several. 26:40-27:30
- A coding agent, given enough context and the ability to test against regression tests, has fixed an entire suite of issues with one prompt; complex clusters were handed to AutoAgent to build draft PRs. 27:00-27:51
- Harness Engineering enables both loops — building the environment around the coding agent (constraints, tasks, feedback loop, governance) so it changes code, validates its own changes, and proposes new changes reliably. 27:51-28:40
- Harness Engineering components: spec-driven environment (each failure mode becomes a spec for expected behavior, then implemented), quality gates (linting, unit tests, evals, LLM code review), context engineering, and observability (so blind-in-production is avoided and the coding agent can fix found bugs). 28:40-29:30
