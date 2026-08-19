# Separate What Generated Audio Says From When It Plays

Summary: Generated speech does not have to be played back the way it was synthesized. If the utterance is sliced into units and each unit is fired by an external event, the model decides the content while a human or instrument decides the timing, expression, and pitch — which also hides the generation latency behind the performer's own pacing.

Use when:
- Building an interactive or performative surface over TTS or an LLM rather than a conversational one.
- Looking for control surfaces over generated media beyond editing the prompt.
- Deciding how much of a real-time feel has to come from fast inference versus from decoupled playback.

Details:
- The pipeline is a plain cascade of interchangeable parts: microphone → Whisper speech-to-text → "run a local model on my computer. It doesn't really matter what LLM, just any local model" → text-to-speech → "from that output go and plop it on the guitar" (13:53-14:27). Demonstrated live, an audience question ("What is reality?") comes back as an answer played note by note on the strings (14:34-15:19).
- The decoupling is what makes it a control surface rather than a speaker. The words are sliced per word (07:31-07:53) and each note event releases the next unit, so the performer controls rhythm, emphasis, and — once pitch is applied — melody, without touching the text. Every generation step happens before the first note; the interaction feels immediate because the live path only triggers already-produced audio.
- Pitch is applied on the same principle. The played note is measured with the YIN algorithm to recover its fundamental frequency out of the many present, that pitch drives an ADSR-shaped synthesized tone, and the tone is pushed through the voice clip and a vocoder so the speech takes the melody (09:52-11:17). The plugin exposes a "clarity" lever to "balance or mixing the synthesized note with the actual voice that the AI is giving" (13:38-13:47) — a continuous dial between machine tone and machine voice, set by ear during performance.
- The model layer is explicitly commodity here (Piper or Apple TTS, Whisper, "any local model"), and every part the speaker describes as hard is the non-model signal path: segmentation, pitch detection, envelopes, vocoding, and the offline/live boundary. For a class of AI media products, model choice is the least consequential decision in the build.
- Positioned against this wiki's real-time media pages: Reactor's argument is that steerability arrives when *generation* becomes fast enough to interrupt. This is the cheap version of the same affordance — you cannot change what the guitar is about to say, but you own everything about how it is delivered, and the generation never had to be fast.
- Honest limits: the result is "a choppy version, but it is working" (15:21-15:25), the sliced-word delivery is audibly mechanical, and there is no measurement of end-to-end latency from question to first note.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Voice Agents](../topics/voice-agents.md)

Related concepts:
- [Segment Synthesized Speech With Multiple Cues, Then Let a Human Fix the Rest](segment-synthesized-speech-with-multiple-cues-and-manual-repair.md)
- [Pre-Bake Transforms Too Heavy for the Real-Time Path](pre-bake-transforms-too-heavy-for-the-realtime-path.md)
- [Ship AI Audio Features as Plugins Inside the Host DAW](ship-ai-audio-features-as-plugins-inside-the-host-daw.md)
- [Real-Time Generation Changes the Medium, Not Just the Latency](real-time-generation-changes-the-medium-not-the-latency.md)
- [Expose explicit control signals for generative media models](expose-explicit-control-signals-for-generative-media-models.md)

Sources:
- [While my guitar gently speaks — Todd Fisher, Philo Ventures](../sources/20260818_E_Txocq-Lrw.md), 07:31-07:53, 09:52-11:17, 13:38-15:25
