# Infrastructure

## Overview

AI infrastructure spans local training environments, edge deployment, server-side inference operations, observability systems, identity systems, and the product systems that meter expensive AI usage. Edge AI needs a path from model conversion through quantization, runtime integration, accelerator selection, and fleet validation; CPU/GPU deployment can use a shared artifact, while NPU deployment may require ahead-of-time vendor compilation behind a consistent app API. Apple local inference adds a native runtime path: MLX Swift LM can integrate Hugging Face-hosted MLX weights into iOS, iPadOS, and macOS apps, but product infrastructure still needs curated model catalogs and model-download planning. Server-side small-model inference needs model-aware runtimes plus routing, queueing, autoscaling, observability, and GPU provisioning so many specialized models can run efficiently in production. Model-family access also becomes infrastructure: downloadable open weights support local/self-hosted deployment, while hosted playgrounds and managed endpoints let teams prototype larger reasoning models before owning serving operations. Open model infrastructure also depends on ecosystem fit: permissive licensing, Hugging Face or Ollama-style distribution, llama.cpp, MLX, vLLM, Unsloth, and product integrations determine whether teams can fine-tune, quantize, self-host, or run locally without rebuilding their stack. Production AI applications also need managed prompts, tools, scoring functions, trace metadata, and online scoring automation so local prototypes can become monitored systems. Eval and observability infrastructure for agents must handle production traces that are text-heavy, semi-structured, large, and high velocity, then make those traces usable for offline replay and online scoring. Local training work adds a smaller-scale infrastructure lesson: choose a setup that can run on MPS, CUDA, CPU, or Colab, and keep the model, tokenizer, and batch sizing proportional to the available memory. AI monetization adds a billing-infrastructure lesson: usage caps, threshold notifications, top-ups, rate limits, and detailed metering protect customers and providers when AI calls can burn spend unexpectedly. Enterprise MCP deployments need identity infrastructure as well: centrally managed cross-app trust can reduce local standing credentials and make agent tool access revocable through SSO. Gateways extend this into a broader MCP control plane: one trusted platform can provide auth, authorization, observability, secure connectivity, routing, deployment, and credential primitives while individual teams build domain-specific servers. Remote MCP infrastructure also needs ordinary horizontal-scaling discipline: session storage, observability, policy-derived tool surfaces, and stateless request handling keep large tool-call volumes from depending on one stateful server process. As APIs become agent-facing surfaces, infrastructure also needs compact API exposure mechanisms such as generated SDK types and code-mode execution, plus sandboxes, network controls, secret boundaries, and rate limits so model-written code cannot turn broad API access into an abuse path. Large enterprises may also need internal AI engineering platforms around monorepos, service discovery, on-call systems, and code review because their context and workflow boundaries are too specific for generic agents.

Agent-built applications add a deployment boundary: the harness that plans and controls work should not be treated as the same trust domain as generated code. Infrastructure for the new application layer needs sandboxes and execution separation so agent-written software can run without giving that code direct authority over the agent runtime.

## Key Concepts

- [Use hosted model playgrounds to prototype before owning infrastructure](../concepts/use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md) - hosted tools can validate model and deployment choices before teams own the runtime.
- [Open model families need ecosystem-compatible tooling](../concepts/open-model-families-need-ecosystem-compatible-tooling.md) - open model infrastructure includes license, runtime, fine-tuning, and distribution support.
- [Use MLX Swift LM for Apple local model integration](../concepts/use-mlx-swift-lm-for-apple-local-model-integration.md) - native Apple app infrastructure can use MLX-compatible Hugging Face models without building a cloud service first.
- [Build internal AI engineering platforms when off-the-shelf tools lack enterprise context](../concepts/build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md) - internal platforms can connect agents to monorepos, service catalogs, operational tools, and review systems.
- [Route Gemma 4 model variants by deployment and workflow shape](../concepts/route-gemma-4-model-variants-by-deployment-and-workflow-shape.md) - Gemma 4 supports both downloadable local/self-hosted paths and hosted access for larger models.
- [Unified coding-agent harnesses combine models, tools, environments, and safety](../concepts/unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md) - agent infrastructure includes harnesses that manage tool execution, environments, and safety around models.
- [LiteRT provides a cross-platform path from model conversion to edge deployment](../concepts/litert-provides-a-cross-platform-path-from-model-conversion-to-edge-deployment.md) - TensorFlow Lite format compatibility and conversion support allow models to target multiple edge platforms.
- [Benchmark edge models across the device fleet before shipping](../concepts/benchmark-edge-models-across-the-device-fleet-before-shipping.md) - compilation and acceleration choices should be validated against representative Android devices.
- [Hot-swap small models to avoid one-model-per-GPU waste](../concepts/hot-swap-small-models-to-avoid-one-model-per-gpu-waste.md) - dynamic model loading helps keep accelerator capacity productive when many small models share the fleet.
- [Production inference combines model support with cluster operations](../concepts/production-inference-combines-model-support-with-cluster-operations.md) - runtime support and infrastructure operations have to be designed together.
- [Local LLM training exposes the core model-building stack](../concepts/local-llm-training-exposes-the-core-model-building-stack.md) - local model training makes tokenizer, architecture, training, and inference decisions explicit.
- [Tokenizer size must match data and compute budget](../concepts/tokenizer-size-must-match-data-and-compute-budget.md) - tokenizer capacity has direct implications for memory, convergence, and required training data.
- [Multilingual tokenizers improve low-resource fine-tuning paths](../concepts/multilingual-tokenizers-improve-low-resource-fine-tuning-paths.md) - multilingual tokenization can lower friction for low-resource language adaptation.
- [Modular tiny-model pipelines reuse specialized models across mobile app workflows](../concepts/modular-tiny-model-pipelines-reuse-specialized-models-across-mobile-app-workflows.md) - app infrastructure can combine LiteRT and LiteRT-LM components instead of treating the LLM as the whole application.
- [Prevent AI billing surprises with caps, notifications, and rate limits](../concepts/prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md) - AI billing infrastructure should prevent runaway usage and unexpected invoices.
- [Shared cloud workspaces make agent sessions collaborative](../concepts/shared-cloud-workspaces-make-agent-sessions-collaborative.md) - cloud micro-VM sessions can host shared terminals, previews, branches, and agent history for multiplayer coding work.
- [Apply online scoring to production traces with cost-aware sampling](../concepts/apply-online-scoring-to-production-traces-with-cost-aware-sampling.md) - production eval infrastructure should distinguish always-on cheap checks from sampled expensive judge-model scoring.
- [Connect production observability to offline eval loops](../concepts/connect-production-observability-to-offline-eval-loops.md) - observability systems should feed real production examples back into offline agent improvement.
- [Agent traces require specialized eval infrastructure](../concepts/agent-traces-require-specialized-eval-infrastructure.md) - trace storage and query systems need to account for large, semi-structured, text-heavy agent data.
- [Code-backed content can replace fragile CMS workflows for agents](../concepts/code-backed-content-can-replace-fragile-cms-workflows-for-agents.md) - repository-backed content can make agent-managed operational data reviewable.
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](../concepts/agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md) - infrastructure should include machine-friendly surfaces for agent users.
- [Agent software factories need runnable, contextual, and verifiable primitives](../concepts/agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md) - infrastructure for agents includes reproducible dev setup and executable checks, not only model hosting.
- [Cloud agents turn coding work into asynchronous VM-backed queues](../concepts/cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md) - VM-backed environments can isolate and parallelize coding-agent execution.
- [Cross-app access centralizes MCP authentication through the identity provider](../concepts/cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md) - IdP-managed trust bridges MCP clients and servers across enterprise applications.
- [Short-lived IdP-derived tokens reduce standing MCP access](../concepts/short-lived-idp-derived-tokens-reduce-standing-mcp-access.md) - short-lived access tokens improve revocation behavior for MCP tools.
- [MCP gateways create an enterprise root of trust](../concepts/mcp-gateways-create-an-enterprise-root-of-trust.md) - gateway infrastructure centralizes trust, routing, observability, and deployment for many MCP servers.
- [Gateway platform primitives let teams focus on MCP business logic](../concepts/gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md) - platform primitives prevent every domain MCP server from rebuilding common infrastructure.
- [Decouple agent harnesses from enterprise data layers](../concepts/decouple-agent-harnesses-from-enterprise-data-layers.md) - a stable gateway boundary lets agent surfaces change without coupling directly to internal data layout.
- [Stateless remote MCP servers rebuild allowed tools per request](../concepts/stateless-remote-mcp-servers-rebuild-allowed-tools-per-request.md) - stateless request handling and shared session storage let remote MCP servers scale horizontally.
- [Filter MCP tools by scopes and step-up authorization](../concepts/filter-mcp-tools-by-scopes-and-step-up-authorization.md) - authorization state should shape the runtime tool surface exposed to agents.
- [Expose large APIs through typed code mode](../concepts/expose-large-apis-through-typed-code-mode.md) - generated types can expose broad APIs without loading every endpoint as tool context.
- [Run agent-written API code inside programmable sandboxes](../concepts/run-agent-written-api-code-inside-programmable-sandboxes.md) - generated-code execution needs infrastructure-level isolation and abuse controls.
- [Separate agent harnesses from generated-code execution](../concepts/separate-agent-harnesses-from-generated-code-execution.md) - agent control planes and generated-code runtimes should be separate trust domains.

## Open Questions

- Which conversion and quantization recipes preserve enough model quality for each target device class?
- Which autoscaling signal best captures useful utilization for mixed small-model workloads?
- How far can local CPU, MPS, or Colab training runs be trusted before moving to larger accelerator infrastructure?
- Which billing events and dimensions should be metered so AI invoices are explainable without exposing implementation noise?
- Which prompt, tool, score, and trace artifacts should be promoted from local code into managed production infrastructure?
- Which Gemma variants should be self-hosted, edge-deployed, or consumed through hosted endpoints for a given workflow?
- Which open-model ecosystem integrations are mandatory before a team can depend on a model family in production?
- Which agent trace fields should be normalized versus stored as text blobs so replay and scoring remain performant?
- Which operational data belongs in code-backed infrastructure when agents are responsible for maintaining it?
- Which MCP credentials should be replaced by IdP-backed exchanges so offboarding and compromise response flow through SSO policy?
- Which MCP controls belong in a shared gateway, and which should remain inside each domain server's business logic?
- Which MCP session fields are worth storing centrally when request routing should remain stateless?
- Which sandbox and rate-limit policies are required before a platform lets agents run generated code against its APIs?
- Which enterprise-specific context and workflow integrations justify custom internal agent platforms instead of vendor tools?

## Sources

- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md)
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md)
- [Why building eval platforms is hard - Phil Hetzel, Braintrust](../sources/20260428__fQ7Z_Wfouk.md)
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Training an LLM from Scratch, Locally - Angelos Perivolaropoulos, ElevenLabs](../sources/20260504_UsB70Tf5zcE.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [Mastering AI Pricing: Flexible & Agile Monetization - Mayank Pant, Stripe](../sources/20260501_CrqPcIZOOXA.md)
- [Shipping complex AI applications - Braintrust & Trainline](../sources/20260501_ZdheJTfLu-s.md)
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md)
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md)
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md)
- [One Login to Rule Them All: Cross-App Access for MCP - Garrett Galow, WorkOS](../sources/20260428_EmhRyw6xeT0.md)
- [Scaling GitHub for your Agents — Sam Morrow, GitHub](../sources/20260427_0n3MKk7r60w.md)
- [Gateways are All You Need - Karan Sampath, Anthropic](../sources/20260427_CD6R4Wf3jnY.md)
- [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment - Maggie Appleton, GitHub](../sources/20260426_ClWD8OEYgp8.md)
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md)
- [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @pragmaticengineer](../sources/20260421_CS5Cmz5FssI.md)
- [The New Application Layer - Malte Ubl, CTO Vercel](../sources/20260420_XKup1pj-34M.md)
- [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](../sources/20260420__gVFUEdhCyI.md)
- [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX - Adrien Grondin, Locally AI](../sources/20260420_a2muGkT4WD4.md)
