# Agent swarms create reusable KV-cache working sets

Summary: Agent and subagent systems often resend large shared prompt, tool-call, and tool-response regions; cache planning should model these repeated token regions as a working set rather than treating each request as unrelated text.

Use when:
- Estimating context cost and latency for orchestrator-plus-subagent coding systems.
- Debugging why long-running agent sessions hit summarization, rate-limit, or latency cliffs.

Details:
- In agentic coding data, direct user input can be a small part of the prompt, while system text, tool calls, and tool responses dominate the repeated token volume (07:04-07:48).
- Agent loops have a cadence mismatch: tool-using agents may issue requests every 10-15 seconds, while human responses may take minutes or hours, so cache policy has to cover both fast inner loops and slower human pauses (07:48-08:17).
- Multi-agent systems add orchestrators and subagents whose contexts may be short-lived or persistent; targeting context to subtasks can improve task focus, but it also increases total context that the platform may need to cache (08:18-09:14).
- Summarization after context-window high-water marks can lose fidelity, so extending the useful cache working set can preserve more original context before compaction is required (06:20-06:55).
- **Numbers for the working set, from production traces rather than reasoning about prompt structure.** Red Hat's traces of SWE-bench-style workloads and real Claude Code sessions report turn counts running "from a few turns all the way to 3,000 turns," cache hit rates "oftentimes well exceeding 90%" because agents reuse the system prompt and tool definitions, and an input-to-output token ratio "oftentimes over a 100 ratio and even higher." The 100:1 figure is the sharpest addition to this page's argument: the repeated region is not merely large relative to the user's input, it is roughly two orders of magnitude larger than everything the model generates. They also note that subagent fan-out "further complicates scheduling" — the multi-agent structure this page describes is visible to the serving layer as a scheduling problem, not only as extra tokens. ([Fama](../sources/20260827_YXowceUKYJI.md), 03:16-04:34)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)

Related concepts:
- [KV-cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Context window editing clears stale tool results](context-window-editing-clears-stale-tool-results.md)
- [Replay Agentic Traces, Because Steady-State Benchmarks Hide the Workload](replay-agentic-traces-because-steady-state-benchmarks-hide-the-workload.md)

Sources:
- [Context Platform Engineering to Reduce Token Anxiety - Val Bercovici, WEKA](../sources/20251124_NTBX-wxUhHs.md), 06:20-09:14
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 03:16-04:34
