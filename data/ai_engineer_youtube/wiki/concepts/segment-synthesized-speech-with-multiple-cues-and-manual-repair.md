# Segment Synthesized Speech With Multiple Cues, Then Let a Human Fix the Rest

Summary: Cutting a synthesized utterance into individual words is harder than generating it. Energy-gap segmentation assumes silence between words and running speech frequently has none; adding a sonority-peak syllabifier (vowel nuclei) as a second, independent cue gets close; the last few boundaries are cheaper to fix with a drag-to-edit UI than with a better heuristic.

Use when:
- Splitting TTS output into words, phrases, or syllables so downstream code can trigger, time-align, or re-order them.
- Choosing between improving an automatic detector and shipping a manual repair affordance.
- Debugging a pipeline where the model output is fine and the post-processing is what looks broken.

Details:
- Getting a single word out of a TTS clip was trivial — type text, synthesize, play the clip on a note event (06:30-07:20). The problem only appears at sentence length: "it turns out, you know, in English or in any languages for that matter, there's more than one word" (07:25-07:31).
- Energy-gap segmentation, the obvious first heuristic: "there's typically silence in between words. So, let's just cut it whenever the decibels are very much close to zero." Its failure is a property of speech, not of the implementation — "as I'm speaking right now, for example, there's actually no silence in between some of my words. So, it gets a little bit challenging to where it's not 100% foolproof" (08:04-08:34).
- The second cue looks at what *is* there rather than at what is absent: a sonority-peak syllabifier "identifying the syllables of the audio signal and identifying that there's vowels in here. Vowels typically lead to syllables" (08:34-08:48). Amplitude gaps and sonority peaks fail on different inputs, which is why combining them helps: "let's take the sonority peak, add it to the energy gap, and figure out if we could just make that work automatically" (08:48-08:56).
- The combined detector is demonstrated on a full sentence and is audibly imperfect — "it's working pretty well. Not quite as good as I want to" (09:23-09:26). Rather than iterate further, the shipped answer is an editor: "I settled on just the ability to go and actually I could drag this and manually edit some of these segments in here. So, worked okay" (09:26-09:37).
- The generalizable rule is about where the remaining error goes. When a heuristic's residual is small, bounded, and inspectable by the person who will use the output anyway, a manual repair affordance converts an unbounded algorithmic problem into a bounded UI one. This is a different arrangement from the wiki's human-in-the-loop review pages, where a human approves or rejects model output; here the human edits a boundary the machine already proposed.
- Caveats: no accuracy numbers, ablation, or comparison against forced alignment (which would be the standard alternative when the text is known in advance) appears in the source, and the whole exercise is single-speaker synthesized audio rather than recorded conversational speech.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Separate What Generated Audio Says From When It Plays](separate-what-generated-audio-says-from-when-it-plays.md)
- [Ship AI Audio Features as Plugins Inside the Host DAW](ship-ai-audio-features-as-plugins-inside-the-host-daw.md)
- [Remove head-of-line silence from voice models](remove-head-of-line-silence-from-voice-models.md)
- [Preserve speaker channels before voice agent transcription](preserve-speaker-channels-before-voice-agent-transcription.md)

Sources:
- [While my guitar gently speaks — Todd Fisher, Philo Ventures](../sources/20260818_E_Txocq-Lrw.md), 06:30-09:37
