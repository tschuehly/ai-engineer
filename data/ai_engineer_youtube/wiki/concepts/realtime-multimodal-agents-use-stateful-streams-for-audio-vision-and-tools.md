# Realtime multimodal agents use stateful streams for audio, vision, and tools

Summary: Realtime conversational agents can run as stateful streaming sessions where audio, visual frames, tool calls, transcriptions, and model events flow over one connection. This makes the agent responsive to live conversation and screen context, but forces latency, frame-rate, tool, and context-retention tradeoffs into the runtime design.

Use when:
- Designing a voice or multimodal assistant that reacts to live audio, screen share, camera, or canvas input.
- Choosing between a realtime streaming model API and a request-response chat API.

Details:
- The Live API is described as a stateful WebSocket API that accepts realtime text, audio, and video input; audio is sent as streaming buffers and video can be sent at up to one frame per second. 55:36-56:05
- Visual input can represent a camera feed, canvas, or screen share, allowing the agent to talk a user through a task while observing the current UI state. 56:05-56:36
- The server streams realtime events back, including audio buffers and audio transcription, and supports tool calls such as built-in Google Search grounding. 56:36-57:00
- Native audio avoids a cascading speech-to-text, LLM, and text-to-speech pipeline by reasoning over sound tokens directly; the same section notes that higher thinking levels increase latency. 57:04-57:28, 62:06-62:30

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Choose voice-agent architecture by latency, accuracy, and semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)
- [Prompt voice agents for persona, prosody, and brand fit](prompt-voice-agents-for-persona-prosody-and-brand-fit.md)
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)

Sources:
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md), 55:36-57:28, 62:06-62:30
