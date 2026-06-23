# Pair Low-Bandwidth Voice Input With High-Density Multimodal Output

Summary: Voice is an excellent *input* channel for dumping raw human intent quickly but a poor *output* channel for receiving dense information, so the winning interaction shape is single-stream voice input paired with parallel, high-density multimodal output (text, diagrams, generative UI) plus lightweight non-voice cues that manage turn-taking — not a symmetric voice-in/voice-out conversation.

Use when:
- Designing a voice or multimodal agent and deciding how much of the experience should actually be spoken.
- Diagnosing why a working voice agent still feels frustrating, slow, or rude despite good ASR/TTS.
- Choosing affordances (push-to-talk, interject cues, skim controls) to overcome interruption and turn-taking friction.

Details:
- The asymmetry: a heavy voice-output user reports the information density per second of spoken replies "isn't quite high enough" — he wants to speak raw intent in (high bandwidth, semantically understood) and receive a high-density artifact back (diagrams, text, or whatever UI he's in the context of): "parallel input parallel output, but single input, my voice." 23:00-24:30
- Voice's value is not only information transfer: spoken interaction can deliver *companionship* that "lessens the loneliness feel" and makes a user more motivated to keep tinkering, even when they would *learn* more from text or a diagram — different modalities trigger different feelings, so don't assume voice output is for conveying facts. 21:00-21:30
- Terseness penalty: a concise *text* answer doesn't offend, but a concise *spoken* answer "just sounds rude," so the same brevity that's good in text is a worse default in speech. 21:55-22:05
- "Skim listening" is the missing affordance: forward/backward controls to jump half a sentence and to scroll forward in *concepts* (the higher-level sections) rather than in sentences — the Claude app already shows tappable higher-level sections that differ from the spoken stream. 22:00-23:00
- The thing you talk to is often not the thing doing the work: prefer speaking to a "halfway-house" product-manager agent that triggers a worker (e.g. a coding agent) over addressing the worker directly, so the voice layer is an orchestrator interface, not the executor. 10:50-11:15
- Interaction is still mostly *binary* (voice OR another modality); "generative UI plus voice" — multimodal conversations where the app visibly shows what the agent is extracting and the user interacts with it in parallel — is the underexplored direction. 10:30-10:55
- Turn-taking friction cuts both ways: people are too polite to interrupt voice agents (interrupting aggressively actually improves the experience, but there's no good way to "give people permission to interrupt"), and an "agent-wants-to-interject" nudge (a small visual cue signaling the agent has something to add *and which topic*) can make the agent's barge-in richer than a human's. 11:30-11:55, 25:44-26:10
- Push-to-talk / hold-to-talk (whisper-flow style) is a reliable production workaround because purely audio-driven interruptibility detection is unreliable; augment the raw audio stream with another explicit cue rather than depending on the model to detect turn boundaries. 25:30-25:45
- Barge-in handling can edit the agent's internals: platforms usually generate the full text then start TTS, and a mid-speech interruption merely *appends* the user's reply after the whole generated message — but with audio playback timestamps you know how far it got, so you can truncate the transcript at the interruption point and make the model "forget it even generated more text" (treating the conversation transcript as an editable internal, not a black box). 28:40-29:15

Related topics:
- [Voice Agents](../topics/voice-agents.md)

Related concepts:
- [Semantic turn detection improves voice interruption timing](semantic-turn-detection-improves-voice-interruption-timing.md)
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md)
- [Use voice-dumped UI and code observations as agent feedback](use-voice-dumped-ui-and-code-observations-as-agent-feedback.md)

Sources:
- [How to talk to statues — Joe Reeve, ElevenLabs](../sources/20260601_u-rJwPPU3QA.md), 10:30-11:15, 21:00-23:00, 25:30-26:10, 28:40-29:15
