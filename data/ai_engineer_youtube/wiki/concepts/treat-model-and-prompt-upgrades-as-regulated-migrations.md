# Treat Model and Prompt Upgrades as Regulated Migrations

Summary: In high-stakes AI products, changing the model or prompt is a migration, not a transparent dependency bump. Vendor contracts, prompt behavior, model latency, and domain-year changes can all create lock-in that needs explicit eval gates before rollout.

Use when:
- Planning hosted-model upgrades in a regulated or large-scale production AI application.
- Deciding whether fine-tuning, prompt compression, or provider changes are worth the migration cost.

Details:
- Intuit reports that long-term model contracts can reduce cost but also tie the product to a vendor relationship, 10:11-10:29.
- The talk frames both vendors and prompts as forms of lock-in, and says even upgrading to a newer model from the same vendor for the next tax year was not easy, 10:29-10:49.
- A move from Claude Instant to Claude Haiku for tax year 2024 required clear evals to test the change before rollout, 09:25-09:47.
- Fine-tuning Claude 3 Haiku on AWS Bedrock was explored to reduce prompt size and latency while preserving response quality, but specialization and training effort made evals necessary, 07:20-08:04.
- LLM latency differs from ordinary backend-service latency; complex tax profiles and peak filing traffic require fallback and product-design strategies, 10:52-12:10.

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Plan AI Products for a Multimodel Market](plan-ai-products-for-a-multimodel-market.md)
- [Compare Models by Task, Thinking Budget, Cost, and Latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Prompt Management Lags Prompt Iteration](prompt-management-lags-prompt-iteration.md)

Sources:
- [How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit](../sources/20250723__zl_zimMRak.md), 07:20-08:04, 09:25-10:49, 10:52-12:10
