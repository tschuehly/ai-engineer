# Keep Evals in the Repo as Tests, Not in a Prompt Playground

Summary: The unit under test used to be a string, so a hosted prompt playground was a reasonable place to keep it. It is now the whole harness — code, tools, loop, and everything connected to them — so the eval has to live where that lives: in the repository, in the test runner, run locally.

Use when:
- Choosing between a hosted eval/prompt-management product and a test file in the repo.
- An eval passes in the playground and the behavior is still wrong in the product.
- Setting up the first eval layer for an agent rather than a chatbot.
- A prompt-management tool is being adopted for versioning and evals as one bundle.

Details:
- The premise: "the prompt is actually like the whole thing now. It's like all the code. It's your whole harness. It's like everything you're connect— It's not just like some string where you tell the agent what to do." ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 12:06-12:19)
- The conclusion drawn from it: "the evals themselves actually should look a lot more like code. In other words, like a lot more like tests. Whether that's unit tests, whether that's end-to-end tests." (12:19-12:30)
- Named prior art, offered as existence proof rather than endorsement: "[Sentry] has this a really cool package called like Vitest evals. It's literally just like Vitest with like some syntactic sugar on top," and "OpenAI calls this like macro evals." His own summary: "I don't think it really matters what you call it, but… run tests on your agent uh locally is is the advice. And keep these evals as code." (12:31-12:53)
- The reported market movement: "I actually don't know many companies that use some sort of like managed prompt like in the cloud anymore. There's like one or two I can think of," attributed to "how the shape of agents has really changed." (11:57-12:06, 12:55-13:08)
- What the older shapes assumed: "string contains… on the text output" assertions and playground UIs both presuppose that the interesting variation lives inside one prompt and one response. Neither holds for a loop that calls tools, reads files, and runs for many turns. (11:44-11:57)
- Two concrete things being in the repo buys that a hosted playground cannot: the eval moves atomically with the harness change in one commit and one review, and it runs against the real tool surface rather than a mocked one.
- This is the mechanism behind the CI-gating advice the wiki already carries ([Run eval suites in CI/CD before and during production](run-eval-suites-in-cicd-before-and-during-production.md)) — evals as code is the precondition for evals in CI — and it fits the general preference for validation that is fast, local, and deterministic ([Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)).
- The cost side is the same coupling seen from the other direction: an eval that lives with the harness also *depends* on the harness, and swapping harnesses invalidates most of it ([A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)). Repo-resident evals do not fix that; they make it visible in the diff.
- The wiki's counterweight worth holding alongside this: PM-facing and cross-functional eval work has real needs that a test file serves badly — non-engineers annotating traces, comparing experiments, curating datasets. The claim here is about where the *assertion* lives, not about abolishing the shared surface ([Mature Eval Platforms From Spreadsheets Into Experiment Systems](mature-eval-platforms-from-spreadsheets-into-experiment-systems.md)).
- Caveat: the market claim ("I don't know many companies…") is an impression from an observability vendor's customer base, which self-selects toward teams that already abandoned playground workflows. No adoption data is given, and the two named packages are mentioned without any evaluation of either.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)
- [Run eval suites in CI/CD before and during production](run-eval-suites-in-cicd-before-and-during-production.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Mature Eval Platforms From Spreadsheets Into Experiment Systems](mature-eval-platforms-from-spreadsheets-into-experiment-systems.md)
- [Use Evals As Durable AI System Specifications](use-evals-as-durable-ai-system-specifications.md)
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)

Sources:
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 11:35-13:08
