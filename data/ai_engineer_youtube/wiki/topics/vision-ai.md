# Vision AI

## Overview

Vision AI covers model and evaluation choices for systems that perceive images, video, physical scenes, documents, and specialized imaging domains. The current source-backed lesson is that practical vision should not be inferred from generic multimodal fluency or saturated classification/detection benchmarks. Real-world vision often has strict latency constraints, needs edge execution, and fails on fine visual details that language-aligned models can gloss over.

For AI engineers, the key distinction is visual fidelity versus language alignment. Caption-contrastive models can align images and text while missing pose, part, direction, or small-object distinctions that captions omit. Self-supervised vision-only features such as DINOv2 can preserve richer visual structure, but production VLMs still need ways to align those features with language and downstream detection tasks. Evaluation should therefore include domain-shifted object detection, specialized imaging modalities, few-shot examples, and annotator instructions instead of only common-class COCO performance.

## Key Concepts

- [Do not trust saturated vision benchmarks as visual intelligence](../concepts/do-not-trust-saturated-vision-benchmarks-as-visual-intelligence.md) - high scores on common visual benchmarks can hide weak spatial and fine-detail reasoning.
- [Use vision-only features when captions erase visual distinctions](../concepts/use-vision-only-features-when-captions-erase-visual-distinctions.md) - self-supervised visual features can preserve distinctions omitted from image captions.
- [Evaluate vision models on domain adaptability and few-shot grounding](../concepts/evaluate-vision-models-on-domain-adaptability-and-few-shot-grounding.md) - practical vision benchmarks should test class context, instructions, examples, and specialized domains.
- [Tune multimodal token budgets by visual or audio task](../concepts/tune-multimodal-token-budgets-by-visual-or-audio-task.md) - visual input resolution and token allocation should match the task's need for detail.
- [Keep visual inputs at native shape for GUI and video agents](../concepts/keep-visual-inputs-at-native-shape-for-gui-and-video-agents.md) - GUI and video agents need layout and temporal cues that fixed reshaping can damage.

## Open Questions

- How should rich vision-only feature spaces be aligned with language features without losing fine visual fidelity?
- Which domain-adaptability benchmark shapes best predict production object-detection success outside common web-photo classes?

## Sources

- [Vision AI in 2025 - Peter Robicheaux, Roboflow](../sources/20250803_IQc05eCvNYE.md)
