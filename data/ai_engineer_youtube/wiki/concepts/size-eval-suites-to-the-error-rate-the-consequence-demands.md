# Size Eval Suites to the Error Rate the Consequence Demands

Summary: Translate an accuracy percentage into daily harmed users before accepting it, then size the eval suite by the statistics of detecting that failure rate — catching a 1% error with confidence takes hundreds of tests, which is why high-stakes systems combine synthetic cases with continuous human evaluation and grade outputs on a harm scale rather than a correctness bit.

Use when:
- Someone reports agent accuracy as a headline percentage and you need to decide whether it is good enough.
- Setting the size of a regression or release eval suite for a production agent.
- Choosing between synthetic eval data, human evaluation, or both.
- Designing a grading rubric for a system whose failures are not equally bad.

Details:
- Convert the rate into people: at 10,000 calls a day, "most agentic systems would claim 80%, 90% accuracy, and that's great for them. For us, even the 99% is pretty bad" — 1% error means 100 people a day get the wrong appointment type, showing up on the wrong date or time, or worse, missing a critical appointment. "It's not just an annoyance." The acceptable error rate is a property of volume × consequence, not of the model. (Hippocratic AI, 16:24-17:06)
- Detection arithmetic, which sets the suite size: "you need about 450 tests to be 99% sure that you can catch this 1% error rate, and 1,900 tests to be able to see that you've caught it like 10 times." A 20-case eval suite cannot observe a 1% failure mode at all, so a passing suite of that size carries no information about it. (17:06-17:23)
- Consequence: synthetic data alone does not get you there — "you can't purely rely on synthetic data from our experience to be able to get to the scale of accuracy" — so evaluation is a standing human operation. 7,000+ trained clinicians on the platform have run roughly 700,000-800,000 clinical conversations as continuous evaluation, alongside synthetic cases. (17:24-17:52)
- Grade on harm, not correctness: outputs are scored on the same scale used for human clinicians — correctness, no harm, minor harm, severe harm, death — rather than only "correct/valid." Reusing the profession's existing human rubric also makes the AI-vs-human comparison meaningful. (17:53-18:18)
- Reported result across five shipped generations: 99.89% on no-harm, against about 81% for humans on the same rubric. The explanation offered is structural rather than flattering — "AI systems don't get tired and unfortunately we do," and humans don't have "30 plus supervisors helping us at any given point of time" (see [Run Parallel Specialist Models Behind a Speak-Up Gate](run-parallel-specialist-models-with-a-speak-up-gate.md)). (18:18-18:44)
- Benchmarks you need may not exist: none of the common voice benchmarks covered the workflows that decide their product (lab results check, IVR navigation), and no good benchmark existed for the empathy the product depends on, so they built one — HEART — and published the paper. When a quality dimension is load-bearing and unmeasured, building the benchmark is part of the work. (06:47-07:21, 18:45-19:14)

- There is also a prior question that decides whether the statistical half of this is available at all. Ben Hylak asks it first of every team — "how many users do you have?" — because his customers span "millions of users" and "like five," and the method set differs completely: at 10–100 million messages a day "experiments become extremely valuable" and can be run "on a very small sample of your free tier," while at five or ten users he "would not recommend experiments or AB tests." Crucially, the low end is not the low-stakes end; a five-user internal enterprise app "giving like very critical information" sits in the same high-consequence quadrant as this page's clinical example with none of its volume. Consequence sets the target error rate; user count sets which instruments can measure against it ([Match the Quality Method to Your User Count](match-the-quality-method-to-your-user-count.md)). ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 14:27-15:26)

- Sizing has a second dimension this arithmetic does not cover: *where* the cases come from. D'Oro's coverage measurement shows that a sample spread only across repetitions of a fixed starting state produces confidence intervals containing the true performance ~20% of the time rather than 95%, because environment variance is missing from the estimate. Count of cases and spread across configurations are separate budgets, and only the first is set by detection statistics. See [computing intervals over both action and environment variance](compute-confidence-intervals-over-both-action-and-environment-variance.md). ([Computer Use at the Edge of the Statistical Precipice](../sources/20260814_CTLa_p6iOiY.md), 11:05-13:19)
- **The eval as a commercial instrument, not only an engineering one.** Advising founders on how to answer a customer's request for a pilot, Rosenthal lists "an eval on part of their data" alongside a reference call and a seller-driven demo as ways to satisfy the objection without handing over product access. For an AI product these substitutes are not equivalent: only the eval addresses the buyer's actual uncertainty, which is behavior on their distribution rather than behavior in general. That makes the sizing question on this page a sales question too — a slice small enough to run in a week may not be large enough to say anything about the error rate the buyer's use case tolerates, and offering it anyway converts a pilot request into a stalled deal. See [Treat a Pilot as a Second Sales Process You Run for Free](treat-a-pilot-as-a-second-sales-process-you-run-for-free.md). ([Rosenthal](../sources/20260826_wdTRsfw0KG0.md), 07:27-08:15)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Healthcare Operations](../topics/healthcare-operations.md)
- [Voice Agents](../topics/voice-agents.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)
- [Simulate Voice Agents With Probabilistic Conversation Evals](simulate-voice-agents-with-probabilistic-conversation-evals.md)
- [Hire humans for context, verification, and accountability](hire-humans-for-context-verification-and-accountability.md)
- [Run Parallel Specialist Models Behind a Speak-Up Gate](run-parallel-specialist-models-with-a-speak-up-gate.md)
- [Compute Confidence Intervals Over Both Action and Environment Variance](compute-confidence-intervals-over-both-action-and-environment-variance.md)
- [Match the Quality Method to Your User Count](match-the-quality-method-to-your-user-count.md)
- [Treat a Pilot as a Second Sales Process You Run for Free](treat-a-pilot-as-a-second-sales-process-you-run-for-free.md)

Sources:
- [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](../sources/20260819_AN65uc645mE.md), 06:47-19:14
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 14:27-15:26
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 11:05-13:19
- [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../sources/20260826_wdTRsfw0KG0.md), 07:27-08:15
