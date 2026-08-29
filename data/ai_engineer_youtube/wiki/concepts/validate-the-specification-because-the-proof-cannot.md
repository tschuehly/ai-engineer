# Validate the Specification, Because the Proof Cannot

Summary: Once machines own the code and the proof, the specification is the only artifact left in human hands and the only place an error can still hide — and unlike an ordinary bug, a wrong specification comes out of the pipeline certified. Verification therefore adds a workflow step rather than removing one: validate the spec before anything downstream runs, by human review or by testing that it holds on sample inputs.

Use when:
- Adopting formal verification, property-based testing, or any other check whose guarantee is stated relative to a spec you wrote.
- Letting a model auto-formalize a natural-language requirement into a checkable form, and deciding what confirms the translation.
- Explaining why "the verifier passed" is not the same claim as "the code does what we wanted."
- Deciding what tests are still for in a codebase that has proofs.

Details:
- **The division of labour that creates the exposure.** "Humans own the specification and machines own the code and proof." Everything a human used to check — implementation choices, edge cases, the reasoning that connects them — moves to the machine side, and all residual human responsibility concentrates in one document. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 02:04-02:10)
- **The step is explicit and load-bearing, and the talk interrupts itself twice to say so.** "Now, this is really important. You then validate the specification. So, either the human reviews it, or you test that it holds on some inputs… the specification is upstream. It's a living, breathing artifact that the builder interacts with. You want this to be correct. Everything else is downstream from this." (01:32-01:52) Later, mid-example: "you have an AI that generates the formal spec. Now, remember this is important. Checking the specification is key." (05:11-05:19)
- **Tests do not disappear under proof; they change target.** One of the two offered validation methods is "you test that it holds on some inputs" — the same technique the talk disqualified forty seconds earlier for checking *code* ("they only check some inputs, not all") is reinstated for checking *specs*. That is coherent rather than contradictory: sampling is a weak way to establish a universal claim about an implementation but a reasonable way to catch a specification that says something you did not mean. Reading it as demotion misses the move; the test suite is re-aimed, not retired. (00:29-00:33, 01:36-01:41)
- **Auto-formalization inserts a second, unproved gap.** You can "write it in natural language, and you let the AI auto formalize it" — after which the proof binds the code to the *formal* spec, while nothing binds the formal spec to the sentence a human actually approved. The chain has two links and the verifier only certifies one; a mistranslation is invisible to the kernel and produces a proof that is entirely valid about the wrong statement. (01:23-01:32)
- **Why human review of a spec is feasible at all: the specs that get written are short and algebraic.** The talk's examples are a round trip ("you decompress the output of compress returning the original data"), an algebraic law (reverse of `a ++ b` equals reverse of `b` plus reverse of `a`), and an authorization invariant ("for any forbid policy being satisfied, the request is always denied"). Each is one sentence, states a relationship rather than a procedure, and can be read by someone who could not have written the implementation. A specification long enough to need its own review process has probably lost the property that made this workflow tractable. (02:52-03:04, 05:04-05:11, 06:22-06:32)
- **How this differs from the spec risk the wiki already tracks.** [Spec-Driven Development Without a Feedback Loop Is Waterfall](spec-driven-development-without-a-feedback-loop-is-waterfall.md) and [Keep spec artifacts feature-scoped, mutable, and context-backed](keep-spec-artifacts-feature-scoped-mutable-and-context-backed.md) worry about staleness — a spec drifting out of agreement with a system that moved on. The risk here is the opposite and worse-behaved: perfect agreement with a spec that was wrong on the day it was written, delivered with a machine-checked certificate attached. Staleness announces itself when the code diverges; a wrong invariant never does.
- **Caveat: the method is named, not specified.** "Either the human reviews it, or you test that it holds on some inputs" is the entire treatment in a ten-minute talk. There is no criterion for when a spec has been validated enough, no account of how a reviewer validates an auto-formalized spec written in a language they do not read, and no measurement of how often auto-formalization goes wrong. Treat the step as a known requirement with an open method.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Ship a Proof a Small Kernel Can Recheck, Not a Claim You Must Trust](ship-a-proof-a-small-kernel-can-recheck.md)
- [Use formal specifications and proofs for critical generated code](use-formal-specifications-and-proofs-for-critical-generated-code.md)
- [Translate structured requirements into property-based tests](translate-structured-requirements-into-property-based-tests.md)
- [Spec-Driven Development Without a Feedback Loop Is Waterfall](spec-driven-development-without-a-feedback-loop-is-waterfall.md)
- [Spec-driven development turns prompts into requirements, design, and tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)
- [Verify Spec Adherence With Executable, Readable BDD Scenarios](verify-spec-adherence-with-executable-readable-bdd-scenarios.md)
- [Treat the Specification as the Product and Derive Bespoke Implementations](treat-the-specification-as-the-product-and-derive-bespoke-implementations.md)
- [Write the Test First So the Agent Cannot Fit It to the Code](write-the-test-first-so-the-agent-cannot-fit-it-to-the-code.md)

Sources:
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 00:29-00:33, 01:23-01:52, 02:04-02:10, 02:52-03:04, 05:04-05:19, 06:22-06:32
