# Breadcrumb Coding Agents Through Staged Discovery and Implementation

Summary: Coding agents can be steered by sequencing information and tasks gradually instead of handing them the full desired path upfront. This reduces improvisation while preserving the agent's ability to solve local problems.

Use when:
- A codegen workflow produces many valid-looking but inconsistent implementations.
- An agent rushes through early steps and over-polishes or derails later steps.

Details:
- At high volume, many acceptable integration paths can create a support burden because each customer ends up with a different setup shape. 06:50-07:28
- PostHog limits improvisation by first asking the agent to find files with business value, such as login, payments, churn, or other areas where events would matter. 07:29-08:39
- The next step asks for interesting events and descriptions without writing code yet; only after that does the workflow introduce PostHog implementation and relevant framework or language docs. 08:39-09:29
- The design goal is to sequence enough information for the agent to do the intended work, rather than over-scaffolding every behavior in code or prompt constraints. 16:03-16:24

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Prompt-coded product behavior reduces code but weakens hard guarantees](prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md)

Sources:
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md), 06:50-09:29, 16:03-16:24
