# Use Frame Pipelines to Compose Realtime Voice Agents

Summary: Realtime voice agents can be built as ordered pipelines of processors that stream audio, text, tool events, and other frames between transport, model, and utility services. This keeps STT, LLM, TTS, recording, transcription, and provider-specific integrations swappable while preserving a single live conversation flow.

Use when:
- Designing a voice agent runtime that must combine realtime transport, model services, and utility processors.
- Deciding whether to hand-code one voice flow or compose reusable pipeline processors.

Details:
- Pipecat is described as an open source Python framework for voice and multimodal AI agents; its pipeline is a multimedia stream of processors that can receive, modify, or emit audio, video, text, or other data frames. 01:35-04:06
- A cascaded voice stack can be represented as transport input, speech-to-text, LLM, text-to-speech, and transport output; a native speech-to-speech model such as Gemini Live can collapse some of those processors while leaving orchestration utilities such as recording or artifact generation in the pipeline. 04:06-05:47
- Pipecat treats a pipeline as a list of processors, and a pipeline can itself act as a processor, which lets builders compose pipelines of pipelines for more complex realtime applications. 48:34-49:15
- Pipeline tasks run pipelines with parameters such as whether interruptions are allowed; a runner then executes the task, making realtime behavior an explicit runtime configuration rather than only prompt text. 49:15-50:08

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Choose voice-agent architecture by latency, accuracy, and semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md)

Sources:
- [Full Workshop: Realtime Voice AI - Mark Backman, Daily](../sources/20250803_nxuTVd7v7dg.md), 01:35-05:47, 48:34-50:08
