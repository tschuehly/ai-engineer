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
- A Databricks production playbook formalizes this as governance: model change management means treating provider upgrades as risk, never relying on a single model, and testing each candidate on the team's own evaluation dataset because vendor leaderboard benchmarks are not useful in the enterprise's context. (`ObTPqBGsEbA`, 23:30-23:56)
- The same playbook treats prompt versioning as enterprise change management ("prompt as code"): commits cannot be terse, and should document why a prompt changed, which failure caused it, and what it is expected to correct, so later versions remain traceable. (`ObTPqBGsEbA`, 23:02-23:30, 33:50-34:45)
- Onlay states the same rule from the system-design side: "you can't just replace the model and assume it's going to be better. It's different." A model that is better "on certain evals … as measured by these different metrics" is not necessarily better for the situations you need it to be better at, "because of the way you've designed your system" — so you "really have to redo everything from scratch" and confirm evals, testing, and validation are in place before a new model can be introduced without breaking the system. The cost side is part of the decision too: an overpowered, over-expensive model on "routine things that need to be done a thousand times a day" defeats the cost-reduction goal the deployment exists to serve. (`UyyOoJmuATU`, 07:40-08:23, 19:40-20:02)
- Meta's gaming team generalizes the risk to the whole agentic stack: nondeterminism runs from front-end user prompting through runtime-LLM decisions to platform ranking/serving, so engineers who used to get stability and scalability by writing code, writing tests, and debugging against a *known* code base find that a model upgrade or a changed prompt "can entirely throw off your system," and how to debug that at scale is still an open challenge. (`grdoOC1BT1s`, 14:14-15:07)

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
- [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../sources/20260618_ObTPqBGsEbA.md), 23:02-23:56, 33:50-34:45
- [Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta](../sources/20260708_grdoOC1BT1s.md), 14:14-15:07
- [Healthcare's Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](../sources/20260819_UyyOoJmuATU.md), 07:40-08:23, 19:40-20:02
