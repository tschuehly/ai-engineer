# On-Device Agents Can Combine Local Reasoning With Tool And API Calls

Summary: Gemma 4 edge use cases extend beyond chat into agentic workflows with function calling, local API interaction, structured JSON output, and thinking-mode demonstrations. The core inference can stay on-device while selected skills call external or local tools.

Use when:
- Building privacy-sensitive local agents that still need tool use.
- Evaluating whether a small on-device model can power structured agent workflows.

Details:
- The talk describes built-in support for function calling and tool calling, allowing an edge model to interact with local APIs while keeping core inference on the device.
- Structured JSON output is presented as native model support rather than a behavior achieved only through prompt engineering.
- Example skills include Wikipedia lookup, mood and sleep tracking with trend analysis, image-understanding plus music pairing, and multi-app local workflows.

Related topics:
- [Agents](../topics/agents.md)
- [Edge Inference](../topics/edge-inference.md)

Related concepts:
- [Use edge inference when latency, privacy, offline access, or token cost dominate](use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md)

Sources:
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md), 04:02-10:06
