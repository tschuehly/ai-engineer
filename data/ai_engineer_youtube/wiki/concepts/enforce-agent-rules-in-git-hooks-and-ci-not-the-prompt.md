# Enforce Agent Rules in Git Hooks and CI, Not the Prompt

Summary: Put the rules an agent must follow into deterministic commit-time and CI gates — git hooks, linters, type checks, architecture/import checks, document linting — rather than into the prompt, so the rules survive context compaction and the agent self-corrects against concrete rejection feedback instead of remembering instructions.

Use when:
- Designing a coding-agent loop that must stay on-policy across long, multi-hour autonomous sessions.
- Deciding whether a recurring "the agent forgot the rule" problem belongs in the system prompt or in the harness.

Details:
- The loop is git hooks, skills, CI, and linters plus other checks. Because the agent's goal is to deliver a pull request, it is forced to use git, so git hooks run predefined tasks; the same tasks run on CI, so an agent that gets lazy and skips them gets caught. Checks include linting, formatting, type checking, code duplication, architecture checks, and document linting — "everything that's possible." 07:44-08:23
- The payoff is compaction resilience: the speaker's sessions run 20–50 context compacts and "I have no fear of context compacts," because the important rules live outside the prompt — the important things survive a compact and the agent will always look them up again. This is what makes multi-hour autonomous sessions with a clear goal work. 11:04-11:44
- The motivating frame is that humans and LLMs share the same weakness, limited context: people forget and LLMs compact; humans leave and LLMs have no memory — so rules and rationale must be externalized into durable, enforced artifacts rather than held in anyone's (or any prompt's) head. 01:27-01:36
- Enforcement is paired with rationale: when the agent tries to commit/push it gets feedback, gets rejected, gets linked back to the document (an ADR that states the rule, why it exists, and how to fix it), then reads it, fixes it, and iterates. 09:36-09:50, 02:47-03:26
- Code review shifts up a level: style, tabs, and spaces are no longer for discussion — they are rules, enforced and automated — so human review is freed to focus on high-level concepts. 08:23-08:43
- The loop (do work → push → get feedback → iterate) stays generic, but skills change its *focus*: an ADR skill, a PRD skill, a UI loop that skips checks for fast browser iteration, a test skill that runs only the tests implicated by code coverage and file changes, and a goal-execution skill that records the model's decisions for later review. 09:50-11:04

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Lint Module Imports to Make Failure Classes Structurally Impossible](lint-module-imports-to-make-failure-classes-structurally-impossible.md)
- [Verify Spec Adherence With Executable, Readable BDD Scenarios](verify-spec-adherence-with-executable-readable-bdd-scenarios.md)
- [Make Validation Fast, Local, Deterministic, and Actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Use hooks for deterministic agent verification and live context injection](use-hooks-for-deterministic-agent-verification-and-live-context-injection.md)
- [AI Review Gates Turn Standards Into Executable Feedback](ai-review-gates-turn-standards-into-executable-feedback.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Use PRDs to align agents on the design concept](use-prds-to-align-agents-on-the-design-concept.md)

Sources:
- [BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence](../sources/20260603_504PvfXou5Y.md), 01:27-01:36, 02:47-03:26, 07:44-11:44
