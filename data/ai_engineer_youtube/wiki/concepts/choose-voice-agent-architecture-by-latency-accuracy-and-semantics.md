# Choose Voice-Agent Architecture by Latency, Accuracy, and Semantics

Summary: Voice agents can use a chained speech-to-text, LLM, and text-to-speech stack or a direct speech-to-speech model. The right choice depends on whether the workflow values low latency and preserved conversational semantics more than deterministic control and task-specific model selection.

Use when:
- Designing a production voice or audio agent.
- Deciding between a single realtime speech model and a multi-model chained audio pipeline.

Details:
- Chained audio systems transcribe incoming speech, pass text to an LLM, then synthesize speech on output; this gives builders more explicit control over each step but adds latency and can lose prosody or semantic nuance across the conversion boundaries, 04:16-05:23.
- Speech-to-speech systems collapse transcription, reasoning, and spoken output into one realtime model, reducing time to first response and preserving conversational meaning better for low-latency interactions, 04:54-05:23.
- Consumer-facing voice apps usually prioritize user experience, expressiveness, and latency, while customer-service workflows often prioritize accuracy, internal-system integrations, and correct tool outcomes even if the interaction feels less fluid, 05:25-07:19.
- Gemini Live API is described as a native audio approach where the model reasons sound-token to sound-token rather than cascading through transcription, text LLM reasoning, and speech synthesis; the workshop also notes that higher thinking levels improve reasoning at the cost of latency. 57:04-57:28, 62:06-62:30.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Delegate complex voice-agent tasks through specialist tools and handoffs](delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md)
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md)

Sources:
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md), 04:16-07:19
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md), 57:04-57:28, 62:06-62:30
