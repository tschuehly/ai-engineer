# Expose Forbidden-Fruit Facts in Simulation for Agent Debugging

Summary: A simulation environment can record facts the real platform deliberately hides — information the production algorithm may *not* depend on but that lets an agent explain *why* its design was wrong. Give the algorithm only what production would return, but emit richer trace events (labeled "forbidden fruit") that make cause and effect visible to the debugging agent.

Use when:
- An agent needs to repair a distributed or concurrent algorithm and only sees an opaque failure (a write failed, an invariant broke) with no causal explanation.
- You are building a deterministic simulator for a backend whose consistency model hides whether a read was fresh or stale.
- You want agent feedback that shows *why and how* something went wrong, not just *that* it went wrong.

Details:
- Motivation: agents thrive on immediate, unambiguous feedback that shows why and how a run went wrong — what stale value was returned, what logic was triggered, what write failed, which invariant broke — not merely a signal that it failed. (12:00-12:38)
- The hidden fact: in production, reading a versioned KV store returns only the value at the version you observed; you do not get to know whether that read was fresh or stale, or the latest value you missed, and you *shouldn't*, because real code cannot be allowed to depend on it. (13:53-14:35)
- The "forbidden fruit": in simulation you *can* record it — every get emits a trace event that, for a stale read, says "this was stale, this is what you got, and this is what the latest value was." The algorithm is forbidden to depend on this information, but the agent is allowed to use it to explain why the algorithm it designed was wrong. (14:35-15:05)
- Trace-event shape: production code only receives the result (e.g. "the promise was pending"), which is all the real platform would report; the simulation additionally records the read type (stale) and the hidden latest value (e.g. the same promise is already settled). That difference is exactly the fact an agent needs when debugging a distributed algorithm. (15:05-15:45)
- Payoff: cause and effect becomes visible — the invariant failed *because* the algorithm made a decision from a stale view of the world — so the agent learns not just that the system is wrong but *why* it is wrong, and can repair the algorithm against the exact reproduced trace. (15:45-16:16)
- Requires the underlying simulation to be deterministic, repeatable, and inspectable so the failing execution can be reproduced and the extra facts attributed to a specific event. (13:23-13:53)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Use deterministic simulation as executable design for agents](use-deterministic-simulation-as-executable-design-for-agents.md)
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)
- [Treat the specification as the product and derive bespoke implementations](treat-the-specification-as-the-product-and-derive-bespoke-implementations.md)

Sources:
- [The Prompt is the Platform - Dominik Tornow, Resonate HQ](../sources/20260629_DqtmZE6Hl0g.md), 12:00-16:16
