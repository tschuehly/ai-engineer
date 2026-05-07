# Serve Realtime TTS By Audio-Token Throughput

Summary: Realtime text-to-speech models should be served against the generated audio-token rate required for uninterrupted playback. For codec-token voice models, a deployment that is only slightly slower than the audio-token requirement creates gaps even when the model is otherwise usable.

Use when:
- Capacity-planning a streaming TTS or realtime voice-agent inference service.
- Comparing GPU, quantization, batching, or model choices for audio-token generation.

Details:
- Orpheus is described as a Llama 3B-derived voice model trained to emit 24 kHz SNAC audio tokens, with SNAC acting as the codec layer that turns generated tokens back into audio. (04:45-05:20)
- The talk gives a practical throughput target: about 85 SNAC tokens correspond to one second of audio, so serving Orpheus needs roughly 90-100 generated tokens per second to keep up with realtime playback and avoid audible gaps. (05:20-05:39)
- vLLM batch inference plus dynamic FP8 quantization moved Gabber's L40S setup into the realtime range, with about 105 tokens/s for non-fine-tuned voices and 95 tokens/s for LoRA voices at batch size 10. (10:55-12:28)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Design voice agents around voice-to-voice latency budgets](design-voice-agents-around-voice-to-voice-latency-budgets.md)
- [Treat quantization as a memory-bandwidth lever](treat-quantization-as-a-memory-bandwidth-lever.md)
- [Route LoRA Voice Clones With Sticky GPU Affinity](route-lora-voice-clones-with-sticky-gpu-affinity.md)

Sources:
- [Serving Voice AI at $1/hr: Open-source, LoRAs, Latency, Load Balancing - Neil Dwyer, Gabber](../sources/20250731_rD23-VZZHOo.md), 04:45-05:39, 10:55-12:28
