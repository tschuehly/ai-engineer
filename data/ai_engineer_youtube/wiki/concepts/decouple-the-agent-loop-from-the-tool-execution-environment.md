# Decouple the Agent Loop From the Tool Execution Environment

Summary: Run the "brain" (model reasoning and the agent loop) and the "hands" (the container tools execute in) as separately-lifecycled services rather than one process. Anthropic shipped the coupled version first and hit three distinct problems with it — first token waited on container boot, either half dying killed the whole run, and a container was allocated even for turns that never called a tool. The split is usually argued on security grounds; these three are independent reasons that hold even when you trust the code.

Use when:
- Designing a hosted agent runtime and deciding what a "session" is made of.
- Diagnosing time-to-first-token that scales with sandbox provisioning rather than prompt length.
- A single infrastructure failure in the tool environment is taking down whole agent runs.

Details:
- **The coupled starting point and its two named failures.** The original managed-agent design put the agent loop and the container in one box. "The container was blocking the agent being able to start its model reasoning" — the model could not emit a token until the sandbox was up, even for a turn that would never touch it. And blast radius was the whole unit: "if one part of this component went down, the entire box of the agent would go down." ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 11:16-12:00)
- **What the split buys, in three parts.** (1) *Latency*: setup runs in parallel with reasoning, or is skipped entirely for turns with no tool call. (2) *On-demand allocation*: the container is created when a tool actually needs it rather than at session start. (3) *Independent recovery*, below. (12:00-12:19, 23:15-24:12)
- **Failure recovery becomes directional rather than fatal.** If the sandbox dies, "the brain could just spin up a new sandbox and retry and then continue as it left off" — the hands are replaceable because they hold no irreplaceable state. If the brain dies, it resumes from the durable session log. Both recoveries depend on state living somewhere other than the failed component, which is why this page and [keeping the session log separate from the context window](keep-the-session-log-separate-from-the-context-window.md) are one design rather than two. (12:25-12:52)
- **The reported latency effect.** "60% faster time to first token for P50" and "over 90% improvements in latency for time to first token in P95 use cases." The P95 gap being far larger than P50 is the internally consistent part and the part worth reasoning from: it is what you would expect if the tail was dominated by cold container starts, which the split removes from the critical path entirely rather than shortening. (23:15-24:12)
- **How this differs from the security argument for the same split.** [Separating agent harnesses from generated-code execution](separate-agent-harnesses-from-generated-code-execution.md) reaches the identical architecture from a different premise — the generated code is untrusted, so it must not run where the harness runs. That argument justifies isolation but says nothing about lifecycle: a security-motivated split can still boot the sandbox synchronously at session start and still die with it. The reasons here are about *when* the container exists and *what it takes down*, so they add requirements the security argument does not imply. Both arguments landing on the same boundary is a reason to trust the boundary.
- **The cost the talk does not price.** Decoupling means the loop and the container communicate over a network, so every tool call now pays a round trip and can fail in ways an in-process call could not (partial results, timeouts, a sandbox that is alive but unreachable). The talk reports the latency win at first token and is silent about per-tool-call latency thereafter; on a run with a hundred tool calls, that is where the accounting would have to be done.
- Provenance: an Anthropic vendor talk for Claude managed agents. The percentages are internal and unmethodized — no workload, no sample size, no absolute values, and no description of the coupled baseline beyond "the coupled design," so it is not knowable whether the comparison is against a tuned implementation or a naive one. The architectural reasoning stands on its own; the numbers should be read as directional.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Separate Agent Harnesses From Generated-Code Execution](separate-agent-harnesses-from-generated-code-execution.md)
- [Model a Managed Agent as Agent, Environment, and Session](model-a-managed-agent-as-agent-environment-session.md)
- [Keep the Session Log Separate From the Context Window](keep-the-session-log-separate-from-the-context-window.md)
- [Decrypt Agent Credentials Only at Tool Execution Time](decrypt-agent-credentials-only-at-tool-execution-time.md)
- [Do Not Roll Your Own Agent Code Sandbox](do-not-roll-your-own-agent-code-sandbox.md)
- [Agent-Native Runtimes Provide Fast API-Controlled Sandboxes](agent-native-runtimes-provide-fast-api-controlled-sandboxes.md)

Sources:
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 11:16-12:52, 23:15-24:12
