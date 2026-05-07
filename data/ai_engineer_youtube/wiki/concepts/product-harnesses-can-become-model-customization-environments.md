# Product Harnesses Can Become Model Customization Environments

Summary: When model behavior is central to the product experience, the product harness itself can become the training environment. This lets teams customize models against the actual interaction loop instead of treating model selection as a black-box API wrapper decision.

Use when:
- A product's user experience depends directly on agent or model behavior.
- Deciding where model customization should happen in the product stack.

Details:
- Brown argues that winning AI products often need the option to customize or improve a model somewhere in the model, stack, product, or full workflow rather than only wrapping an API. 04:46-05:05
- Cursor's Composer model and OpenAI Codex are presented as examples where the product experience is tightly bound to a model trained for that product. 05:09-05:39
- The reusable pattern is to take a harness representing the product and train the model inside that harness as an RL environment, with tasks and rewards aligned to product behavior. 05:42-05:55
- Building the environment forces teams to name the agent, product, harness, and optimization target before they tune prompts, select models, fine-tune, or run RL. 13:42-14:12
- Cursor Composer is a concrete instance of this pattern: the IDE, cloud-agent VM fleet, tool loop, semantic-search tool, and training setup were co-designed so RL rollouts could match the production product environment. 08:15-09:05

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Treat model behavior as a product craft](treat-model-behavior-as-a-product-craft.md)
- [Train coding-agent models with environments and expert developer reward](train-coding-agent-models-with-environments-and-expert-developer-reward.md)
- [Production-Matched RL Environments Train Coding Agents on Real Tool Surfaces](production-matched-rl-environments-train-coding-agents-on-real-tool-surfaces.md)
- [Treat environments as eval, data, and training substrates](treat-environments-as-eval-data-and-training-substrates.md)

Sources:
- [RL Environments at Scale - Will Brown, Prime Intellect](../sources/20251209__IzZWeuTx7I.md), 04:46-14:12
- [Building Cursor Composer - Lee Robinson, Cursor](../sources/20251202_fL1iJHtl51Q.md), 08:15-09:05
