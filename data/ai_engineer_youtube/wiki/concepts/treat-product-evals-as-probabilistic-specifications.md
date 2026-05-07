# Treat Product Evals as Probabilistic Specifications

Summary: For AI products, evals can become the executable product specification for behavior that deterministic requirements cannot capture. Product teams should inspect and shape evals because thresholds define what behavior is shippable.

Use when:
- Product, design, or support teams need a shared definition of acceptable probabilistic behavior.
- A behavior feels subjective, such as tone, helpfulness, interruption level, or whether an agent asked too many questions.

Details:
- The talk frames evals as a testing framework for probabilistic AI and agents, contrasting deterministic bank-account tests with subjective checks such as whether an agent was snarky in Slack. (08:56-09:28)
- A product behavior like "funny but not mean" can be turned into repeated judged outputs and an acceptable threshold, such as passing most of the time rather than requiring deterministic success. (09:32-09:56)
- Because evals are how the team knows what the product can do, product managers should have visibility into them and treat them as a product specification rather than an engineering-only artifact. (09:58-10:12)
- Bug triage becomes clearer when behavior is tied to eval thresholds: a refund workflow may need a 100% bar, while personality or tone may use lower thresholds; without that spec, "too many emojis" is hard to classify as a bug. (14:41-15:48)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Treat Evals as the Home of Domain Knowledge](treat-evals-as-the-home-of-domain-knowledge.md)
- [Build Scoring Systems From Inspectable Quality Signals](build-scoring-systems-from-inspectable-quality-signals.md)
- [Map application evals to the product court](map-application-evals-to-the-product-court.md)

Sources:
- [Shipping Products When You Don't Know What they Can Do - Ben Stein, Teammates](../sources/20250728_PthmdT92qNg.md), 08:32-10:12, 14:41-15:48
