# Correlate Entities Across Documents to Surface Cross-Document Risk

Summary: The most consequential fraud and compliance risks live in the *relationships between* documents, not inside any single one, so systems that validate each record independently structurally miss them; build a graph that links shared entities (employees, vendors, accounts, transactions, filings) across payroll/tax/procurement/financial systems and reason over the connected network.

Use when:
- Designing fraud, compliance, or anomaly-detection systems over heterogeneous enterprise documents where each record already passes its own validation.
- Explaining why rule-based or document-level NLP pipelines fail on sophisticated cross-system patterns and why a graph/entity-correlation layer is the fix.

Details:
- Framing: a payroll record, vendor invoice, and tax filing can each be individually accurate and correctly submitted, yet reveal fraud when connected — "the information already exists; what is missing is the ability to understand the relationship between these documents." (03:44-04:59)
- Traditional rule-based and document-level NLP systems are built to validate individual records, not to understand relationships across documents; that is the structural gap this pattern closes. (02:48-03:25)
- The correlation engine is graph-based: it links employees, vendors, accounts, transactions, and regulatory filings into a unified network, exposing structural anomalies invisible to per-document analysis. It answers the foundational question "what is connected?" and provides the relational substrate for downstream risk scoring. (06:31-07:27)
- Reported effect at scale (~3M records, 5 years, 4 jurisdictions): connecting data across documents produced ~91% precision / 87% recall / F1 0.89 and better detection with fewer false positives than isolated-document analysis. (10:22-13:22)
- Contrast with GraphRAG concepts: here the graph is an *analysis/correlation substrate for anomaly detection*, not a retrieval index answering user queries — the win is finding cross-record inconsistencies, not fetching passages.

Related topics:
- [Business Intelligence](../topics/business-intelligence.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Learn risk scoring from audit feedback for predictive compliance](learn-risk-scoring-from-audit-feedback-for-predictive-compliance.md)
- [Extract enterprise interaction data into structured graphs](extract-enterprise-interaction-data-into-structured-graphs.md)
- [Knowledge graphs make agent memory traversable and explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)

Sources:
- [AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent](../sources/20260628_Iwe_RY-fYgI.md), 02:48-13:22
