# Run eval suites in CI/CD before and during production

Summary: LLM evals should become CI/CD automation, not only notebook experiments. The intended workflow is to rerun evaluation suites when prompts, data sets, models, or production use cases change, similar to ordinary software tests.

Use when:
- Moving evals from manual experiments into release gates.
- Connecting offline prompt/model tests to production customer behavior.

Details:
- Smith says teams need a CI process for continuously improving evaluation and benchmark setups because no eval suite catches everything at first. (11:13-11:31)
- When asked how evals connect to running customer use cases, she describes the desired shape as CI/CD automation of an evaluation framework, analogous to software-engineering tests. (31:03-31:49)
- The CI/CD eval suite should include evaluation tests like unit testing setups, but scoped to the LLM application's prompts, data sets, model swaps, and real production use cases. (31:49-31:58)
- **The precondition, and the reason the analogy has gotten literal for agents.** Ben Hylak's version is that the unit under test is no longer a string — "the prompt is actually like the whole thing now. It's like all the code. It's your whole harness" — so evals "should look a lot more like code… a lot more like tests. Whether that's unit tests, whether that's end-to-end tests," kept in the repo and run locally, with Sentry's Vitest-evals package and what "OpenAI calls… macro evals" named as existing shapes ([Keep Evals in the Repo as Tests, Not in a Prompt Playground](keep-evals-in-the-repo-as-tests-not-in-a-prompt-playground.md)). Evals as code is what makes CI gating possible at all. ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 12:06-12:53)
- **The caveat that limits how much to build here.** The same talk reports that these suites depreciate fast: they "break as soon as you have a new model, as soon as you like switch harnesses," on the order of "80% of your evals suck" after moving to a different agent CLI, because trajectory-level assertions name the harness rather than the task ([A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)). A CI gate nobody will wait two weeks to update is not a gate, so size the suite to a change rate you can actually maintain. ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 04:23-05:23)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Keep Evals in the Repo as Tests, Not in a Prompt Playground](keep-evals-in-the-repo-as-tests-not-in-a-prompt-playground.md)
- [A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)

Sources:
- [Strategies for LLM Evals (GuideLLM, lm-eval-harness, OpenAI Evals Workshop) - Taylor Jordan Smith](../sources/20250727_89NuzmKokIk.md), 11:13-11:31, 31:03-31:58
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 04:23-05:23, 12:06-12:53
