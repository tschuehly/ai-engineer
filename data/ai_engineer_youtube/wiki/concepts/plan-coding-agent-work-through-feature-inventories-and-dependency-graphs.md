# Plan Coding-Agent Work Through Feature Inventories and Dependency Graphs

Summary: Coding-agent planning should transform a vague project idea into a feature inventory, atomic specifications, a dependency matrix, and a phase-ordered implementation plan. This keeps architectural decomposition in human-controlled planning instead of leaving it to the agent during implementation.

Use when:
- Preparing a new AI-assisted application build before implementation starts.
- Breaking a large coding-agent request into atomic, dependency-ordered work units.

Details:
- The planning phase is where the human completes architectural thinking, decomposition, specification writing, and dependency analysis; the agent may help surface gaps, edge cases, and assumptions, but the human makes the decisions (17:31-17:58, 20:54-21:04).
- Gallon's five planning steps are vision, features, specification, dependencies, and plan; the output is atomic, sequenced, fully specified features ready for implementation (17:31-18:19).
- Vision capture turns an incomplete idea into a master project specification covering problem, users, essential functionality, scope boundaries, technical context, and workflow details (18:41-20:54).
- Feature identification extracts all discrete functionality from the master project specification into an inventory with categories, feature IDs, descriptions, complexity estimates, and traceability to source sections (21:43-25:26).
- Feature atomicity keeps agents from making architectural decomposition decisions on the fly; each feature should be an irreducible task small enough for an agent to execute completely (11:22-12:11).
- Dependency-driven development treats features as an interconnected graph and schedules implementation so agents do not implement features that depend on incomplete work (12:19-12:54).
- The implementation plan topologically sorts features into phases, verifies same-phase independence, identifies the critical path, and defines binary phase success criteria and validation strategies (35:01-37:17).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use PRDs to align agents on the design concept](use-prds-to-align-agents-on-the-design-concept.md)
- [Spec-driven development turns prompts into requirements, design, and tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)
- [Decompose large refactors into dependency-aware agent batches](decompose-large-refactors-into-dependency-aware-agent-batches.md)

Sources:
- [The Cure for the Vibe Coding Hangover - Corey J. Gallon, Rexmore](../sources/20251124_JsKTQbT58BY.md), 11:22-12:54, 17:31-25:26, 35:01-37:17
