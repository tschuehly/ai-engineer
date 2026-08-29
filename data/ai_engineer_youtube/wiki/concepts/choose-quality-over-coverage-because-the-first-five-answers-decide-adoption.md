# Choose Quality Over Coverage Because the First Five Answers Decide Adoption

Summary: A free-form assistant is judged on a handful of early answers by each user independently, so breadth bought at the cost of accuracy destroys the thing it was meant to grow. Answer fewer questions well rather than more questions passably: 50 questions at 95% beats 100 at 70%, because a user who bounces is roughly ten times harder to recover than one who was never asked.

Use when:
- Deciding the scope of a first launch for an internal assistant, chat surface, or agent with an open input box.
- A stakeholder is pushing to connect more data sources before the connected ones answer reliably.
- Prioritizing a backlog where "add a new data source" and "fix accuracy on an existing one" are competing.
- Estimating the cost of shipping a known-weak capability to a population you will need again later.

Details:
- The failure principle, stated as the reason non-deterministic products die: "user trust is earned extremely hard and is lost overnight." ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 03:16-03:36)
- **The mechanism is specific to a free-form input, and it is per-user rather than aggregate.** "At the end what you're doing is you're putting a free-form chatbot there, and people will come in and they will ask any question they can think of. If they like what they see in the first five questions, they come back. If they don't like what they see, it's 10 times more effort for you to win them back, if you can ever win them back." A 70% system does not deliver 70% satisfaction; it delivers a distribution of first-five experiences, and every user who draws two bad answers early is expensive or impossible to get back. (03:38-03:57)
- The rule that follows is a deliberate refusal of coverage: "we don't want to try to answer 100 questions and get them 70% right. We want to answer 50 questions, but get them 95% right… with that you get a good first impression, you build trust with them. And then rather than being in that boat of 'oh, this thing doesn't work,' people are like 'oh, this thing is awesome. Can I get more of that?'" (04:42-05:05)
- The team encodes it as a priority label rather than a value: "we have a saying in our team, we say quality is P minus one" — ranked above P0. (03:58-04:03)
- **The coverage is recoverable; the trust is not.** Starting narrow cost this team nothing durable: "we started small and 60% of the data we actually added after the launch," over the six to seven months following. Data sources can be connected later into a product users already trust; a reputation formed in week one cannot be re-formed later. (05:06-05:11, 05:14-05:31)
- He restates it as the first of his closing takeaways and as a hard rule rather than a tradeoff to tune: "quality over coverage. I'm very, very religious about this. If you go for the coverage, you are going to shoot yourself in the foot." (16:38-16:47)
- Scope note: this is an argument about *open-input* surfaces with a population of repeat users who choose whether to return. A fixed-workflow feature with no free-form box does not have a first-five-questions problem, and a one-shot consumer surface with no retention need does not carry the ten-times reacquisition cost.
- Limits: the "first five questions" threshold and the "10 times" reacquisition multiplier are asserted from operating experience, not measured; no churn or reactivation study is offered. The 95%/70% figures are illustrative targets, not observed accuracies — the only measured accuracy in the source is the 50% first run against a 150-question set. ([Provenance and Limits](../sources/20260826_DrTdD-ttjCY.md))

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Business Intelligence](../topics/business-intelligence.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Earn AI Product Trust Before Asking for Delight](earn-ai-product-trust-before-asking-for-delight.md)
- [Write the Question Set From the Business Process Before the Data Is Connected](write-the-question-set-from-the-business-process-before-the-data-is-connected.md)
- [Gate Each Rollout Phase on a Different Question](gate-each-rollout-phase-on-a-different-question.md)
- [Start GenBI with certified assets before autonomous SQL](start-genbi-with-certified-assets-before-autonomous-sql.md)
- [Nail Deterministic UX Before Probabilistic Delight](nail-deterministic-ux-before-probabilistic-delight.md)
- [Optimize Onboarding Around One Aha Moment](optimize-onboarding-around-one-aha-moment.md)

Sources:
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 03:16-05:31, 16:38-16:47
