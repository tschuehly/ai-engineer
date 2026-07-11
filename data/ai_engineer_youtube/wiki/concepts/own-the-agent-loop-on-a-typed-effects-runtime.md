# Own the Agent Loop on a Typed Effects Runtime

Summary: When an agent framework stops fitting as the team scales, moving to a self-owned agent loop built on a typed functional-effects library (Effect-TS) gives full control of the loop while making cross-cutting concerns — tracing/spans, structured concurrency, logging, dependency-injected model hot-swap, and schema validation — propagate uniformly across the whole loop instead of being bolted on per feature.

Use when:
- A graph/agent framework (e.g. LangGraph) has become the constraint as use cases evolve and you need custom control over the loop.
- You want observability, dependency injection, and structured concurrency to be uniform across the agent loop rather than added ad hoc.
- You are choosing the substrate for a production TypeScript agent and weighing a framework against owning the loop.

Details:
- OpenGov started on LangGraph, which "was fine until the team really started to scale and our use cases started to evolve," then moved to an Effect-native loop to have full control ("regency") over complex features. ([Gabe De Mesa](../sources/20260626_4uFVSLgD2Q4.md), 05:50-06:22)
- Owning the loop is what propagates the benefits: because everything runs on Effect, tracing, structured concurrency, logging, and fine-grained control apply throughout the entire loop, "from the ground up." ([Gabe De Mesa](../sources/20260626_4uFVSLgD2Q4.md), 06:22-06:45)
- The Effect AI package supplies the loop primitives: a `chat` plus a `language model` abstraction where you instantiate a chat and `stream text` from a prompt; dependency injection under the hood means you can hot-swap the underlying language model without rewriting the loop. ([Gabe De Mesa](../sources/20260626_4uFVSLgD2Q4.md), 06:45-07:45)
- Observability comes "out of the box": Effect functions auto-tag with spans that feed traces, so you can profile end-to-end latency, locate bottlenecks, and cross-reference failures across services — "you can't scale what you can't see," which matters most in agentic systems integrating with many teams and APIs. ([Gabe De Mesa](../sources/20260626_4uFVSLgD2Q4.md), 14:53-16:19)
- Tools plug into the same loop the Effect way: define a tool, add it to a tool kit (a collection of tools), and register the tool kit with the language model. ([Gabe De Mesa](../sources/20260626_4uFVSLgD2Q4.md), 16:19-17:38)
- Effect is credited as an open-source TypeScript library that also brings schema (Zod-like), error handling, and logging, which the team uses beyond the loop for architecture and new services. ([Gabe De Mesa](../sources/20260626_4uFVSLgD2Q4.md), 04:35-05:47)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Use Durable Execution for Production Agent Loops](use-durable-execution-for-production-agent-loops.md)
- [Type-Safe Agent Schemas Make Refactoring and Validation Easier](type-safe-agent-schemas-make-refactoring-and-validation-easier.md)
- [Constrain Agent Effects, Not Expression, With a Typed SDK](constrain-agent-effects-not-expression-with-a-typed-sdk.md)

Sources:
- [Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](../sources/20260626_4uFVSLgD2Q4.md), 04:35-07:45, 14:53-17:38
