# Evaluate Voice Agents With Traces, Transcripts, Audio Checks, and Simulations

Summary: Voice-agent evaluation starts with observability and labeled conversations, then layers transcript-based task checks, audio-specific judgments, synthetic conversations, and asynchronous guardrails. Text evals still matter, but audio adds tone, pacing, interruption, and safety-timing concerns.

Use when:
- Building an eval plan for a realtime voice application.
- Deciding which guardrails can run without ruining voice latency.

Details:
- Start with traces that capture what happened across the agent, audio, and tool flow; without observability, teams cannot inspect data or act on failures, 12:56-13:24.
- Human labeling and prompt iteration are presented as the most effective early eval loop for customer voice-agent work, even when the process is not initially scalable, 13:24-13:48.
- Transcript-based evals can reuse LLM-as-judge rubrics and function-call checks for business criteria, while audio evals should focus on properties harder to capture in text such as tone, pacing, and intonation, 13:50-14:36.
- Synthetic conversations can run customer personas against the realtime agent, then evaluate the resulting transcripts or audio to understand behavior across many scenarios, 14:40-15:03.
- Because realtime generated text may arrive faster than spoken audio, asynchronous guardrails can run with configurable debounce windows, such as every 100 characters, without necessarily blocking the voice stream, 15:08-15:52.
- Voice-agent eval programs should include bug reproduction, larger regression sets, presubmit and postsubmit checks, release evals, live monitoring, and feedback from production failures into future simulations, 07:04-08:05.
- Automated voice metrics should be calibrated against human review rather than trusted as generic "conversation successful" judges, because broad LLM-as-judge metrics can be noisy across repeated runs, 13:49-14:56.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Prompt voice agents for persona, prosody, and brand fit](prompt-voice-agents-for-persona-prosody-and-brand-fit.md)
- [Simulate voice agents with probabilistic conversation evals](simulate-voice-agents-with-probabilistic-conversation-evals.md)
- [Calibrate voice eval realism to the behavior under test](calibrate-voice-eval-realism-to-the-behavior-under-test.md)

Sources:
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md), 12:56-15:52
- [From Self-driving to Autonomous Voice Agents - Brooke Hopkins, Coval](../sources/20250731_kDczF4wBh8s.md), 07:04-14:56
