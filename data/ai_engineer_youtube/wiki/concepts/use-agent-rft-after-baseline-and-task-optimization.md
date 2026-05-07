# Use Agent RFT after baseline and task optimization

Summary: Agent reinforcement fine-tuning is a weight-changing optimization for tool-using agents that should come after data matching, base-model baselining, prompt optimization, and task/tool simplification. It is most useful when the remaining performance gap is specific to a well-defined agent workflow.

Use when:
- Deciding whether to improve an agent through prompts, tools, task design, or model post-training.
- Planning a reinforcement fine-tuning run for a tool-using reasoning agent.

Details:
- The talk places agent improvement in a sequence: prompt engineering can steer behavior, task optimization can simplify the task, add guardrails, add or remove tools, and adjust tool behavior, and fine-tuning changes model weights only after those levers have been tried. (01:44-02:45)
- Before using Agent RFT, teams should ensure train and eval datasets match production traffic, run the base model against those datasets to understand baseline performance, and optimize prompts or task shape before turning to RFT. (05:46-06:29)
- Agent RFT is framed for reasoning models that interact with the outside world through multi-step tool use, not for generic single-turn answer polishing. (03:21-03:36)
- Domain shift is a central reason to use RFT: a model may over-call tools, pass wrong inputs, or fail to reason over tool outputs when the production environment differs from the model's original training distribution. (03:53-04:47)

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Specialize models against private benchmarks with RL](specialize-models-against-private-benchmarks-with-rl.md)
- [Optimize LLM programs with metrics and teacher feedback](optimize-llm-programs-with-metrics-and-teacher-feedback.md)

Sources:
- [Agent Reinforcement Fine Tuning - Will Hang & Cathy Zhou, OpenAI](../sources/20251209_p1CmPZ2j6Lk.md), 01:44-06:29
