# Own Open Models for Sovereignty and Permissionless Adoption

Summary: Open-weight models give teams and institutions sovereignty — they own the weights, run on their own hardware, customize freely, and keep proprietary data inside their infrastructure — and a permissive license removes the legal-review barrier that blocks sovereign and regulated adoption of custom-licensed models.

Use when:
- Deciding whether a workload needs an owned open model instead of (or alongside) a hosted frontier API.
- Explaining to a legal, compliance, or procurement function why open-weight licensing matters as much as raw capability.
- Planning national, public-sector, or regulated-language deployments where loss-of-service and data-residency risk are unacceptable.

Details:
- Sovereignty here means owning the model so a team is not exposed to loss of service or a vendor revoking access, can run it on its own hardware, can adapt it to its own use cases, and can send proprietary data that cannot leave its infrastructure. Even the best proprietary model cannot help directly under those constraints. (01:11-02:15, 07:07-07:35)
- The framing is complementary, not either/or: a hosted frontier model (Gemini) is positioned as the most intelligent option but lives on the provider's servers behind an API, while an open model (Gemma) is the answer when control, on-prem hardware access, customization, or data locality dominate. (01:55-02:15, 02:55-03:24)
- The license is treated as a first-class adoption lever: a custom model license forces sovereign institutions through roughly 18 months of procurement and legal review, which usually fails; moving Gemma 4 (and going forward) from a custom Gemma license to Apache 2.0 makes legal sign-off tractable and unlocks permissionless adoption. (07:35-08:25)
- Concrete sovereign deployments cited: Ukraine uses Gemma in parts of its services; Bulgaria built a national LLM fine-tuned on Gemma 2 (moving toward Gemma 4); Brazil has a Portuguese variant fine-tuned on Gemma 3. (08:25-09:00)
- Sovereignty caveat on language adaptation: because a strong multilingual base is already top-2-3 in many languages, fine-tuning it for one specific language now yields diminishing returns (sometimes ~1%), so verify base-model quality before investing in language fine-tuning. (09:00-09:35, see [Multilingual tokenizers improve low-resource fine-tuning paths](multilingual-tokenizers-improve-low-resource-fine-tuning-paths.md))

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Enterprise Open-Model Adoption Follows Task Pressure](enterprise-open-model-adoption-follows-task-pressure.md)
- [Open Model Families Need Ecosystem-Compatible Tooling](open-model-families-need-ecosystem-compatible-tooling.md)
- [Decide open-model ownership by capability, hardware, latency, and cost thresholds](decide-open-model-ownership-by-capability-hardware-latency-and-cost-thresholds.md)
- [Route Gemma 4 model variants by deployment and workflow shape](route-gemma-4-model-variants-by-deployment-and-workflow-shape.md)
- [Multilingual tokenizers improve low-resource fine-tuning paths](multilingual-tokenizers-improve-low-resource-fine-tuning-paths.md)
- [Domain Gemma variants package specialized policy and task behavior](domain-gemma-variants-package-specialized-policy-and-task-behavior.md)

Sources:
- [Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind](../sources/20260610_SS-A8sE7hkw.md), 01:11-09:35
