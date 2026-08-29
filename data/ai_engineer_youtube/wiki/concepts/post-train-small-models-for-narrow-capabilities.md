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


- **Routing is a good example of the narrow-capability profile, and it comes with a latency argument this page does not otherwise make.** DigitalOcean serves model routing from "a custom mixture of experts model purpose-built for routing" and claims it beats "frontier models like the GPT-5 series models at routing task itself with a fraction of the latency," deciding in "under 200 milliseconds" ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 05:07-05:35, 13:47-14:28). The task fits the profile exactly — high-frequency classification over a fixed, caller-declared label set — but the deciding constraint is not accuracy: a router sits on every request's critical path, so its own latency is subtracted from the saving it produces, which rules out a general-purpose model regardless of how well that model routes. Narrow post-training is sometimes chosen for capability and sometimes, as here, because nothing large is allowed on the path at all. See [A Router Must Be Cheap and Fast Enough to Disappear](a-router-must-be-cheap-and-fast-enough-to-disappear.md). Vendor claim with no accuracy figure, no routing benchmark named, no model size, and no description of the training data or label set.

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Constrained decoding makes small-model tool calls production-usable](constrained-decoding-makes-small-model-tool-calls-production-usable.md)
- [A Router Must Be Cheap and Fast Enough to Disappear](a-router-must-be-cheap-and-fast-enough-to-disappear.md)

Sources:
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md), 01:25-10:37
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 05:07-05:35, 13:47-14:28
