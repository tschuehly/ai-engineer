# Post-Train Small Models for Narrow Capabilities

Summary: Small models are strongest when post-training focuses them on a small set of valuable capabilities, such as structured extraction or tool use, instead of trying to make them broadly average.

Use when:
- Fine-tuning a Hugging Face small model for a product-specific task.
- Deciding whether a small model should own data extraction, tool calling, summarization, or broad chat behavior.

Details:
- The LFM 2.5 recipe follows familiar stages: pre/mid-training, supervised fine-tuning, preference alignment, and reinforcement learning. The source says its 350M model was pre-trained on 28T tokens and still benefited from more pre-training at small scale. (06:08-07:40)
- Labonne frames small models as task-specific because their limited knowledge capacity can be turned into strength when the model is tuned for one narrow thing rather than general chatbot coverage. (01:25-01:49)
- For LFM 2.5 350M, the desired strengths were data extraction and tool use; weak coding or math performance mattered less because those were not the intended use cases. (07:41-08:31)
- Narrow SFT data is recommended for small-model fine-tuning, especially when the product needs a particular function call or similarly constrained behavior. (08:33-09:12)
- For RL, small models benefit from many focused environments and tasks; missing cold-start SFT examples for a target RL task can cause training to fail or stall. (09:39-10:37)

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Constrained decoding makes small-model tool calls production-usable](constrained-decoding-makes-small-model-tool-calls-production-usable.md)

Sources:
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md), 01:25-10:37
