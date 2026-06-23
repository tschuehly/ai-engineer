# Treat Speaker Diarization as a Distinct, Unsolved Task

Summary: Speaker diarization — "who speaks when" — is a separate problem from transcription with its own pipeline (voice activity detection → segmentation/overlap → speaker assignment), its own evaluation metric (diarization error rate), and structural difficulties that keep it unsolved: the number of speakers is unknown and the speaker labels are permutation-invariant.

Use when:
- Building a conversation-understanding stack (meeting notes, dubbing, podcast intelligence, call analytics) and deciding whether transcription alone is enough.
- You need "who said what," "who said what and when," or paralinguistic detail (interruptions, backchannels, pauses) on top of a transcript.
- Choosing or benchmarking a diarization model and you need to know what its error number (DER) actually measures.

Details:
- Diarization answers "who speaks when," distinct from STT's "what was said." It is the foundation for a ladder of conversation understanding: who said what (speaker-attributed transcription, enough to assign meeting action items) → who said what *and when* (precise timestamps expose interruptions and a short backchannel "yes"/"mhm" that can carry the most important signal) → who said what, when, *and how* (laughter, coughing, stress/prosody — "the dog ate the cake" with different stress means different things) → who is talking to whom in what acoustic environment. (02:04-07:34)
- Standard pipeline: (1) voice activity detection — is anyone speaking; (2) segmentation — split speech regions into turns, find speaker-change points, and detect overlapping/interrupting speech and backchannels you must not miss; (3) assign a speaker identity to each turn. The system itself decides the number of speakers. (08:42-10:08)
- Why it stays hard despite years of work: the number of speakers (the number of classes to detect) is unknown a priori, unlike classical ML — an attendee list is only a hint (two people can share one channel; an uninvited person can join). Labels are permutation-invariant: output is "speaker 1/2/3," not real names, and swapping the labels is still a correct answer, which the evaluation metric must account for. Add overlapping speech, very short turns, speech-time imbalance across speakers, and ordinary acoustic noise. (10:25-12:24)
- Diarization error rate (DER) is the standard metric: DER = (confusion + false alarm + missed detection) / total speech duration, computed with the `pyannote.metrics` library. Confusion = wrong speaker; false alarm = detect speech where there is none; missed detection = miss speech, frequently during overlap when only one of two simultaneous speakers is detected. (14:16-15:24)
- Concrete grounding: on a 30-second two-party telephone call, the open-source `pyannote` Community-1 pipeline scored ~5% DER and pyannoteAI's cloud Precision-2 model scored ~3% DER. The `pyannote` open-source toolkit (creator Hervé Bredin) became popular after Whisper shipped free STT without speaker tags, so people combined Whisper + pyannote; it is near ~10K GitHub stars. (12:57-16:01, 01:04-01:55)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Benchmark Voice AI on Distant-Mic Multi-Speaker Audio, Not Headset Single-Speaker](benchmark-voice-ai-on-distant-mic-multi-speaker-audio.md)
- [Reconcile Diarization and STT for Speaker-Attributed Transcription](reconcile-diarization-and-stt-for-speaker-attributed-transcription.md)
- [Extract a Rich Structured Audio Profile in One Multimodal Call](extract-a-rich-structured-audio-profile-in-one-multimodal-call.md)
- [Preserve speaker channels before voice-agent transcription](preserve-speaker-channels-before-voice-agent-transcription.md)

Sources:
- [Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI](../sources/20260605_mFLlVpnGpds.md), 02:04-16:01
