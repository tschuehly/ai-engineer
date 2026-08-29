# Agent Software Factories Need Runnable, Contextual, and Verifiable Primitives

Summary: A coding-agent factory is not just more agents. It needs repository structure, reproducible project commands, accessible external context, and validation paths that let agents work without repeated human setup.

Use when:
- Preparing a repository for parallel or autonomous coding-agent work.
- Diagnosing why agents require constant human setup, navigation, or verification.

Details:
- Codebase structure matters because colocated and modular files let an agent discover relevant implementation areas with a local listing instead of broad repository search (05:02-05:50).
- Usage patterns such as authentication helpers, startup scripts, and test conventions should exist as reproducible references the agent can follow instead of rediscovering each workflow (05:50-06:17).
- The factory readiness checklist includes whether the project is runnable, whether required context is accessible, whether agents can interface with systems such as Linear, Notion, Datadog, or Slack, and whether the work is verifiable (09:24-10:10).
- Verifiability should cover unit tests, integration tests, and UI tests; front-end work may require actual DOM interaction and user-flow checks rather than only backend contracts (07:51-10:42).
- Developer environments are also an agent input: conventional tools, local package managers, linters, and workflows reduce setup friction because models already have stronger priors for common development patterns (02:50-04:34).
- External context that is not encoded in code, such as requirements, intent, data shape, or meeting decisions, should be written where agents can access it; agents cannot infer why a system exists from source structure alone (08:00-09:40).

- **What the validation primitive looks like at the top end, and how it gets wired.** Cedar's is an executable specification plus a scheduled reconciliation with teeth: "about 100 million differential random tests run nightly. No version ships until this is satisfied" — a validation path that is not just available to agents but positioned where it can block a release. The entry cost is deliberately low at the other end: Lean runs in the browser, so a team can "pick your most critical code, write what correct means" without standing up infrastructure first. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 06:36-06:58, 09:17-09:35)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Unified coding-agent harnesses combine models, tools, environments, and safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Standardize development environments around common model priors](standardize-development-environments-around-common-model-priors.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Gate Releases on Agreement Between an Executable Spec and the Shipping Code](gate-releases-on-agreement-between-an-executable-spec-and-the-shipping-code.md)

Sources:
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md), 05:02-10:42
- [Developer Experience in the Age of AI Coding Agents - Max Kanat-Alexander, Capital One](../sources/20251223_rT2Del5pwg4.md), 02:50-04:34, 08:00-09:40
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 06:36-06:58, 09:17-09:35
