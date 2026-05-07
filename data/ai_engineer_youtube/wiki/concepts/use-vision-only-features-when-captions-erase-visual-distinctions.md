# Use vision-only features when captions erase visual distinctions

Summary: Caption-aligned vision-language pretraining can discard distinctions that captions do not express. Vision-only self-supervised features can preserve fine visual structure that object detectors or VLMs may need.

Use when:
- Deciding whether a computer-vision model should rely on CLIP-style caption embeddings, DINO-style visual features, or a hybrid.
- Debugging VLM failures where language labels look correct but the model misses geometry, pose, parts, or visual state.

Details:
- MMVP constructs pairs that are close in CLIP space but far in DINOv2 space, exposing cases where caption-contrastive features treat visually distinct images as nearly the same. (04:05-05:21)
- Robicheaux's explanation is that CLIP learns from image-caption matching, but captions often omit discriminating details such as a dog's pose or facing direction; if the loss cannot tell the images apart, the model has little pressure to learn that distinction. (05:25-05:58)
- DINOv2's self-supervised features can discover masks, segments, and analogous parts such as dog legs and human legs, suggesting useful visual structure exists outside caption supervision. (05:58-06:37)
- The open engineering question is how to align rich visual features with language features so VLMs can use them without losing visual fidelity. (06:37-06:49)

Related topics:
- [Vision AI](../topics/vision-ai.md)
- [Models](../topics/models.md)

Related concepts:
- [Tune multimodal token budgets by visual or audio task](tune-multimodal-token-budgets-by-visual-or-audio-task.md)
- [Keep visual inputs at native shape for GUI and video agents](keep-visual-inputs-at-native-shape-for-gui-and-video-agents.md)

Sources:
- [Vision AI in 2025 - Peter Robicheaux, Roboflow](../sources/20250803_IQc05eCvNYE.md), 04:05-06:49
