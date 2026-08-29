# Show the Prompt Diff So a Non-Engineer Can Promote an Optimized Judge

Summary: Automated judge-prompt optimization has an adoption gate that is separate from its accuracy: someone has to decide the optimized prompt is now the team's judge. When that someone is a product manager or an operator rather than the engineer who ran the optimizer, the blocker is legibility — "a lot of this is a closed box." DoorDash's answer was to render the original system prompt and the calibrated prompt side by side next to the score movement, and to make promotion an explicit human act.

Use when:
- A prompt optimizer (GEPA, DSPy, or similar) produces a better-scoring judge and nobody outside the engineering team will adopt it.
- Designing a self-serve calibration surface for people who will own a judge but not read optimizer internals.
- Deciding what an automated optimization run must expose beyond its final metric.
- The judge's owner is not the person who runs the optimization.

Details:
- **The loop being wrapped is ordinary; the wrapping is the contribution.** Start from a judge prompt, decide "what exactly do you want to measure from the output," run the judge across your traces for baseline scores, then run an optimization loop against a golden dataset — with the caption-garbled "JPEA library," described as "a pretty commonly used library out there for prompt optimization," as the optimizer. ([Paranjape](../sources/20260828_bMjlRrWjdT0.md), 10:29-11:14)
- **The stated blocker is trust, not accuracy.** "A lot of this is a closed box where you can't really — it's hard to see what's actually happening. So the second piece that we built was actually giving them visualization and visibility into what's actually happening… we actually show the original system prompt and the calibrated prompt to our partners so that they are also able to gain that trust as we build this." The artifact is a prompt diff plus the score movement on the same screen, and its purpose is a human decision, not debugging. (12:19-12:58)
- **Promotion is an explicit step with a named actor.** "Once the iteration loop is complete, our partner teams are happy, they're going to then elevate that judge prompt as their LLM as a judge." The optimizer proposes; the owning team promotes. Nothing is auto-adopted on a score improvement, which is what keeps a judge from silently drifting under its own optimizer.
- **The friction it was built to remove is organizational.** "What we wanted to do was really reduce the friction of back and forth with an engineering team. So we tried to really remove all the complicated logic and make this into a self-serve UI." A PM or operator sets the configs and runs the calibration themselves, choosing the model — "in this example I have Gemini, they can run it using any of the Claude or the OpenAI models too" — without knowing which knobs the optimizer exposes. (11:35-12:19)
- **The justification for self-serve is the field's immaturity, which cuts both ways.** "LLM as a judge as a concept, the whole prompt calibration concept might be straightforward to a lot of folks, but it is still like a pretty new and evolving field." Handing an unsettled technique to non-specialists is defensible when the alternative is a queue at the engineering team — and it is also how a badly-calibrated judge gets promoted by someone who cannot tell that the score improved because the rubric learned the label distribution rather than the criterion. This surface shows what changed; it does not show whether the [dev/test discipline behind the number](calibrate-llm-judges-like-binary-classifiers.md) was sound. (11:24-11:47)
- **Where it sits against the wiki's other judge-optimization material.** [Optimize Judge Prompts With Diagnostic Feedback](optimize-judge-prompts-with-diagnostic-feedback.md) is about what the *optimizer* must see — verdict, ground truth, reasoning — to repair a rubric. This page is about what the *human owner* must see to accept the repair. They are complementary and independently necessary: an optimizer with rich diagnostics that emits only a new prompt and a number still stalls at the person who has to sign off on it.
- **What is not reported.** No score, no before/after number, no accuracy delta — only "one of the good examples where we saw like a significant amount of improvement in the judge prompt," narrated over a screenshot. There is also no account of how often partners *rejected* a calibrated prompt after reading the diff, which is the measurement that would show the review step is doing work rather than rubber-stamping. (12:36-12:58)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Optimize Judge Prompts With Diagnostic Feedback](optimize-judge-prompts-with-diagnostic-feedback.md)
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Evaluator Quality Is a Dependency of Prompt Optimization](evaluator-quality-is-a-dependency-of-prompt-optimization.md)
- [Check Whether the Judge Is Right Before Changing the Agent](check-the-judge-before-changing-the-agent.md)
- [Keep Judge-Prompt Ownership Configurable While the Org Is Still Learning](keep-judge-prompt-ownership-configurable-while-the-org-is-still-learning.md)
- [Mature Eval Platforms From Spreadsheets Into Experiment Systems](mature-eval-platforms-from-spreadsheets-into-experiment-systems.md)

Sources:
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 10:29-12:58
