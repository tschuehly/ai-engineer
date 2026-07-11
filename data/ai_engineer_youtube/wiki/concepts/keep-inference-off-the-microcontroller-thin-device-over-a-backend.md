# Keep Inference Off the Microcontroller: Build the AI-Native Device as a Thin Client Over a Backend

Summary: When you put a local LLM in a pocket device, the microcontroller is far too small to run the model, so the durable architecture is a thin firmware client that does only I/O and rendering, talking to a self-hosted backend that owns all inference, agents, and heavy state. "Keep the model off the metal."

Use when:
- Building a physical AI device (handheld, terminal, appliance) around a local/self-hosted model.
- Deciding what work belongs on the microcontroller versus a companion backend or box (e.g. a DGX-class machine on the same network).
- Sizing firmware for tiny MCUs that cannot allocate memory freely or host a model runtime.

Details:
- The MCU (an ESP32-S3 dual-core here) runs a tiny, fast firmware that handles keyboard/encoder/display I/O and rendering only; all model dispatch happens on the backend. Rendering is done with fixed static buffers of pre-allocated one-bit images — "no markdown engine and no `malloc` on the MCU side" — so the device stays fast and memory-safe. (06:54)
- The backend is a dependency-free Python service that dispatches to local models, autonomous agents (OpenClaw), and a game engine; the firmware talks to it over Wi-Fi. Inference is deliberately kept there because of the microcontroller's power draw and lack of compute. (09:00-09:40)
- The demo serves an open-source ~120B model (gpt-oss:120b) via NVIDIA TensorRT-LLM, exposed OpenAI-style behind an **LLM proxy** — a needed adapter because not every open-source model matches the OpenAI API shape, which cost a lot of debugging when swapping models. (09:14-09:40)
- This is the four-axis ownership decision resolved for a pocket device: the 120B model fails the "fits the hardware" axis for the MCU, so the whole model is offloaded and only the interaction surface stays local. Contrast with tiny-model-on-device approaches (LiteRT-LM, MLX): here the product wants a full frontier-class local model, so the compute moves to a self-hosted backend rather than shrinking the model.
- Fault tolerance falls out of keeping the device thin: independent surfaces and inputs degrade gracefully (OLED down → e-paper; keyboard down → encoder; Wi-Fi down → local shell still works). (14:50)
- Takeaway framing: "keep the model off the metal" — there are no LLMs today that run on super-tiny MCUs, so plan for a backend from the start. (17:28-17:46)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Decide open-model ownership by capability, hardware, latency, and cost thresholds](decide-open-model-ownership-by-capability-hardware-latency-and-cost-thresholds.md)
- [Treat edge models as their own architecture class](treat-edge-models-as-their-own-architecture-class.md)
- [On-device agents can combine local reasoning with tool and API calls](on-device-agents-can-combine-local-reasoning-with-tool-and-api-calls.md)

Sources:
- [OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack](../sources/20260628_akk6KRlcwW4.md), 06:54-17:46
