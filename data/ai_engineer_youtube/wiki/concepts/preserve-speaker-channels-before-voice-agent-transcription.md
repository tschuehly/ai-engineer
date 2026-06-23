# Preserve Speaker Channels Before Voice-Agent Transcription

Summary: Voice intelligence pipelines should preserve separate speaker channels before transcription so the model can identify who said what. Mixing an agent and customer into one mono track makes downstream summaries and intent extraction less reliable.

Use when:
- Designing call-center, meeting, or voice-agent ingestion where multiple speakers can overlap.
- Debugging summaries that confuse operator actions with customer requests.

Details:
- Contact-center audio is often messy, overlapping, emotionally charged, and multi-channel before it becomes text. Treating that stream as clean text hides the hardest part of the system. (01:12-01:38)
- The capture layer should tap the telephony system for high-fidelity audio, apply noise filters and level normalization, then map stereo channels so the agent and customer stay separate. (07:11-08:49)
- Combining both speakers into one mono track can make the AI struggle to identify who said what, ruining downstream summaries. (08:52-09:17)
- Early PII masking should run during capture or buffering so credit cards, passwords, and other sensitive details do not reach the LLM path. (09:20-09:48)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Choose Voice-Agent Architecture by Latency, Accuracy, and Semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)
- [Evaluate Voice Agents with Traces, Transcripts, Audio Checks, and Simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)
- [Treat Speaker Diarization as a Distinct, Unsolved Task](treat-speaker-diarization-as-a-distinct-unsolved-task.md)
- [Reconcile Diarization and STT for Speaker-Attributed Transcription](reconcile-diarization-and-stt-for-speaker-attributed-transcription.md)

Sources:
- [Contact Center Voice AI: Low-Latency Intelligence Extraction from Messy Audio Streams - Dippu Singh](../sources/20260408_IEF842ZEU5A.md), 01:12-09:48
