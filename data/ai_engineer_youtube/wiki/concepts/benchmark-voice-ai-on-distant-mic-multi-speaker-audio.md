# Benchmark Voice AI on Distant-Mic Multi-Speaker Audio, Not Headset Single-Speaker

Summary: Public ASR/diarization leaderboards mostly score clean, single-speaker, close-talk (headset) audio, which dramatically overstates real-world performance; the same model on the same dataset can roughly double its error rate when you switch to the distant table microphone with overlapping speakers, so benchmark on audio that matches the deployment.

Use when:
- Reading a leaderboard WER/DER number and estimating how a model will do on your real recordings (meetings, calls, rooms).
- Choosing a transcription or diarization model for multi-speaker, distant-mic, or noisy conditions.
- Designing a voice-AI benchmark and deciding which microphone, speaker count, and noise level to evaluate.

Details:
- NVIDIA Parakeet reports 11.4% word error rate on the AMI meeting dataset on the Hugging Face open ASR leaderboard, but the speaker measures 26% WER on the same model and the same AMI recordings. The only difference is the microphone: the leaderboard uses each person's headset mic (single-speaker, close-talk), he uses the one central table mic (multi-speaker, distant). (17:28-18:39)
- AMI is meetings of ~4-5 people in meeting rooms recorded with both per-person headset mics and one mic in the middle of the table — so the same dataset yields a "single-speaker" benchmark and a much harder "distant multi-speaker" benchmark depending on which channel you score. (18:01-18:34)
- Takeaway: "Most voice AI benchmarks are measuring single-speaker speech and calling it solved." A headline number is only meaningful paired with the microphone, speaker count, and acoustic condition it was measured under. (17:24-17:28)
- Diarization shows the same use-case sensitivity: state-of-the-art DER is roughly single-digit on clean two-party telephone speech (the talk abstract cites ~2%; the spoken slide's auto-caption read ~8%) but climbs to ~41% in a noisy restaurant — the task is far from solved once conditions get realistic. (16:11-16:49)
- Practical consequence for speaker-attributed transcription: because STT models are mostly trained on single-speaker data, their leaderboard generalization to multi-speaker, overlapping, code-switching, distant-mic audio is poor, so a strong leaderboard WER does not predict strong transcripts on real conversations. (16:52-19:02)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Voice Agents](../topics/voice-agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Treat Speaker Diarization as a Distinct, Unsolved Task](treat-speaker-diarization-as-a-distinct-unsolved-task.md)
- [Reconcile Diarization and STT for Speaker-Attributed Transcription](reconcile-diarization-and-stt-for-speaker-attributed-transcription.md)
- [Calibrate Voice Eval Realism To The Behavior Under Test](calibrate-voice-eval-realism-to-the-behavior-under-test.md)

Sources:
- [Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI](../sources/20260605_mFLlVpnGpds.md), 16:11-19:02
