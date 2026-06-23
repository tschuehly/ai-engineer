# Direct TTS Voices With a Director's Note, Not a Voice Catalogue

Summary: Instead of picking a voice from a large library filtered by gender, accent, and language, a speech model with strong audio understanding can take a small set of base voices and a natural-language "director's note" — audio profile, scene, performance guidance, sample context — and synthesize a specific persona or accent on demand, the way you would direct a human actor.

Use when:
- Designing a text-to-speech product and choosing between a large fixed voice catalogue and a small directable base set.
- You need many personas, accents, or performance styles without curating and maintaining a separate voice per variant.

Details:
- Typical TTS providers ship a huge library of voices that users filter by gender, accent, and language; Gemini instead exposes roughly 30 base voices that you direct to act a certain way, 08:10-09:00.
- Because the model has audio understanding (it knows what scenarios and accents sound like), it can modify a base voice to use a target accent or demeanor rather than needing a pre-recorded voice for each, going from a small base set to a very specific target voice, 08:37-09:00, 11:41-11:55.
- The prompt structure (shown in the "Voice Library" app) is an audio profile + a scene + a director's note giving performance guidance, plus sample context and the transcript to speak — explicitly framed as directing a human performer, 09:17-09:36.
- Example: a request for a "high pitch Irish male" had Gemini 3 Flash construct the speech-generation system prompt — character "Finian," scene a cozy crowded pub on the coast of County Clare, deliver lines with a strong authentic Irish accent — transforming a standard-American base voice; a separate base voice ("Zephyr") was directed into Singaporean Singlish, 09:46-11:33.
- This extends persona/prosody prompting from voice-agent runtime into the generation model itself: the directability is a property of the base voice plus the model's audio understanding, not a catalogue entry.
- Caveat from the live model: a directed accent can bleed across languages (an Irish-accent instruction carried into a German poem), so system instructions must scope the accent per language, 14:31-14:46.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Prompt voice agents for persona, prosody, and brand fit](prompt-voice-agents-for-persona-prosody-and-brand-fit.md)
- [Extract a Rich Structured Audio Profile in One Multimodal Call](extract-a-rich-structured-audio-profile-in-one-multimodal-call.md)
- [Multilingual Voice Agents Need Language Detection and Switching](multilingual-voice-agents-need-language-detection-and-switching.md)

Sources:
- [From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](../sources/20260609_Bc6Ojl2XS1w.md), 08:10-11:55, 14:31-14:46
