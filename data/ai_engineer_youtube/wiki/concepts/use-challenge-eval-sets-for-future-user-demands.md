# Use Challenge Eval Sets For Future User Demands

Summary: Agent evals should include standard current workloads and harder challenge sets that anticipate what users will ask once the product succeeds on easier cases.

Use when:
- A product's AI feature improves enough that users naturally escalate to harder documents, fields, or questions.
- Evaluating extraction, Q&A, or private-content research agents that need both present reliability and headroom.

Details:
- Box combines LLM-as-judge checks, standard eval sets, harder challenge eval sets, and user feedback for agent evaluation.
- The challenge set exists because customers ask more difficult questions after seeing the system succeed: long documents, many fields, risk assessments, and edge cases become the new quality bar.
- Judge feedback is useful inside a loop when it can tell the agent to keep trying, not only when it reports uncertainty to the user after the answer is already produced.
- Enterprise feedback may be limited by privacy and visibility constraints, so explicit eval sets and opt-in feedback become important signals alongside production behavior.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build AI app benchmarks before optimization](build-ai-app-benchmarks-before-optimization.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Calibrate LLM judges like binary classifiers](calibrate-llm-judges-like-binary-classifiers.md)

Sources:
- [Building an Agentic Platform - Ben Kus, CTO Box](../sources/20250824_12v5S1n1eOY.md), 08:15-08:44, 12:08-12:23, 17:21-17:54
