# Verification Is Cheap for Detection and Expensive for Materiality

Summary: Verifier's law is not a property of a whole task — it holds for the detection half and inverts on the materiality half. Spotting what differs between a source and an output is mechanical and cheap; deciding which of those differences matters can be harder than producing the output was, because the standard that decides it was never written down anywhere the checker can read.

Use when:
- Deciding whether "the checker's job is easier than the generator's" applies to your task before budgeting an eval system around it.
- A judge reliably finds diffs, hallucinations, and contradictions and still misses the failures your domain experts care about.
- Porting an eval technique that worked on code or math into summarization, extraction, note-taking, contract review, or advisory output.
- Explaining to a team why adding a stronger model to the judge does not move the numbers that matter.

Details:
- **The asymmetry argument, stated in its strongest form first.** "The generator has to get everything right and pay attention to lots of varying instructions, whereas the checker only has to find the one thing that's wrong and just focus on that task. You can also give it more time, more tokens, the exact failure modes to hunt for. Evaluation should be easier than generation. It's the asymmetry of verification, verifier's law." Fox grants the whole argument before splitting it. ([Fox](../sources/20260822_yqF6XhzbWBk.md), 07:56-08:38)
- **Where the free verifier came from, and what its absence costs.** "In math or code, the verifier comes free — a unit test, a compiler. But for 'is this note safe and complete', there's no unit test. You have to build the verifier yourself, and verification is only easier than generation for the easy bit, i.e. spot the difference between transcript and note." The domains where verifier's law paid off are exactly the ones where somebody else already built and validated the checker. (10:54-11:20)
- **The half that inverts.** "The hard bit is knowing, of all those differences you've seen, which matter. And that's harder than writing that plausibly good general note in the first place. Because that standard of good was never written down anywhere that the judge can read it." The generator only has to produce something defensible; the verifier has to hold an ordering over every possible defect. (11:20-11:36)
- **What is left when the two halves are separated.** The generator failure classes are only three — "it adds something that was never said, it changes something that was, or it omits something that should be there" — and "the blatant version of each of these is really easy to catch. The hard part in all three is the same. It's telling whether that thing that was added or changed or dropped actually matters… A dropped line of small talk versus a dropped allergy." Detection collapses the space to a diff; materiality is a separate scoring problem over that diff. (06:05-06:49)
- **The demonstration that materiality is not a property of the edit.** Two patients with blood in the urine, both notes dropping the same kind of line about where they had been on holiday: France in one, Lake Malawi in the other. "Same omission, same shape, same mistake" — except "the France trip is irrelevant. The Lake Malawi trip is the diagnosis. Fresh water in sub-Saharan Africa means schistosomiasis until proven otherwise, and it completely changes what the management plan is." No property of the diff distinguishes them; only the case does. (11:56-12:36)
- **The consequence for eval design.** Any technique whose leverage is "make the checker better at finding things" — a stronger model, a longer rubric, more tokens, deterministic diffing — improves the half that was already cheap. Fox's own strongest judge included frontier reasoning, worked pass/fail examples, rubric auto-optimization, and deterministic medical-concept counting, and its residual failure was materiality, not detection. See [A Judge Without Taste Is a Second Silent Failure](a-judge-without-taste-is-a-second-silent-failure.md). (09:02-09:49)
- **How this refines the wiki's generator–verifier gap page.** [Size Your Eval Effort to the Generator–Verifier Gap](size-your-eval-effort-to-the-generator-verifier-gap.md) treats the gap as one scalar per task, sized before you build. This source shows the gap is composite even inside a single task: ambient scribing has a wide gap on detection and a collapsed one on materiality, which is why teams measure a "cheap to verify" task and then find the eval failing anyway. The practical test is to ask which half your judge's score is actually reporting.
- **Caveat on the evidence.** The claim that materiality is harder than generation is argued, not measured; no experiment separates the two costs. What is measured — on the speaker's own generated dataset — is that a strong detection-oriented judge misses serious errors at a rate of about one in five of the notes it passes. (09:49-10:12)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [A Judge Without Taste Is a Second Silent Failure](a-judge-without-taste-is-a-second-silent-failure.md)
- [Size Your Eval Effort to the Generator–Verifier Gap](size-your-eval-effort-to-the-generator-verifier-gap.md)
- [An Output Faithful to the Source Can Be Wrong About the Decision](an-output-faithful-to-the-source-can-be-wrong-about-the-decision.md)
- [You Cannot Iterate on Output You Cannot Judge](you-cannot-iterate-on-output-you-cannot-judge.md)
- [Keep a Moving Standard in Examples, Not in a Rubric or the Weights](keep-a-moving-standard-in-examples-not-in-a-rubric-or-the-weights.md)
- [Prefer Outcome Verifiers Over Ground-Truth Path Checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)

Sources:
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 06:05-06:49, 07:56-08:38, 09:02-10:12, 10:54-12:36
