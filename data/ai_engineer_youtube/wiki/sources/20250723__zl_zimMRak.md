# How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit

Source: [How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit](https://www.youtube.com/watch?v=_zl_zimMRak)
Uploaded: 2025-07-23
Transcript: `raw/20250723__zl_zimMRak/_zl_zimMRak.en-orig.vtt`

## Summary

Jaspreet Singh describes Intuit's TurboTax LLM explanation system as a regulated, high-scale AI product: static tax-summary explanations and dynamic tax Q&A route through platform orchestration, RAG or GraphRAG when tax knowledge is needed, expert-authored prompts, phased manual and automated evals, and guardrails that keep numerical tax calculations grounded in deterministic tax-engine outputs rather than model arithmetic.

## Extracted Concepts

- [Ground Regulated Explanations in Deterministic Engines](../concepts/ground-regulated-explanations-in-deterministic-engines.md) - this source shows TurboTax using LLMs to explain tax outcomes while keeping calculations and numbers sourced from a proprietary tax engine.
- [Stage Regulated LLM Evals From Experts to Automated Judges](../concepts/stage-regulated-llm-evals-from-experts-to-automated-judges.md) - this source describes tax analysts creating initial manual baselines that become golden data and LLM-as-judge checks.
- [Treat Model and Prompt Upgrades as Regulated Migrations](../concepts/treat-model-and-prompt-upgrades-as-regulated-migrations.md) - this source warns that vendor contracts, prompt dependence, and same-vendor model upgrades still require clear evals before rollout.

## Topic Links

- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)
- [Product Strategy](../topics/product-strategy.md)
- [Security](../topics/security.md)
- [Models](../topics/models.md)

## Notes

- TurboTax explanations are built on Intuit's GenOS platform with UI, orchestration, and multiple LLM solution paths so teams can route different questions to appropriate components, 01:37-02:45.
- Static explanation prompts cover known contexts such as tax summaries and refund components, while dynamic user tax questions use a different Q&A path, 03:04-04:31.
- The talk reports using Claude for one production explanation use case and OpenAI models for other dynamic Q&A, while treating model changes as frequent and requiring evaluation, 03:32-04:41.
- Tax knowledge changes yearly and Intuit uses RAG plus GraphRAG over IRS changes, proprietary tax information, and tax engines to answer questions more accurately, 04:43-05:01.
- Tax analysts supply domain knowledge, prompt engineering, and initial manual evaluations; those judgments become the basis for automated LLM-as-judge evaluation, 05:52-07:14.
- The eval pillars called out are accuracy, relevancy, and coherence, with broad monitoring over sampled real-user outputs and in-house tooling for automated prompt changes, 08:32-09:22.
- Fine-tuning Claude 3 Haiku on AWS Bedrock was tested to improve quality and reduce prompt size and latency, but the result was also specialized to its use case and required eval validation, 07:20-08:04.
- Model contracts and prompts create lock-in; even upgrading from one Anthropic model to another for the next tax year took effort and depended on clear evals, 09:25-10:49.
- LLM latency is materially slower than ordinary backend services, and complex tax profiles plus tax-day traffic require fallback and product-design strategies, 10:52-12:10.
- For numeric tax answers, TurboTax does not have the LLM perform calculations; the numbers come from the proprietary tax knowledge engine and guardrails check against hallucinated numbers before user delivery, 15:37-16:36.
- The Q&A states GraphRAG produced better response quality than regular RAG for this use case, while personalized answers were even more important for user helpfulness, 16:42-17:28.
