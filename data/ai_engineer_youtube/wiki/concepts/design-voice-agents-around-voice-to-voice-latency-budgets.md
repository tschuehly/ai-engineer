# Design Voice Agents Around Voice-To-Voice Latency Budgets

Summary: Realtime voice agents should be designed around the elapsed time from a user's speech ending to the first returned audio. A model or orchestration choice that looks acceptable in text can still fail voice UX when the response crosses conversational latency expectations.

Use when:
- Setting latency targets for a spoken assistant, realtime voice app, or voice-controlled agent.
- Deciding whether extra model reasoning, guardrails, transcription, tool calls, or routing can fit inside a spoken interaction.

Details:
- The talk frames latency as the main difference between ordinary multi-turn agents and voice agents: a human conversation feels natural around 500 ms, while voice-agent responses much above one second can produce low completion rates, low NPS, and hang-ups. (01:46-02:31)
- Voice-to-voice latency is the elapsed time between the human stopping speech and hearing the first returned audio, so instrumentation should measure the whole speech-input-to-speech-output path rather than only model latency. (02:33-02:41)
- A real browser-to-cloud Pipecat voice app was shown at just under one second; the speakers call that good but not great, and note that further speed can trade off against quality or cost. (02:47-03:13)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Choose voice-agent architecture by latency, accuracy, and semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)

Sources:
- [Your realtime AI is ngmi - Sean DuBois (OpenAI), Kwindla Kramer (Daily)](../sources/20250731_E71YtNbCFXY.md), 01:46-03:13
