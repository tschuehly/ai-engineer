# Text Diffusion Trades Serving Throughput for Low Latency

Summary: Text diffusion is much lower latency per request than autoregressive decoding because it does far fewer memory transfers, but it costs more to serve at scale because it spends extra FLOPs per token and loses big-batch throughput — so today it fits on-device, not frontier-scale serving.

Use when:
- Deciding whether a low-latency diffusion model fits a workload, or explaining why frontier production models are still autoregressive.
- Planning on-device / robotics inference where you serve one request at a time.
- Reasoning about the latency vs throughput vs cost tradeoff of a non-autoregressive generator.

Details:
- Why it is faster (memory-bound serving): a GPU/TPU is a tensor core (lots of FLOPs) plus HBM holding weights, activations, and KV cache, joined by a tight bandwidth channel; the chips are FLOP-rich and bandwidth-poor (bandwidth is expensive to add, FLOPs are cheap), so the more FLOPs done per streamed byte, the better. Serving an autoregressive model is memory-bound — each token streams the entire network and KV cache to produce one token. Diffusion generating ~256 tokens in ~24 denoising passes does ~10x fewer memory transfers, so up to ~10x faster if truly memory-bound. (06:13-08:00)
- Gemini Diffusion hit ~2,000 tokens/second consistently (genuine raw browser tokens, including prefill). Longer generations are less prefill-dominated, so you can lean into long sequences of very fast tokens; a one-token output is dominated by prefill cost. (08:00-08:45)
- The disadvantage: diffusion does multiple forward passes over the same data, so it hits a compute threshold earlier and has lower throughput in big-batch serving — higher cost to serve. Autoregressive models are slow per user, but you batch many queries through the GPU to keep cost down and serve a lot, so even though diffusion is lower latency per user it is lower throughput overall. This is why "no one's landing text diffusion into any of these big models" yet — too expensive to serve, even at much lower latency, and "people really care about throughput right now" (the speaker notes Claude has had throughput concerns). (04:02-06:13, 25:00-25:40)
- On-device is the sweet spot: on a phone or robot you serve batch-of-1 and are not batching thousands of queries, so throughput is not the concern — and since quality is "the same quality basically" as frontier autoregressive models, you may as well pick the lowest-latency one. Gemini Diffusion is already in a couple of on-device applications within the Alphabet ecosystem (e.g. robotics). (25:00-26:30)
- Diminishing serving cost even for large models: bigger models tend to need fewer denoising steps for the same output, so as the model grows (more FLOPs per forward pass) the number of forward passes drops, partly offsetting the per-pass cost. (20:30-21:30)

Related topics:
- [Inference](../topics/inference.md)
- [Edge Inference](../topics/edge-inference.md)

Related concepts:
- [Generate Text by Iterative Denoising, Not Left-to-Right](generate-text-by-iterative-denoising-not-left-to-right.md)
- [Scale Text-Diffusion Quality With More Denoising Steps](scale-text-diffusion-quality-with-more-denoising-steps.md)
- [Treat quantization as a memory-bandwidth lever](treat-quantization-as-a-memory-bandwidth-lever.md)
- [Distill diffusion models to reduce sampling steps](distill-diffusion-models-to-reduce-sampling-steps.md)
- [Use edge inference when latency, privacy, offline access, or token cost dominate](use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md)
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)

Sources:
- [Text Diffusion — Brendan O'Donoghue, Google DeepMind](../sources/20260604_r305-aQTaU0.md), 04:02-08:45, 20:30-26:30
