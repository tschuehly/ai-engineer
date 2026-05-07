# Voice Agents

## Overview

Voice agents add realtime audio constraints to the usual agent stack of model, instructions, tools, and runtime. The central architecture choice is whether to chain speech-to-text, text reasoning, and text-to-speech components or use a speech-to-speech model that preserves conversational semantics and reduces latency. Stateful streaming APIs extend that decision into a runtime shape: audio buffers, visual frames, transcriptions, realtime events, and tool calls may all flow over one session. Low-latency consumer products may prioritize expressiveness and responsiveness, while customer-service workflows often need stronger accuracy, integrations, and guardrails even if the experience is less fluid. Frameworks such as Pipecat make that runtime explicit as a frame pipeline: transports, STT, LLMs, TTS, native speech models, tools, recording, transcription, and observers can be composed as streaming processors instead of hidden inside one monolithic bot. Voice AI can also become a hardware and developer ecosystem: app editors, dev kits, open source, and custom hardware form factors let assistants move from smart speakers into robots, toys, appliances, and home automation. Voice can also be a presentation layer over explicit retrieval workflows: a visual-document RAG agent can retrieve page images, construct multimodal answer prompts, and then speak the grounded answer. Contact-center voice intelligence adds a data-pipeline shape: preserve speaker channels, tune STT with domain vocabulary and normalization, extract structured JSON, mask PII before LLM processing, and verify CRM-bound summaries before durable updates. Production voice systems should keep the conversational agent's tool surface small, delegate complex tasks to specialist agents or models, and preserve context through summarized handoffs. Turn-taking is itself a production behavior: semantic end-of-turn detection can use audio and text cues to avoid fixed silence thresholds that cut users off while they pause to think. Evaluation needs traces, labeled conversations, transcript-based checks, audio-specific judgments, synthetic conversations, release evals across realtime provider services, and guardrails that fit within the timing of spoken responses.

## Key Concepts

- [Realtime multimodal models should plan over specialized local actuators](../concepts/realtime-multimodal-models-should-plan-over-specialized-local-actuators.md) - realtime multimodal models can interpret speech or vision while specialized components execute embodied actions.
- [Choose voice-agent architecture by latency, accuracy, and semantics](../concepts/choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md) - architecture should match whether the product prioritizes responsiveness, semantic preservation, deterministic control, or system integration.
- [Delegate complex voice-agent tasks through specialist tools and handoffs](../concepts/delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md) - realtime voice agents can stay conversational while specialist agents handle harder tool and policy decisions.
- [Prompt voice agents for persona, prosody, and brand fit](../concepts/prompt-voice-agents-for-persona-prosody-and-brand-fit.md) - voice prompts shape spoken demeanor, tone, pacing, and brand realism.
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](../concepts/evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md) - voice evals combine standard task checks with audio-specific and latency-aware validation.
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](../concepts/realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md) - live audio agents can include visual context, streaming events, transcriptions, and tools in the same session.
- [Use frame pipelines to compose realtime voice agents](../concepts/use-frame-pipelines-to-compose-realtime-voice-agents.md) - streaming processors make transports, model services, utilities, and runtime settings composable.
- [Semantic turn detection improves voice interruption timing](../concepts/semantic-turn-detection-improves-voice-interruption-timing.md) - voice agents need complete/incomplete turn signals rather than only fixed silence timeouts.
- [Test realtime voice services with bot-to-bot release evals](../concepts/test-realtime-voice-services-with-bot-to-bot-release-evals.md) - provider integrations should be checked end to end before release.
- [Make voice AI devices developer-extensible](../concepts/make-voice-ai-devices-developer-extensible.md) - voice AI hardware can become an open platform for custom applications and form factors.
- [VoiceVision agents wrap visual RAG with retrieval, image-reading, and speech tools](../concepts/voicevision-agents-wrap-visual-rag-with-retrieval-image-reading-and-speech-tools.md) - document-grounded voice assistants can keep retrieval and image prompt construction explicit before speaking the answer.
- [Preserve speaker channels before voice-agent transcription](../concepts/preserve-speaker-channels-before-voice-agent-transcription.md) - voice pipelines should keep agent and customer speech separable before STT and summarization.
- [Extract contact-center intelligence as structured JSON](../concepts/extract-contact-center-intelligence-as-structured-json.md) - contact-center voice workflows need schema-aligned intent, action, entity, sentiment, and CRM fields rather than free-form summaries.
- [Verify AI call summaries before CRM sync](../concepts/verify-ai-call-summaries-before-crm-sync.md) - operators should validate AI-generated summaries before they update durable customer records.

## Open Questions

- Which voice-agent workflows should accept extra latency for chained control rather than use a lower-latency speech-to-speech model?
- What audio-specific eval rubrics reliably measure brand fit, pacing, interruption handling, and conversational comfort?
- How should teams evaluate multimodal voice agents when the relevant context includes screen frames or camera input as well as transcript content?
- When is voice output enough over a visual-RAG backend, and when does the product need a fully realtime speech-to-speech architecture?
- Which contact-center fields can be auto-confirmed safely, and which always require operator validation before CRM sync?
- Which voice-device capabilities should be exposed through app editors and dev kits, and which should remain fixed platform behavior?
- How should teams set thresholds for semantic end-of-turn models so interruption behavior balances latency with the user's need to pause and think?

## Sources

- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md)
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md)
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md)
- [Contact Center Voice AI: Low-Latency Intelligence Extraction from Messy Audio Streams - Dippu Singh](../sources/20260408_IEF842ZEU5A.md)
- [VoiceVision RAG - Integrating Visual Document Intelligence with Voice Response - Suman Debnath, AWS](../sources/20251206_hwCmfThIiS4.md)
- [The Next Unicorns: 7 Top AI startups from the HF0 Residency](../sources/20250821_L8-5ezsoI5A.md)
- [Full Workshop: Realtime Voice AI - Mark Backman, Daily](../sources/20250803_nxuTVd7v7dg.md)
