# Earn AI Product Trust Before Asking for Delight

Summary: AI products earn the right to delight only after they fulfill the first promise users test. Trust comes from reliable first-use delivery, honest model edges, and humane failure handling.

Use when:
- Designing first-run or first-query experiences for AI products.
- Choosing how much uncertainty, novelty, or model failure to expose in the UI.

Details:
- The source describes a product as a promise to the user; a user who spends time trying the product has limited patience for the first promised job to fail. 13:21-14:02
- Trust can be built by exposing model edges and showing where the model is weak instead of papering over failures. 14:02-14:15
- The early NotebookLM summarization query was a trust bottleneck: roughly 90% of first queries were summarization attempts, and failure on that path could cause users to leave permanently. 15:20-16:52
- Delight comes after trust: once the first promise is credible, the product can push one step beyond what is familiar without alienating users. 16:53-18:23
- **The enterprise-internal version of the same rule, with a price attached to failing it.** Izmit runs a go-to-market assistant for ~6,000 users on the principle that "user trust is earned extremely hard and is lost overnight," and gives the mechanism for an open input box rather than a single promised job: "people will come in and they will ask any question they can think of. If they like what they see in the first five questions, they come back. If they don't like what they see, it's 10 times more effort for you to win them back, if you can ever win them back." The operating consequence is a refusal of breadth — "we don't want to try to answer 100 questions and get them 70% right. We want to answer 50 questions, but get them 95% right" — and it was affordable because coverage is recoverable later: 60% of that system's data was connected after launch. NotebookLM's version is one promise tested by nearly every first user; this one is a distribution of promises the user selects themselves, which is why the remedy is scope rather than reliability on a known path. Both figures are experience claims, not measured churn. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 03:16-05:11)

Related topics:
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Nail Deterministic UX Before Probabilistic Delight](nail-deterministic-ux-before-probabilistic-delight.md)
- [Use Agency Instead of Trickery for AI Delight](use-agency-instead-of-trickery-for-ai-delight.md)
- [Start with augmentation when autonomous reliability is not ready](start-with-augmentation-when-autonomous-reliability-is-not-ready.md)
- [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)

Sources:
- [Everything is ugly, so go build something that isn't - Raiza Martin, Huxe (ex NotebookLM)](../sources/20250728_yG5d5UaGz1M.md), 13:21-18:23
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 03:16-05:11
