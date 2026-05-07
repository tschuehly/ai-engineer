# Resolve AI Capability Risk Before Product Surface Commitment

Summary: When the largest product risk is whether the AI can perform the core task, evaluate the capability before committing to the surrounding product. Real user data, synthetic eval cases, and user-tested outputs can reveal both feasibility and where human input belongs in the workflow.

Use when:
- An AI product idea depends on uncertain model quality, extraction quality, classification quality, or reasoning quality.
- A team is tempted to build a product surface around an existing model, benchmark, or NLP technique before validating the task outcome.

Details:
- The Consult case started from a seemingly obvious AI use case: analyzing large government consultation responses that can take months and cost millions. Existing NLP techniques such as BERTopic created pressure to build immediately. 05:10-06:05
- Productizing the existing technique first failed in user testing because outputs were inaccurate, inconsistent, did not meet user needs, and would not meet the legal threshold required for the workflow. 06:03-06:25
- The team reset by prioritizing the AI capability: collect real user data, generate synthetic data, create evals, optimize against them, and test outputs with real users before shaping the product. 06:27-06:46
- Capability-first evaluation changed the product because it exposed the pipeline points where human input and human-in-the-loop review were valuable. 06:50-07:17
- The explicit lesson is to resolve AI uncertainties early with evaluations and user tests so teams avoid both impossible products and wrong product surfaces. 07:17-07:43

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Reverse-engineer AI app evals from user outcomes](reverse-engineer-ai-app-evals-from-user-outcomes.md)
- [Treat Evals as the Home of Domain Knowledge](treat-evals-as-the-home-of-domain-knowledge.md)

Sources:
- [Why your product needs an AI product manager, and why it should be you — James Lowe, i.AI](../sources/20250728_xzJdSi2Tsqw.md), 05:10-07:43
