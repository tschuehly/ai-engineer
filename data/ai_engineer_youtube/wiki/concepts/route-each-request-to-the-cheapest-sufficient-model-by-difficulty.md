# Route Each Request to the Cheapest Sufficient Model by Difficulty

Summary: Don't send every agent call to the most expensive frontier model; classify each request's difficulty and route it to the cheapest model that can handle it — simple work to a cheap model, harder work to a mid model, only the hardest to a frontier model — so per-token cost tracks task difficulty instead of a fixed worst-case.

Use when:
- An agent uses one expensive model for every call, including simple inference steps that a cheaper model could do.
- A production agent's cost is dominated by model price rather than context size, and different requests vary in difficulty.
- Designing an agent loop where you can insert a routing decision before the model call.

Details:
- The lever: "I highly recommend don't use the most expensive model for everything you're doing… use multiple different models based on the use case, and then try to route to it inside your agent." Map difficulty to a tier — a newer frontier model for a very difficult task, a cheaper model (e.g. Claude Haiku) for something simple, Claude Sonnet for something in between. ([Erik Hanchett](../sources/20260628_uiP88SpCi1Q.md), 01:01-01:51)
- The router can be as simple as an `if` statement on task type, or "you can even have another model that's very cheap decide which model to use" — a cheap classifier picks the tier per request, so the routing overhead stays far below the cost of over-serving every call with the frontier model.
- This is a *difficulty*-triggered routing policy, distinct from other cheaper-model paths in the wiki: [verification guardrails let you downshift to cheaper models](verification-guardrails-let-you-downshift-to-cheaper-models.md) uses a check-and-retry harness (not task difficulty) as the trigger, and [abstract LLM inference behind one routing API](abstract-llm-inference-behind-one-routing-api.md) is the routing *mechanism* rather than the per-request policy. Use this concept for the "which tier does this request need" decision and those for the harness and plumbing.
- Caveats implicit in the pattern: routing adds logic and possibly one extra (cheap) classifier call per request, and mis-routing a hard task to a too-cheap model trades cost for quality, so the difficulty signal needs to be reliable enough that cheap-tier outputs still complete the task.
- **The same argument stated at the industry level, and extended past model choice to compute per request.** Sara Hooker frames one-model-for-everyone as a compute waste before it is an equity problem: "it's not a particularly good use of compute… You're spending the same amount of compute on everything. And some problems are hard and some are very easy" ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 04:12-04:27). She names the next step past tier routing as making the budget itself difficulty-dependent — "even your test time compute should be adaptive based on your task" (08:29-08:34) — which is the same policy applied to reasoning tokens, search width, or verification passes rather than to which checkpoint answers. Stated as a direction with nothing implemented or measured in that talk.
- **The premise stated plainly, and the case for a cheap default rather than per-request classification.** Rizwan's version of the routing argument skips difficulty estimation entirely: open-weight models "are powerful enough where you don't always need the best one for all your work," so Coinbase "defaulted to using GLM and Kimi in their internal LLM gateway" and cut spend nearly in half while volume grew. A blanket cheap default with escalation on failure is the crude form of this page's policy and needs no difficulty classifier, which is worth considering when the classifier itself is the part that is hard to build or validate. The cost he names for the crude version is not accuracy but features: you lose "the latest new feature in something like Claude Code." ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 08:27-08:47, 10:27-10:55)
- **Difficulty routing manufactures the mixed-workload problem, so it has to come with per-route instrumentation.** Once one endpoint dispatches to a cheap tier, a mid tier, and a frontier reasoning model, its aggregate latency describes nothing: "you should be tracking your P99 per model per route, not a gateway wide number," since "a reasoning model's normal is actually a chat model's outage." Timeouts inherit the same requirement, set "per model class per route," because a timeout tuned to the cheap tier will cut off the expensive one and a timeout tuned to the expensive tier lets a cheap-tier hang run for a minute. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 06:54-08:16)


- **A commercial implementation of this policy, and the amendment it makes to the routing key.** DigitalOcean's inference router does not estimate difficulty at all: it matches each request to a *named task* from a declared config — bug fixing, code generation, test writing, code snippets, code performance optimization — and each task carries its own model pool. The published mapping is the same ladder this page describes, stated per task class rather than per difficulty score: classification and labelling to "a small open model," "code generation and bug fixing" to "a mid open-weight model," and "accuracy critical tasks like code review and security" to a frontier model ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 02:45-03:19, 06:29-07:52). The amendment matters for the caveat above about needing a reliable difficulty signal: a task label is inspectable and correctable in a way a score is not, so a bad route decomposes into "matched the wrong task" or "the task points at the wrong model," which have different fixes. See [Declare Routing Preferences So a Bad Route Is Fixable](declare-routing-preferences-so-a-bad-route-is-fixable.md).
- **The overhead this page names — one extra cheap classifier call per request — has a stated budget in that implementation.** A purpose-built mixture-of-experts routing model decides in "under 200 milliseconds" at no incremental charge (05:07-05:23, 13:47-14:28). That is the condition under which per-request routing beats the crude blanket-cheap-default alternative described above, because escalation-on-failure pays for a failed generation plus a retry rather than a sub-second classification; see [A Router Must Be Cheap and Fast Enough to Disappear](a-router-must-be-cheap-and-fast-enough-to-disappear.md). Vendor figures, unmeasured externally and stated without a percentile.
- **Where the saving actually shows up is the session, not the request.** In a two-terminal coding-agent comparison the routed arm spent 8 cents against an always-Opus arm's 25 after one feature, and 14 against 44 after three prompts, because "every single request that I write goes to the same premium model" on one side while the other pays each call's own tier (09:36-13:25). A per-request price comparison understates the policy; see [Routing Savings Compound Across an Agent Session](routing-savings-compound-across-an-agent-session.md).

Related topics:
- [Inference](../topics/inference.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Pre-Training Size Is No Longer the Most Lucrative Scaling Axis](pretraining-size-is-no-longer-the-most-lucrative-scaling-axis.md)
- [Shrink the Per-Step Payload the Agent Loop Re-Sends](shrink-the-per-step-payload-the-agent-loop-re-sends.md)
- [Verification Guardrails Let You Downshift to Cheaper Models](verification-guardrails-let-you-downshift-to-cheaper-models.md)
- [Abstract LLM inference behind one routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Split discovery and validation across reasoning and deterministic models](split-discovery-and-validation-across-reasoning-and-deterministic-models.md)
- [A Subsidized Coding-Agent Subscription Is a Lock-In Ramp](a-subsidized-coding-agent-subscription-is-a-lock-in-ramp.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)
- [Declare Routing Preferences So a Bad Route Is Fixable](declare-routing-preferences-so-a-bad-route-is-fixable.md)
- [Give Each Task a Model Pool With an Explicit Selection Policy](give-each-task-a-model-pool-with-an-explicit-selection-policy.md)
- [A Router Must Be Cheap and Fast Enough to Disappear](a-router-must-be-cheap-and-fast-enough-to-disappear.md)
- [Routing Savings Compound Across an Agent Session](routing-savings-compound-across-an-agent-session.md)
- [Evaluate a Router Against the Always-Frontier Arm](evaluate-a-router-against-the-always-frontier-arm.md)

Sources:
- [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](../sources/20260628_uiP88SpCi1Q.md), 01:01-01:51, 04:50-05:03
- [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../sources/20260812_XEd_SRVHBgU.md), 04:12-04:27, 08:29-08:34
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 08:27-08:47, 10:27-10:55
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 06:54-08:16
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 02:45-03:19, 05:07-05:23, 06:29-07:52, 09:36-13:25, 13:47-14:28
