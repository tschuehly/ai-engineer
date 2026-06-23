# Delegate Complex Voice-Agent Tasks Through Specialist Tools and Handoffs

Summary: A realtime voice model can act as the conversational front line while delegating complex, higher-risk, or more deterministic work to specialist agents and tools. This keeps the voice experience responsive without forcing one agent to carry every tool and policy decision.

Use when:
- A voice agent needs to answer simple conversational turns and perform business actions.
- Tool count, tool risk, or specialist model choice is making the voice agent brittle.

Details:
- The source describes a frontline realtime voice agent that handles normal interaction and easy questions, then calls other agents powered by stronger or more specialized models for harder tasks such as return-policy decisions, 08:47-09:55.
- Voice agents should start with a limited tool surface rather than 10 or 20 tools; additional tools can be added after the workflow proves it needs them, 11:37-12:14.
- When handing off between agents, summarize conversation state and pass it forward so the specialist agent receives the relevant context without losing the user's prior interaction, 12:16-12:45.
- Together AI names this the "thinker-talker" pattern and makes the latency motivation explicit: a small, fast LLM handles all conversation flow and emits an immediate filler response ("let me think about it" / "let me get back to you"), then issues a *single* tool call to a much larger model that has better instructions, all the tools, and more guardrails; the bigger model's cleaner response feeds the TTS. This keeps the fast path inside the LLM time-to-first-token budget while still handling complex requests. (`N7b1PJc7SFc`) 21:29-22:14

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Choose voice-agent architecture by latency, accuracy, and semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)
- [Split large automation surfaces into specialized subagents and subworkflows](split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md)
- [Keep Voice Agents Conversational During Long Tool Latency](keep-voice-agents-conversational-during-long-tool-latency.md)
- [Size the Voice-Agent LLM to the Time-to-First-Token Budget](size-the-voice-agent-llm-to-the-time-to-first-token-budget.md)

Sources:
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md), 08:47-12:54
- [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](../sources/20260531_N7b1PJc7SFc.md), 21:29-22:14
