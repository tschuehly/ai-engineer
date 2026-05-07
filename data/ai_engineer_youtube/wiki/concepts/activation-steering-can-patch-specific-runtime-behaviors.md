# Activation Steering Can Patch Specific Runtime Behaviors

Summary: Activation steering uses model-internal feature controls at inference time to push a model toward or away from a behavior. It can target a narrower behavior than prompt rewrites when the relevant feature is discoverable and validated.

Use when:
- A model repeatedly violates a runtime policy such as privacy handling, tone, or jailbreak resistance.
- You need a steering mechanism that can be tested against evals without retraining the model.

Details:
- The talk contrasts activation steering with prompt whack-a-mole, LLM-as-judge cost, and fine-tuning risks such as spurious correlations, mode collapse, and reward hacking. 04:35-06:24
- In the Ember demo, token attribution identifies internal features active when the model says "confidential," including a feature related to sensitive and protected information. 08:02-08:44
- Raising that sensitive-information feature changes the model's next answer from revealing a stored email to refusing to share it, showing feature-level steering as a runtime control. 08:44-09:16
- The source also names jailbreak resistance and conditional information lookup as other possible neural-programming patterns, but those examples are described from developer docs rather than shown in depth. 09:27-09:50

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Mechanistic Interpretability Turns Model Internals Into Engineering Surfaces](mechanistic-interpretability-turns-model-internals-into-engineering-surfaces.md)
- [LLM Guardrails Need Checkpoints at Every Untrusted Boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)

Sources:
- [Why you should care about AI interpretability - Mark Bissell, Goodfire AI](../sources/20250727_6AVMHZPjpTQ.md), 04:35-09:50
