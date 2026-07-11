# Spec-driven development is a tool-portable pattern, not a single product

Summary: Spec-driven development is a portable workflow pattern — generate reviewable requirements, then design, then a task list in markdown before writing code — that can be run manually with any coding assistant, via an open-source scaffold like GitHub's Spec Kit, or via a purpose-built tool like Kiro. The durable value is the artifact chain plus a human review gate between steps, not lock-in to a specific product.

Use when:
- Deciding whether adopting spec-driven development requires buying into one vendor's tool.
- Bootstrapping the requirements→design→tasks discipline in whatever coding assistant a team already uses.
- Explaining why several products (Kiro, Spec Kit, plan modes) all implement the same underlying idea.

Details:
- The pattern originated as a "bespoke pattern" customers were hand-rolling: pointing coding assistants to generate full requirements documents and design documents before code. AWS observed this and productized it as Kiro (GA late 2025), an AI IDE plus CLI whose differentiator is vibe mode vs spec mode. (06:25-08:24)
- Three ways to run it: (1) manually with any assistant — ask it to create user requirements (optionally seeded with your own), review, have it create the design document, review, then have it create the implementation task list; (2) GitHub's open-source Spec Kit ("Spec It"), installable into a variety of coding assistants; (3) Kiro's IDE spec mode or CLI plan mode. (08:28-09:49)
- The reusable core is the reviewable markdown artifact chain (requirements, design, tasks) with the human staying in the loop between phases, editing docs with their own taste before code is generated — "it's only as good as what you put in." (05:26-06:22, 11:45-12:12)
- Context feeding the pattern belongs in a steering/AGENTS.md/CLAUDE.md file kept in a "Goldilocks zone" — enough rules and guidelines, not too much or too little — and can be augmented with on-demand skills. (04:06-05:23)
- Not greenfield-only: the same pattern applies to years-old legacy apps that accumulate "dozens and dozens" of spec files, and to bug-fix spec modes; it is most valuable for in-depth features and complex projects that need upfront planning. (10:02-10:46)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Spec-driven development turns prompts into requirements, design, and tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)
- [Reorder the generated task list to ship an MVP first](reorder-the-generated-task-list-to-ship-an-mvp-first.md)
- [Use research-plan-implement loops for coding agents](use-research-plan-implement-loops-for-coding-agents.md)
- [Treat the Specification as the Product and Derive Bespoke Implementations](treat-the-specification-as-the-product-and-derive-bespoke-implementations.md)

Sources:
- [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](../sources/20260628_IddXPepIAS4.md), 04:06-10:46
