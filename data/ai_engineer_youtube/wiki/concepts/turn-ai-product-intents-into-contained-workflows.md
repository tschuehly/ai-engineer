# Turn AI Product Intents Into Contained Workflows

Summary: After user intents are discovered, AI product teams can improve reliability by turning them into semi-deterministic workflows that are broad enough to be useful, narrow enough to evaluate, and contained enough that fixes do not spill across the product.

Use when:
- A broad AI feature behaves unpredictably across many user intents.
- A team needs to prioritize which AI workflow to harden next.

Details:
- Sid Bendre describes the Trellis framework as a loop for grouping traffic by intent, converting intents into workflows, prioritizing the workflows, analyzing failures inside them, and recursively refining sub-intents. (16:30-17:02)
- A workflow should be broad enough to cover many possibilities but narrow enough to be reliable; it should produce a defined output through a predefined set of steps. (16:30-16:45)
- Workflow priority should use business-linked scoring, not volume alone; the talk suggests moving from volume to negative sentiment times volume, then adding estimated achievable delta and strategic relevance. (16:45-17:49)
- Contained workflows make improvements self-attributable, deterministic, and self-bound, so teams can change one workflow without accidental effects across other workflows. (17:52-18:29)

Related topics:
- [Workflows](../topics/workflows.md)
- [Product Strategy](../topics/product-strategy.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Add structure where agent reliability fails](add-structure-where-agent-reliability-fails.md)
- [Build domain-specific workflow wrappers around models](build-domain-specific-workflow-wrappers-around-models.md)

Sources:
- [Building AI Products That Actually Work - Ben Hylak (Raindrop), Sid Bendre (Oleve)](../sources/20250724_eSvXbb2EBYc.md), 16:30-18:29
