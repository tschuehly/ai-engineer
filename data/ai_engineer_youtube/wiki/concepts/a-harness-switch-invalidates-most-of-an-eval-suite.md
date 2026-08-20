# A Harness Switch Invalidates Most of an Eval Suite

Summary: Offline eval suites are written against a specific harness — its tools, its loop, its interaction shape — so swapping the harness or the model breaks most of them. The reported figure is that roughly 80% stop meaning anything. Treat suite size as a liability with a depreciation schedule, not as an asset.

Use when:
- Someone proposes spending months building a large offline eval suite before shipping.
- Planning a migration from a homegrown loop to a vendor CLI, or between agent frameworks.
- A model upgrade is being held back to update evals.
- Sizing how much eval investment a fast-moving agent product can carry.

Details:
- The claim, with its worked example: evals "break as soon as you have a new model, as soon as you like switch harnesses… you're like oh yeah, I'm going to write an eval where it has to like call this tool if I ask it this question and it's like oh then you switch to like Claude Code CLI and now 80% of your evals suck." ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 04:23-04:39)
- Why the coupling is structural rather than sloppy: the assertion in that eval is about *the harness's* tool inventory and dispatch behavior, not about the model's competence at the task. Change the harness and the assertion is about nothing. This follows from the unit under test having grown — "the prompt is actually like the whole thing now. It's like all the code. It's your whole harness" ([Keep Evals in the Repo as Tests, Not in a Prompt Playground](keep-evals-in-the-repo-as-tests-not-in-a-prompt-playground.md)). (12:06-12:19)
- The prescription that follows is about *rate of change*, not about skipping evals: "the one thing I could promise you is that things are going to keep changing. Like we're not done and so I'd be very careful about… investing months in some sort of eval set that's going to slow you down." (04:41-04:54)
- The decision test worth stealing: "do you actually delay… upgrading to the new model on your product? Do you actually delay it 2 weeks to update your evals or not? I think most people would say no." A suite nobody will wait for is a suite that is not gating anything, whatever the dashboard says. (05:11-05:23)
- The failure this names is not a missing suite but a costly one: "you want more safety but you don't want theater." (04:55-05:00)
- Adoption evidence, such as it is, is anecdotal and points the same way: on the thousand-example prescription, "the reality is like nobody's doing that. Um very few people anyway." (04:10-04:19)
- **What survives a harness swap and what does not.** Evals asserting on the *task outcome* — did the refund get issued, is the answer grounded — mostly survive; evals asserting on the *trajectory* — which tool, in what order — mostly do not. That is a design lever, not just an observation, and it cuts against trajectory-level assertions being the default ([Evaluate Agent Retrieval by Trajectory, Not Task Success](evaluate-agent-retrieval-by-trajectory-not-task-success.md), [Choose Eval Scope Across Span, Multispan, Trajectory, and Session](choose-eval-scope-across-span-multispan-trajectory-and-session.md)) — trajectory scope buys diagnostic precision and pays for it in portability.
- This tightens rather than replaces the wiki's existing warning that [evals only cover known AI product failures](evals-only-cover-known-ai-product-failures.md). That page says the suite misses failures it never named; this one says the suite can stop covering even the failures it *did* name, without anyone editing it, the day the harness changes.
- The complement is production-side detection, which is harness-agnostic because it observes what actually happened rather than asserting what should ([Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)). The talk's whole argument is that the balance between the two should shift toward the second as harness churn rises.
- **Harness churn is not optional, which sharpens the problem.** Anthropic's Applied AI team argues the harness *must* change on every model release, because "harnesses encode assumptions about what Claude cannot do on its own… they go stale as models improve," and reports deleting a whole context-reset subsystem when a newer model stopped needing it ([A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)). Put the two claims together and the invalidation event on this page is not an occasional migration — it is scheduled to recur with every upgrade, which is a stronger argument for portable outcome-level assertions than the churn rate alone. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 07:36-08:57)
- **A rubric moved into the loop is one response to the same pressure.** Anthropic's "outcomes" grades a run against a user-defined rubric *while it runs* and retries on failure ([Grade With a Parallel Rubric Agent and Retry Until It Passes](grade-with-a-parallel-rubric-agent-and-retry-until-it-passes.md)). Rubrics about the task outcome are exactly the assertions this page says survive a harness swap, so an in-loop grader is portable in a way a trajectory assertion is not — but it also measures nothing about first-attempt quality, so it complements the offline suite rather than replacing it. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 29:08-30:03)
- Caveat: "80%" is an illustrative estimate from a vendor whose product is the alternative to offline suites, with no methodology and no sample. The mechanism is checkable in your own repo — count what fraction of your assertions name a tool, a step order, or a message shape — and that count, not this number, is the one to act on. The Anthropic additions above come from a different vendor talk and are likewise unmeasured.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep Evals in the Repo as Tests, Not in a Prompt Playground](keep-evals-in-the-repo-as-tests-not-in-a-prompt-playground.md)
- [Evals Only Cover Known AI Product Failures](evals-only-cover-known-ai-product-failures.md)
- [Choose Eval Scope Across Span, Multispan, Trajectory, and Session](choose-eval-scope-across-span-multispan-trajectory-and-session.md)
- [Continuously reconcile eval datasets with user reality](continuously-reconcile-eval-datasets-with-user-reality.md)
- [Keep eval data constant and task logic variable](keep-eval-data-constant-and-task-logic-variable.md)
- [Match the Quality Method to Your User Count](match-the-quality-method-to-your-user-count.md)
- [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)
- [Grade With a Parallel Rubric Agent and Retry Until It Passes](grade-with-a-parallel-rubric-agent-and-retry-until-it-passes.md)

Sources:
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 04:00-05:23, 12:06-12:19
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 07:36-08:57, 29:08-30:03
