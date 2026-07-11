# Contain Retry Amplification Before It Becomes a Compute Incident

Summary: Uncontrolled retries are one of the biggest risks in agentic systems: when an agent responds to a tool error by regenerating a slightly different but still-invalid request, the loop compounds — each retry consumes more compute and deeper reasoning — until a minor API error becomes a runaway compute incident. Bound retries with circuit breakers, resource quotas, and controlled recovery so infrastructure absorbs the mistake instead of amplifying it.

Use when:
- An agent can retry tool calls, model calls, or workflow steps on failure without a hard bound.
- Diagnosing unexplained GPU/cost spikes that trace back to an agent looping on a failing dependency.
- Designing recovery behavior for a long-running agent that must stay within a cost, latency, and outcome budget.

Details:
- The amplification mechanism: an agent calls a tool incorrectly, the tool returns an error, and instead of recovering the agent generates a "slightly different but still invalid request." The cycle repeats; each retry consumes more compute, reasoning depth increases, GPU consumption rises, and you get exponential resource growth — "what started as a minor API error became a compute incident."
- This is the concrete example of the broader failure class: real agent failures are usually infrastructural (retry amplification, recursive reasoning loops, workflow deadlocks, context corruption, memory poisoning, cost explosions), not hallucinations — "the model makes a mistake, but the infrastructure turns that mistake into an outage." Hallucinations are "often the least interesting failure mode."
- The fix is to reuse distributed-systems reliability primitives rather than invent new ones: retries become *controlled recovery* (bounded, backed-off, escaping the loop on repeated failure), circuit breakers become tool isolation so a failing tool fails fast instead of being hammered, and resource quotas become cost governance so a runaway loop hits a ceiling.
- Detecting these loops requires causal observability — traces of the chain of tool calls and reasoning decisions — because a retry storm looks like normal activity in aggregate logs until the compute bill spikes.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Build an Agentic Control Plane So the Model Proposes and the Platform Decides](build-an-agentic-control-plane.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)
- [Prevent AI billing surprises with caps, notifications, and rate limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)

Sources:
- [Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](../sources/20260629_APh1Vx0oLmQ.md), 02:06-03:06
