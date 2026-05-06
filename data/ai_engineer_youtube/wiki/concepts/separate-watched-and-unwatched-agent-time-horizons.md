# Separate Watched and Unwatched Agent Time Horizons

Summary: Long-task capability should distinguish unmonitored autonomy from work done under close model or human supervision. Monitoring can reduce effective risky autonomy even if the underlying model can execute longer tasks.

Use when:
- Evaluating agent autonomy, capability risk, or safety-monitoring designs.
- Comparing long-task benchmark performance with production deployment constraints.

Details:
- The source proposes replacing a single time-horizon curve with separate curves for agents that are "watched very closely" and agents that are not, because supervision changes the effective capability profile. (48:32-49:02)
- Monitoring examples include other AIs inspecting transcripts of AI work, looking for suspicious behavior, and escalating to humans or applying safety controls. (49:08-49:47)
- The discussion conjectures that close monitoring could reduce effective autonomy by an order of magnitude or two for high-risk capability-relevant tasks, while still allowing longer benign work under appropriate controls. (49:29-50:39)
- This framing complements ordinary evals: teams should measure not only whether an agent can complete a long task, but whether it can do so without monitors, resource-use controls, external-service checks, or human escalation. (57:24-58:24)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)
- [LLM guardrails need checkpoints at every untrusted boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)

Sources:
- [How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR](../sources/20260119_k1t2xyWMUdY.md), 48:32-50:39, 57:24-58:24
