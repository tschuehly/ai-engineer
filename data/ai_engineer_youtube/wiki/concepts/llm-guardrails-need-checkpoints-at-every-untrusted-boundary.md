# LLM Guardrails Need Checkpoints at Every Untrusted Boundary

Summary: LLM safety should be implemented as checkpoints around each untrusted boundary, not as a single prompt or output filter. More autonomous systems need more checkpoints because user input, retrieval, tool metadata, memory, plans, and outputs can all carry attack signals.

Use when:
- Designing production guardrails for agents, RAG systems, MCP tools, or memory-bearing applications.
- Choosing where to run safety classifiers, policy checks, canary-token checks, or constrained decoding.

Details:
- The talk argues that more complex and autonomous systems need more checkpoints; minimum production checks should cover user inputs and model responses. 17:01-17:21
- Stronger coverage should also inspect retrieval augmentation, MCP interactions, context memory, and agentic plans because those components can introduce instructions the model treats as context. 17:21-17:34
- Available implementation options include rule filtering, canary tokens, discriminators, constrained decoding, and LLM-as-judge checks when extra latency is acceptable. 17:34-17:50
- The source warns that model alignment is not a hard constraint and that human review alone can fail when the reviewer sees a simplified surface instead of the actual instructions or parameters being approved. 15:14-15:39

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)
- [Constrained decoding makes small-model tool calls production-usable](constrained-decoding-makes-small-model-tool-calls-production-usable.md)

Sources:
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md), 15:14-17:50
