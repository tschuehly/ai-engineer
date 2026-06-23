# Choose Voice-Agent Architecture by Latency, Accuracy, and Semantics

Summary: Voice agents can use a chained speech-to-text, LLM, and text-to-speech stack or a direct speech-to-speech model. The right choice depends on whether the workflow values low latency and preserved conversational semantics more than deterministic control and task-specific model selection.

Use when:
- Designing a production voice or audio agent.
- Deciding between a single realtime speech model and a multi-model chained audio pipeline.

Details:
- Chained audio systems transcribe incoming speech, pass text to an LLM, then synthesize speech on output; this gives builders more explicit control over each step but adds latency and can lose prosody or semantic nuance across the conversion boundaries, 04:16-05:23.
- Speech-to-speech systems collapse transcription, reasoning, and spoken output into one realtime model, reducing time to first response and preserving conversational meaning better for low-latency interactions, 04:54-05:23.
- Consumer-facing voice apps usually prioritize user experience, expressiveness, and latency, while customer-service workflows often prioritize accuracy, internal-system integrations, and correct tool outcomes even if the interaction feels less fluid, 05:25-07:19.
- ElevenLabs' conversational-agent workshop describes the cascaded production shape as speech-to-text, an external text LLM such as GPT-4o or Gemini, and text-to-speech; the speaker says this path can be easier to monitor and understand than a direct sound-token-to-sound-token model. 08:29-10:41.
- To offset the latency of a cascaded architecture, the workshop says the speech, LLM, and voice models are deployed close together. 10:41-10:49.
- Gemini Live API is described as a native audio approach where the model reasons sound-token to sound-token rather than cascading through transcription, text LLM reasoning, and speech synthesis; the workshop also notes that higher thinking levels improve reasoning at the cost of latency. 57:04-57:28, 62:06-62:30.
- Native speech-to-speech models preserve information that transcription can lose and can reduce chained inference calls, but the talk warns that current audio-mode models can be less reliable for enterprise instruction following, function calling, and language control than text-mode models. 19:16-20:51, 24:03-26:39.
- Gemini 3.1 Flash Live is a concrete native sound-to-sound example: full-duplex, multimodal real-time ingest of text/audio/video over a WebSocket with audio plus a text transcript returned, and thinking/reasoning/intelligence baked directly into the model rather than cascaded through a separate text LLM; it is reachable for no-cost trial at `ai.studio/live`, with video-frame ingest capped at one frame per second. (`Bc6Ojl2XS1w`) 02:42-02:57, 12:08-13:27, 14:54-15:08.
- Even a native model still needs explicit instruction control: in the live demo an Irish-accent system instruction bled into a German-language response, so language-scoped accent instructions remain necessary. (`Bc6Ojl2XS1w`) 14:31-14:46.
- Audio-space benchmarks are explicitly called untrustworthy, reinforcing that architecture choice should rest on product behavior and evals rather than published audio scores. (`Bc6Ojl2XS1w`) 12:31-12:34.
- Together AI confirms the cascading pipeline (STT → LLM → TTS, fronted by an agent orchestrator such as Pipecat, LiveKit, or homegrown) as "the dominant way to build agents in production today." (`N7b1PJc7SFc`) 04:22-04:50
- The production reason speech-to-speech is not yet default: single-model S2S systems (OpenAI Realtime API; NVIDIA's recently launched "voice chat") still struggle with instruction following and tool calling, so the real-world path is "try them → prompt-engineer to patch issues → eventually move back to a pipeline." (`N7b1PJc7SFc`) 14:24-15:35
- The upside that will pull teams toward S2S as it matures: it preserves speech nuance (tone, emotion, hesitation) that STT→text destroys, and it is full-duplex — the model can produce audio while still receiving audio, enabling native backchannels ("I see," "aha") and far easier interruption/barge-in handling than a pipeline's bespoke engineering. (`N7b1PJc7SFc`) 15:35-16:22
- Even within the cascaded path, the STT stage is evolving from batch to streaming-native: Whisper was trained on 30-second clips (too long for live, forcing chunking/silence-padding/multi-call stitching), whereas a recent NVIDIA streaming encoder trains with variable look-ahead (~80 ms up to ~1 s) and caches activations so stepping forward by small audio frames only does the heavy compute once. (`N7b1PJc7SFc`) 07:06-08:16

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Delegate complex voice-agent tasks through specialist tools and handoffs](delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md)
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md)
- [Evaluate Speech-To-Speech Models Against Enterprise Control Needs](evaluate-speech-to-speech-models-against-enterprise-control-needs.md)
- [Multilingual Voice Agents Need Language Detection and Switching](multilingual-voice-agents-need-language-detection-and-switching.md)
- [Orchestrate Generative Media From a Real-Time Voice Agent via Tool Use](orchestrate-generative-media-from-a-realtime-voice-agent.md)

Sources:
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md), 04:16-07:19
- [[Full Workshop] Building Conversational AI Agents - Thor Schaeff, ElevenLabs](../sources/20250731_MPtCBaZn84A.md), 08:29-10:49
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md), 57:04-57:28, 62:06-62:30
- [Pipecat Cloud: Enterprise Voice Agents Built On Open Source - Kwindla Hultman Kramer, Daily](../sources/20250731_IA4lZjh9sTs.md), 19:16-20:51, 24:03-26:39
- [From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](../sources/20260609_Bc6Ojl2XS1w.md), 02:42-02:57, 12:08-15:08
- [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](../sources/20260531_N7b1PJc7SFc.md), 04:22-04:50, 07:06-08:16, 14:24-16:22
