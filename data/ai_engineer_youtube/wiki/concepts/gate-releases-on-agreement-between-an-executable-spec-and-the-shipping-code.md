# Gate Releases on Agreement Between an Executable Spec and the Shipping Code

Summary: When the prover's language cannot be the production language, keep both artifacts — an executable specification in the prover and the implementation you actually ship — and make their agreement a release gate rather than a report. AWS's Cedar keeps its authorization semantics in Lean and its production code in Rust, reconciles them with about 100 million differential random tests nightly, and ships nothing until they agree.

Use when:
- You want the guarantees of a formal model but cannot rewrite or ship the production system in the prover's language.
- You have a reference implementation available and are deciding what to do with it beyond documentation.
- Designing a release gate for a component where "correct" is a property of a whole input space, not of a scenario list.
- Judging what a differential-testing suite actually establishes before describing a system as verified.

Details:
- **The structure.** "The specification of Cedar is written in Lean. The production code runs in Rust." Cedar is the open-source authorization policy language behind AWS Verified Permissions and Verified Access, and the properties that matter are whole-system invariants such as forbid-trumps-permit: "for any forbid policy being satisfied, the request is always denied." ([Pant](../sources/20260828_lRa9sPaMyy4.md), 06:06-06:32)
- **The reconciliation mechanism, and why the spec has to be executable.** "You run differential random testing to check that both of those for the same inputs give the same output." Differential testing needs a reference to differ against, and an executable specification is exactly that — the same artifact the proofs are written about doubles as the oracle. A specification that can only be read supports review; one that can be run supports a gate. (06:36-06:50)
- **Volume and cadence are the substitute for exhaustiveness, and they are chosen deliberately.** "About 100 million differential random tests run nightly. No version ships until this is satisfied." That is a nightly batch and a ship blocker, not a per-commit check: the design trades immediate feedback for a sample large enough to be worth trusting, and puts the verdict where it can stop a release rather than where it can be waved through. (06:50-06:58)
- **Be precise about what is proved and what is tested.** The proofs live on the Lean side and are about the model. The shipping Rust binary's conformance to that model is established by *sampling* — high-volume sampling, but sampling — so the honest claim is "the model has been proved to have this property, and the implementation has not been caught disagreeing with the model," which is strictly weaker than a proof about the shipped code. The talk presents both inside one formal-verification narrative without marking that boundary; a team copying the pattern should mark it, because it is exactly the seam an auditor will ask about.
- **What determines whether the gate is worth its cost is the input distribution, which is unstated.** A hundred million uniformly random policy sets can miss a narrow disagreement that a hundred thousand structure-aware ones would find. The number is the least transferable part of the pattern; the generator is the part that decides its value.
- **Where the pattern is easiest, and the limit that implies.** Cedar is an unusually friendly target — a deterministic, total policy evaluator whose inputs are structured data and whose outputs are small — so the reference model is cheap to write and comparison is trivially decidable. Systems with I/O, concurrency, or large opaque outputs make both harder, and the talk does not say where the approach stops being practical.
- **Relation to the wiki's gating pages.** [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md) and [Gate Generated Output With a Deterministic Post-Generation Veto](gate-generated-output-with-a-deterministic-veto.md) both place a deterministic verdict after a probabilistic producer; this page supplies the strongest available form of the oracle those gates need — a second implementation whose correctness is separately argued — and shows it working at release cadence rather than per-task.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Pick a Verification Route by Which Translation You Can Afford](pick-a-verification-route-by-which-translation-you-can-afford.md)
- [Ship a Proof a Small Kernel Can Recheck, Not a Claim You Must Trust](ship-a-proof-a-small-kernel-can-recheck.md)
- [Translate structured requirements into property-based tests](translate-structured-requirements-into-property-based-tests.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [Gate Generated Output With a Deterministic Post-Generation Veto](gate-generated-output-with-a-deterministic-veto.md)
- [Use Deterministic Simulation as Executable Design for Agents](use-deterministic-simulation-as-executable-design-for-agents.md)
- [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md)

Sources:
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 05:58-06:58
