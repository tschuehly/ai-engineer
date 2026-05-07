# Map Application Evals to the Product Court

Summary: Application evals should define the product's in-bounds domain, then cover the easy, hard, passing, and failing regions users actually exercise. This prevents teams from optimizing against anecdotes or irrelevant tests.

Use when:
- Building an eval set for an AI application with unpredictable user prompts.
- Deciding whether a proposed eval case represents core product behavior or out-of-bounds work.

Details:
- A fruit-letter-counter demo can pass a few manual checks and still fail once a user asks a more complex but in-domain prompt, showing why repeated spot checks are not enough, 01:55-04:31.
- Deterministic unit and end-to-end tests can cover most of the app, while the LLM-dependent behavior remains the crucial unreliable area that needs evals, 04:34-04:50.
- The talk maps evals to a basketball court: data points are user prompts, misses and makes show outcomes, boundaries define what the product should care about, and distance from the basket represents harder cases, 05:08-07:17.
- Out-of-bounds evals can create fake productivity because they test behavior users do not need, while concentrated eval sets can miss important regions of the actual product domain, 07:20-07:50.
- Teams can build court coverage from thumbs up/down feedback, observability logs, random weekly log samples, community forums, and noisy social reports, 07:54-08:40.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Reverse-engineer AI app evals from user outcomes](reverse-engineer-ai-app-evals-from-user-outcomes.md)
- [Continuously reconcile eval datasets with user reality](continuously-reconcile-eval-datasets-with-user-reality.md)
- [Build AI app benchmarks before optimization](build-ai-app-benchmarks-before-optimization.md)

Sources:
- [Evals Are Not Unit Tests - Ido Pesok, Vercel v0](../sources/20250806_L8OoYeDI_ls.md), 01:55-08:40
