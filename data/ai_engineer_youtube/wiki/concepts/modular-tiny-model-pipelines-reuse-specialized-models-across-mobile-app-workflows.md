# Modular Tiny-Model Pipelines Reuse Specialized Models Across Mobile App Workflows

Summary: Mobile AI apps can be built as pipelines of specialized tiny models rather than one monolithic model. Separate ASR, personalization, denoising, voice-activity, and text-polishing components can be reused across workflows and debugged independently.

Use when:
- Designing an on-device app that combines speech, personalization, and generation under mobile memory constraints.
- Deciding whether to fine-tune one model for an end-to-end task or compose multiple smaller models.

Details:
- AI Edge Eloquent is described as a transcription and text-polishing app that separates the transcription engine, personalization flow, and text-polishing engine.
- The source says one model could theoretically do the combined task, but separate models are often the pragmatic mobile choice because weights can be reused in multiple places and intermediate stages are easier to inspect.
- LiteRT supports non-autoregressive support models around an LLM, such as voice-activity detection and denoising models, while LiteRT-LM provides the autoregressive LLM loop.
- The workshop describes using stronger cloud LLMs to generate synthetic data for fine-tuning smaller Gemma-derived models for narrow mobile tasks.

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Tokenizer size must match data and compute budget](tokenizer-size-must-match-data-and-compute-budget.md)

Sources:
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md), 54:07-54:44, 59:31-01:01:34
