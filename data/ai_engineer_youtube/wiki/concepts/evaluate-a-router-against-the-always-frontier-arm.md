# Evaluate a Router Against the Always-Frontier Arm

Summary: A router demo always looks good, because a cheaper model answering a simple prompt is visibly faster and cheaper. The only thing that separates that from a vibe check is running the same task set through two arms — the router and an always-premium baseline — and reporting correctness, tokens, and latency together. The acceptance shape is asymmetric: quality has to land within noise of the baseline, while cost and latency have to be strictly better.

Use when:
- Deciding whether to adopt a model router, or defending one you built.
- A routing change is being justified by a side-by-side screenshot or a session cost total.
- Designing the eval for any component whose job is to substitute a cheaper path for an expensive one.
- Reading a vendor's routing numbers and trying to work out what was actually measured.

Details:
- **The presenter draws the line himself, which is the most useful thing in the segment.** After three playground prompts each route faster and cheaper: "it's a pattern. It matches my, you know, vibe check, right? It's still vibes, though. How you actually prove it is working it through" an evaluation. ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 08:54-09:15)
- **The comparison arm is the whole design.** The baseline is not "no router" in the abstract but *the policy you would otherwise run*: every request to one premium model. That makes the eval answer the question a buyer actually has — what do I give up by not always paying for Opus — rather than the question a leaderboard answers. The reported result: "the scores 90% for my router, 95% correctness for Opus are very very close… the router used significantly less tokens and was significantly faster than Opus" (09:15-09:36).
- **Three metrics, reported jointly, because any two of them can be gamed.** A router that routes everything to the frontier model matches quality and saves nothing; a router that routes everything to the cheapest model wins cost and loses correctness. This is the router-shaped case of [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md), and it is why token count belongs in the report even when cost is already there — token savings and dollar savings diverge when the tiers price differently.
- **The move to be suspicious of is "within a judge margin of error."** 90 against 95 is dismissed with "that's pretty much within a judge margin of error" (09:15-09:24), and no margin is ever measured or stated. A five-point gap is either noise or a one-in-twenty regression depending on a number nobody produced. If you run this eval yourself, the margin is cheap to get — repeat the judge on the same outputs, or bootstrap over the task set — and it converts the strongest claim in the comparison from an assertion into a result.
- **What a single aggregate correctness score still hides.** It cannot tell you whether the router loses uniformly or fails badly on one task class, which is the failure that matters, because a router's errors are concentrated by construction: a mis-matched task sends *every* request of that kind to the wrong tier. Report per-task correctness alongside the aggregate, and treat the routing decision itself as separately scorable — the source claims its routing model "beat frontier models like the GPT-5 series models at routing task itself" (05:23-05:35) without naming a routing benchmark or a correct-decision criterion.
- **Guard the arms.** In the same talk's end-to-end run the "single premium model" arm was not pure — "I think OpenCode sometimes routes to haiku by itself" (10:37-10:47) — so the harness was already routing underneath the control. Any coding-agent comparison has to pin the harness's own internal model choices, or the baseline is a different, cheaper policy than the one being claimed.
- **Where the eval sits in the lifecycle.** The vendor's framing is a loop, not an acceptance gate: "route, evaluate, adjust, then feed that back in. That loop is key" (06:04-06:08), with evaluation named as the first thing built on top of routing, "to prove that the right model works with your use case and your test well" (14:28-14:43). That makes the task set a durable asset — it gets re-run every time a pool member, a task definition, or a model version changes, which is more often than a model evaluation gets re-run.
- **Caveats on the reported numbers.** Nothing about the evaluation is described beyond the two percentages: no task count, no task distribution, no judge model, no definition of correctness, no per-task breakdown, and no interval. Token and latency advantages are given only as "significantly." The end-to-end session totals (8¢ against 25¢, then 14¢ against 44¢) are single runs of one small app with output quality judged by inspection on stage. Treat the method as the transferable part and the figures as unverified vendor results.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Declare Routing Preferences So a Bad Route Is Fixable](declare-routing-preferences-so-a-bad-route-is-fixable.md)
- [Routing Savings Compound Across an Agent Session](routing-savings-compound-across-an-agent-session.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Don't Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md)
- [Verification Guardrails Let You Downshift to Cheaper Models](verification-guardrails-let-you-downshift-to-cheaper-models.md)

Sources:
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 05:23-05:35, 06:04-06:08, 08:54-09:36, 10:37-10:47, 14:28-14:43
