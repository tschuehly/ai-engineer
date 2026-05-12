# The Billable Hour is Dead; Long Live the Billable Hour - Kevin Madura + Mo Bhasin, Alix Partners

Source: [The Billable Hour is Dead; Long Live the Billable Hour - Kevin Madura + Mo Bhasin, Alix Partners](https://www.youtube.com/watch?v=Wv1tAxKYLeE)
Uploaded: 2025-07-23
Transcript: `raw/20250723_Wv1tAxKYLeE/Wv1tAxKYLeE.en-orig.vtt`

## Summary

AlixPartners describes enterprise GenAI adoption as a shift from individual productivity demos to workflow-level productivity: use LLMs to ingest, classify, retrieve from, and extract structured fields across full corpora, while preserving validation, business context, demos, and user trust.

## Extracted Concepts

- [Enterprise AI Productivity Needs Workflow-Level Outcomes](../concepts/enterprise-ai-productivity-needs-workflow-level-outcomes.md) - distinguishes employee productivity from enterprise productivity and ties value to compressed engagement phases.
- [Schema-First Classification Turns LLMs Into Enterprise Categorization Tools](../concepts/schema-first-classification-turns-llms-into-enterprise-categorization-tools.md) - shows structured outputs, taxonomies, and tool lookups replacing bespoke text-classification pipelines.
- [Enterprise RAG Becomes More Useful With API Tool Access](../concepts/enterprise-rag-becomes-more-useful-with-api-tool-access.md) - frames RAG as a substrate that can call licensed or proprietary APIs instead of only searching internal documents.
- [Use Field-Level Confidence Signals for Human Review](../concepts/use-field-level-confidence-signals-for-human-review.md) - uses log probabilities aligned to structured-output values as a review aid for extracted fields.

## Topic Links

- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

## Notes

- The speakers separate professional-services work into upfront data understanding, analysis or hypothesis generation, and client-facing recommendation; they argue AI currently compresses the first phase from roughly half the work to a smaller human share in some engagements. (03:38-05:07)
- A core value claim is broader corpus coverage: instead of prioritizing only the top portion of contracts or data because human review is expensive, AI can inspect a full corpus and free experts for higher-value interviews, analysis, and recommendations. (05:10-06:28)
- The talk calls out a gap between AI investment and measurable enterprise productivity, then distinguishes employee productivity from enterprise productivity as the target for useful use cases. (06:36-07:24)
- For categorization, they contrast older text-classification work such as stemming, stop-word removal, SVMs, and Naive Bayes with structured-output LLM classification against a business taxonomy such as NAICS codes, optionally enriched with web-query tool calls. (07:27-09:10)
- Classification gains required business-partner review, taxonomy context, and accuracy work; the source reports 95% accuracy on 10,000 vendor categorizations in minutes at much lower cost than manual work. (09:13-10:32)
- The enterprise RAG example handles large mixed-format data rooms and can add tool calls to proprietary third-party databases by embedding API specs so the LLM can call those APIs. (10:34-12:31)
- The speakers caution that "reason across all documents" is not how RAG works by default; broad document reasoning needs stepwise solution design rather than user expectation alone. (12:31-12:46)
- For structured extraction from contracts, they combine document, schema, LLM, validation, and scaffolding; business value is in the schema that captures what matters for an engagement. (12:48-13:51)
- They expose model confidence to users by aligning OpenAI API log probabilities with structured-output values, ignoring JSON field names and scoring the extracted values for review. (14:16-15:21)
- Scaling GenAI internally required monthly demos, Streamlit prototypes that later become React applications, ROI/NPS focus instead of chasing agents, MCP, or the latest model, and close partnership with business users. (15:55-16:47)
