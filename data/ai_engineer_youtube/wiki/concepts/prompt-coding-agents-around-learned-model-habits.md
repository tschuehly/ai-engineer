# Prompt coding agents around learned model habits

Summary: Coding-agent prompts should account for both model capability and learned behavior. Instructions copied from another model or older harness can overconstrain a model, causing unnecessary exploration, latency, or worse task performance.

Use when:
- Migrating an agent harness to a newer coding model.
- Debugging why a capable model is slow, overexplores, or follows inefficient instructions.

Details:
- The source separates "intelligence" from "habit": intelligence covers the model's capabilities across languages, frameworks, and coding tasks, while habits are learned behaviors such as planning, context gathering, implementation, and testing. 06:01-06:57
- A model may already be trained to inspect context before editing; adding prompts from another model that demand exhaustive file inspection can make the agent spend too long looking around. 06:57-07:50
- One practical debugging technique is to ask the agent what instruction caused the inefficient behavior, then remove or change the prompt that pushes against the model's native coding workflow. 07:50-08:07
- Building or tuning the model and harness together makes these behavior assumptions more visible because the harness can be shaped around the model's trained tool and planning habits. 08:12-08:25

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Fresh Markdown context mitigates model rot in codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md)
- [Ask agents after each run what blocked their success](ask-agents-after-each-run-what-blocked-their-success.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)

Sources:
- [Future-Proof Coding Agents - Bill Chen & Brian Fioca, OpenAI](../sources/20251205_wVl6ZjELpBk.md), 06:01-08:25
