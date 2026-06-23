# Extract a Rich Structured Audio Profile in One Multimodal Call

Summary: A frontier multimodal model can return a rich structured profile of an audio recording — diarization with speaker names, accurate timestamps, per-segment language detection with translation, emotion tags, and a summary — from a single API call with a response schema, replacing a chain of separate ASR, diarization, language-ID, and emotion-classification models.

Use when:
- Building an audio-understanding or transcription pipeline and deciding whether to chain specialized models or use one multimodal call.
- You need more than a transcript: who spoke, when, in what language, with what emotion, plus a summary.

Details:
- Demonstrated as "EchoScript": one call to Gemini 3 Flash Preview prompted to identify distinct speakers, label them by name when context allows, return accurate timestamps, detect language, translate to English when the language is not English, classify emotion from {happy, sad, angry, neutral}, and produce a brief summary at the beginning, 04:16-07:24.
- The output is requested as structured output via a response schema, so the single response populates a UI directly instead of being parsed from prose, 07:08-07:24.
- This is positioned as "rich transcription," distinct from pure transcription: the model understands nuance beyond words — emotion, pacing, accents, and the context of speech — and handles overlapping speakers and seamless code-switching between languages, 03:17-04:12, 05:17-05:27.
- The capability rests on the frontier model's audio understanding (the Gemini 3 base research), which is the same foundation that powers speech generation and real-time conversation, so one model family covers understanding and generation, 07:32-08:08.
- Speaker-by-name labeling depends on in-audio context (e.g. someone introducing themselves); without context it falls back to generic speaker labels, 04:58-05:10, 06:44-06:53.
- Contrast with preprocessing-heavy pipelines: where contact-center stacks preserve separate speaker channels before STT, a multimodal call can diarize from a single mixed stream — useful when channels are not separable, but channel separation remains more robust when available.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Preserve speaker channels before voice-agent transcription](preserve-speaker-channels-before-voice-agent-transcription.md)
- [Extract contact-center intelligence as structured JSON](extract-contact-center-intelligence-as-structured-json.md)
- [Multilingual Voice Agents Need Language Detection and Switching](multilingual-voice-agents-need-language-detection-and-switching.md)
- [Direct TTS Voices With a Director's Note, Not a Voice Catalogue](direct-tts-voices-with-a-directors-note.md)

Sources:
- [From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](../sources/20260609_Bc6Ojl2XS1w.md), 03:17-08:08
