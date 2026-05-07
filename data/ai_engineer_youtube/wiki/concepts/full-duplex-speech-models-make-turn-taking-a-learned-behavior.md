# Full-Duplex Speech Models Make Turn-Taking a Learned Behavior

Summary: Full-duplex speech models process incoming audio and generate output at the same time, making turn-taking closer to a learned conversational behavior than a post-hoc VAD timeout. They may improve natural interruptions and backchannels, but current production voice agents may still need cascaded control for brand, pronunciation, instruction following, and integrations.

Use when:
- Comparing cascaded voice-agent turn detection with native speech-to-speech or full-duplex designs.
- Deciding whether a realtime voice product should prioritize natural conversation or explicit production control.

Details:
- Human listeners are full duplex: comprehension, endpoint prediction, and response generation overlap before the prior speaker's turn ends. 04:20-07:55
- Full-duplex models are described as always listening and always generating; Moshi is used as an example where the model emits natural silence when it is not its turn to speak. 16:06-17:41
- The talk contrasts rule-like turn detection with raw-audio learning: full-duplex models can learn turn-taking from audio data rather than relying on hand-written silence and end-of-turn rules. 16:20-17:05
- Sync LLM is described as forecasting the user's speech roughly five tokens or 200 milliseconds ahead, approximating part of the human turn-taking prediction loop. 17:41-18:12
- The tradeoff is production control: the speaker argues that commercial voice AI still needs controllable cascaded components for instruction following, brand names, and faster specialized models, so smarter VAD augmentation may remain practical even if full-duplex research is promising. 17:19-19:02
- Full-duplex models can natively produce backchannels such as short acknowledgements because they learn from raw conversational audio, but backchanneling remains a difficult field-wide problem. 26:27-26:44

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Semantic Turn Detection Improves Voice Interruption Timing](semantic-turn-detection-improves-voice-interruption-timing.md)
- [Choose Voice-Agent Architecture by Latency, Accuracy, and Semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)

Sources:
- [Why ChatGPT Keeps Interrupting You - Dr. Tom Shapland, LiveKit](../sources/20250731_1v9zBiZKlIY.md), 04:20-07:55, 16:06-19:02, 26:27-26:44
