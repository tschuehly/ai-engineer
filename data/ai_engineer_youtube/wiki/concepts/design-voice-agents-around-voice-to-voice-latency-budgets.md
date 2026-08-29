# Design Voice Agents Around Voice-To-Voice Latency Budgets

Summary: Realtime voice agents should be designed around the elapsed time from a user's speech ending to the first returned audio. A model or orchestration choice that looks acceptable in text can still fail voice UX when the response crosses conversational latency expectations.

Use when:
- Setting latency targets for a spoken assistant, realtime voice app, or voice-controlled agent.
- Deciding whether extra model reasoning, guardrails, transcription, tool calls, or routing can fit inside a spoken interaction.

Details:
- The talk frames latency as the main difference between ordinary multi-turn agents and voice agents: a human conversation feels natural around 500 ms, while voice-agent responses much above one second can produce low completion rates, low NPS, and hang-ups. (01:46-02:31)
- Voice-to-voice latency is the elapsed time between the human stopping speech and hearing the first returned audio, so instrumentation should measure the whole speech-input-to-speech-output path rather than only model latency. (02:33-02:41)
- A real browser-to-cloud Pipecat voice app was shown at just under one second; the speakers call that good but not great, and note that further speed can trade off against quality or cost. (02:47-03:13)
- Together AI independently corroborates the thresholds with sharper numbers: humans respond to each other's conversational cues in ~300 ms; above ~500 ms the user starts to notice the AI's delay; at 1-2 s "people will just hang up." (`N7b1PJc7SFc`) 02:55-03:12
- The budget decomposes into per-component sub-budgets: a concrete STT target is time-to-complete-transcript (after the user stops speaking) at P90 ~100 ms, leaving room for the LLM's TTFT and the TTS time-to-first-audio inside the overall voice-to-voice budget. (`N7b1PJc7SFc`) 06:00-06:19
- Together also frames latency as an "and problem": low latency must hold simultaneously with intelligence/tool-calling, natural voice, and reliability across 100/1,000/10,000 concurrent calls — solving one in isolation is not enough. (`N7b1PJc7SFc`) 03:58-04:18
- **Everything you place around the model competes for the same budget, and one rule keeps it honest.** Manuja's constraint for guardrails generalizes to any pre- or post-processing stage in a latency-budgeted pipeline: "your request should never be bound by your guardrail timing. It should always be the LLM that is the rate determining step," enforced with timeouts and an explicit per-stage time budget rather than with hope. His placement taxonomy is the other half — serial before the model is safest but adds latency directly, concurrent with generation hides the cost, and after generation is for auditing rather than for blocking. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 11:03-11:38, 12:04-12:47)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Choose voice-agent architecture by latency, accuracy, and semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)
- [Size the Voice-Agent LLM to the Time-to-First-Token Budget](size-the-voice-agent-llm-to-the-time-to-first-token-budget.md)
- [Separate Engine Latency From Network Latency in Voice Pipelines](separate-engine-latency-from-network-latency-in-voice-pipelines.md)
- [Treat Guardrails as a Failable Dependency With Its Own Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md)

Sources:
- [Your realtime AI is ngmi - Sean DuBois (OpenAI), Kwindla Kramer (Daily)](../sources/20250731_E71YtNbCFXY.md), 01:46-03:13
- [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](../sources/20260531_N7b1PJc7SFc.md), 02:55-06:19
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 11:03-11:38, 12:04-12:47
