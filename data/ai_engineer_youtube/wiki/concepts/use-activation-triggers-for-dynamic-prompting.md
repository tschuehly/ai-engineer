# Use Activation Triggers for Dynamic Prompting

Summary: Dynamic prompting can watch internal model features during generation and inject prompt context only when a relevant feature activates. This turns model internals into a conditional routing signal for runtime instructions.

Use when:
- You need topic-specific or policy-specific context without forcing it into every prompt.
- You want intervention timing based on what the model is currently representing, not only on user-visible keywords.

Details:
- The talk describes setting a listener on a model feature so the system can keep a default prompt until a relevant internal feature starts firing. 09:55-10:17
- The demo watches for beverage and consumer-brand features; when the model begins generating a drink recommendation, the system injects a Coca-Cola-specific prompt in real time. 10:00-10:55
- The user sees one ordinary generation, while the orchestration layer observes feature activations and changes the prompt midstream. 10:55-11:13
- This pattern is powerful but should be evaluated carefully because hidden prompt injection can introduce bias, policy, or disclosure behavior that users and reviewers may not see directly. 10:17-11:13

Related topics:
- [Models](../topics/models.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Mechanistic Interpretability Turns Model Internals Into Engineering Surfaces](mechanistic-interpretability-turns-model-internals-into-engineering-surfaces.md)
- [Treat Prompts as Distributed Harness Surfaces](treat-prompts-as-distributed-harness-surfaces.md)

Sources:
- [Why you should care about AI interpretability - Mark Bissell, Goodfire AI](../sources/20250727_6AVMHZPjpTQ.md), 09:55-11:13
