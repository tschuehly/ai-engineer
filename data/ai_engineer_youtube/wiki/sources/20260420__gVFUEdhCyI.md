# Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind

Source: [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](https://www.youtube.com/watch?v=_gVFUEdhCyI)
Uploaded: 2026-04-20
Transcript: `raw/20260420__gVFUEdhCyI/_gVFUEdhCyI.en-orig.vtt`

## Summary

Omar Sanseviero presents Gemma as a family of open models designed for local, edge, hosted, fine-tuned, and community-built workflows. The talk reinforces Gemma 4 model routing and per-layer embeddings, then adds durable patterns around Apache-licensed open models, ecosystem-compatible tooling, multilingual tokenizer design, low-resource language adaptation, and domain variants such as Shield Gemma and MedGemma.

## Extracted Concepts

- [Route Gemma 4 Model Variants By Deployment And Workflow Shape](../concepts/route-gemma-4-model-variants-by-deployment-and-workflow-shape.md) - supports choosing among effective, MoE, and dense Gemma variants by device and workload.
- [Per-Layer Embeddings Move Effective-Model Capacity Out Of VRAM](../concepts/per-layer-embeddings-move-effective-model-capacity-out-of-vram.md) - explains why E2B/E4B can run on phones by keeping PLE lookup data outside GPU memory.
- [Open Model Families Need Ecosystem-Compatible Tooling](../concepts/open-model-families-need-ecosystem-compatible-tooling.md) - shows Gemma adoption depending on Apache licensing and support across common runtimes and fine-tuning tools.
- [Multilingual Tokenizers Improve Low-Resource Fine-Tuning Paths](../concepts/multilingual-tokenizers-improve-low-resource-fine-tuning-paths.md) - connects tokenizer design to fine-tuning for low-resource and sovereign-language use cases.
- [Domain Gemma Variants Package Specialized Policy And Task Behavior](../concepts/domain-gemma-variants-package-specialized-policy-and-task-behavior.md) - uses Shield Gemma and MedGemma as examples of open variants for safety and medical tasks.

## Topic Links

- [Agents](../topics/agents.md)
- [Edge Inference](../topics/edge-inference.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)
- [Tools](../topics/tools.md)

## Notes

- Gemma is framed as open models that developers can download, run on their own infrastructure or devices, and fine-tune for their own use cases. (00:30-00:41)
- Gemma 4 spans roughly 2B to 32B parameters, with the smallest two models positioned for Android, iOS, Raspberry Pi, multimodal reasoning, and on-device agentic workflows. (01:26-01:59)
- On-device demos included a phone in airplane mode with no API calls, parallel local Gemma instances generating SVGs through llama.cpp, and offline coding/Android development examples. (02:38-03:35)
- The talk explicitly cautions that LM Arena is not a perfect benchmark, treating it as a community preference proxy rather than a complete engineering evaluation. (03:40-03:58)
- Gemma 4 moved to Apache 2 licensing, which the speaker presents as important for developer flexibility and open-source adoption. (05:06-05:24)
- E2B stands for effectively 2B parameters; per-layer embeddings behave like lookup tables that can live on CPU or disk while only the operating parameters need GPU memory. (05:28-06:55)
- Gemma 4's smaller models support image, video, and audio understanding, including speech recognition and speech-to-translated-text workflows. (06:57-07:18)
- The tokenizer is described as multilingual, based on Gemini, and useful when fine-tuning for low digital-resource languages. (07:35-08:27)
- Google worked with Unsloth, MLX, llama.cpp, Hugging Face, vLLM, and other ecosystem projects so developers can fine-tune and run Gemma where they already work. (09:27-10:05)
- Shield Gemma is positioned for policy-aligned safety classification over toxic images or text, while MedGemma is positioned for multimodal medical tasks such as radiology and chest X-ray understanding. (11:26-12:13)
- Community examples include Southeast Asian language work by AI Singapore, sovereign-language efforts in India, and domain research such as lab-validated cancer-therapy pathway exploration. (12:17-13:22)
