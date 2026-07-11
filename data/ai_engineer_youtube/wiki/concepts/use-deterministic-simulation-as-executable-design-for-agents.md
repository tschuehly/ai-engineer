# Use Deterministic Simulation as Executable Design for Agents

Summary: To make an agent *design* a correct concurrent/distributed system rather than only build and verify one, insert a deterministic simulation step between the abstract specification and the production code. The agent first builds a simulated implementation — "executable design" whose job is to discover the correct algorithm under partial order and partial failure — and only then writes the concrete specification and the production implementation.

Use when:
- An agent produces happy-path code that passes basic tests but breaks under concurrency, process failure, or network failure.
- You want the agent to participate in system design, not just implementation and verification.
- You are targeting a backend whose consistency model allows legal-but-inconvenient behavior (stale reads, optimistic-concurrency write failures) that must be handled correctly.

Details:
- Failure that motivates it: asking an agent to go straight from an abstract spec to a concrete Rust-on-Postgres server left too large a gap — the result worked on the happy path and passed basic tests but broke on concurrency, process failure, and network failure (a prototype, not a production system). (05:11-05:52)
- A first patch (inserting a human-authored concrete specification: schema, indices, SQL, transaction boundaries) let the agent *build* the production system, but the human was still the designer — the agent did not help *design*, so the reusable spec wasn't really produced by the agent. (05:52-06:57)
- The upstream move: change the question from "can the agent build the production system" to "what does the agent need in order to *design* the system first and build it second," and give it a deterministic simulation environment. (07:04-07:31)
- Pipeline: abstract specification → **simulated implementation (executable design)** → concrete specification → concrete implementation. The simulated implementation is not the product; its purpose is to discover the correct algorithm under partial order under partial failure, tested and verified in simulation before any production code is written. This is where the agent becomes the driver (humans stay in the design loop). (07:31-08:29)
- Build the simulation over the *target platform's* primitives, not your own concepts: for NATS.io that was queues, a versioned key-value store, and delayed/scheduled messages — the design question is to express your protocol using only those. (09:24-09:54)
- The simulated dependency must reproduce legal target behavior, not convenient behavior: a Python simulated KV store keeps full version history, on get usually returns the latest version but sometimes (deterministic RNG) returns an older version, and on update enforces optimistic concurrency (write succeeds only if the read version is still latest, else raises). It behaves like the real store where correctness matters but is deterministic, repeatable, and inspectable, so a broken run can be reproduced exactly and the agent can repair the algorithm against that trace. (10:52-13:53)
- Outcome: from a single abstract spec the agent built a simulator proof of concept (verified by first testing), derived a concrete spec where the algorithm was already known correct, then derived the implementation — deterministic simulation let the agent participate in design, not just implementation. (16:16-17:18)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Expose forbidden-fruit facts in simulation for agent debugging](expose-forbidden-fruit-facts-in-simulation-for-agent-debugging.md)
- [Treat the specification as the product and derive bespoke implementations](treat-the-specification-as-the-product-and-derive-bespoke-implementations.md)
- [Understand Agent Work to Participate, Not Just to Verify](understand-agent-work-to-participate-not-just-to-verify.md)
- [Use neural debugging to fill code by simulated execution](use-neural-debugging-to-fill-code-by-simulated-execution.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)

Sources:
- [The Prompt is the Platform - Dominik Tornow, Resonate HQ](../sources/20260629_DqtmZE6Hl0g.md), 05:11-08:29, 09:24-13:53, 16:16-17:18
