# Evaluate vision models on domain adaptability and few-shot grounding

Summary: Vision evaluation should test whether a model can adapt to new visual domains using class names, annotator instructions, and a few examples. That better matches practical object-detection work than only measuring common-class performance on COCO.

Use when:
- Building a benchmark for object detectors or VLMs that must work on specialized domains.
- Comparing general VLMs against fine-tuned specialist detectors.

Details:
- RF100-VL is described as 100 curated object-detection datasets from Roboflow Universe chosen to include difficult domains, camera poses, and imaging modalities such as aerial imagery, microscopes, and X-rays. (10:17-11:17)
- Robicheaux frames RF100-VL as measuring feature richness and domain adaptability more comprehensively than COCO because it includes less common classes and specialized imaging contexts. (11:10-12:31)
- In the talk's comparison, a YOLOv8 model trained on 10 examples per class can outperform a large VLM such as Qwen 2.5-VL 72B on RF100-VL, suggesting current VLMs generalize better linguistically than visually. (12:42-13:09)
- The few-shot track provides class names, annotator instructions, and 10 visual examples per class; current models struggle to combine all three, which the talk treats as a core VLM shortcoming. (15:33-17:10)
- Specialist detectors still lead on the benchmark: zero-shot Grounding DINO is weaker than a 10-shot YOLOv8 Nano baseline, while fine-tuned Grounding DINO with federated loss is the strongest reported model. (16:23-16:58)

Related topics:
- [Vision AI](../topics/vision-ai.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Domain evals need expert-built environments](domain-evals-need-expert-built-environments.md)
- [Use challenge eval sets for future user demands](use-challenge-eval-sets-for-future-user-demands.md)

Sources:
- [Vision AI in 2025 - Peter Robicheaux, Roboflow](../sources/20250803_IQc05eCvNYE.md), 10:17-17:10
