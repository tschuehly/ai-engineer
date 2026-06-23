# Orchestrate Generative Media From a Real-Time Voice Agent via Tool Use

Summary: A real-time conversational model can drive generative media by exposing the media-generation model as a tool: the voice agent conversationally elicits the creative brief, then calls the generator (e.g. a music model) and returns the result, turning a one-shot generation API into an interactive, requirement-gathering experience.

Use when:
- Building a voice or chat agent that produces images, video, or music on request.
- You want the conversation to refine a creative brief before committing to an expensive generation call.

Details:
- Demonstrated as "Life Jukebox": the real-time Gemini Live model is given a tool to generate a song using Lyria, so a DJ persona asks for the vibe and buzzwords, then calls the tool to produce the track, 16:42-18:08.
- The conversational layer does the brief-gathering — it confirms genre, energy, and lyric themes ("manic energy," "German techno Schlager about the UK startup scene") before invoking generation — so the user shapes the output through dialogue rather than a single static prompt, 17:10-18:08.
- The media model is Lyria 3, which now generates full songs with lyrics and ships as two variants: Lyria 3 clip (clip generation) and Lyria 3 Pro (full-length song generation); the voice agent picks and calls the appropriate generation tool, 16:02-16:38.
- This composes two model families: a native sound-to-sound real-time model for the interaction and a dedicated media-generation model for the artifact, connected by ordinary tool use rather than a bespoke integration.
- Pattern generalizes beyond music: any generative-media endpoint (image, video, audio) can sit behind a voice-agent tool so the agent handles clarification, defaults, and surprise-me requests before generating.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Generative Media](../topics/generative-media.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Delegate complex voice-agent tasks through specialist tools and handoffs](delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md)
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md)
- [Choose Voice-Agent Architecture by Latency, Accuracy, and Semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)

Sources:
- [From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](../sources/20260609_Bc6Ojl2XS1w.md), 16:02-18:08
