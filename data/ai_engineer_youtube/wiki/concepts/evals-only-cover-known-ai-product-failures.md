# Evals Only Cover Known AI Product Failures

Summary: Offline evals are useful regression tools, but they should not be treated as a complete measure of AI product quality. They mostly cover failures the team already knows how to name, so real production use and fresh user signals must keep discovering new issue classes.

Use when:
- A team wants eval scores to answer whether an AI product is good overall.
- A product is moving offline evals directly into production scoring without checking cost, coverage, or emerging behavior.

Details:
- Ben Hylak argues that evals do not tell teams how good a product is, because they cover known cases and can be saturated; newer models can score lower on some evals while still feeling better in real use. (08:31-09:18)
- LLM-as-judge scoring is tempting for subjective qualities, but the talk says strong teams usually prefer curated datasets and autogradable checks where deterministic pass/fail is possible. (09:21-10:12)
- Moving offline judges directly onto production traffic can be expensive, hard to configure accurately, and still limited to patterns the team already expected. (10:14-11:04)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Keep eval data constant and task logic variable](keep-eval-data-constant-and-task-logic-variable.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)

Sources:
- [Building AI Products That Actually Work - Ben Hylak (Raindrop), Sid Bendre (Oleve)](../sources/20250724_eSvXbb2EBYc.md), 08:31-11:04
