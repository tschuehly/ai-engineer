# Choose Eval Scope Across Span, Multispan, Trajectory, and Session

Summary: Beyond choosing what *kind* of eval to run, an agent eval has a scope — how much of the execution tree it reads. Arize's four scopes are single span, multispan, trajectory, and session; the scope axis is orthogonal to the signal flavor, and you should run the minimal set of scopes that gives signal because each eval costs.

Use when:
- An output looks correct but you suspect the failure is in how components were sequenced or how the whole conversation went.
- Deciding whether an eval should read one LLM call, several components, the full run, or the whole session.

Details:
- Single span: one input/output — one part of an LLM call. This is what most people mean by an eval and it is the simplest scope. (10:08-10:48)
- Multispan: the eval needs data across several components, e.g. "how well are agents passing data back and forth to each other?" requires the input/output of every agent in the exchange, not one. (10:49-11:11)
- Trajectory: over all spans in total — "did we call things in the right trajectory to finish the business process?" This catches sequencing failures an output check misses; the canonical example is calling B before A when B depends on A. (11:11-11:21, 06:01-06:22)
- Session: zoom out and evaluate the state machine of the whole conversation — "was the user ever frustrated? did we answer all their questions?" (11:21-11:42)
- Picking an eval is therefore two questions at once: which *flavor* of signal, and at what *scope and depth* — you can get very granular or zoom out. (11:42-11:49)
- Minimal-set caveat: "just because you can eval something doesn't mean you always should." Find the minimal set of evals that tells you whether the application works as intended, because there is a recurring cost to running them. (11:52-12:11)
- The scope axis sits on top of observability: an agent should be viewed distributionally across all runs (paths, branches, loops), and the trajectory/session scopes are where that view becomes an eval rather than just a dashboard. (05:00-05:45)
- **Scope is a per-team requirement, which is what makes it a platform problem.** DoorDash's three founding customers each needed a different scope: the consumer discovery and shopping assistant team needed "session level quality judgments," personalization ML needed "a way to scale up human judgment," and "with multi-agent systems we needed trajectory based evals" — leading to the question "how do you cater to all these different needs under a common platform." Treating scope as an axis rather than a choice is what lets one telemetry layer serve all three; a platform that hardcodes one scope forces the other teams to build their own. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 02:11-02:50)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Catalog Eval Signal Sources Across Judge, Human, Golden, Deterministic, and Business](catalog-eval-signal-sources-judge-human-golden-deterministic-business.md)
- [Layer Agent Evals as Deterministic, Semantic, and Behavioral Checks](layer-agent-evals-as-deterministic-semantic-and-behavioral-checks.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Golden Workflows Evaluate Agent Trajectories](golden-workflows-evaluate-agent-trajectories.md)
- [Trace Agent Tool Arguments to Debug Real Failures](trace-agent-tool-arguments-to-debug-real-failures.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)

Sources:
- [LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](../sources/20260607_JsCCrBF7F1g.md), 10:08-12:11
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 02:11-02:50
