# Separate generation and verification prompts or models

Summary: Agent workflows can borrow the high-assurance pattern of separate implementation and verification teams by using distinct prompts, contexts, or model providers for coding and testing. The goal is to reduce shared assumptions between the agent that creates code and the agent or process that validates it.

Use when:
- Designing coding-agent review flows for changes where confirmation bias or shared blind spots are likely.
- Choosing whether to use a second model, second prompt, or independent context for tests and safety analysis.

Details:
- The source recommends adapting independent verification teams into agent workflows by using separate prompts for testing versus writing code. 27:10-27:28
- It suggests using multiple model providers when stronger diversity is needed: one foundation model can generate tests while another writes the implementation. 27:28-27:39
- This pattern complements explicit risk analysis and safety cases, where the LLM describes what could go wrong and how the code mitigates each failure. 26:37-27:05
- The source also names adversarial testing as part of the high-assurance agent toolkit. 33:46-33:59
- **A stronger form of the same instinct: vary the method class, not just the model.** Chatterjee (Sonar) argues that prompt- or provider-level separation still leaves both sides inside one technique — "different AIs will write code in different ways, and… you're not going to want to use that same AI to validate the code because you're going to want a diversity of… tools" — and compresses it to "use a different methodology to review the code that was used to write the code." On that reading, the patterns on this page are the weak form of independence and a computational analyzer beside the LLM reviewer is the strong form; the two are complements, since a deterministic layer cannot judge intent. See [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md). Asserted in a vendor talk, with no measurement of what either layer catches that the other misses. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 09:35-10:13)
- Volkov (ThursdAI) captures why self-grading fails with an exam analogy: having the same agent write the code, inspect the outputs, and write the tests is "like coming up with an exam, taking it, and scoring myself" — not productive. The same caveat applies to self-verifying loops: "if the builder grades itself, you didn't remove the review, you hid it." (ZpK5PWX2YRM 15:33-19:45)
- **A third axis, orthogonal to both and cheaper than either: vary what the verifier is shown.** Coyle's critic subagent gets "the claim and the evidence, but we're not giving it the thought processes that went in to creating this claim," because "when you get a bunch of agents together collaborating and talking to each other, there's a tendency to have group think. And all the agents seem to kind of devolve into one idea." This works even when the verifier is the same model behind the same prompt, and it also says something uncomfortable about the patterns on this page: a second provider handed the first one's full reasoning trace has had part of its independence spent before it starts. See [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md). Asserted by analogy, with no agreement-rate measurement. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 13:44-15:12)
- **Ordering is a fourth separation, available when a second prompt or model is not.** Where this page separates the generator from the verifier by prompt or by model, the same independence can be bought by sequence alone: have the agent commit the test before the implementation exists, because otherwise "it will fit the test to the code rather than fit the code to pass the verification criteria." Nothing has to be duplicated, so it applies inside a single-agent loop where a second verifier would be too expensive — and it is correspondingly weaker, removing the fitting failure without touching the shared blind spots. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 06:12-06:42)

- **Separation can be structural instead of procedural.** Varying prompt, context, or provider still leaves two systems drawn from similar training distributions. In a proof-carrying setup the verifier is not a model at all — it is a fixed program small enough that "you yourself can actually go write one," with open-source kernels "in C++, Rust, Lean" — so there is no shared prior for assumptions to leak through, and "you only need to trust the small kernel." This is available only where the property can be formalized, so it complements rather than replaces the prompt- and model-level separation described above. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 02:20-02:30, 04:14-04:30)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Use hierarchical verification before trusting weak agent feedback](use-hierarchical-verification-before-trusting-weak-agent-feedback.md)
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)
- [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md)
- [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)
- [Write the Test First So the Agent Cannot Fit It to the Code](write-the-test-first-so-the-agent-cannot-fit-it-to-the-code.md)
- [Ship a Proof a Small Kernel Can Recheck, Not a Claim You Must Trust](ship-a-proof-a-small-kernel-can-recheck.md)

Sources:
- [Vision: Zero Bugs — Johann Schleier-Smith, Temporal](../sources/20251124_qLqttdO33UM.md), 26:37-27:43, 33:46-33:59
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../sources/20260710_ZpK5PWX2YRM.md), 15:33-19:45
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 09:35-10:13
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 13:44-15:12
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 02:20-02:30, 04:14-04:30

- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 06:12-06:42
