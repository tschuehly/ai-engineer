# Treat the Specification as the Product and Derive Bespoke Implementations

Summary: When agents can synthesize implementations on demand, reuse moves upstream — from reusing a general-purpose implementation to reusing an abstract, target-agnostic specification from which many bespoke, target-specific implementations are derived as minimal extensions of infrastructure already in place. Value shifts from the implementation to the specification/protocol.

Use when:
- Deciding what a library, framework, or platform vendor actually sells once coding agents can generate implementations.
- Designing an infrastructure component that must run correctly on many different backends (Postgres, NATS, a partner's stack) without maintaining a hand-written port for each.
- Judging whether a "spec" is reusable: an implementation-agnostic protocol versus a plan for one app.

Details:
- Thesis: in 2026 coding agents will "quietly retire their first software platform" — not because it is bad, but because the platform is *unnecessary*; general-purpose implementations are increasingly replaced by bespoke ones generated on demand, "not as a new library, a new framework, or a new platform, but as a minimal extension of the infrastructure that is already in place." (00:02-00:57)
- If implementations become generatable, reuse moves upstream: instead of reusing a general-purpose implementation, you reuse a *specification* and derive a bespoke implementation from it — value moves "from implementation to specification." (00:57-02:05)
- Reframes the vendor's product: Resonate's product is no longer the implementation but the specification/protocol; from one protocol they derive multiple server implementations (a general-purpose reference server plus implementations built with infrastructure partners), giving customers durable execution on top of existing infrastructure with minimal added dependencies. (01:33-02:40)
- The operative question is not "can we build a server" but "can we *repeatedly synthesize trusted* servers from the same specification, and if so how" — reuse is about repeatable synthesis, not a single generation. (02:40-02:52)
- The specification must be abstract: it must not assume a DB schema/indices, not even a relational DB with tables/transactions, not a key-value store, and not a particular consistency model; only the implementation is concrete. Abstractness is what lets one spec target many platforms. (03:53-05:11)
- Enabler: minimalism and simplicity are the finish line, not the starting point (three years shrinking the protocol to two objects — a durable promise and a durable task) — a small protocol is what makes repeatable agent synthesis tractable. (08:29-09:24)
- Slogan: "The prompt is a platform and the specification is a product." (17:18-17:24)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Use deterministic simulation as executable design for agents](use-deterministic-simulation-as-executable-design-for-agents.md)
- [Spec-driven development turns prompts into requirements, design, and tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)
- [Use evals as durable AI system specifications](use-evals-as-durable-ai-system-specifications.md)
- [Use durable execution for production agent loops](use-durable-execution-for-production-agent-loops.md)

Sources:
- [The Prompt is the Platform - Dominik Tornow, Resonate HQ](../sources/20260629_DqtmZE6Hl0g.md), 00:02-02:52, 03:53-05:11, 08:29-09:24, 17:18-17:24
