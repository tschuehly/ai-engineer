# Off-the-Shelf Audio Encoders Are Trained on Audiobooks, So They Flatten Generated Emotion

Summary: In an audio-driven avatar model, the audio embedding is what carries emotion and facial expression — so the encoder, not the video model, sets the expressiveness ceiling. Sidney Primas (LemonSlice) reports that most available audio encoders are trained on audiobooks, which are monotone by construction, and that an expressive model therefore has to train its own encoder and curate its own audio data.

Use when:
- Choosing an audio encoder for a talking-head, avatar, or any audio-conditioned generation model.
- Debugging generated output that is technically correct but emotionally flat, and looking upstream of the generator.
- Deciding whether a borrowed pretrained component can be treated as neutral infrastructure or has to be retrained.
- Evaluating a pretrained encoder along an axis its training corpus does not cover.

Details:
- Where expressiveness comes from, in this architecture: "the big thing here for us that really matters is the audio. The audio turns out to be very important for getting emotions right and the facial expressions right. People care about that a lot" (09:11-09:29). The claim is specific — the emotional read of a generated face is driven by the audio conditioning, not by a separate expression control.
- The two consequences Primas draws: "we really focus on getting great audio data that we can train on. And then actually also getting the encoders very right" (09:27-09:36). Both halves matter; curating expressive audio data does nothing if the encoder that embeds it discards the prosody.
- The specific corpus bias: "most audio encoders today are trained on basically audiobooks, which is very monotone, very simple, don't have a lot of emotions. So, if you want to have a very expressive model, you can't use those audio encoders and you actually have to spend a lot of time getting the audio embeddings right so that the video model is super expressive" (09:36-09:59).
- Why this generalizes past avatars: a frozen upstream encoder silently bounds every downstream capability along any axis its corpus lacks. Audiobooks are a reasonable speech corpus by every ordinary measure — clean, well recorded, abundantly transcribed — and are still disqualifying here, because the property being selected for (emotional range) is exactly the property a professional read-aloud performance suppresses. The check to run is not "is this encoder good" but "does this encoder's corpus vary along the dimension my product depends on."
- The same failure shape appears one modality over, which is the reason to trust it as a pattern rather than an anecdote. Krea reports that a captioner's *systematic* omission — captions that never mention the frame and the wall behind a photographed painting — becomes an unconditional artifact in the trained generator, and the fix is a data-selection decision rather than a better prompt (-tviRdpmHvs). Both cases are an upstream model's consistent blind spot becoming the downstream generator's ceiling; neither is visible by inspecting the generator.
- Practical scoping: this is one talk's account with no ablation, benchmark, or named encoder, and the encoder LemonSlice built is not described. What is durable is the diagnosis and where to look, not a recipe.
- Related control path in the same system, worth keeping separate: audio drives expression, but actions and emotions are *addressed* in words — "if you can describe it in words, you can generate those actions and emotions" (21:53-22:02) — and the emotion engine under construction predicts the right action from the avatar's audio plus the text it is about to say (18:24-18:37). So the audio embedding is the expressive carrier and language is the control surface over it.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Voice Agents](../topics/voice-agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Filter Training Images Your Captioner Systematically Mis-Describes](filter-images-your-captioner-systematically-mis-describes.md) - the same upstream-blind-spot failure in the image modality, with a data-selection fix.
- [Split an Embodied Conversational Agent Into an EQ Layer and an IQ Model](split-an-embodied-agent-into-an-eq-layer-and-an-iq-model.md) - where expressive control is headed once it is no longer only an embedding property.
- [Point a General World Model at a Narrow Domain Instead of Building a Task-Specific Model](point-a-general-world-model-at-a-narrow-domain.md) - the surrounding architecture bet that makes emotion a model property rather than an animation parameter.
- [Direct TTS Voices With a Director's Note](direct-tts-voices-with-a-directors-note.md) - the generation-side counterpart, where prosody and persona are steered in language rather than selected from a catalogue.
- [Prompt voice agents for persona, prosody, and brand fit](prompt-voice-agents-for-persona-prosody-and-brand-fit.md) - the voice-stack equivalent of steering expressive delivery.
- [Curate generative-media data before tuning model internals](curate-generative-media-data-before-tuning-model-internals.md) - the general form of "the data decides this, not the architecture."

Sources:
- [Voice agents with Realtime Video — Sidney Primas, LemonSlice](../sources/20260818_z1dqv74SpUs.md), 09:11-09:59, 18:24-18:37, 21:53-22:02
- [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../sources/20260818_-tviRdpmHvs.md)
