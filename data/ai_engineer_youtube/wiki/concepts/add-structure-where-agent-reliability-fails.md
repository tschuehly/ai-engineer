# Add structure where agent reliability fails

Summary: Start with the flexible agent behavior you need, then add workflow structure around the parts that fail reliability checks or need clearer traceability.

Use when:
- An agent works in broad strokes but fails at a specific subtask.
- Deciding whether to decompose one LLM call into multiple calls, steps, or handoffs.

Details:
- Bhagwat frames the design choice as a power-versus-control tradeoff: use agentic power where exploration matters and add control where behavior goes off the rails. (10:05-10:20)
- Workflows are popular in AI engineering because nondeterminism makes tracing what happened much more important than in ordinary deterministic code. (09:25-10:01)
- In a medical-documentation example, one broad LLM call over a large PDF and 12 symptoms can be decomposed into 12 LLM calls to improve reliability and retrieval specificity. (10:30-10:55)
- A practical whiteboarding exercise is to explain the architecture to a colleague, find the underperforming part, and add structure to that segment rather than redesigning the whole system around a doctrine. (10:55-11:42)
- Dynamic tool injection is another form of adding structure: avoid handing double-digit tool counts to an agent when a narrower task-specific tool set would reduce selection failure. (13:23-13:43)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Retrieve Tool Descriptions Before Loading Large Tool Catalogs](retrieve-tool-descriptions-before-loading-large-tool-catalogs.md)

Sources:
- [Agents vs Workflows: Why Not Both? - Sam Bhagwat, Mastra.ai](../sources/20250801_8SUJEqQNClw.md), 09:25-13:43
