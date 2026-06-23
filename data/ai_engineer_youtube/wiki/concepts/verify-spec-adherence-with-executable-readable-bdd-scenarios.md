# Verify Spec Adherence With Executable, Readable BDD Scenarios

Summary: Spec-driven development leaves a loop open — you have a markdown spec but no proof the product behaves that way, and AI-written tests are even harder to audit than AI-written code. Behavior-driven-development scenarios (Cucumber) are an intermediate layer that is both executable and human-readable, so they verify behavior and stay reviewable, closing that gap.

Use when:
- A team has markdown specs or PRDs but no trustworthy way to confirm the implementation matches them.
- Choosing a test representation for agent-generated code where reviewers must understand what is actually being checked.

Details:
- The gap: a spec is a markdown document describing how the product is supposed to work, but how do you know it actually works like that? "One thing harder than reading an AI code is reading AI tests" — so an intermediate layer should describe behavior in human language. 04:07-04:46
- BDD/Cucumber is "almost forgotten, suddenly useful again": the scenarios are executable *and* readable, and easier to review than your average tests. 04:46-05:02
- Connect scenarios directly to PRDs and critical user journeys, and let them refer back to the documents that explain why things exist, so the test layer is traceable to intent. 05:02-05:08, 05:42-05:59
- Mechanically, the specs are parsed by steps and executed as code, but a human can still write, read, review, and understand them — "the language is on you," so it doubles as living documentation of behavior. 05:15-05:31
- A parallel reviewable-spec idea applies to UI: a documented design system and pattern library (state the language and rules, e.g. "only one primary button visible on a page at any point in time," with component previews and snippets that agents can see) lets you and the agent review whether generated UI adheres before reuse. 05:59-07:18

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Spec-driven development turns prompts into requirements, design, and tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)
- [Translate structured requirements into property-based tests](translate-structured-requirements-into-property-based-tests.md)
- [Generated Tests Need Meaningful Plans, Coverage, and Pruning](generated-tests-need-meaningful-plans-coverage-and-pruning.md)
- [Use PRDs to align agents on the design concept](use-prds-to-align-agents-on-the-design-concept.md)
- [Enforce Agent Rules in Git Hooks and CI, Not the Prompt](enforce-agent-rules-in-git-hooks-and-ci-not-the-prompt.md)

Sources:
- [BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence](../sources/20260603_504PvfXou5Y.md), 04:07-07:18
