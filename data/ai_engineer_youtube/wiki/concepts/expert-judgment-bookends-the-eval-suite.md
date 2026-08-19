# Expert Judgment Bookends the Eval Suite

Summary: In a domain where correctness is a professional judgment, the expert enters the loop twice: before any prompt exists, to define what good looks like as hundreds of test cases, and after the suite passes, as a person who uses the product and notices the register drifting. The suite in between is run tens of thousands of times to surface outliers, with a zero-tolerance bar on the safety subset.

Use when:
- Starting an agent in a professional domain and deciding what the first artifact should be.
- Deciding what a domain expert's standing contribution is, beyond reviewing production output.
- Setting a pass bar for a stochastic suite that mixes ordinary quality cases with safety cases.
- A conversational product passes its evals and something about it still feels wrong.

Details:
- **Order of operations: the clinician precedes the prompt.** "Start with your clinician, not with your prompt. Sit with your clinician, encode what good looks like in evals. Write hundreds of evals TDD style. That becomes your number one tool." Two claims are packed in: the expert's first deliverable is the specification, not feedback on a draft; and the specification's form is executable cases rather than a written brief. ([Tony Fabrikant](../sources/20260819_yoONZwV2smc.md), 14:38-14:57)
- **Failing first is treated as the normal state.** "Watch those evals fail" is the expected outcome of writing the suite before the system — the TDD framing is used literally, with the suite defining the target the prompt and harness are then built toward. ([Tony Fabrikant](../sources/20260819_yoONZwV2smc.md), 15:00-15:02)
- **Volume is aimed at the tail, not the average.** "Run your agent through them thousands of times, tens of thousands of times. Watch for those outliers." The object of interest is the rare bad run, which a single pass or a pass-rate average hides by construction. ([Tony Fabrikant](../sources/20260819_yoONZwV2smc.md), 15:02-15:09)
- **The safety subset gets a different bar than everything else.** "When safety's on the line, even one failing test is not okay." This qualifies the repeated-run pass-rate gate the wiki documents from Maven Clinic (hundreds of integration tests, many runs each, a ~90% threshold): a rate bar is right for quality cases and wrong for the safety subset, so the suite needs at least two classes with different pass semantics rather than one global threshold. ([Tony Fabrikant](../sources/20260819_yoONZwV2smc.md), 15:09-15:13)
- **The residual: tone has no scorer, so the builder has to be a user.** "No matter how many evals you run and write, nothing replaces your gut when emotional context is on the line. So eat your own dog food. Talk to your agent. Feel when the tone starts shifting off." This is a claim about a specific gap rather than general skepticism about evals — emotional register is exactly the property that survives a passing suite, because each response is individually defensible and the drift is in how the whole thing lands. ([Tony Fabrikant](../sources/20260819_yoONZwV2smc.md), 15:14-15:33)
- **Dogfooding here means real stakes, not a test account.** Fabrikant used the product with his partner "since the beginning of my relationship," through "some serious situations early on" and later milestones such as moving in together, and reports "Maxine really challenged me about how I showed up." The detection method requires the builder to be in the situation the product is for; a synthetic session would not register the tone shift the same way — which also bounds the pattern, since most teams cannot dogfood their domain and have to buy the equivalent signal from expert users. ([Tony Fabrikant](../sources/20260819_yoONZwV2smc.md), 15:33-16:03)
- **The closing formulation ties both ends together.** "Partner with a clinician who challenges you to aspire to create AI that meets the clinical standard, so that you can create AI that challenges your users." The expert relationship is framed as adversarial in the same way the product's relationship to its user should be — the property being transferred through the eval suite is a willingness to say the unwelcome thing. ([Tony Fabrikant](../sources/20260819_yoONZwV2smc.md), 16:12-16:25)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Earn Release Confidence From Repeated Runs and Post-Launch Sampling](earn-release-confidence-from-repeated-runs-and-post-launch-sampling.md)
- [Use Evals as Durable AI System Specifications](use-evals-as-durable-ai-system-specifications.md)
- [Build Judge References From Independently Written, Adjudicated Expert Rubrics](build-judge-references-from-adjudicated-expert-rubrics.md)
- [AI System Evaluation Still Depends on Human Review](ai-system-evaluation-still-depends-on-human-review.md)
- [Encode the Field's Validated Method, Not General Empathy](encode-the-fields-validated-method-not-general-empathy.md)

Sources:
- [AI is the World's largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI](../sources/20260819_yoONZwV2smc.md), 14:38-16:25
