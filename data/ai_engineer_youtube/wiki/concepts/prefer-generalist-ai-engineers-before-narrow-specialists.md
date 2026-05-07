# Prefer Generalist AI Engineers Before Narrow Specialists

Summary: Early AI transformation usually benefits from adaptable generalists who can build, integrate, use abstractions, understand tradeoffs, and work with customers. Specialists become more important once the team has a stable baseline and needs the next increment of performance.

Use when:
- Staffing an early AI product team under budget constraints.
- Choosing between broad AI engineers and narrowly specialized model, serving, or research hires.

Details:
- Linkov's 2021 team prioritized model training, model serving, and business acumen, but the model-training bar was general architecture knowledge, encoder fine-tuning, data engineering, and Hugging Face fluency rather than GPT-scale training depth, 07:51-08:36.
- Platform abstractions lowered the need for every engineer to understand Kubernetes or training/serving internals deeply, but they still needed to understand the tradeoffs those abstractions made, 08:36-09:00.
- Business acumen was treated as an engineering requirement: engineers needed to join customer calls rather than define their role as isolated coding, 09:00-09:16.
- As tools evolved, some serving work moved to open-source offerings and commercial APIs, while domain nuance became a higher bar for the medical-record-processing product, 09:18-10:30.
- Generalists are strongest while teams are finding fit and making basic progress; specialists become more valuable after the general team has exhausted its knowledge and needs the extra performance, 11:59-12:42.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Open model families need ecosystem-compatible tooling](open-model-families-need-ecosystem-compatible-tooling.md)
- [Build domain-specific workflow wrappers around models](build-domain-specific-workflow-wrappers-around-models.md)

Sources:
- [Structuring a modern AI team - Denys Linkov, Wisedocs](../sources/20250724_SbUxRluVRwk.md), 07:51-12:42
