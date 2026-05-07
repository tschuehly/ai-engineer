# Semantic Turn Detection Improves Voice Interruption Timing

Summary: Voice agents need more than fixed silence detection to decide when a user is done speaking. Semantic end-of-turn models can combine audio and text cues to delay or trigger responses in ways that feel less interruptive.

Use when:
- Tuning voice-agent interruption, barge-in, or end-of-turn behavior.
- Diagnosing voice agents that answer too early after pauses or filler words.

Details:
- The workshop frames natural conversation as a balance between low latency and avoiding interruption while a speaker pauses to think; fixed "stopped speaking" logic can make bots respond before the user's turn is semantically complete. 01:01:05-01:01:50
- Semantic end-of-turn detection can use filler words, pauses, intonation, and text context rather than only a VAD timeout. 01:01:50-01:02:13
- Daily's smart-turn model is described as a native audio-in classifier that outputs complete or incomplete; Pipecat can use an incomplete signal to dynamically extend the VAD timeout and give the user more time to finish. 01:02:13-01:02:46
- The workshop demonstration also shows interruption as an explicit runtime capability: the bot starts a long story, then accepts a user interruption and switches tasks mid-speech. 59:52-01:00:23

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)
- [Prompt voice agents for persona, prosody, and brand fit](prompt-voice-agents-for-persona-prosody-and-brand-fit.md)

Sources:
- [Full Workshop: Realtime Voice AI - Mark Backman, Daily](../sources/20250803_nxuTVd7v7dg.md), 59:52-01:00:23, 01:01:05-01:02:46
