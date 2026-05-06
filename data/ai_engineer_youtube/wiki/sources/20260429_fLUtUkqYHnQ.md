# Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI

Source: [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](https://www.youtube.com/watch?v=fLUtUkqYHnQ)
Uploaded: 2026-04-29
Transcript: `raw/20260429_fLUtUkqYHnQ/fLUtUkqYHnQ.en-orig.vtt`

## Summary

Maxime Labonne explains why edge-scale language models need model design, training, and evaluation choices that differ from simply shrinking large-model recipes. The talk covers memory-bound architecture tradeoffs, on-device profiling for LFM-style short-convolution blocks, post-training small models for narrow extraction and tool-use strengths, doom-loop failure modes in tiny reasoning models, and agentic tool use as a way to compensate for limited knowledge and context capacity.

## Extracted Concepts

- [Treat edge models as their own architecture class](../concepts/treat-edge-models-as-their-own-architecture-class.md) - the source argues that small models are memory-bound, task-specific, and latency-sensitive rather than just scaled-down large models.
- [Profile small-model architectures on target hardware](../concepts/profile-small-model-architectures-on-target-hardware.md) - the source shows Liquid AI choosing short-convolution blocks through real CPU, phone, and GPU profiling.
- [Post-train small models for narrow capabilities](../concepts/post-train-small-models-for-narrow-capabilities.md) - the source frames data extraction and tool use as better targets than average capability across every benchmark.
- [Mitigate small-model doom loops during preference alignment and RL](../concepts/mitigate-small-model-doom-loops-during-preference-alignment-and-rl.md) - the source gives a concrete training pattern for detecting and reducing repetitive reasoning failures.

## Topic Links

- [Agents](../topics/agents.md)
- [Edge Inference](../topics/edge-inference.md)
- [Evaluation](../topics/evaluation.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

## Notes

- Liquid AI focuses on edge models for on-device deployment across text, vision, and audio, with model sizes discussed from 350M parameters to 24B parameters. (00:00-01:01)
- Small models are described as memory-bound, narrower than general-purpose chatbots, and latency-sensitive; the main design warning is that they are not merely scaled-down large models. (01:01-02:18)
- The talk calls out embedding-layer overhead in some tiny model families: Gemma 3 270M is described as 63% embedding parameters, leaving fewer effective parameters for reasoning and knowledge capacity. (02:27-03:58)
- LFM 2 uses a hybrid architecture with short convolutions and GQA, selected through on-device profiling against target hardware rather than only theoretical comparisons. (04:01-05:55)
- LFM 2.5 training uses pre/mid-training, SFT, preference alignment, and reinforcement learning; a 350M model is described as trained on 28T tokens, with performance still improving from more tokens at very small scale. (06:08-07:40)
- For small models, Labonne recommends targeting narrow strengths such as data extraction and tool use instead of trying to be average across coding, math, and every other benchmark. (07:41-09:12)
- Doom loops are repeated word or reasoning sequences that become more likely when tiny reasoning models face tasks beyond their capability. (10:41-11:33)
- Liquid AI reduces doom loops by generating multiple stochastic rollouts plus a deterministic rollout, scoring them with an LLM jury, and using preference alignment to choose non-looping answers over looping answers. (11:34-12:54)
- A second mitigation uses reinforcement learning with verifiable rewards, n-gram repetition penalties, and diverse temperature-sampled rollouts; the talk says SFT barely moved the doom-loop ratio while DPO and RL reduced it substantially. (12:55-15:12)
- The talk frames web search, Python, and other agentic tools as ways for small models to compensate for low knowledge capacity and weak long-context capability. (15:28-17:09)
