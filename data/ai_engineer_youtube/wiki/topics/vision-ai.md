# Vision AI

## Overview

Vision AI covers model and evaluation choices for systems that perceive images, video, physical scenes, documents, and specialized imaging domains. The current source-backed lesson is that practical vision should not be inferred from generic multimodal fluency or saturated classification/detection benchmarks. Real-world vision often has strict latency constraints, needs edge execution, and fails on fine visual details that language-aligned models can gloss over.

For AI engineers, the key distinction is visual fidelity versus language alignment. Caption-contrastive models can align images and text while missing pose, part, direction, or small-object distinctions that captions omit. Self-supervised vision-only features such as DINOv2 can preserve richer visual structure, but production VLMs still need ways to align those features with language and downstream detection tasks. Evaluation should therefore include domain-shifted object detection, specialized imaging modalities, few-shot examples, and annotator instructions instead of only common-class COCO performance.

Krea's image-model training talk shows the same caption-versus-pixels gap from the generative side, and inverts its consequence. In representation learning, a distinction the caption omits is one the encoder never learns; in generation, a property the caption omits becomes one the decoder always renders — Krea's captioner reliably failed to mention that a photographed painting was framed on a white wall, so the trained model hung every painting it generated on a white wall. Their fix is data selection rather than better captioning ([filter training images your captioner systematically mis-describes](../concepts/filter-images-your-captioner-systematically-mis-describes.md)), with the caption pipeline ordered to extract what the VLM under-reports first: OCR before captioning because text rendering matters, then optional metadata, then the detailed VLM pass. The same talk repurposes vision-model internals as tooling rather than analysis: a sparse autoencoder trained on a CLIP-style vision model becomes an [unsupervised tagging system](../concepts/use-sparse-autoencoder-features-as-an-unsupervised-data-tagger.md) whose activated features (watermarks, signatures, border artifacts, "black and white," "blurry") serve as filter or oversampling criteria with no labeled data. Both moves reinforce this topic's core distinction — language alignment is not visual fidelity — by showing what it costs downstream of the encoder.

A third use of a captioner appears in Arturo Nunez's game-engine talk, and it is neither training data nor perception at runtime: the vision model is labeling infrastructure for a catalog no one had time to annotate. With 6,000-7,000 3D assets and nothing but filenames and geometry, he screenshotted each model and ran a vision model over the render to [manufacture searchable descriptions in bulk](../concepts/bulk-tag-asset-libraries-with-a-vision-model-for-retrieval.md); the live product is then "mostly an LLM" and the vision pass never runs on the interaction path. Read against the caption-fidelity thread above, the same weakness applies with a different consequence: whatever the captioner systematically omits about an asset is what users will be unable to search for, and unlike a generation artifact it produces no visible symptom. The single-canonical-view assumption is the other untested part — interiors, thin geometry, and symmetric objects are exactly the cases where one render under-describes the asset.

## Key Concepts

- [Bulk-Tag an Asset Library With a Vision Model Over Rendered Views](../concepts/bulk-tag-asset-libraries-with-a-vision-model-for-retrieval.md) - a captioner used as offline labeling infrastructure for a non-textual catalog, where omissions become silent retrieval gaps.
- [Filter Training Images Your Captioner Systematically Mis-Describes](../concepts/filter-images-your-captioner-systematically-mis-describes.md) - consistent caption omissions become unconditional artifacts in a generative model trained on them.
- [Use Sparse Autoencoder Features as an Unsupervised Data Tagger](../concepts/use-sparse-autoencoder-features-as-an-unsupervised-data-tagger.md) - SAE features on a vision model act as off-the-shelf tags for corpus filtering.
- [Do not trust saturated vision benchmarks as visual intelligence](../concepts/do-not-trust-saturated-vision-benchmarks-as-visual-intelligence.md) - high scores on common visual benchmarks can hide weak spatial and fine-detail reasoning.
- [Use vision-only features when captions erase visual distinctions](../concepts/use-vision-only-features-when-captions-erase-visual-distinctions.md) - self-supervised visual features can preserve distinctions omitted from image captions.
- [Evaluate vision models on domain adaptability and few-shot grounding](../concepts/evaluate-vision-models-on-domain-adaptability-and-few-shot-grounding.md) - practical vision benchmarks should test class context, instructions, examples, and specialized domains.
- [Tune multimodal token budgets by visual or audio task](../concepts/tune-multimodal-token-budgets-by-visual-or-audio-task.md) - visual input resolution and token allocation should match the task's need for detail.
- [Keep visual inputs at native shape for GUI and video agents](../concepts/keep-visual-inputs-at-native-shape-for-gui-and-video-agents.md) - GUI and video agents need layout and temporal cues that fixed reshaping can damage.

## Open Questions

- How should rich vision-only feature spaces be aligned with language features without losing fine visual fidelity?
- Which domain-adaptability benchmark shapes best predict production object-detection success outside common web-photo classes?
- Which properties do production captioners systematically omit, and can that omission set be enumerated in advance rather than discovered from generation artifacts?
- How many rendered views does a 3D asset need before a captioner's description is reliable enough to serve as its only search metadata?

## Sources

- [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../sources/20260818_VBCDhRrvlYo.md)
- [Vision AI in 2025 - Peter Robicheaux, Roboflow](../sources/20250803_IQc05eCvNYE.md)
- [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../sources/20260818_-tviRdpmHvs.md)
