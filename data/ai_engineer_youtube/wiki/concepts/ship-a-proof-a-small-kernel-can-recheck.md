# Ship a Proof a Small Kernel Can Recheck, Not a Claim You Must Trust

Summary: The property that makes machine-checked proof interesting for agent-generated code is an asymmetry, not rigour for its own sake: finding the proof cost a week and 32,000 lines, while checking it costs a small kernel you could reimplement yourself over a weekend. That decouples the size of what an agent produces from the size of what a human has to trust — which is the one verification property in this wiki that does not degrade as agent output grows.

Use when:
- Agent output has outrun review capacity and you need a check whose cost does not scale with the volume or length of what the agent wrote.
- Deciding what "independent verification" should mean when a second model, a second prompt, or a second vendor still shares a technique class with the first.
- Justifying why a verifier is allowed to accept a 32,000-line artifact no human will read.
- Explaining to a security or compliance reviewer what the trusted computing base of an AI-assisted pipeline actually is.

Details:
- **The gap being answered is throughput, and each usual check fails it differently.** "Coding agents are generating more code than ever. Builders are generating hundreds and thousands of PRs every week. How do you know that this is correct?" LLM-as-a-judge on the code "is probabilistic," tests "only check some inputs, not all," and "human code review doesn't scale to match agent speed" — so "none of these can say for all inputs the code is correct." Note these are three distinct failures: a confidence failure, a coverage failure, and a capacity failure. Only the third is fixed by more people. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 00:12-00:42)
- **The trust base is a deliberate design artifact, not a property of the language.** Lean "has a small trusted kernel. Proofs can be exported and independently checked," an incorrect proof "is rejected immediately. And you only need to trust the small kernel." Everything else in the system — the tactic library, the elaborator, the agent that searched for the proof — can be wrong without producing a false accept, because the kernel re-derives the result from the exported proof term. (02:20-02:30, 04:03-04:14)
- **Independent rechecking is available in practice, which is what makes the claim more than rhetorical.** "You can have multiple independent kernels. You yourself can actually go write one. It's completely open source. You have kernels in C++, Rust, Lean." Independence here is at the level of *implementation of the checking rule*, not of model, prompt, or vendor — a strictly stronger form of the wiki's method-independence rule, and one where you can eliminate the checker as a shared point of failure rather than merely diversify it. (04:14-04:30)
- **The asymmetry, stated as numbers.** An AI converted zlib, a C compression library, to Lean "over a week or so," starting from a natural-language round-trip specification, generating the formal spec, writing the Lean implementation, generating "helper lemma subgoals," and assembling them into a final theorem — "this particular example had 32,000 lines of proof." The proof is the largest artifact in the pipeline and the least trusted; the kernel is the smallest and the only trusted one. (04:41-05:56)
- **The search side maps onto an agent loop, which is why this is newly practical.** "In Lean, you have a bunch of tactics which are your moves… you want to prove the goal, the theorem, checkmate. And you're kind of going down a tree… for some goals, you're not able to prove it, so you backtrack and then you try another branch." That is tree search with a cheap terminal oracle and no reward-hacking surface: a wrong branch cannot be talked into passing, and the labour that historically made proof assistants expensive — driving that search by hand — is the part an agent can absorb. (03:04-03:53)
- **What the kernel does not certify.** Its verdict is exactly the theorem statement and nothing wider. A proof that closes against a wrong specification is still accepted immediately, so the residual risk concentrates entirely upstream — see [Validate the Specification, Because the Proof Cannot](validate-the-specification-because-the-proof-cannot.md). The kernel also says nothing about the compiled binary, the runtime, or anything outside the model of computation the proof is written in.
- **Caveat on the evidence.** This is a ten-minute conference talk with no measurement in it. The zlib figures are an outcome with no compute cost, retry rate, or human-intervention count attached, and the organization credited is unrecoverable from the captions. Proof maintenance — the standard objection, since a proof breaks when the code or spec moves — is not raised anywhere in the talk, so nothing here bounds the recurring cost of keeping 32,000 lines of proof alive across changes.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Validate the Specification, Because the Proof Cannot](validate-the-specification-because-the-proof-cannot.md)
- [Pick a Verification Route by Which Translation You Can Afford](pick-a-verification-route-by-which-translation-you-can-afford.md)
- [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md)
- [Use formal specifications and proofs for critical generated code](use-formal-specifications-and-proofs-for-critical-generated-code.md)
- [Gate Generated Output With a Deterministic Post-Generation Veto](gate-generated-output-with-a-deterministic-veto.md)
- [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md)

Sources:
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 00:12-00:42, 02:20-02:30, 03:04-03:53, 04:03-04:30, 04:41-05:56
