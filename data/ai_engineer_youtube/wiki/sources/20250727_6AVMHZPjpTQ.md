# Why you should care about AI interpretability - Mark Bissell, Goodfire AI

Source: [Why you should care about AI interpretability - Mark Bissell, Goodfire AI](https://www.youtube.com/watch?v=6AVMHZPjpTQ)
Uploaded: 2025-07-27
Transcript: `raw/20250727_6AVMHZPjpTQ/6AVMHZPjpTQ.en-orig.vtt`

## Summary

Mark Bissell frames mechanistic interpretability as an emerging engineering layer for reverse-engineering and steering model internals, not only as lab research. The talk shows how feature attribution can explain token choices, activation steering can improve privacy behavior, feature-triggered dynamic prompting can inject context during generation, model diffs can inspect post-training behavior changes, and concept-level controls can create new generative-media interfaces.

## Extracted Concepts

- [Mechanistic Interpretability Turns Model Internals Into Engineering Surfaces](../concepts/mechanistic-interpretability-turns-model-internals-into-engineering-surfaces.md) - this source defines interpretability as reverse engineering neural networks and applying that knowledge to model behavior.
- [Activation Steering Can Patch Specific Runtime Behaviors](../concepts/activation-steering-can-patch-specific-runtime-behaviors.md) - this source demonstrates raising a sensitive-information feature so a chat model refuses to reveal stored PII.
- [Use Activation Triggers for Dynamic Prompting](../concepts/use-activation-triggers-for-dynamic-prompting.md) - this source shows feature listeners that inject prompts when a topic feature starts firing during generation.
- [Model Diffs Inspect Post-Training Feature Changes](../concepts/model-diffs-inspect-post-training-feature-changes.md) - this source proposes diffing model features after post-training to catch behavioral shifts before deployment.
- [Interpretability-Native Interfaces Expose Concept-Level Model Controls](../concepts/interpretability-native-interfaces-expose-concept-level-model-controls.md) - this source demonstrates painting with learned image-model concepts instead of relying only on text prompts.

## Topic Links

- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)

## Notes

- Mechanistic interpretability is described as reverse engineering neural networks to understand and manipulate what happens inside them, with the Golden Gate Claude example illustrating a found feature that can be amplified to change behavior. 01:00-02:21
- The speaker positions interpretability as moving from lab demos into practical AI engineering use cases: developer power tools, new UI/UX surfaces, and scientific discovery over model-learned representations. 02:23-04:02
- Prompt edits, LLM-as-judge checks, and fine-tuning are presented as useful but limited levers: prompt changes can create off-target failures, judges add cost and another system to maintain, and fine-tuning can learn spurious correlations, collapse modes, or reward hacks. 04:35-06:24
- Goodfire's Ember demo uses token attribution to show which internal features influenced a token, then increases a sensitive-information feature so the model refuses to reveal a confidential email. 06:49-09:16
- Dynamic prompting is shown as a feature-triggered listener: when beverage-related features fire during generation, the system injects a Coca-Cola-specific prompt in real time. 09:30-11:13
- Model diffs are proposed for post-training inspection: comparing changed features could surface shifts such as increased sycophancy before a model is deployed. 11:44-12:24
- Paint with Ember demonstrates a concept palette for image models, where users place and scale learned concepts such as pyramid, wave, lion face, and opening mouth directly on a canvas. 12:38-15:28
