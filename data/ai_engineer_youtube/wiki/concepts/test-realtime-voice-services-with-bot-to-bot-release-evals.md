# Test Realtime Voice Services With Bot-to-Bot Release Evals

Summary: Realtime voice frameworks need release evals that exercise provider services end to end, not only unit tests around local code. Bot-to-bot conversations can drive examples, verify outcomes, and catch integration regressions across LLM, STT, TTS, and transport services.

Use when:
- Validating a realtime voice framework or voice-agent provider integration before release.
- Replacing manual demo checks with automated service-level regression tests.

Details:
- The workshop describes an eval bot that connects to the same room, asks a test question, receives another bot's answer, and uses an LLM to check whether the answer is correct. 57:54-58:12
- Pipecat previously ran more than 100 examples manually for each release, then moved toward release evals because manual end-to-end service checks were slow and painful. 58:12-58:29
- The release evals test services such as Gemini Live, Cartesia, and Deepgram end to end, with bots talking to each other to verify that integrations still work. 58:29-58:40
- Because voice stacks depend on networked realtime services, the workshop also warns that poor connectivity can become a practical failure mode during development and demos. 00:55-01:11

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)
- [Monitor whole agent systems, not single models](monitor-whole-agent-systems-not-single-models.md)

Sources:
- [Full Workshop: Realtime Voice AI - Mark Backman, Daily](../sources/20250803_nxuTVd7v7dg.md), 00:55-01:11, 57:54-58:40
