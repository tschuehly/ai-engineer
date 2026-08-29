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

- Ankit Jain (Aviator) reaches the same "closer to BDD than TDD" placement from the review side, with one variation worth weighing: instead of a maintained scenario suite, an LLM generates a per-change test plan from the coding session plus codified invariants, and a verification system executes it against a live preview. The readable-behavior property is identical and is justified the same way — "the test plan is now something which even you can share with your product managers, your designers. Everyone can participate because these things are now in English" — but the maintenance claim is stronger and unproven: "you don't have to maintain tests at all. This is creating tests in real time." A generated per-change plan gives up the regression net a persistent Cucumber suite provides, so the two are better read as complements than as substitutes. (YgEv7IQzGdM 10:44-11:43)

- **The same open loop closed from the other end, and the readability requirement survives the move.** Instead of an intermediate layer that is both executable and human-readable, formal verification makes adherence machine-checked and puts the whole readability burden on the property statement — which is why the examples are one-liners: a round trip ("you decompress the output of compress returning the original data"), an algebraic law (reverse of `a ++ b` equals reverse of `b` plus reverse of `a`), and an authorization invariant ("for any forbid policy being satisfied, the request is always denied"). Each can be read by someone who could not have written the implementation, which is the same property BDD scenarios are chosen for. A specification too long to read has lost it. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 02:52-03:04, 05:04-05:11, 06:22-06:32)

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
- [Make Intent and Evidence the Review Surface](make-intent-and-evidence-the-review-surface.md)
- [Validate the Specification, Because the Proof Cannot](validate-the-specification-because-the-proof-cannot.md)

Sources:
- [BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence](../sources/20260603_504PvfXou5Y.md), 04:07-07:18
- [How to Kill the Code Review — Ankit Jain, Aviator](../sources/20260817_YgEv7IQzGdM.md), 10:44-11:43
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 02:52-03:04, 05:04-05:11, 06:22-06:32
