# Voice Agents

## Overview

Voice agents add realtime audio constraints to the usual agent stack of model, instructions, tools, and runtime. The central architecture choice is whether to chain speech-to-text, text reasoning, and text-to-speech components or use a speech-to-speech model that preserves conversational semantics and reduces latency. Low-latency consumer products may prioritize expressiveness and responsiveness, while customer-service workflows often need stronger accuracy, integrations, and guardrails even if the experience is less fluid. Production voice systems should keep the conversational agent's tool surface small, delegate complex tasks to specialist agents or models, and preserve context through summarized handoffs. Evaluation needs traces, labeled conversations, transcript-based checks, audio-specific judgments, synthetic conversations, and guardrails that fit within the timing of spoken responses.

## Key Concepts

- [Choose voice-agent architecture by latency, accuracy, and semantics](../concepts/choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md) - architecture should match whether the product prioritizes responsiveness, semantic preservation, deterministic control, or system integration.
- [Delegate complex voice-agent tasks through specialist tools and handoffs](../concepts/delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md) - realtime voice agents can stay conversational while specialist agents handle harder tool and policy decisions.
- [Prompt voice agents for persona, prosody, and brand fit](../concepts/prompt-voice-agents-for-persona-prosody-and-brand-fit.md) - voice prompts shape spoken demeanor, tone, pacing, and brand realism.
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](../concepts/evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md) - voice evals combine standard task checks with audio-specific and latency-aware validation.

## Open Questions

- Which voice-agent workflows should accept extra latency for chained control rather than use a lower-latency speech-to-speech model?
- What audio-specific eval rubrics reliably measure brand fit, pacing, interruption handling, and conversational comfort?

## Sources

- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md)
