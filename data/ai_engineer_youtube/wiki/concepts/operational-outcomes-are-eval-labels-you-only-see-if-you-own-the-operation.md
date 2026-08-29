# Operational Outcomes Are Eval Labels You Only See If You Own the Operation

Summary: In an operated business the world produces the eval label for free — the roof is repaired or it is not, the books close or they do not — so the scoring problem that makes most agent evals expensive disappears. The catch is positional: the label lands on whoever owns the outcome, which is the operator, not the vendor who shipped the agent.

Use when:
- Designing evals for agent work whose correctness is not checkable from the transcript.
- Deciding whether to build an LLM judge, hire annotators, or wait for a downstream business event to settle the score.
- Arguing about what a vertical AI company gets from owning operations rather than selling software into them.
- Auditing whether your feedback pipeline captures the human's correction as well as the human's rating.

Details:
- The claim, and the two examples it rests on: agents collaborating with employees on real work generate "rich traces of data and information. Tool calls, the hiccups, the papercuts, everything that goes wrong with doing real work. This in turn allows us to build real-world evals. There is a ground truth here. In the case of the roofing example, the question is, did the roof get repaired? Did the books get closed?" ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 10:52-11:21)
- What that buys, stated as a property of the pipeline rather than of the model: "we get to generate amazing evals that are built and scored automatically." The scorer is the business process. Nobody writes a rubric for whether a roof is fixed. (11:37-11:49)
- The ratchet that follows, which is the operationally useful half: "every week our hill climbing benchmarks become a regression test." A task set used to chase improvement this week becomes the thing that must not break next week, so the eval suite grows out of the optimization work rather than being budgeted separately. (11:21-11:37)
- **The implicit signal most feedback pipelines drop.** Explicit feedback is thumbs up and down plus an optional note. The stronger signal is the correction: "maybe there's some data that the AI generated and there's a real diff between the data that the AI generated and what was ultimately submitted. That's rich information that almost no one else has." A rating says the output was wrong; the diff says what right looked like, and it is produced as a byproduct of the human doing their job. (11:49-12:14)
- Why the position matters, and where the argument is self-serving. Long Lake buys the businesses it deploys into: "we own these businesses. So, when the AI doesn't work, it's not their problem. We're not the vendor. It's our problem… We are the operator owners." A vendor sees the interaction and the rating; the operator also sees whether the world changed. That is a real asymmetry, and it is also the claim that justifies Long Lake's entire structure, so it is argued rather than tested. (04:16-04:31)
- The label is the scarce half, not the corpus. "The most valuable tasks are not on the internet," and the knowledge for them "lives in people's heads, in 20-year-old software, in the way that one senior person on one of these teams just knows how to do it" — which is a data-access problem this wiki already tracks. What is added here is that the *outcome* for those tasks is observable to an operator without annotation, so the expensive step in eval construction is the one that comes free. (10:13-10:52)
- Where this stops. An outcome label is coarse and slow: "did the roof get repaired" arrives days or weeks after the agent's decision, is a single bit, and does not attribute the failure to a step. It answers whether to ship, not what to fix — for which the traces, not the labels, are the substrate. Nothing in the source reports how many tasks are under evaluation, what any of them score, or how the delay is handled.
- Limits. Nothing in this talk is measured; no eval result, pass rate, or task count is given, and the automatically scored evals are described as underway rather than as results. ([Provenance and Limits](../sources/20260828_B0fjR3yaZFU.md))

- **A software-internal instance of the same idea, and a demonstration of how much weaker the label gets when the outcome is not physical.** Uber grades review comments by whether the developer addressed them, which is settled by the existing workflow at no annotation cost — the same structural move as letting the roof repair settle the score. But a repaired roof is the outcome; an addressed comment is a human's reaction to advice, and the human may comply with a wrong comment or reject a right one. So the free label is available much more widely than the operator framing suggests, and its validity degrades as the distance grows between the recorded action and the thing you actually wanted to know. Uber reports 67% addressal with no labelled sample behind it. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 05:47-06:07, 10:29-10:47)
- **The plumbing that makes the free label usable: attribution back to the decision.** Notion's fourth layer requires that "every action is a decision log and every outcome threads back to the decision that caused it," which is what lets engagement history re-enter the decision layer and drive continue / advance / pivot. The position argument is the same as this page's — the outcomes accrue to the operator running its own go-to-market — and the addition is that owning the operation is necessary but not sufficient: without decision-level attribution the label lands on a dashboard and an analyst reads it. ([Liu](../sources/20260826_L4I7WgiEquo.md), 14:53-15:37)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Learn coding preferences from implicit edit feedback](learn-coding-preferences-from-implicit-edit-feedback.md)
- [High-Value Vertical Data Is Withheld by Design](high-value-vertical-data-is-withheld-by-design.md)
- [Continual Learning and Enablement Are One Loop With a Cold Start](continual-learning-and-enablement-are-one-loop-with-a-cold-start.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)
- [Thread Every Outcome Back to the Decision That Caused It](thread-every-outcome-back-to-the-decision-that-caused-it.md)

Sources:
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 04:16-04:31, 10:13-12:14
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 05:47-06:07, 10:29-10:47
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 14:53-15:37
