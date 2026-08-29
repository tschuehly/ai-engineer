# An Error Rate With No Incident Reports Is a Measurement Gap

Summary: A deployed AI system with no adverse-event channel produces no incidents by construction. The absence of reported harm is then read as evidence of safety, when it is evidence only that nobody is looking — and the errors that generate no complaint are exactly the quiet, high-consequence ones.

Use when:
- Arguing for eval or monitoring investment against "we haven't had any problems."
- Deploying into a workflow where the affected party never sees the output (a record, a summary filed downstream, an internal note).
- Setting up a feedback channel and deciding whether user complaints are a sufficient signal.
- Assessing a category's real-world safety from adoption figures and incident counts.

Details:
- **The base rates, from a study the talk cites without naming.** "In the largest real-world study of these notes, about 1 in 20 carried an error that was serious enough that it could cause significant harm to the patient… that's in production on real patients. And that's only the serious ones. If you widen that lens to all errors, nearly 1 in 5 had an important omission and more than 1 in 10 had a hallucination." No study name, size, or citation is given. ([Fox](../sources/20260822_yqF6XhzbWBk.md), 02:03-02:25)
- **Deployment scale against that rate.** Ambient scribes are "already in about a third of US practices and climbing. Physician AI use doubled last year, and none of this is tracked." (02:25-02:48)
- **The gap itself.** "For most of these systems, there's no adverse event reporting at all. The errors never show up as incidents, they just sit in the record." (02:48-03:00)
- **The inference to refuse.** "It's not that we checked and it's fine, it's that we're flying blind." A category can be simultaneously widely adopted, apparently incident-free, and unmeasured — and the first two facts are what make the third comfortable. (03:00-03:09)
- **Why the silent errors are the dangerous ones, not merely the undetected ones.** The loud failure — a sore throat written up with chest pain, suspected angina, diabetes medications the patient never took, and a nonexistent hospital address — is self-reporting: "these kind of crazy ones someone notices." The quiet ones "sit in the record uncalled" and, in the opening case, a missing line about jaw pain on chewing turns a same-day steroid emergency into a paracetamol headache. Complaint-driven feedback systematically samples the loud class. (00:35-02:03)
- **Structural reason there is nothing to complain about.** The error is an omission in a document the patient never reads and the clinician signs off in seconds. When the affected party cannot observe the output, user feedback is not a weak signal — it is not a signal at all, and a monitoring plan that rests on it has no coverage of the failure class it most needs.
- **What this argues for.** Proactive sampling of production output by someone qualified to judge it, which is also the input to [Discover Failure Modes From Production Outputs, Not Synthetic Cases](discover-failure-modes-from-production-outputs-not-synthetic-cases.md). The same reasoning applies one level in: a judge's pass set needs sampling for the same reason production needs an incident channel, because a pass generates no complaint either ([A Judge Without Taste Is a Second Silent Failure](a-judge-without-taste-is-a-second-silent-failure.md)).
- **How this qualifies the wiki's consequence-sizing rule.** [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md) converts a consequence into a required error rate and a suite size — which presumes you can observe the rate you are hitting. This page names the prior condition: in a domain with no reporting channel, the deployed error rate is unknown, so the suite is being sized against an assumption rather than a measurement.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md)
- [Discover Failure Modes From Production Outputs, Not Synthetic Cases](discover-failure-modes-from-production-outputs-not-synthetic-cases.md)
- [A Judge Without Taste Is a Second Silent Failure](a-judge-without-taste-is-a-second-silent-failure.md)
- [Do Not Report Agent Autonomy Without Quality Accountability](do-not-report-agent-autonomy-without-quality-accountability.md)
- [Score Every Production Conversation to Judge Agent Health](score-every-production-conversation-to-judge-agent-health.md)

Sources:
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 00:35-03:09
