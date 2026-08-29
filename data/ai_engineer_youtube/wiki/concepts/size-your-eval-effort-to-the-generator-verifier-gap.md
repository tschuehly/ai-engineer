# Size Your Eval Effort to the Generator–Verifier Gap

Summary: How hard evaluation will be is a property of the task, not of your tooling: when checking an answer is far easier than producing one, evals are cheap and you can hill-climb freely, but when checking is nearly as hard as producing, any verifier good enough to trust would already be your generator — so the reference has to come from outside the model, and the target has to be covered by several partial judges instead of one score.

Use when:
- Deciding how much of a project's budget the eval system deserves, before building it.
- Considering LLM-as-judge for a domain where you cannot say why an answer is right.
- Explaining why a technique that worked on code or math evals does not transfer to a clinical, legal, or advisory product.

Details:
- The contrast is stated with Sudoku: "it's really really hard to generate a solution to Sudoku, but it's extremely easy to verify once you do have the solution. And that makes it much easier to hill climb against and build evaluation for." ([From Ambient Documentation to Clinical Intelligence](../sources/20260819_u6q-byPWUuo.md), 15:44-16:04)
- The collapsed case is contextual clinical decision support — "does this patient meet the criteria for febrile neutropenia?" answered from EHR labs, the live doctor-patient conversation, and clinical guidelines — where "the generator and verifier gap is really small. If I had a really really good generator verifier, then that would just be my generator itself." The operative question becomes "how do I create a reference that isn't just a language model itself and ground itself to I have trust?" (14:48-16:20)
- First response: buy the reference from humans, but not as a golden answer, because many different responses can be right. See [build judge references from independently written, adjudicated expert rubrics](build-judge-references-from-adjudicated-expert-rubrics.md).
- Second response: stop trying to measure the target with one number. Abridge runs "many many different signals" at once — a clinical quality judge, "a boundary and adversarial judge," a clinical safety judge, and judges for product aspects "like tone and style, and that matters a lot as well for AI products" — each getting "a piece of this like really really hard to measure problem." A small gap is an argument for coverage by partial signals, not for a better single judge. (16:21-16:49)
- The gap is what determines whether stakes are affordable. Asawa's contrast with his previous product is explicit: at Glean "I could be wrong and it would have been fine. Maybe we answered a question incorrectly. But in healthcare, if we answer something incorrectly, there's actually consequences and we entirely lose our trust." High stakes plus a wide gap is manageable; high stakes plus a collapsed gap is what makes evaluation the hard part of the product. (11:47-12:07)
- This is the mechanism behind the wiki's harder claim that [you cannot iterate on output you cannot judge](you-cannot-iterate-on-output-you-cannot-judge.md), and the two diagnose the same failure from different sides. That page locates the gap in the *team* (nobody on staff can tell whether the output is good, and the remedy is to hire the practitioner); this one locates it in the *task* (verification is intrinsically near as hard as generation, even for the experts you employ). Abridge already has clinicians embedded throughout the company and still cannot write a golden answer — which is why its remedy is a reference-construction procedure rather than a hire.
- The same boundary appears in RL: verifiable rewards work "really good at math and code because you have answer keys," which is the wide-gap regime, and the technique does not transfer to domains that cannot be checked mechanically. See [use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md).
- **The gap is composite inside a single task, which changes how you size it.** Fox splits verification into two sub-tasks with opposite economics: spotting what differs between a transcript and a generated note is cheap and mechanical, while deciding which of those differences matters is, he argues, "harder than writing that plausibly good general note in the first place. Because that standard of good was never written down anywhere that the judge can read it." An ambient scribe therefore has a *wide* gap on detection and a *collapsed* one on materiality — so a team that measures the task as cheap-to-verify, builds the eval accordingly, and then finds it missing serious errors has not mis-sized the effort but mis-located it. The diagnostic question is which half a given judge score is reporting. See [Verification Is Cheap for Detection and Expensive for Materiality](verification-is-cheap-for-detection-and-expensive-for-materiality.md). ([Fox](../sources/20260822_yqF6XhzbWBk.md), 06:05-06:49, 10:54-11:36)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Build Judge References From Independently Written, Adjudicated Expert Rubrics](build-judge-references-from-adjudicated-expert-rubrics.md)
- [You Cannot Iterate on Output You Cannot Judge](you-cannot-iterate-on-output-you-cannot-judge.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Check Whether the Judge Is Right Before Changing the Agent](check-the-judge-before-changing-the-agent.md)
- [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)
- [Verification Is Cheap for Detection and Expensive for Materiality](verification-is-cheap-for-detection-and-expensive-for-materiality.md)

Sources:
- [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](../sources/20260819_u6q-byPWUuo.md), 11:47-12:07, 14:48-16:49
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 06:05-06:49, 10:54-11:36
