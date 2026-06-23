# Size the Voice-Agent LLM to the Time-to-First-Token Budget

Summary: In a cascading voice pipeline the LLM consumes the majority of the latency and cost budget, so its size is dictated by a time-to-first-token target rather than by raw capability. A ~200-300 ms TTFT goal pins the model into an ~8-30B sweet spot: larger models blow the latency budget, smaller ones break tool calling and intelligence.

Use when:
- Choosing which LLM to run inside a real-time voice agent.
- Trading off model intelligence and tool-calling reliability against spoken-response latency.
- Allocating a latency/cost budget across the STT, LLM, and TTS stages.

Details:
- Across the orchestrated models there is one shared latency and cost budget, and the LLM dominates it — followed by TTS, then STT, on both latency and cost — so the LLM is the stage to size first. (11:08-11:32)
- The governing LLM metric is streaming latency / time-to-first-token; ~200-300 ms TTFT is a good target so tokens begin feeding the TTS model as fast as possible. (08:40-09:00)
- That TTFT budget dictates model size: a good fit is typically ~8-30B parameters. Go bigger and you burn through the latency budget; go too small and you lose the intelligence and tool-calling needed for a voice agent that does meaningful real-world work. (09:00-09:13)
- Tool calling is the hard floor: it is how the agent acts on the world, so the model must clear a baseline of tool-calling competence that very small models miss. (03:17-03:37)
- Recovery move within the budget: fine-tune a smaller LLM on use-case-specific data to push tool-calling quality up while keeping the model small enough to stay inside the latency budget. (17:50-18:29)
- Validate with component-level tool-calling evals (was the call correct? was the output possible?) — tool-call *structure* should be near 100%, with correctness judged against the use case. (16:44-17:38)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Design voice agents around voice-to-voice latency budgets](design-voice-agents-around-voice-to-voice-latency-budgets.md)
- [Separate Engine Latency From Network Latency in Voice Pipelines](separate-engine-latency-from-network-latency-in-voice-pipelines.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Decide when to fine-tune from three signals](decide-when-to-fine-tune-from-three-signals.md)

Sources:
- [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](../sources/20260531_N7b1PJc7SFc.md), 08:40-09:13, 11:08-11:32, 16:44-18:29
