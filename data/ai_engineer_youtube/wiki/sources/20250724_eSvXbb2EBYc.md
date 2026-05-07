# Building AI Products That Actually Work - Ben Hylak (Raindrop), Sid Bendre (Oleve)

Source: [Building AI Products That Actually Work - Ben Hylak (Raindrop), Sid Bendre (Oleve)](https://www.youtube.com/watch?v=eSvXbb2EBYc)
Uploaded: 2025-07-24
Transcript: `raw/20250724_eSvXbb2EBYc/eSvXbb2EBYc.en-orig.vtt`

## Summary

This talk frames AI product reliability as an iterative product-engineering loop rather than a one-time eval exercise: teams should expect undefined behavior, use evals for known regressions, mine production usage for signals plus intent, and convert discovered intents into contained semi-deterministic workflows that can be prioritized and improved.

## Extracted Concepts

- [Evals Only Cover Known AI Product Failures](../concepts/evals-only-cover-known-ai-product-failures.md) - this source explains why evals do not fully measure product quality and why production use must discover new failures.
- [AI Product Issues Need Signals and Intents](../concepts/ai-product-issues-need-signals-and-intents.md) - this source defines AI issue discovery around explicit and implicit signals plus user intent.
- [Turn AI Product Intents Into Contained Workflows](../concepts/turn-ai-product-intents-into-contained-workflows.md) - this source describes converting discovered intents into prioritized, semi-deterministic workflows.

## Topic Links

- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Product Strategy](../topics/product-strategy.md)

## Notes

- Model and API improvements can make some mechanics easier, such as structured JSON output becoming an API parameter, but communication and product intent remain hard because richer AI products create more undefined behavior and edge cases. (06:02-08:27)
- Evals are important but incomplete: they mostly test known cases, can saturate, and should not be expected to state whether the whole product is good. (08:31-09:18)
- The talk discourages defaulting to LLM judges for subjective quality and says stronger teams usually rely on curated datasets and autogradable checks where possible. (09:21-10:12)
- Production AI issues often have no exception; teams need explicit and implicit signals such as feedback, copy behavior, preference choices, regenerations, task failures, refusals, syntax errors, user frustration, and marked-correct or marked-wrong search results. (11:09-13:02)
- AI issue exploration should combine signal clusters with user intent and metadata such as product properties, models, keywords, and intents. (13:07-13:39)
- The Trellis-style workflow loop groups intents, converts them into semi-deterministic workflows, prioritizes by business-linked scoring, analyzes sub-intents, and recursively refines the workflows. (16:30-18:29)
