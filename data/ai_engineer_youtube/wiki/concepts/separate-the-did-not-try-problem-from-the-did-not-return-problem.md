# Separate the Did-Not-Try Problem From the Did-Not-Return Problem

Summary: Low usage after a launch has two causes that look identical on a usage dashboard and have opposite owners. If people tried it and did not come back, that is a product defect. If most of the organization never tried it at all, no amount of product work will move the number, and the remedy is months of unglamorous activation work.

Use when:
- Two weeks after a launch, leadership is asking why the numbers are flat.
- Deciding whether to spend the next sprint on quality or on adoption.
- Reporting on an internal AI rollout and needing a metric that assigns the problem correctly.
- Budgeting the time of whoever owns an internal agent, before assuming it is all engineering.

Details:
- The setup, and why engineers are the intended audience: "I know that this is a technical conference, but this is also where a lot of these products fail. It's basically how do you drive change management? So you launch your product, you are 2 weeks into the launch, and all your management is disappointed or frustrated. Why aren't people using this? Why are numbers real low?" ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 07:13-07:34)
- **The split, stated as an ownership boundary.** "I show them this graph. I say that only 20% of your organization actually tried the product. I cannot do anything. This is not the product's fault if people are not even taking 5 minutes to try the product. If they try it and if they don't come back, okay, that's my problem. But if they don't try it, then we have another problem." Two numbers, not one: trial rate and return rate. A usage total conflates them and points every diagnosis at the product. (07:34-07:53)
- The activation work is a real workload with a real owner, and it is not engineering: "usually this is a couple of month process. And then you significantly invest in change management, in activation. I will spend 60-70% of my time in sales meetings, giving demos, building dashboards, which teams adopted, shaming the managers whose team is actually doing good, getting sponsorship from sales leaders to make sure that they push their people to try these things." Note that one of the listed activities is itself instrumentation — per-team adoption dashboards, which is what makes manager-level pressure possible. (07:53-08:26)
- The counterfactual he offers for the effort: "if we hadn't done this, we would probably be doing half of where we are today. So this is a very important part. And as engineers, if you spend all your effort, you want to have a good product, make sure that the activation and the change management is lined up post launch of the product as well." (08:32-08:50)
- **Why the earlier stages cannot warn you about this.** Pilot and beta cohorts either volunteered or were small enough to be reached in person ([Gate Each Rollout Phase on a Different Question](gate-each-rollout-phase-on-a-different-question.md)), so trial rate is ~100% by construction and only return rate varies. General availability is the first cohort containing people with no interest, which is exactly when the trial-rate denominator becomes the binding constraint — and it arrives at the moment leadership starts reading the dashboard.
- This is the operational form of the cold-start problem in [Continual Learning and Enablement Are One Loop With a Cold Start](continual-learning-and-enablement-are-one-loop-with-a-cold-start.md): traces come from usage, usage does not appear on its own, and a log-mining improvement loop in a 20%-trial deployment is starved by construction ([Classify the Assistant Question Log to Find Feature and Content Gaps](classify-the-assistant-question-log-to-find-feature-and-content-gaps.md)).
- Limits: 20% is one measurement, two weeks after one GA, at one company; no trial curve over time and no eventual ceiling is reported. "Half of where we are today" is a counterfactual with no control. The tactics listed (executive sponsorship, manager-level comparison dashboards) assume a hierarchical sales organization and may not transfer to populations without that structure. ([Provenance and Limits](../sources/20260826_DrTdD-ttjCY.md))

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Go To Market](../topics/go-to-market.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Continual Learning and Enablement Are One Loop With a Cold Start](continual-learning-and-enablement-are-one-loop-with-a-cold-start.md)
- [Gate Each Rollout Phase on a Different Question](gate-each-rollout-phase-on-a-different-question.md)
- [Move enterprise AI adoption beyond spot experiments](move-enterprise-ai-adoption-beyond-spot-experiments.md)
- [Drive Org-Wide Agentic Adoption Through Champions and AI-Ready Repos](drive-org-wide-agentic-adoption-through-champions-and-ai-ready-repos.md)
- [Measure feature adoption, not shipping velocity](measure-feature-adoption-not-shipping-velocity.md)
- [Optimize Onboarding Around One Aha Moment](optimize-onboarding-around-one-aha-moment.md)

Sources:
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 07:13-08:50
