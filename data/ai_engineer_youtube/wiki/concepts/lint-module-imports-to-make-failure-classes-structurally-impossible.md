# Lint Module Imports to Make Failure Classes Structurally Impossible

Summary: Forbid the imports that would let a whole class of failure occur, so the failure can never happen, instead of writing checks that detect instances after the fact. Structural prevention through module-import boundaries is stronger than detection because "what you cannot find, you cannot enforce."

Use when:
- A recurring failure class (N+1 queries, layering violations, test suites reaching production state) keeps reappearing despite review and ad-hoc checks.
- Designing an agent-legible codebase architecture whose constraints can be enforced mechanically rather than by prompt instruction.

Details:
- Enforce architecture by separating modules and linting their imports — controlling what each module is allowed to use and from where. 08:48-09:00
- Concrete prevention examples: rendering templates are forbidden from talking to the database, so there are no N+1 queries ever; the end-to-end BDD test suite is forbidden from importing any module that could access the database, which forces it to iterate without the database using only the application's browser features. 09:00-09:25
- A complementary data-shape rule reinforces the boundary: reads from the database return plain shapes instead of ORM objects, so the queries simply cannot be made and duplication is prevented. 02:18-02:41
- The principle is prevention over detection: "we just define ways to prevent these problems from happening ever. You cannot keep finding them. You need to prevent them entirely." 09:25-09:36
- Each rule is backed by an architecture decision record (~50 ADRs define the product's architecture) that states why the boundary exists and how it is enforced, and the import lint is the tool that makes the ADR enforceable rather than aspirational. 02:41-02:47, 02:47-03:00

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Enforce Agent Rules in Git Hooks and CI, Not the Prompt](enforce-agent-rules-in-git-hooks-and-ci-not-the-prompt.md)
- [Put brittle edge cases behind rigorous tools](put-brittle-edge-cases-behind-rigorous-tools.md)
- [Agent-legible codebases reduce generated-code entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [Delegate implementations behind reviewed module interfaces](delegate-implementations-behind-reviewed-module-interfaces.md)
- [Use deep modules to make agent work testable](use-deep-modules-to-make-agent-work-testable.md)

Sources:
- [BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence](../sources/20260603_504PvfXou5Y.md), 02:18-03:00, 08:48-09:36
