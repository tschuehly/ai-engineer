# Filter Background Audio Before Voice-Agent Inference

Summary: Voice agents should treat background noise and background voices as inference-triggering inputs, not only as transcription-quality issues. Speech-like noise can cause unwanted interruptions, spurious transcript content, and downstream LLM calls even when the transcription model itself is robust.

Use when:
- Diagnosing voice agents that interrupt unexpectedly or react to non-user speech.
- Designing preprocessing, turn detection, or noise suppression for realtime voice pipelines.

Details:
- The talk notes that transcription models can be resilient to noisy environments while LLMs and speech-to-speech models remain less resilient to the pseudo-speech created by background audio. 13:06-13:18, 13:42-13:48
- Background noise that sounds speech-like can trigger unintended interruptions and inject spurious pseudo-speech into transcripts, causing inference to fire down the chain at the wrong time. 13:18-13:42
- The recommended mitigation is to use dedicated noise suppression or filtering before inference; the talk cites Krisp as a commercial option and notes that Pipecat Cloud exposes it for hosted pipelines. 13:48-14:08
- Turn detection and interruption handling should be treated as runtime components, not only prompt behavior, because their errors decide when the model receives context and when the agent speaks. 03:19-03:46, 12:38-12:57

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Semantic turn detection improves voice interruption timing](semantic-turn-detection-improves-voice-interruption-timing.md)
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)

Sources:
- [Pipecat Cloud: Enterprise Voice Agents Built On Open Source - Kwindla Hultman Kramer, Daily](../sources/20250731_IA4lZjh9sTs.md), 03:19-03:46, 12:38-14:08
