# Sort Failures by Whether the User Can Retry

Summary: Refuse a single reliability bar for a GenAI product. Sort each action by whether a wrong answer is absorbed by the user clicking again or escalates immediately, accept the tolerable class at a rate that would be unacceptable elsewhere, and spend the extra machinery — several different models reading the same input, proceeding only on agreement, handing off to a human on disagreement — only on the class that cannot be retried.

Use when:
- Setting reliability targets for a product where different actions have very different consequences.
- Deciding which agent actions deserve cross-model verification and which do not.
- Justifying why a team is *not* trying to eliminate hallucination everywhere.
- Designing the fallback for a verification step that fails to resolve.

Details:
- The starting position is that traditional software "does what we implement there, no more, no less," whereas for GenAI "hallucination is there. We cannot ignore it," and "completely eliminating them can be very costly. Sometimes is not necessary, either." So the first design step, "even from the get beginning," is "identify which failures is acceptable, which ones are not acceptable." (Maven Clinic, 13:29-14:11)
- The tolerable class is defined by user-absorbable recovery, not by a low number: an appointment-scheduling action failing one in a thousand "probably it's okay. I'm not saying it's a good experience, but the users really can just click the button again, we will reschedule for them." The retry, not the error rate, is what makes it acceptable. (14:11-14:28)
- The intolerable class is defined by immediate escalation in *either* direction: on reimbursement claims, "if people ask of $200, we issue them 50 or they ask 50, we give them 200. Each case will cause a escalation right away." Overpaying and underpaying are both incidents, so there is no safe side to bias toward and no tolerance to spend. (14:28-14:48)
- The gate for that class is cross-model agreement on the same input: "when we receive their receipt, we will use different models to review the same receipt. We only move forward if the results from different models agree with each other." Note the shape — different models rather than repeated samples of one, and agreement as a precondition for action rather than as a confidence score. (14:48-15:02)
- Disagreement resolves to a human handoff, and admitting failure is treated as a legitimate outcome rather than a fallback of last resort: "if we really have trouble to figure it out which one is right, it's okay to tell the customer, say, 'Hey, we have trouble to process your stuff. Do you want us to get you connect to a human agent?'… That's acceptable solutions." (15:02-15:17)
- The generalization: retryability is a cheap proxy for the harm-scale grading that high-stakes systems build explicitly, and it makes the classification something a product team can do in a planning meeting. Where the consequence is not user-absorbable, the volume × consequence arithmetic in the related eval-sizing concept takes over and sets both the accuracy bar and the size of the test suite.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md)
- [Separate Generation and Verification Prompts or Models](separate-generation-and-verification-prompts-or-models.md)
- [Run Parallel Specialist Models Behind a Speak-Up Gate](run-parallel-specialist-models-with-a-speak-up-gate.md)
- [Keep Human Review on High-Risk Agent Operations](keep-human-review-on-high-risk-agent-operations.md)
- [Use Field-Level Confidence Signals for Human Review](use-field-level-confidence-signals-for-human-review.md)
- [Plan AI Reliability Risk Inside Product Work](plan-ai-reliability-risk-inside-product-work.md)

Sources:
- [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](../sources/20260819_WJRdLNhrsLQ.md), 13:29-15:17
