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

- **The boundary of this approach, stated as a pun.** Pant's closing goal is software "not probably correct, but provably correct," and his opening move disqualifies judged output for code specifically: "using LLM as a judge for the code? Well, that's probabilistic." Read as a boundary rather than a rebuttal, it says: where behaviour can be stated as a property over all inputs, thresholds on judged samples are the weaker instrument and a mechanical check is available; where it cannot — tone, helpfulness, whether the agent was snarky — probabilistic specification remains the only instrument there is. The distinction to keep is which claims a threshold is standing in for. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 00:24-00:29, 09:38-09:46)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Treat Evals as the Home of Domain Knowledge](treat-evals-as-the-home-of-domain-knowledge.md)
- [Build Scoring Systems From Inspectable Quality Signals](build-scoring-systems-from-inspectable-quality-signals.md)
- [Map application evals to the product court](map-application-evals-to-the-product-court.md)
- [Ship a Proof a Small Kernel Can Recheck, Not a Claim You Must Trust](ship-a-proof-a-small-kernel-can-recheck.md)

Sources:
- [Shipping Products When You Don't Know What they Can Do - Ben Stein, Teammates](../sources/20250728_PthmdT92qNg.md), 08:32-10:12, 14:41-15:48
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 00:24-00:29, 09:38-09:46
