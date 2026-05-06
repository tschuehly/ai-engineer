# Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI

Source: [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](https://www.youtube.com/watch?v=-OXiljTJxQU)
Uploaded: 2025-07-20
Transcript: `raw/20250720_-OXiljTJxQU/-OXiljTJxQU.en-orig.vtt`

## Summary

This OpenAI talk explains how production voice agents differ from text agents: builders must choose between chained and speech-to-speech architectures, tune latency and accuracy tradeoffs by product type, keep tool surfaces small, preserve context across handoffs, prompt for spoken persona, and evaluate both transcripts and audio behavior with observability, labels, simulations, and asynchronous guardrails.

## Extracted Concepts

- [Choose Voice-Agent Architecture by Latency, Accuracy, and Semantics](../concepts/choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md) - supports the architecture tradeoff between chained STT/LLM/TTS and realtime speech-to-speech models.
- [Delegate Complex Voice-Agent Tasks Through Specialist Tools and Handoffs](../concepts/delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md) - shows how realtime voice frontends can delegate complex work to specialist agents and preserve conversation state.
- [Prompt Voice Agents for Persona, Prosody, and Brand Fit](../concepts/prompt-voice-agents-for-persona-prosody-and-brand-fit.md) - identifies voice-specific prompt controls such as demeanor, tone, enthusiasm, and brand realism.
- [Evaluate Voice Agents With Traces, Transcripts, Audio Checks, and Simulations](../concepts/evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md) - describes voice-agent observability, transcript evals, audio evals, synthetic conversations, and asynchronous guardrails.

## Topic Links

- [Voice Agents](../topics/voice-agents.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

## Notes

- Speech-to-speech voice models are presented as reaching a production tipping point: newer models respond faster, sound more expressive, and handle interruption better than prior slower and more brittle audio systems, 01:44-04:13.
- Chained voice architectures stitch together transcription, text reasoning, and text-to-speech, which increases latency and can lose semantic nuance; realtime speech-to-speech collapses those layers into one model and is better suited to low-latency experiences, 04:16-05:23.
- Product context changes the tradeoff: consumer experiences often prioritize latency and expressiveness, while customer-service workflows require accurate order, refund, and internal-system actions, 05:25-07:19.
- A voice agent can use the realtime API as a frontline conversational agent while delegating harder work to specialist agents or models through tools, 08:47-09:55.
- Voice prompts should control both instructions and spoken qualities such as demeanor, tone, enthusiasm, and brand fit, 09:55-11:35.
- Voice-agent evals should begin with traces and human labels, then add transcript rubrics, audio-specific checks for tone and pacing, synthetic customer conversations, and asynchronous guardrails with configurable debounce windows, 12:56-15:52.
