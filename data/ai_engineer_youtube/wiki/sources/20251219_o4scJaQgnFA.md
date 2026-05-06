# From Arc to Dia: Lessons learned building AI Browsers - Samir Mody, The Browser Company of New York

Source: [From Arc to Dia: Lessons learned building AI Browsers - Samir Mody, The Browser Company of New York](https://www.youtube.com/watch?v=o4scJaQgnFA)
Uploaded: 2025-12-19
Transcript: `raw/20251219_o4scJaQgnFA/o4scJaQgnFA.en-orig.vtt`

## Summary

Samir Mody describes The Browser Company's shift from Arc to Dia as an AI-native product rebuild, with lessons about building AI iteration tools into the product itself, treating model behavior as a product craft, using prompt mutation loops for hill climbing, and designing browser AI features around prompt-injection risk rather than assuming prompts or tags can fully solve it.

## Extracted Concepts

- [Build AI product iteration tools into the product context](../concepts/build-ai-product-iteration-tools-into-the-product-context.md) - this source shows why prompt, model, context, and tool editors should run in the same product environment users and teammates rely on.
- [Treat model behavior as a product craft](../concepts/treat-model-behavior-as-a-product-craft.md) - this source frames model behavior as a specialized function that turns principles into requirements, prompts, evals, and shipped assistant personality.
- [Use prompt mutation loops to hill-climb product behavior](../concepts/use-prompt-mutation-loops-to-hill-climb-product-behavior.md) - this source describes seeding, scoring, selecting, reflecting, mutating, and repeating prompts as a sample-efficient improvement loop.
- [Browser agents sit in the prompt-injection lethal trifecta](../concepts/browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md) - this source explains why browser-based agents combine private data, untrusted web content, and external action channels.

## Topic Links

- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Dia is presented as an AI-native browser with an assistant alongside browser work, personalization, tab context, and work across apps. (03:08-03:29)
- The team moved from a dev-only prompt editor to internal tools embedded in Dia, covering prompts, tools, context, models, and parameters; this expanded iteration beyond engineers to the CEO, PMs, designers, customer support, strategy, and operations. (04:45-06:26)
- The Browser Company also built tools for memory-knowledge-graph optimization and tried many computer-use strategies before integrating one into the product. (05:44-06:05)
- The product-development loop is described as broad ideation and dogfooding, followed by eval collection, requirement clarification, code/prompt/automation hill climbing, internal dogfooding, and shipping. (08:02-09:28)
- A prompt mutation mechanism is described as a sample-efficient way to improve a complex LLM system without reinforcement learning or fine-tuning: seed prompts, run tasks, score them, select better variants, use an LLM to reflect on failures and generate new prompts, then repeat. (06:50-07:42)
- Model behavior work includes defining desired style, tone, response shape, measurement data, evals, model selection, context-window contents, parameters, prompts, and feedback loops. (09:32-10:43)
- A non-engineer from strategy and operations used prompt tools to rewrite prompts over a weekend, and that work led to a model-behavior team, illustrating that the right model-behavior contributors may not be engineers. (11:47-12:47)
- Browser AI prompt injection is dangerous because the browser has private data, untrusted page content, and external communication channels such as websites, email, and calendar actions. (12:50-14:05)
- Tag-wrapping and role separation can reduce prompt-injection risk but do not guarantee safety; the product still needs UX and technical design that assumes attacks will happen. (14:08-15:16)
- For Dia autofill, email, and scheduling, user confirmation before writing sensitive data or taking external actions is presented as a control that gives awareness and trust even though it does not prevent prompt injection by itself. (15:21-16:14)
