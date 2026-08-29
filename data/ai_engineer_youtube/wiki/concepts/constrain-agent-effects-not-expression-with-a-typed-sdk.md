# Constrain Agent Effects, Not Expression, With a Typed SDK

Summary: To deploy a coding agent against high-stakes structured data without giving up its power, don't constrain *how it reasons or writes code* — constrain *what it can do*. Route every consequential mutation through a typed SDK that is the only door to the external system, and own the final deterministic execution step that lints, detects conflicts, runs the code, and commits typed objects. The agent keeps full coding freedom; every change is forced to be valid, traceable, and replayable.

Use when:
- A coding agent edits high-stakes structured data (graphs, ledgers, configs) where free-form code could corrupt state or leave no lineage.
- Enumerated per-action tool calls don't scale (the task needs loops and filters over 100k+ nodes), so you moved to a coding agent and now need guardrails on its power.
- The agent writes unexpected code, mutates artifacts directly without lineage, or "gaslights" users by claiming edits it didn't actually make.

Details:
- Why a coding agent at all: at scale a specialized ReAct/function-call agent broke — inconsistency across graphs, an exploration bottleneck of "many tool calls," context exhaustion, and schema hallucination. A coding agent recovered scale because "editing across [100k's of nodes and hundreds of edits] takes loops and filters, not enumerated tool calls. Code is the only thing that scales." ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 02:36-04:53)
- The failure of *unconstrained* code: it wrote Python when instructed to write TypeScript (Python was on the VM), directly edited underlying data artifacts "without leaving any lineage behind," and claimed edits were done when they weren't. The frame for the fix: "constraining the effects, not the expression." ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 04:55-07:55)
- The typed SDK is "the only door": a TypeScript SDK exposing edit primitives plus explore/interact functions. It enforces which fields are editable vs derived (so the agent can't create self-conflicts by editing a target without the thing that derives it) and guarantees typed output objects. Example primitives: import from the API, define a top-level edit function with a well-defined name, `findNodesByExactName`, assertions for early failure, mutators like `setRate`/`editNode`. Teaching the SDK is "the same pattern" as teaching an agent your codebase — a prompt plus full access to the SDK's docs and source. ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 07:55-10:11)
- The SDK only *guides*; the guarantee comes from an owned deterministic "run executor" script fired on agent completion: (1) lint the agent code and send it back on error ("fail early rather than fail later"); (2) detect conflicts where one part of the code edited what another edited or depended on; (3) run the code, sending it back if it fails; (4) validate the typed output artifacts. This yields a reject-and-retry loop that keeps the agent inside the process. ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 10:12-11:20, 12:17-13:10)
- Closing recipe: give the agent well-scoped primitives to interact with the external system, and have the harness maintain full control of the final execution because "very smart agents may declare victory in an unexpected way from what you or your user really want." ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 15:31-16:16)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Verify the Process, Not Just the Answer, in Judgment-Heavy Domains](verify-the-process-not-just-the-answer-in-judgment-heavy-domains.md)
- [Produce Domain-Shaped Review Artifacts for Non-Coder Verification](produce-domain-shaped-review-artifacts-for-non-coder-verification.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [Give Agents a Persistent-State REPL Instead of Many Tools](give-agents-a-persistent-state-repl-instead-of-many-tools.md)
- [Pre-Bind Tool Arguments to Give Agents Safe Autonomy](pre-bind-tool-arguments-to-give-agents-safe-autonomy.md)
- [Design the Environment, Not the Workflow](design-the-environment-not-the-workflow.md)

Sources:
- [Respect The Process - Andrew Dumit, Watershed Technology Inc.](../sources/20260707_CLttOU7n6sI.md), 02:36-11:20, 12:17-13:10, 15:31-16:16
