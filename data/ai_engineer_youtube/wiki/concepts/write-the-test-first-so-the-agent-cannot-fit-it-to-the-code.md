# Write the Test First So the Agent Cannot Fit It to the Code

Summary: When an agent writes the implementation and then writes its test, the test is authored with the answer already in hand and gets shaped to whatever the code does. Reversing the order — criterion first, then implementation — makes the check a target the agent must reach rather than a description of what it produced. Ordering is the cheapest independence axis available between a generator and its verifier: same model, same prompt, same method, only the sequence changes.

Use when:
- An agent's changes always arrive with passing tests and the tests never seem to catch anything.
- Deciding whether "have the agent write tests" is a verification win or a verification theatre.
- You want generator/verifier independence but cannot afford a second model, a second harness, or a second review pass.
- Writing the prompt or skill that governs how an agent implements a task.

Details:
- **The claim and its reason.** "If you tell your agent to write the [test for] the code that you're writing… at the red to green to red to green[,] at the TDD style, it almost always gives you better results because you set a goal, then you tell the agent to strive toward that goal… better results than writing the code and then writing the test afterward because then it will fit the test to the code rather than fit the code to pass the verification criteria." ([Blum](../sources/20260828_5Bn0xro2ol8.md), 06:12-06:42)
- **What makes this more than restated TDD.** For a human, test-after is mostly a discipline problem — the developer knows what the code should do and may write a weak test out of haste. For an agent, test-after is a *structural* problem: the agent is optimizing for a passing check, and when it authors the check after seeing the output, the cheapest path to passing is to describe the output. The failure needs no bad intent and leaves no trace, because the artifact produced is a green test suite.
- **Placement in the wiki's independence taxonomy.** The existing pages vary *who or what* verifies: [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md) changes the method class, [Separate generation and verification prompts or models](separate-generation-and-verification-prompts-or-models.md) changes the prompt or the model, and [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md) changes what the reviewer is allowed to see. This page changes none of those — it changes *when*. The criterion is committed before the output exists, which denies the generator the one input it would need to trivially satisfy itself. It is the only axis on the list that costs nothing to adopt.
- **It is also the weakest axis, and should be stacked rather than substituted.** A test written first still comes from the same model with the same blind spots about what is worth testing; ordering removes the fitting failure, not the coverage failure. It is a complement to the layers in [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md), not a replacement for any of them.
- **The ordering rule is what makes a self-verifying loop safe to run at all.** [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md) warns that an agent checking its own work relocates the review rather than eliminating it. Test-first is the cheapest structural constraint that keeps such a loop honest about at least one thing: the loop's exit condition was fixed before the loop started.
- **The surrounding argument this sits inside** is a left-shift of verification generally: "anytime that we can left shift anything in our workflow from a human needing to do it to an agent being able to verify it," with the further step of freezing anything that proved useful into a deterministic flow, because "you also know that you're using the LLM when it needs to reason, but when you have something that is already known and basically can be encoded into a test, spending that time always pays dividends." (05:00-06:11)
- **Caveats.** "Almost always gives you better results" is an unquantified impression from one practitioner — no pass rate, defect rate, or comparison is offered, and the wiki has no measurement anywhere of how much fitting actually occurs in test-after agent runs. The rule also assumes the criterion is expressible before the code exists, which is exactly the condition that fails for exploratory, visual, and stateful work; where a task cannot be specified up front, test-first is unavailable and the other independence axes have to carry the load.

- **The order rule at its limit, and where the fitting risk moves.** In a verification workflow the criterion is written first by construction and cannot be bent afterwards, because the kernel checks the proof against the stated theorem and "an incorrect proof is rejected immediately." The fitting pressure does not disappear, though — it relocates to whoever writes the property, which is why Pant makes spec authorship a separate step with its own check: the specification is written directly in Lean or auto-formalized from natural language, and then "you validate the specification. So, either the human reviews it, or you test that it holds on some inputs." An agent that writes both the property and the proof has recreated the problem one level up. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 01:23-01:52, 04:03-04:14)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md)
- [Separate generation and verification prompts or models](separate-generation-and-verification-prompts-or-models.md)
- [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)
- [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md)
- [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)
- [Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)
- [Structure an Agent Plan With a Frozen Why and Reviewer-Sized Phases](structure-an-agent-plan-with-a-frozen-why-and-reviewer-sized-phases.md)
- [Validate the Specification, Because the Proof Cannot](validate-the-specification-because-the-proof-cannot.md)

Sources:
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 05:00-06:42
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 01:23-01:52, 04:03-04:14
