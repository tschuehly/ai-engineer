# AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent

Source: [AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent](https://www.youtube.com/watch?v=Iwe_RY-fYgI)
Uploaded: 2026-06-28
Transcript: `raw/20260628_Iwe_RY-fYgI/Iwe_RY-fYgI.en-orig.vtt`

## Summary

Varsha Shah (enterprise technical architect, TCS/Microsoft) presents a research framework for enterprise financial compliance and fraud detection that shifts analysis from single-document validation to cross-document intelligence. The core claim is that the most sophisticated fraud "exists between documents, not within them": a payroll record, a vendor invoice, and a tax filing can each pass independent validation while their *relationships* reveal the anomaly, so rule-based and document-level NLP systems structurally cannot catch these patterns. The proposed architecture layers three complementary components — a graph-based entity correlation engine ("what is connected?"), an adaptive probabilistic risk model that scores and prioritizes cases from multiple signals and learns from audit outcomes ("what is most likely genuine risk?"), and a cross-jurisdictional normalization layer that harmonizes currencies, tax structures, reporting periods, and classification schemes ("how should risk be interpreted in regulatory context?"). Evaluated on ~3M financial records spanning 5 years and 4 jurisdictions, it reports ~91% precision, 87% recall, F1 0.89, a 76% reduction in false positives, and ~40% less manual audit effort. A feedback loop (confirmed frauds strengthen detection patterns; false positives refine scoring) is framed as the mechanism that moves compliance from reactive validation to predictive governance. This is a research/architecture talk without code-level implementation detail.

## Extracted Concepts

- [Correlate entities across documents to surface cross-document risk](../concepts/correlate-entities-across-documents-to-surface-cross-document-risk.md) - the fraud/compliance signal lives in relationships spanning payroll/tax/procurement records, invisible to per-document validation.
- [Learn risk scoring from audit feedback for predictive compliance](../concepts/learn-risk-scoring-from-audit-feedback-for-predictive-compliance.md) - a probabilistic risk model that prioritizes cases and continuously improves from confirmed frauds and false positives, plus a normalization layer for consistent cross-jurisdiction evaluation.

## Topic Links

- [Business Intelligence](../topics/business-intelligence.md)
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

## Notes

- Compliance gap: organizations generate exponentially more payroll/tax/procurement/transaction data, but existing solutions analyze documents independently, so cross-system risk stays hidden and manual review is impractical. (00:39-03:25)
- Modern fraud "rarely appears as an obvious error within a single document"; it exploits subtle inconsistencies across systems that only emerge when records are connected. (02:27-04:40)
- Three-component framework: entity correlation engine, adaptive probabilistic risk model, cross-jurisdictional normalization layer — "individually each provides value; together they enable enterprise-wide compliance intelligence." (04:59-06:31)
- Entity correlation is graph-based: connects employees, vendors, accounts, transactions, and regulatory filings into a unified network to reveal structural anomalies; answers "what is connected?" (06:31-07:27)
- Adaptive probabilistic risk model combines multiple indicators — anomaly strength, source reliability, historic patterns — into a confidence-weighted risk score, prioritizing cases needing attention and reducing unnecessary investigations; "its ability to learn from the audit outcomes" lets it improve over time. (07:27-08:29)
- Cross-jurisdictional normalization standardizes currencies, tax rules, reporting periods, and classification schemes so the same transaction is not interpreted differently by jurisdiction; answers "how should risk be interpreted in regulatory context?" (08:29-09:24)
- Evaluation: ~3M financial records over 5 years across 4 jurisdictions. (09:43-10:22)
- Detection results: ~91% precision, 87% recall, F1 0.89, "consistent across four jurisdictions and large enterprise scale data." (10:22-11:22)
- Operational value: 76% reduction in false positives and ~40% reduction in manual audit effort, freeing investigators to focus on high-risk cases. (11:40-12:39)
- Continuous learning cycle: confirmed fraud cases strengthen future detection patterns; false positives refine risk scoring and reduce unnecessary alerts; the system adapts as fraud patterns evolve "rather than relying on manual rule updates." (13:44-14:43)
- Reactive → predictive shift: instead of "what went wrong," organizations ask "what is likely to go wrong next" — compliance becomes an ongoing intelligence function rather than a periodic review. (14:43-15:45)
- Enterprise deployment considerations: seamless integration with existing ERP/payroll/procurement/tax platforms; jurisdiction-specific configuration; alignment with the audit framework (prioritized-risk queue for investigators); scalability to millions of records. (15:45-16:42)
