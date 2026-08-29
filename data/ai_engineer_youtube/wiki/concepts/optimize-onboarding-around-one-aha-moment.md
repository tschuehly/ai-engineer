# Optimize Onboarding Around One Aha Moment

Summary: A product's first-use workflow should route users to one clear aha moment as quickly as possible. Extra setup, profiling questions, or feature tours before that moment leak users before the product has earned their attention.

Use when:
- Reviewing signup, onboarding, or first-run flows for AI products and developer tools.
- Deciding which feature or interaction should be the first product proof a new user experiences.

Details:
- The aha moment is the interaction where the product clicks, the user understands what it is for, and even a non-target user can see who they would recommend it to. (06:39-07:09)
- Teams should identify the singular moment that matters most and deprioritize other features during onboarding, then inspect every step required to reach it. (07:09-07:46)
- Upfront questions such as company size, employee count, or title can be harmful when they appear before the user knows whether they want the product. (08:17-08:36)
- If only a tiny fraction of attracted users reaches the aha moment, top-of-funnel work is wasted; if no aha moment exists, the team should revisit what it is building. (08:43-09:03)
- **When the driver is an agent, keep the aha moment and discard the flow that led to it.** Metronome's aha moment is seeing a draft invoice against your own pricing model with usage drawn down against a credit balance. The wizard that used to walk a human there is skipped — "we don't need this now because we had an agent set up this environment" — while the destination is preserved and even enriched, since the agent also generates the usage that makes the invoice appear. The transferable rule: identify the moment, then ask separately whether the path to it is a human-sequencing artifact you no longer need. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 13:49-13:59, 14:22-15:41)
- **Optimizing the path to the aha moment does nothing if the population never enters it, and that is the more common failure in internal rollouts.** Two weeks after general availability, Izmit's assistant had been tried by 20% of the organization, and his reading is that no product work can move that number: "this is not the product's fault if people are not even taking 5 minutes to try the product. If they try it and if they don't come back, okay, that's my problem. But if they don't try it, then we have another problem." This page's funnel logic — if only a tiny fraction of attracted users reaches the aha moment, top-of-funnel work is wasted — has a mirror image: if there is no top of funnel at all, aha-moment work is wasted. In an internal deployment the distribution channel is management attention, and the remedy he describes is months of demos, per-team adoption dashboards, and executive sponsorship. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 07:34-08:26)
- **With an agent in the loop, the onboarding path is evaluated before anyone starts it.** Optimizing time-to-value assumes a user who has already begun. Jarmak's point is that an agent reads the shape of the path first and routes around it: a tool that "requires like three different demos and emailing sales reps" never gets recommended, so the aha moment is never reached because the funnel was never entered. The design implication is that the first step of onboarding has to be legible and executable from outside — see [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 12:28-12:53)
- **A direct tension with a signup-capture argument, and where each applies.** This page warns that upfront profiling questions — company size, employee count, title — leak users before the product has earned attention. Rosenthal's regret from OpenAI's inbound wave runs the other way: "add a very in-depth sales form… if people are willing to give you their phone number, you should get it," because the automation built months later had nothing to follow up with. The reconciliation is in her own qualifier — "it can be optional." Required fields before the aha moment cost activation; optional fields after it, or on a waitlist where there is no product to reach yet, cost little and are the only chance to collect something unrecoverable. See [Reply to Every Inbound and Over-Capture at Signup](reply-to-every-inbound-and-over-capture-at-signup.md). ([Rosenthal](../sources/20260826_wdTRsfw0KG0.md), 04:31-05:04)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Reverse-engineer AI app evals from user outcomes](reverse-engineer-ai-app-evals-from-user-outcomes.md)
- [Treat model behavior as a product craft](treat-model-behavior-as-a-product-craft.md)
- [Seed the Agent-Built Sandbox With Usage, Not Just Objects](seed-the-agent-built-sandbox-with-usage-not-just-objects.md)
- [Separate the Did-Not-Try Problem From the Did-Not-Return Problem](separate-the-did-not-try-problem-from-the-did-not-return-problem.md)
- [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md)
- [The Install Handoff Is Now a Prompt](the-install-handoff-is-now-a-prompt.md)
- [Reply to Every Inbound and Over-Capture at Signup](reply-to-every-inbound-and-over-capture-at-signup.md)
- [Never Send the Buyer Away With Homework](never-send-the-buyer-away-with-homework.md)

Sources:
- [AI changes *Nothing* — Dax Raad, OpenCode](../sources/20251123_o3gmwzo-Mik.md), 06:39-09:03
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 13:49-13:59, 14:22-15:41
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 07:34-08:26
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 12:28-12:53
- [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../sources/20260826_wdTRsfw0KG0.md), 04:31-05:04
