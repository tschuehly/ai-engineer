# Reconcile Diarization and STT for Speaker-Attributed Transcription

Summary: Gluing a separate diarization model and a separate STT model into "who said what" is not a trivial timestamp join: words straddle speaker boundaries, the two models' timestamps disagree, overlap is mis-handled, and STT is usually single-speaker-trained — so production stacks add an STT-agnostic orchestration layer that reconciles the two rather than retraining either model.

Use when:
- Building speaker-attributed transcription by composing a diarization model with an STT model (e.g. pyannote + Parakeet/Whisper).
- Debugging transcripts where words are assigned to the wrong speaker, especially around interruptions and overlap.
- Deciding between one multimodal call that diarizes-and-transcribes vs. orchestrating two specialist models.

Details:
- Two failure sources when combining diarization + STT: (1) most STT models are trained on single-speaker data and degrade badly on multi-speaker audio — overlap, speaker change, crosstalk, interruptions, code-switching mid-sentence, distant mics; (2) reconciling diarization and STT *timestamps* is genuinely hard. (16:52-19:43)
- Why the timestamp join is hard: STT does not transcribe overlapping speech well, the timestamps from STT and diarization disagree, and each model can detect speech the other misses (diarization flags speech the STT never transcribes, and vice versa). (19:24-19:43)
- Boundary-word problem: a word ("Oh") whose timestamps straddle two diarization turns has no clean owner; conversely, a single transcribed word can fall inside a region where diarization says two speakers were talking — so there is no obvious rule for assigning words to speakers. (20:39-21:27)
- pyannoteAI's answer is an "STT orchestration" cloud API: hand it a diarization model (Precision-2) and an STT model (Parakeet) and it reconciles them, even interleaving the two speakers' words correctly through overlapping speech. (21:27-22:42)
- The reconciliation method is partly proprietary, but one published part ships in the open Community-1 model as "exclusive diarization": when speech overlaps, select the single most-likely speaker to be transcribed by the STT, which simplifies the reconciliation. (23:34-24:21)
- Design choice: the orchestration is deliberately STT-agnostic — it is not part of STT training, so it works with any STT including internally fine-tuned ones — letting teams keep their own STT and add speaker attribution on top. This is the alternative architecture to collapsing diarization + transcription into one multimodal call. (24:24-24:48)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Treat Speaker Diarization as a Distinct, Unsolved Task](treat-speaker-diarization-as-a-distinct-unsolved-task.md)
- [Benchmark Voice AI on Distant-Mic Multi-Speaker Audio, Not Headset Single-Speaker](benchmark-voice-ai-on-distant-mic-multi-speaker-audio.md)
- [Extract a Rich Structured Audio Profile in One Multimodal Call](extract-a-rich-structured-audio-profile-in-one-multimodal-call.md)
- [Preserve speaker channels before voice-agent transcription](preserve-speaker-channels-before-voice-agent-transcription.md)

Sources:
- [Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI](../sources/20260605_mFLlVpnGpds.md), 16:52-24:48
