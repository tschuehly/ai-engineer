# Pick a Verification Route by Which Translation You Can Afford

Summary: Formal verification is usually presented as one decision — verify or don't. It is really a choice among routes that differ in *who translates your program into the prover's logic and what that translation costs you*: rewrite the code in the prover's language, keep a model beside it, annotate in place and let a solver discharge the conditions, auto-translate the compiler IR, or normalize many languages into a shared verification IR. The guarantee is similar across routes; the disruption to your codebase is not.

Use when:
- Deciding how to introduce verification into a codebase that already exists and is not going to be rewritten.
- Choosing between a proof assistant and an SMT solver and unsure what the difference buys.
- Evaluating a verification tool and wanting to know which of its costs are inherent to the route it took.
- Scoping a first attempt: "pick your most critical code" is the entry rule, and the route determines how much code that can be.

Details:
- **Route 1 — write both spec and code in the prover's language.** Lean is "a programming language and a proof assistant… the same language for the definitions and proofs. There's no translation layer," so there is nothing to lose in translation. The price is that the shipping artifact is now Lean: converting zlib, a single C compression library, took "a week or so" and produced "32,000 lines of proof." Strongest guarantee, largest rewrite. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 02:10-02:20, 04:30-05:56)
- **Route 2 — model in the prover, code in your language, reconciled by testing.** "You can write the functional specification of it or the model in Lean" and keep production in Rust, as Cedar does, comparing the two by differential random testing. No translation is performed at all, so no translation can be wrong — but nothing connects the two artifacts except sampled agreement. See [Gate Releases on Agreement Between an Executable Spec and the Shipping Code](gate-releases-on-agreement-between-an-executable-spec-and-the-shipping-code.md). (05:58-06:58)
- **Route 3 — annotate in place and let a solver discharge it.** Verus, open-source and built on Z3, puts specifications inline in the Rust source as `requires` and `ensures` pre- and post-conditions — "what must be true before and what must be true after" — and "this is a static check. It's enforced by the verifier and erased at runtime. So, almost like ghost code." The translation is done by the verifier, the spec lives next to the code it constrains rather than in a separate document that can drift, and runtime cost is zero by construction. (07:30-08:07)
- **Route 4 — auto-translate the compiler's own IR.** Aeneas "uses the mid-level intermediate representation for Rust and does a functional translation to Lean. And right after that, you use the same theorem prover." The translation is automated and grounded in the compiler's semantics rather than a hand-written model, at the cost of being tied to one source language and its IR. (08:09-08:22)
- **Route 5 — normalize many languages into a shared verification IR.** AWS's open-source, work-in-progress Strata lets you "create what we call a dialect… like a compiler. You have a high-level intermediate representation and you lower it down to a low-level intermediate representation, which is what Strata core is. Now, this is written in Lean." Once programs speak Strata core, "you can dispatch it to any of the engines… the Lean proof… or the very powerful calculator, SMT solvers, or model checkers." The bet is that the IR, not any one prover, is the reusable asset — and it is a plan, not a shipped path. (08:26-09:12)
- **The prover/solver distinction is an automation axis, and it is what makes routes 1 and 3 feel so different.** A proof assistant is interactive: "tactics which are your moves," a goal tree, backtracking when a branch will not close. "A solver is a calculator, a very powerful one. You feed in a formula and it returns an output. In this case, satisfiable or unsatisfiable." The solver route asks for annotations and answers by itself; the prover route asks for a search someone has to drive. That is precisely the labour coding agents can now absorb, which changes the relative cost of the routes rather than the guarantees they offer. (03:04-03:53, 07:07-07:39)
- **How to read the map.** The routes are ordered by descending disruption to your existing codebase and, roughly, by descending strength of the connection between the proof and the bytes you ship. Route 1 proves things about the artifact you run; route 2 proves things about a sibling and samples the difference; routes 3 and 4 prove things about the real code through a translation you are trusting; route 5 is the same bet made once for many languages. Pick the strongest route your codebase can absorb, and record which link in the chain is unproved.
- **Caveat.** This is a slide taxonomy from a ten-minute talk, with no adoption, cost, or defect data for any route, and no guidance on what fraction of a codebase is worth specifying beyond "pick your most critical code." Three of the five named artifacts (Kiro, Cedar, Strata) are the speaker's employer's; Verus and Aeneas are not. Strata is explicitly work in progress, so route 5 should be read as a direction rather than an option available today. (09:17-09:35)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Ship a Proof a Small Kernel Can Recheck, Not a Claim You Must Trust](ship-a-proof-a-small-kernel-can-recheck.md)
- [Gate Releases on Agreement Between an Executable Spec and the Shipping Code](gate-releases-on-agreement-between-an-executable-spec-and-the-shipping-code.md)
- [Validate the Specification, Because the Proof Cannot](validate-the-specification-because-the-proof-cannot.md)
- [Use formal specifications and proofs for critical generated code](use-formal-specifications-and-proofs-for-critical-generated-code.md)
- [Route each change to the proof it needs](route-each-change-to-the-proof-it-needs.md)
- [Use LLMs to generate compiler lowerings under verification](use-llms-to-generate-compiler-lowerings-under-verification.md)
- [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md)

Sources:
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 02:10-02:20, 03:04-03:53, 04:30-05:56, 05:58-06:58, 07:07-09:12, 09:17-09:35
