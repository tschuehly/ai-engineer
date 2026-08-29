# Gate Each Rollout Phase on a Different Question

Summary: A staged launch is only useful if each stage answers a question the previous one could not. Pilot asks whether the answers are right, a ~10% beta asks whether the product is minimally viable — read from where feature requests concentrate — and its exit bar is retention, not satisfaction; general availability comes after both.

Use when:
- Planning the rollout of an internal assistant or agent to a large population.
- A pilot has gone well and someone wants to skip straight to everyone.
- Choosing what to measure at each stage instead of tracking the same usage dashboard throughout.
- Deciding when a request backlog is noise and when it means the product is not yet viable.

Details:
- The reason for staging is the same trust economics that drives quality over coverage: "you cannot just launch these things to everyone… we need to do this in a controlled way because we want to make sure that we earn that first five questions. We don't want to burn our bridges in that first five questions." Each stage risks a bounded number of first impressions. ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 05:33-05:48)
- **Pilot: does it answer correctly.** "The goal of the pilot is to prove the accuracy, prove the quality. You get your top AI-native folks in the organization who are eager to work with you, give you feedback, improve the product, make sure that you got the rough edges through" — a self-selected, tolerant cohort, chosen because they will report defects rather than churn on them. Duration is "a couple of weeks," ending when the rough edges smooth out. (05:49-06:11)
- **Beta: is there a minimum viable product.** At 10% of the organization — 600 people — the question changes: "Is the MVP really there? And what will happen is that you will start getting tons of requests. Can you connect this data? Can you connect that data. And then you are looking at where are the concentrations happening? Because that means that if you don't get those things in, you don't truly have an MVP. It's not going to work for their daily workflows." The request stream is read as a distribution, not a queue; concentration marks the missing capability, and the long tail is deferred. (06:12-06:41)
- **The beta exit bar is return behavior, not volume or sentiment.** "The things that we really track there is basically like, okay, how many questions they're asking, but what is the retention rate? So we exited for example that at like more than 70% retention rate that the weekly active users were coming back." Question count can be produced by novelty; weekly return cannot. (06:41-06:58)
- Only then GA — which introduces a problem none of the earlier stages can detect, because every earlier cohort either volunteered or was small enough to reach personally ([Separate the Did-Not-Try Problem From the Did-Not-Return Problem](separate-the-did-not-try-problem-from-the-did-not-return-problem.md)). (06:59-07:12)
- **What each stage's population buys you is different, and that is the actual design.** Pilot users are unrepresentative on purpose (they forgive), so they can only validate correctness. Beta users are representative enough to reveal workflow fit and to produce a retention number that means something. GA is the first cohort that includes people with no interest in the product, which is why activation only becomes visible there.
- Limits: the 10% / 600-person size and the 70% weekly-active retention bar are this organization's chosen numbers, given without derivation, and the retention denominator is not defined (of beta invitees, or of those who tried). No pilot-stage accuracy threshold is stated at all — "prove the quality" is left qualitative. ([Provenance and Limits](../sources/20260826_DrTdD-ttjCY.md))

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)
- [Separate the Did-Not-Try Problem From the Did-Not-Return Problem](separate-the-did-not-try-problem-from-the-did-not-return-problem.md)
- [Stage productivity pilots to strip one confound at a time](stage-productivity-pilots-to-strip-one-confound-at-a-time.md)
- [Reorder the Generated Task List to Ship an MVP First](reorder-the-generated-task-list-to-ship-an-mvp-first.md)
- [Earn AI Product Trust Before Asking for Delight](earn-ai-product-trust-before-asking-for-delight.md)
- [Move enterprise AI adoption beyond spot experiments](move-enterprise-ai-adoption-beyond-spot-experiments.md)

Sources:
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:33-07:12
