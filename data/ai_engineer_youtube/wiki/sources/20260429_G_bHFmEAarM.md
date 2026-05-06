# Build & deploy AI-powered apps - Paige Bailey, Google DeepMind

Source: [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](https://www.youtube.com/watch?v=G_bHFmEAarM)
Uploaded: 2026-04-29
Transcript: `raw/20260429_G_bHFmEAarM/G_bHFmEAarM.en-orig.vtt`

## Summary

Paige Bailey demonstrates Google AI Studio as a fast prototype surface for AI-powered apps, emphasizing model selection by task, cost, latency, and thinking depth; sandboxed code execution and compare mode for testing model behavior; generative-media workflows that chain prompt generation into video creation; Gemma 4 as a lightweight multimodal model family that can be tested through AI Studio before local deployment; and Gemini Live as a realtime multimodal planner for robotics and augmented-reality style applications.

## Extracted Concepts

- [Use hosted model playgrounds to prototype before owning infrastructure](../concepts/use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md) - AI Studio lets teams test Gemini, Gemma, and generative-media models through a free or API-key-backed interface before downloading models or provisioning deployment infrastructure.
- [Compare models by task, thinking budget, cost, and latency](../concepts/compare-models-by-task-thinking-budget-cost-and-latency.md) - the demo frames Pro, Flash, Flash-Lite, thinking levels, and compare mode as knobs for choosing an adequate model rather than defaulting to the largest model.
- [Sandboxed code execution turns model reasoning into inspectable computation](../concepts/sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md) - AI Studio code execution gives Gemini a Python environment with data science libraries while isolating the user's local environment.
- [Realtime multimodal models should plan over specialized local actuators](../concepts/realtime-multimodal-models-should-plan-over-specialized-local-actuators.md) - Gemini Live can interpret audio, screen, and video context while delegating physical actions to local robot models instead of directly controlling actuators.

## Topic Links

- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)
- [Tools](../topics/tools.md)
- [Voice Agents](../topics/voice-agents.md)
- [Workflows](../topics/workflows.md)

## Notes

- AI Studio exposes model and modality selection in one interface, including Gemini models, video generation models, structured outputs, and code execution; it can be accessed with a personal account and supports API-key workflows for paid models (06:17-07:14, 49:16-49:38).
- Thinking settings for Gemini 3.1 range from minimal through high, and Bailey uses lower settings when speed matters; she also describes Gemini 3.1 Flash-Lite as a favorable price, speed, and performance option for the demo (12:25-13:13).
- Compare mode can run model variants side by side, such as Gemini 3.1 Flash-Lite against Gemini 3 Flash, while keeping code execution enabled (13:18-14:08).
- Code execution gives Gemini a sandboxed Python environment with preinstalled data science libraries, letting the model invoke them as tools without affecting the user's local environment (13:18-13:54, 46:09-46:26).
- Gemini 3.1 Pro is described as the largest, slower, and more expensive option; Gemini 3 Flash as the common production workhorse; and Gemini 3.1 Flash-Lite as gaining traction for users coming from earlier Flash models (18:35-19:11).
- Gemma 4 can be tested through AI Studio before downloading to owned infrastructure, supports multimodal understanding, can be fine-tuned and run under an Apache 2 license, and has smallest versions intended for mobile-class environments (50:50-52:55).
- AI Studio app generation can create Firebase blueprints and rules and offers one-click Cloud Run deployment, though quota and cost still matter during demos and experiments (46:36-46:54, 58:51-59:05).
- For robotics, Bailey says Gemini Live should build the plan and invoke local robot models for actions such as picking up items, rather than directly controlling robotic actions (59:29-60:29).
