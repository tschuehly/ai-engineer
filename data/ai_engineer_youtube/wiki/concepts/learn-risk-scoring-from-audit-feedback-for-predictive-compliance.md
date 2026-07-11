# Learn Risk Scoring From Audit Feedback for Predictive Compliance

Summary: Replace static alerting rules with an adaptive probabilistic risk model that fuses multiple signals into a confidence-weighted score to prioritize cases, and close a feedback loop where confirmed frauds strengthen detection patterns and false positives refine scoring — turning compliance from reactive validation into predictive governance. Pair it with a normalization layer so risk is judged consistently across jurisdictions.

Use when:
- Building fraud/compliance/anomaly systems that generate too many low-value alerts and need prioritization rather than binary rule matches.
- Designing a human-in-the-loop labeling loop (auditor/investigator outcomes) that continuously improves a detection model without manual rule rewrites.
- Operating across regions/currencies/reporting standards where the same transaction must not be scored differently by jurisdiction.

Details:
- Instead of firing an alert per static rule, the model combines indicators — anomaly strength, source reliability, historic patterns — into a confidence-weighted risk score that prioritizes cases needing attention and suppresses unnecessary investigations. Answers "what is most likely to be genuine compliance risk?" (07:27-08:29)
- Feedback loop: every completed audit is training signal — confirmed fraud cases strengthen future detection patterns, false positives refine risk scoring and cut unnecessary alerts, so "the system becomes more accurate with each audit and investigation" and adapts as fraud patterns evolve rather than waiting on manual rule updates. (13:44-14:43)
- The loop enables a reactive→predictive shift: from asking "what went wrong" (after audits/reviews) to "what is likely to go wrong next," making compliance an ongoing intelligence function instead of a periodic review. (14:43-15:45)
- Cross-jurisdictional normalization layer harmonizes currencies, tax rules, reporting periods, and classification schemes so risk is evaluated consistently regardless of transaction origin — the regulatory-context prerequisite for scores to be comparable. (08:29-09:24)
- Reported operational value (~3M records, 4 jurisdictions): 76% reduction in false positives and ~40% less manual audit effort, letting investigators focus on prioritized high-risk cases. (11:40-12:39)
- Deployment considerations: integrate with existing ERP/payroll/procurement/tax platforms, jurisdiction-specific configuration, alignment with the audit framework (a prioritized-risk queue), and scalability to millions of records. (15:45-16:42)

Related topics:
- [Business Intelligence](../topics/business-intelligence.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Correlate entities across documents to surface cross-document risk](correlate-entities-across-documents-to-surface-cross-document-risk.md)
- [Run a jury of analysts and a consensus judge for no-ground-truth questions](run-a-jury-of-analysts-and-a-consensus-judge-for-no-ground-truth-questions.md)

Sources:
- [AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent](../sources/20260628_Iwe_RY-fYgI.md), 07:27-16:42
