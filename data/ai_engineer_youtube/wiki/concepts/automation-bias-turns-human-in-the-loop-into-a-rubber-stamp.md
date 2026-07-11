# Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp

Summary: "Human-in-the-loop" quietly assumes the human produces genuine discernment, but under throughput and trust pressure even skilled reviewers defer to AI signals with minimal scrutiny — so a human oversight step can log rubber stamps as if they were independent judgment. Measure whether your loop actually elicits deliberation before you trust it as a safety layer.

Use when:
- Deciding whether a human-review or approval gate is real oversight or a false safety net.
- Designing high-stakes review workflows (fraud, cheating detection, moderation, admissions, medical, legal) where a reviewer confirms AI alerts.
- Auditing why "accept" rates are suspiciously high or why the model looks more accurate than it is.

Details:
- Cognitive surrender (Wharton, Shaw & Nave 2026): humans forgo deliberation and adopt AI output as their own with minimal scrutiny. In a study giving humans AI resources on reasoning exams, human accuracy rose ~25 pts when the AI was right and fell ~15 pts when it was wrong, and **80% of participants accepted AI answers even when they were wrong** — AI can supplant a human's thinking without the human noticing. As AI enters atomic daily tasks (GPS routes, search-engine AI summaries over primary sources), trust rises and caution drops. ([source](../sources/20260707_CDqzWpwkSls.md), 01:19-03:31)
- The Duolingo English Test "When Machines Mislead" experiment made the failure concrete: inject a *fabricated* copy-typing cheating signal into clean (no-cheating) historical sessions and present them to proctors as normal workflow. Experienced proctors — scoring **>90% on accuracy calibration** — accepted **50% of the fake signals**, i.e. falsely accused test-takers half the time. A coin-flip rate is strong evidence of automation bias: deferring judgment to AI without looking for corroborating evidence. (05:33-07:24)
- Crucial diagnosis: it was **not the model** (1% false-positive rate, and these were negatively-predicted sessions) and **not the people** (skilled, experienced reviewers) — the failure lived in the interface/interaction, which is where the fix belongs. In a high-stakes exam feeding visa and college-admissions decisions, a coin-flip reviewer is unacceptable. (07:24-08:22)
- Mechanism (the vicious cycle): a frictionless interface lets humans rubber-stamp confident model calls; the "yes" is logged as truth; the model grows more confident and the human more deferent until "the AI becomes the person in the driving seat." More oversight headcount does not fix this — the loop has to be engineered to force independent judgment. (10:00-11:56)
- Practical tell: if a review step only collects a binary accept/reject that skews heavily to accept, you likely have automation bias, not oversight. The corrective is to force the human to be an investigator who cites independent evidence (see the related discernment concept) and to capture what they actually changed (see the training-label concept).

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Engineer the Interaction, Not the Model, for Discernment](engineer-the-interaction-not-the-model-for-discernment.md)
- [Treat Every Human-AI Interaction as a Training Label](treat-every-human-ai-interaction-as-a-training-label.md)
- [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)

Sources:
- [Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo](../sources/20260707_CDqzWpwkSls.md), 01:19-11:56
