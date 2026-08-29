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
- **Each checkpoint you add is a dependency you added, which puts this argument in tension with itself.** Manuja treats guardrails as services rather than as policy: "guardrails are just like another service that can go down that can be unreliable and that's where you need to choose do you fail open or do you fail close… that's the trade-off between availability and security." More checkpoints therefore means more failure surface and more serial latency, so each one needs its own timeout — "it should always be the LLM that is the rate determining step" — its own fallback ("secondary provider, secondary checks, cache decisions"), and a deliberate default, where "the default choice should be the worst case that you can live with." The coverage argument on this page and the operational cost per checkpoint should be resolved explicitly rather than one at a time. See [Treat Guardrails as a Failable Dependency With Its Own Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md). ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 10:12-12:02)
- **A boundary most teams never classify: the inbound sales form.** Notion treats a prospect's contact-sales submission as untrusted user input precisely because "there is an agent in the middle," and pairs that classification with a rule that no agent speaks to a customer directly. It is a checkpoint placed by policy rather than by filter — no injection detector, sanitizer, or provenance check is described — and it only guards the write side, since research, enrichment, and draft scoring all consume the untrusted text before a human sees the result. ([Liu](../sources/20260826_L4I7WgiEquo.md), 07:23-07:58)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)
- [Constrained decoding makes small-model tool calls production-usable](constrained-decoding-makes-small-model-tool-calls-production-usable.md)
- [Treat Guardrails as a Failable Dependency With Its Own Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md)
- [Keep Agents Off the Customer Channel and Treat Inbound Forms as Untrusted Input](keep-agents-off-the-customer-channel-and-treat-inbound-forms-as-untrusted-input.md)

Sources:
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md), 15:14-17:50
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 10:12-12:02
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 07:23-07:58
