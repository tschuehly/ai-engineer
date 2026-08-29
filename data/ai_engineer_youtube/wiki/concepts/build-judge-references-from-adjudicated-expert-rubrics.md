# Build Judge References From Independently Written, Adjudicated Expert Rubrics

Summary: When many different responses to the same question are all correct, a golden answer is the wrong reference. Take real cases, have two domain experts *independently* write rubrics listing the elements a good response should contain, have a third adjudicate the two into one rubric, have a fourth QA it, and let an LLM judge semantic-match the system's answers against those elements.

Use when:
- Building an eval for open-ended expert output — clinical answers, legal analysis, advisory writing — where "there's many infinite possible responses."
- An LLM judge exists but its verdicts are not trusted, because nothing grounds them outside the model.
- Deciding how to spend scarce expert time so its judgment keeps paying after the experts stop reviewing.

Details:
- Why not a golden answer: "what we need is we actually need human references to tell are we generating the right thing. But you can't just create a human golden response because there is a lot of variability in the potential responses." ([From Ambient Documentation to Clinical Intelligence](../sources/20260819_u6q-byPWUuo.md), 16:53-17:07)
- The unit of ground truth is an element list, not a text: a rubric holds "elements of what we wanted in the response… not here's the exact response … but a good rubric [of] elements that what a good response would look like," attached to a real clinical case with its context. (17:07-17:20, 17:32-17:40)
- The four roles, and what each buys. Two physicians write rubrics independently, so the two drafts are a disagreement signal rather than one expert's opinion. A third "adjudicated it, brought these two independent rubrics together, created a final rubric." A fourth clinician does QA on the rubrics. Four experts are spent on the *reference*, not on scoring runs. (17:20-17:32)
- Scoring is then cheap and repeatable: "we can actually have an LM judge that compares our agent's responses to these rubric elements and does some basic semantic match" — the judge's job is reduced to element matching rather than holistic quality assessment, which is what makes it hill-climbable "whether it's our agent architecture, our models, or search ranking algorithms." (17:40-17:57)
- The organizational payoff is why the investment is worth it: Abridge has "clinicians embedded throughout the entire company," but "not all of us are clinicians. I'm not a clinician. So how can we, the rest of the company, still move fast is by encoding that clinician judgement into LM judges," and "those judges, once you have that, create a feedback loop so that anyone, whether you're a clinician or not, can actually hill climb and learn from that." The design criterion is stated as a property: "a really great evaluation system … reflects the behaviors that you want in your product." (13:47-14:31)
- The clinical quality judge is one of several — safety, adversarial boundaries, and tone/style get their own judges — because a collapsed [generator–verifier gap](size-your-eval-effort-to-the-generator-verifier-gap.md) is not fixable by improving one score. (16:21-16:49)
- Position against neighbouring wiki pages: [decompose evals into rubrics to target the failing behavior](decompose-evals-into-rubrics-to-target-the-failing-behavior.md) uses rubrics as a *diagnostic* over an existing correctness signal, whereas here the rubric *is* the correctness signal because no other one exists. [Stage regulated LLM evals from experts to automated judges](stage-regulated-llm-evals-from-experts-to-automated-judges.md) converts expert judgments into golden data, which presupposes a golden answer; this is the branch to take when the golden answer does not exist. And [validate the simulated user and the judge](validate-the-simulated-user-and-the-judge.md) checks a judge against expert labels after the fact, where this builds the expert consensus into the reference up front.
- **A source that reaches the opposite conclusion about written references, and the variable that reconciles them.** Fox built the strongest rubric-based judge he had seen — frontier model, faithfulness rubric with worked pass/fail examples, rubric auto-optimization, deterministic concept counting — and reports that "one in five of those clean passes still had some sort of serious error buried in it," concluding that "a rubric that you pre-specify is only the taste you could write down. The taste that matters is the part that you couldn't." That is not a refutation of this page's procedure, because the two rubrics are different objects: Abridge's is an element list pinned to *one* case and adjudicated once, whereas the rubric Fox rejects is a global faithfulness standard applied to every case. The reconciling variable is whether the standard is stable per case or has to be re-decided per case — his Lake Malawi example is precisely a materiality judgment that no case-independent rubric can carry. The cost side inverts accordingly: four experts per reference item is affordable when the reference holds, and unaffordable when it has to be re-authored as guidelines, models, and local definitions move. See [Keep a Moving Standard in Examples, Not in a Rubric or the Weights](keep-a-moving-standard-in-examples-not-in-a-rubric-or-the-weights.md). ([Fox](../sources/20260822_yqF6XhzbWBk.md), 09:02-10:12, 11:36-12:36)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Size Your Eval Effort to the Generator–Verifier Gap](size-your-eval-effort-to-the-generator-verifier-gap.md)
- [Decompose Evals Into Rubrics to Target the Failing Behavior](decompose-evals-into-rubrics-to-target-the-failing-behavior.md)
- [Stage Regulated LLM Evals From Experts to Automated Judges](stage-regulated-llm-evals-from-experts-to-automated-judges.md)
- [Validate the Simulated User and the Judge Before Trusting a Simulation](validate-the-simulated-user-and-the-judge.md)
- [Check Whether the Judge Is Right Before Changing the Agent](check-the-judge-before-changing-the-agent.md)
- [Hand Domain Experts the Pipeline as Skills](hand-domain-experts-the-pipeline-as-skills.md)
- [Keep a Moving Standard in Examples, Not in a Rubric or the Weights](keep-a-moving-standard-in-examples-not-in-a-rubric-or-the-weights.md)
- [Capture Expert Reasoning and Corrections, Not Just a Score](capture-expert-reasoning-and-corrections-not-just-a-score.md)

Sources:
- [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](../sources/20260819_u6q-byPWUuo.md), 13:47-14:31, 16:21-17:57
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 09:02-10:12, 11:36-12:36
