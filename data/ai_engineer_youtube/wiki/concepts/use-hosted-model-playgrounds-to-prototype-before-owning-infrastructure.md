# Use Hosted Model Playgrounds to Prototype Before Owning Infrastructure

Summary: Hosted model playgrounds can reduce early infrastructure burden by letting teams test model families, modalities, API-key flows, and deployment paths before downloading models or provisioning their own runtime.

Use when:
- A team needs to evaluate whether a model, modality, or tool surface fits a product idea before building production infrastructure.
- An agent workflow needs a quick path from prompt experiment to generated app, API call, or cloud deployment.

Details:
- AI Studio exposes Gemini, Gemma, video generation, structured output, and code execution controls in one interface, making it a practical scratchpad for multimodal app prototypes before deeper integration work.
- AI Studio supports API-key-backed use for paid models and lets Gemma models be tested through the hosted interface before downloading them to owned infrastructure or running them on local hardware.
- App generation can create Firebase blueprints and rules and offers one-click Cloud Run deployment, but quota and cost still need to be considered during experimentation.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent skills should point to current docs instead of embedding every API detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)

Sources:
- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md), 06:17-07:14, 46:36-46:54, 49:16-49:38, 50:50-51:33, 58:51-59:05
