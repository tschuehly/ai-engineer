# TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google

Source: [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](https://www.youtube.com/watch?v=BKWpYIWvAo4)
Uploaded: 2026-05-03
Transcript: `raw/20260503_BKWpYIWvAo4/BKWpYIWvAo4.en-orig.vtt`

## Summary

Cormac Brick shows how LiteRT-LM and AI Edge Gallery make on-device LLM workflows practical across Android, iOS, IoT, and desktop-class edge targets. The most reusable engineering points are that small edge models need condensed, progressive-disclosure tool context; constrained decoding improves tool-call reliability for smaller models; and production mobile AI often composes multiple specialized tiny models rather than forcing one model to handle speech, personalization, and text polishing.

## Extracted Concepts

- [Edge agent skills need progressive disclosure to preserve small-model reliability](../concepts/edge-agent-skills-need-progressive-disclosure-to-preserve-small-model-reliability.md) - this source explains why skill metadata, details, and tool calls are loaded only when needed on edge models.
- [Constrained decoding makes small-model tool calls production-usable](../concepts/constrained-decoding-makes-small-model-tool-calls-production-usable.md) - this source describes constraining tool-call outputs to the finite tools available to the runtime.
- [Modular tiny-model pipelines reuse specialized models across mobile app workflows](../concepts/modular-tiny-model-pipelines-reuse-specialized-models-across-mobile-app-workflows.md) - this source shows an app pipeline that separates ASR, personalization, and text polishing into reusable tiny-model components.

## Topic Links

- [Agents](../topics/agents.md)
- [Edge Inference](../topics/edge-inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)
- [Tools](../topics/tools.md)

## Notes

- LiteRT-LM is presented as the LLM runtime for mobile and edge, while LiteRT remains the standard inference framework formerly known as TensorFlow Lite; the same TensorFlow Lite file can target CPU/GPU across platforms, while NPU deployment needs special compilation and a vendor-specific artifact (05:00-06:33).
- For narrowly scoped tasks such as summarization, transcription, or voice-to-action, the talk reports reliable behavior from models in roughly the 100M-500M parameter range when they are fine-tuned for the specific task (09:25-10:37).
- Function Gemma is described as a 270M-parameter model dedicated to function calling, with internal evals reaching about 85-90% reliability for voice-to-function calling across 10 Android-relevant functions (09:56-10:32).
- Agent skills in AI Edge Gallery expose one-line descriptions first, then let the agent load full skill instructions and function details on demand; the speaker says this preserves token efficiency and reliability because small edge models struggle with large context windows (23:44-25:18).
- Skill architecture includes a skill registry, a load-skill operation, JavaScript execution, and native intents; skills can run fully offline as local JavaScript or call web APIs when the workflow needs external services and credentials (31:39-33:04).
- Constrained decoding is applied specifically when generating tool calls, and can be narrowed to the finite set of tools the selected skill is supposed to use rather than generic JSON output (28:02-29:13).
- LiteRT-LM has C++, Java, Python APIs and planned Swift APIs, supports third-party models, and lets AI Edge Gallery load arbitrary LiteRT-LM files and report benchmark stats (42:04-46:42).
- The AI Edge Eloquent example separates transcription, personalization, and text polishing; the speaker argues this modularity lets teams reuse model weights in multiple places and inspect intermediate stages for easier debugging (59:31-01:00:33).
