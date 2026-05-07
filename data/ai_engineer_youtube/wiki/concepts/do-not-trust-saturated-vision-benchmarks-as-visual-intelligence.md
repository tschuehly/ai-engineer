# Do not trust saturated vision benchmarks as visual intelligence

Summary: Common vision benchmarks can become saturated pattern-matching tests. A model that scores well on ImageNet or COCO may still fail fine-grained visual reasoning, spatial interpretation, or domain-shifted detection work.

Use when:
- Choosing evaluation criteria for computer-vision or VLM systems.
- Explaining why a high COCO or ImageNet score does not prove robust visual understanding.

Details:
- Robicheaux argues that vision evals such as ImageNet and COCO are mostly pattern matching and do not require much visual intelligence, so they create weak incentives for smarter visual features. (01:50-02:13)
- The talk uses VLM failures on clock-reading and bus-direction questions as evidence that models can know the abstract concept of a watch or bus while missing precise visual details such as hand positions, numbers, front/back cues, and hallucinated supporting details. (03:24-04:44)
- COCO can be optimized through precise bounding-box refinement on common classes such as people, cats, dogs, and cups, which does not necessarily measure whether a model understands harder domains or rare visual concepts. (09:41-10:12)

Related topics:
- [Vision AI](../topics/vision-ai.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Benchmark narrow slices separately from real expert work](benchmark-narrow-slices-separately-from-real-expert-work.md)
- [Evaluate whether models reject impossible or nonsensical premises](evaluate-whether-models-reject-impossible-or-nonsensical-premises.md)

Sources:
- [Vision AI in 2025 - Peter Robicheaux, Roboflow](../sources/20250803_IQc05eCvNYE.md), 01:50-04:44
