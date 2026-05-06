# Domain Gemma Variants Package Specialized Policy And Task Behavior

Summary: Open model families can ship or support specialized variants for policy checks and domain tasks, giving teams a stronger starting point than prompting a generic conversational model.

Use when:
- Deciding whether to fine-tune a general model or start from a domain-specialized open variant.
- Designing safety, medical, legal, finance, or other high-specificity model workflows.

Details:
- The talk distinguishes using Gemma out of the box from fine-tuning it to change style, improve capabilities, or make the model predict task-specific outputs in a local context. (10:59-11:24)
- Shield Gemma is presented as a family of models for production policy checks, such as identifying toxic image or text inputs that do not match configured policies. (11:26-11:46)
- MedGemma is presented as a multimodal Gemma 3-based model for medical tasks such as radiology and chest X-ray understanding, with further fine-tuning possible for niche use cases. (11:47-12:13)
- The broader claim is that open models are useful beyond chat assistants, including finance, legal review, offline workflows, private server-side use, screen understanding, and on-device control. (13:22-14:18)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Open Model Families Need Ecosystem-Compatible Tooling](open-model-families-need-ecosystem-compatible-tooling.md)
- [Post-train small models for narrow capabilities](post-train-small-models-for-narrow-capabilities.md)

Sources:
- [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](../sources/20260420__gVFUEdhCyI.md), 10:59-12:13, 13:22-14:18
