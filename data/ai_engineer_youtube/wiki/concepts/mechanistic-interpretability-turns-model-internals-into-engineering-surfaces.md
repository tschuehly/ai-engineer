# Mechanistic Interpretability Turns Model Internals Into Engineering Surfaces

Summary: Mechanistic interpretability reverse engineers neural networks so internal features can be inspected and, in some cases, controlled. For AI engineers, the reusable idea is to treat features, activations, and neuron-level interventions as possible debugging and product surfaces alongside prompts, evals, and fine-tuning.

Use when:
- You need to explain why a model produced a behavior that prompt-level logs cannot diagnose.
- You are considering whether model-internal controls could complement prompting, judging, or fine-tuning.

Details:
- The talk defines interpretability as reverse engineering neural networks to understand what happens inside them, using the Golden Gate Claude example as a concrete case where a discovered feature represented a model concept and could be amplified. 01:00-02:21
- Interpretability is framed as moving from research demos into practical AI engineering, including developer power tools, user-facing interfaces, and scientific discovery over what models have learned. 02:23-04:02
- The key engineering claim is not that interpretability replaces existing controls, but that it exposes a lower-level surface for debugging and steering behavior when prompt edits, judges, or fine-tuning are too indirect. 04:35-07:13

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Activation Steering Can Patch Specific Runtime Behaviors](activation-steering-can-patch-specific-runtime-behaviors.md)
- [Model Diffs Inspect Post-Training Feature Changes](model-diffs-inspect-post-training-feature-changes.md)

Sources:
- [Why you should care about AI interpretability - Mark Bissell, Goodfire AI](../sources/20250727_6AVMHZPjpTQ.md), 01:00-07:13
