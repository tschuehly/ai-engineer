# Delegate Complex Voice-Agent Tasks Through Specialist Tools and Handoffs

Summary: A realtime voice model can act as the conversational front line while delegating complex, higher-risk, or more deterministic work to specialist agents and tools. This keeps the voice experience responsive without forcing one agent to carry every tool and policy decision.

Use when:
- A voice agent needs to answer simple conversational turns and perform business actions.
- Tool count, tool risk, or specialist model choice is making the voice agent brittle.

Details:
- The source describes a frontline realtime voice agent that handles normal interaction and easy questions, then calls other agents powered by stronger or more specialized models for harder tasks such as return-policy decisions, 08:47-09:55.
- Voice agents should start with a limited tool surface rather than 10 or 20 tools; additional tools can be added after the workflow proves it needs them, 11:37-12:14.
- When handing off between agents, summarize conversation state and pass it forward so the specialist agent receives the relevant context without losing the user's prior interaction, 12:16-12:45.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Choose voice-agent architecture by latency, accuracy, and semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)
- [Split large automation surfaces into specialized subagents and subworkflows](split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md)

Sources:
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md), 08:47-12:54
