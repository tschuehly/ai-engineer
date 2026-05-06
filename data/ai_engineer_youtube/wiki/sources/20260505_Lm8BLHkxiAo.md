# Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind

Source: [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](https://www.youtube.com/watch?v=Lm8BLHkxiAo)
Uploaded: 2026-05-05
Transcript: `raw/20260505_Lm8BLHkxiAo/Lm8BLHkxiAo.en-orig.vtt`

## Summary

The talk explains when to move inference onto devices, how Gemma edge model sizes map to local interaction classes, how on-device agents can still use tools and structured output, and how LiteRT plus fleet benchmarking support production edge deployment.

## Extracted Concepts

- [Use edge inference when latency, privacy, offline access, or token cost dominate](../concepts/use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md) - explains the product constraints that make local inference valuable.
- [Match Gemma edge model size to device memory and interaction class](../concepts/match-gemma-edge-model-size-to-device-memory-and-interaction-class.md) - maps Gemma edge model sizes to device envelopes and interaction types.
- [On-device agents can combine local reasoning with tool and API calls](../concepts/on-device-agents-can-combine-local-reasoning-with-tool-and-api-calls.md) - shows that local inference can still support tool-using agent workflows.
- [LiteRT provides a cross-platform path from model conversion to edge deployment](../concepts/litert-provides-a-cross-platform-path-from-model-conversion-to-edge-deployment.md) - captures the deployment runtime and conversion path.
- [Benchmark edge models across the device fleet before shipping](../concepts/benchmark-edge-models-across-the-device-fleet-before-shipping.md) - captures the need for representative device benchmarking.

## Topic Links

- [Agents](../topics/agents.md)
- [Edge Inference](../topics/edge-inference.md)
- [Infrastructure](../topics/infrastructure.md)

## Notes

- 02:13-03:06: Edge inference is framed around latency, privacy, offline availability, and cost rather than as a universal cloud replacement.
- 03:10-03:47: Gemma E2B and E4B target different memory and interaction envelopes after quantization.
- 04:02-10:06: The demos combine local reasoning with tool calls, structured JSON, and app-like workflows.
- 11:03-14:10: LiteRT keeps TensorFlow Lite compatibility while broadening the deployment path to PyTorch and JAX conversion.
- 13:27-15:28: Fleet benchmarking is needed because single-device success does not prove broad deployability.
