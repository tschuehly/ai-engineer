# Tools

## Overview

Personal-agent tools need visible orchestration controls. Users should be able to see and collapse tool calls, stop runs, inspect scheduled messages, switch workspaces, attach exact context, and adjust the active agent's capabilities without relying on generic chat commands or hidden execution state.

Agent tools are most useful when their execution surface is paired with clear context about when and how to use them. MCP can expose service-backed integrations and remote actions, while skills can package the workflow guidance, domain instructions, references, and scripts that help an agent choose and use those integrations correctly. Visual automation tools can expose service nodes such as Gmail or calendar actions directly as agent tools, but the tool names and descriptions become part of the prompt surface and need the same care as any other instruction. Tool loops also need a strict runtime contract: when a model requests a function call, the client should validate that the tool exists, execute it, return the structured result, and continue only until final text. Tool design should also narrow sensitive authority: if an agent needs to update a secret-bearing file, a purpose-built operation such as key existence and key write is safer than raw file reads that may send secrets through inference or logs. Skill-like command prompts can function as product surfaces: they are loaded only when invoked, can be updated server-side, and can encode advanced workflows that would otherwise require heavy UI and orchestration code. API-focused skills should avoid embedding every volatile detail; stable guidance plus links to current Markdown docs gives agents a better chance of avoiding stale model names or outdated method signatures. Canvas tools add a different surface: agents can use structured editor objects as prompt context and produce editor-native shapes, diagrams, and UI elements that remain inspectable and editable. Voice agents are another place where tool restraint matters: a realtime conversational agent should start with a small tool surface and delegate complex work through specialist handoffs that preserve conversation state. Realtime multimodal APIs can expose audio buffers, visual frames, transcriptions, and grounding tools over a single stateful stream, which makes tool timing and latency part of the UX. Some workflows should bypass LLM judgment entirely: deterministic scripts, explicit approval gates, and subworkflows are a better fit for known conditional actions, while the LLM handles judgment-heavy interpretation and connection-making. On edge devices, guidance must be especially compact: a skill registry can expose short descriptions first, then load full instructions, JavaScript, native intents, or API calls only when needed. Context packages can also be distributed through libraries and registries, which makes tool guidance reusable across projects but requires evaluation, provenance, dependency management, and context filtering before installation. A context engine can be exposed through MCP, CLI, API, dashboard, or messaging surfaces; the tool surface is the access path, while the engine still needs source relationships, personalization, permissions, and conflict handling behind it. Runtime and browser/editor APIs can turn an agent into a much more capable tool user, but direct code execution against a live app should be treated as executable authority with sandboxing, local/offline constraints, or explicit permission boundaries. Product teams should also treat APIs, CLIs, and MCP servers as first-class user interfaces when agents or bots are the callers; dashboards alone are insufficient for agent experience. Enterprise MCP tools add an authentication layer: Cross-App Access can reduce repeated OAuth consent by letting the identity provider mediate trust between an MCP client and server, but authorization scopes still need their own policy design. A gateway can generalize that control plane by placing auth, authorization, observability, secure connectivity, routing, deployment, and credential primitives between MCP clients and many servers, so domain teams focus on tool workflow while security teams bless one root of trust. At production scale, the tool catalog itself becomes an operational surface: defaults, output payloads, descriptions, and scope filters should be tuned so agents see enough capability to act without burning context or selecting hazardous tools. Very large APIs should use progressive discovery rather than eager endpoint dumps; CLIs, tool search, and typed code-mode surfaces each reduce upfront context in different ways. Code mode is especially useful when generated SDK types can make thousands of endpoints available through model-written code, but that moves safety work into capability-based sandboxes, network policy, secret isolation, observability, and API rate limits. The safest shape starts with no ambient authority and grants only the APIs or network access required for the current task.

Domain skills can act as node-level controls by supplying expert handling for specific work-tree contingencies after the agent discovers them. Persistent artifacts such as documents, comments, and tables can also be tool surfaces because they let the user scope an instruction to the exact clause, row, or review finding instead of relying on a linear chat correction. Research agents especially need tool and artifact discipline: source gathering, YouTube analysis, compilation, and writing can be split into explicit tools or files so downstream workflows consume grounded evidence instead of hidden conversation state.

Agent-facing products should treat APIs and CLIs as primary interfaces once agents become meaningful users. Dashboards still matter for humans, but agent experience asks whether a feature can be automated, called from a CLI, or used through a stable machine surface. Open model families add a model-tooling version of the same rule: release success depends on meeting developers in their existing runtimes, fine-tuning libraries, quantization paths, and product integrations. For Apple local apps, MLX Swift LM and Hugging Face model IDs form a compact tooling path, while curated app model catalogs prevent users from selecting weights that are available but poor on the target phone.

MCP is one part of the agent connectivity stack, not a universal replacement for every surface. Skills carry reusable domain knowledge, CLIs and computer use fit local sandboxed environments, and MCP fits remote semantics, authorization, governance, resources, long-running tasks, and cross-client application surfaces. MCP applications and skills over MCP point to a richer server-authored surface where an integration can ship UI, tools, and current usage guidance together.

Open-source agent tools need extension points as well as integrations. Plugin architecture can keep memory, wiki, dreaming, and other experimental capabilities installable without forcing every idea into core or overloading maintainers with unrelated pull requests.

## Key Concepts

- [Sandboxed code execution turns model reasoning into inspectable computation](../concepts/sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md) - sandboxed execution gives models computation tools while limiting local side effects.
- [Build internal AI engineering platforms when off-the-shelf tools lack enterprise context](../concepts/build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md) - enterprise tool platforms may need custom context and integrations around existing engineering systems.
- [Collaborate with complex agents through high-bandwidth artifacts](../concepts/collaborate-with-complex-agents-through-high-bandwidth-artifacts.md) - documents, tables, and comments can be tool surfaces for precise human-agent collaboration.
- [Encode domain judgment in node-level agent skills](../concepts/encode-domain-judgment-in-node-level-agent-skills.md) - skills can provide contextual guidance at the work node where a special case appears.
- [Use hosted model playgrounds to prototype before owning infrastructure](../concepts/use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md) - playgrounds can be a temporary integration surface before production runtime ownership.
- [Open model families need ecosystem-compatible tooling](../concepts/open-model-families-need-ecosystem-compatible-tooling.md) - open models need toolchain support where developers already run, fine-tune, and integrate them.
- [Use MLX Swift LM for Apple local model integration](../concepts/use-mlx-swift-lm-for-apple-local-model-integration.md) - MLX Swift LM turns Hugging Face model IDs into a native Apple local-inference tool path.
- [Realtime multimodal models should plan over specialized local actuators](../concepts/realtime-multimodal-models-should-plan-over-specialized-local-actuators.md) - embodied tool use should separate conversational planning from local action execution.
- [Use skills for workflow guidance and MCP for integrations](../concepts/use-skills-for-workflow-guidance-and-mcp-for-integrations.md) - separates the integration layer from the contextual guidance layer.
- [Customize subagents by task, model, tools, and permissions](../concepts/customize-subagents-by-task-model-tools-and-permissions.md) - specialist agents should receive scoped tool and MCP access that matches their role.
- [Use agent hooks to automate session rituals](../concepts/use-agent-hooks-to-automate-session-rituals.md) - event hooks can automate setup, audit, and continuation actions around tool use.
- [Prompt-coded product behavior reduces code but weakens hard guarantees](../concepts/prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md) - command or skill prompts can carry advanced behavior, but they should not be confused with hard enforcement.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - a tool surface alone does not make a context engine useful.
- [Edge agent skills need progressive disclosure to preserve small-model reliability](../concepts/edge-agent-skills-need-progressive-disclosure-to-preserve-small-model-reliability.md) - small local models need tool context to be discoverable without all details being preloaded.
- [Constrained decoding makes small-model tool calls production-usable](../concepts/constrained-decoding-makes-small-model-tool-calls-production-usable.md) - tool runtimes can improve small-model reliability by constraining calls to valid tools.
- [Package reusable context as skills, libraries, and registries](../concepts/package-reusable-context-as-skills-libraries-and-registries.md) - tool guidance can be shared as installable context packages.
- [Filter untrusted context before it reaches the agent](../concepts/filter-untrusted-context-before-it-reaches-the-agent.md) - tool and skill ecosystems need controls for unsafe context before execution sandboxes apply.
- [Ambient agents need self-maintenance and memory hygiene](../concepts/ambient-agents-need-self-maintenance-and-memory-hygiene.md) - operational jobs and deterministic scripts keep always-on agent systems reliable.
- [Scope personal and team agents by reachable authority](../concepts/scope-personal-and-team-agents-by-reachable-authority.md) - shared agent tools need authority boundaries tied to who can invoke them.
- [Plugin architectures let agent systems absorb experiments](../concepts/plugin-architectures-let-agent-systems-absorb-experiments.md) - plugins let agent capabilities evolve without bloating the core tool surface.
- [Personal knowledge bases become agent context substrates](../concepts/personal-knowledge-bases-become-agent-context-substrates.md) - note search, memory, tagging, and link ingestion are tool surfaces for personal context.
- [Purpose-built agent workspaces make orchestration visible](../concepts/purpose-built-agent-workspaces-make-orchestration-visible.md) - visible tool calls, cron labels, stop controls, and capability panels make personal-agent tool use easier to supervise.
- [Explicit context attachments can outperform opaque agent memory](../concepts/explicit-context-attachments-can-outperform-opaque-agent-memory.md) - explicit document, skill, and knowledge-base mentions make task context a user-controlled tool surface.
- [Visual agent workflows make tool use observable and adjustable](../concepts/visual-agent-workflows-make-tool-use-observable-and-adjustable.md) - visual nodes expose the trigger, memory, model, tool, and approval surfaces behind an agent.
- [Canvas-native agents turn spatial work surfaces into prompt context](../concepts/canvas-native-agents-turn-spatial-work-surfaces-into-prompt-context.md) - canvas objects and annotations can serve as the tool context for agent edits.
- [Structured canvas outputs make agent edits inspectable and editable](../concepts/structured-canvas-outputs-make-agent-edits-inspectable-and-editable.md) - structured editor objects keep visual agent outputs modifiable rather than flattened into pixels.
- [Hackable agent runtimes need tight safety boundaries](../concepts/hackable-agent-runtimes-need-tight-safety-boundaries.md) - executable editor or browser access needs stricter controls than ordinary shape or API tools.
- [Route high-impact agent actions through explicit human approval gates](../concepts/route-high-impact-agent-actions-through-explicit-human-approval-gates.md) - approval steps keep sensitive tool execution outside model-only control.
- [Use tool names and descriptions as operational prompts](../concepts/use-tool-names-and-descriptions-as-operational-prompts.md) - clear tool metadata improves selection and enables local tool-specific guidance.
- [Expose explicit control signals for generative media models](../concepts/expose-explicit-control-signals-for-generative-media-models.md) - image and video tools should expose structured controls when text alone is too imprecise.
- [Split large automation surfaces into specialized subagents and subworkflows](../concepts/split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md) - subworkflows and specialist agents keep large tool surfaces manageable.
- [Delegate complex voice-agent tasks through specialist tools and handoffs](../concepts/delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md) - voice systems should route harder tool or policy decisions to specialists while preserving context.
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](../concepts/agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md) - agent-facing products need machine-friendly control surfaces, not only human dashboards.
- [Separate agent harnesses from generated-code execution](../concepts/separate-agent-harnesses-from-generated-code-execution.md) - generated code should execute away from the trusted agent harness.
- [Agent tool loops turn model-required actions into executable results](../concepts/agent-tool-loops-turn-model-required-actions-into-executable-results.md) - tool runtimes need to turn model-selected functions into validated execution and structured results.
- [Agent skills should point to current docs instead of embedding every API detail](../concepts/agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md) - skills should stay stable while fast-changing API detail stays in current docs.
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](../concepts/realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md) - streaming sessions can combine live input, transcriptions, and grounding tools.
- [Constrain sensitive file access with purpose-built tools](../concepts/constrain-sensitive-file-access-with-purpose-built-tools.md) - narrow operations keep secrets out of model context and logs.
- [Agent rules should emerge from observed off-rail behavior](../concepts/agent-rules-should-emerge-from-observed-off-rail-behavior.md) - rules, checks, and hooks are tool-context controls that should be grounded in local agent failures.
- [Cross-app access centralizes MCP authentication through the identity provider](../concepts/cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md) - IdP-mediated trust can make enterprise MCP access less repetitive and more governable.
- [Short-lived IdP-derived tokens reduce standing MCP access](../concepts/short-lived-idp-derived-tokens-reduce-standing-mcp-access.md) - short token lifetimes tie MCP access to active SSO sessions.
- [Cross-app access does not replace authorization policy](../concepts/cross-app-access-does-not-replace-authorization-policy.md) - authentication centralization should not be mistaken for fine-grained tool authorization.
- [MCP gateways create an enterprise root of trust](../concepts/mcp-gateways-create-an-enterprise-root-of-trust.md) - a gateway gives enterprise MCP a shared auth, authorization, observability, connectivity, and deployment layer.
- [Gateway platform primitives let teams focus on MCP business logic](../concepts/gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md) - shared platform primitives let domain teams build workflow-specific servers without reimplementing the control plane.
- [Decouple agent harnesses from enterprise data layers](../concepts/decouple-agent-harnesses-from-enterprise-data-layers.md) - gateways keep new agent clients from binding directly to every internal MCP server and data source.
- [MCP tool surfaces need default context budgets](../concepts/mcp-tool-surfaces-need-default-context-budgets.md) - broad tool catalogs need context-aware defaults and compact outputs.
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](../concepts/agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md) - agent connectivity choices should match local execution, remote semantics, governance, and guidance needs.
- [MCP applications ship UI and tools together](../concepts/mcp-applications-ship-ui-and-tools-together.md) - MCP can expose both human-rendered interfaces and model-callable tools from the same server.
- [Ship skills over MCP for server-authored tool guidance](../concepts/ship-skills-over-mcp-for-server-authored-tool-guidance.md) - large MCP servers can ship updatable usage guidance with the integration.
- [Discover large API tool surfaces progressively](../concepts/discover-large-api-tool-surfaces-progressively.md) - broad API surfaces should be discovered on demand instead of loaded as one huge MCP context payload.
- [Expose large APIs through typed code mode](../concepts/expose-large-apis-through-typed-code-mode.md) - generated SDK types can make many endpoints available through compact code-oriented context.
- [Run agent-written API code inside programmable sandboxes](../concepts/run-agent-written-api-code-inside-programmable-sandboxes.md) - code-mode tools need isolation, network controls, secret boundaries, and rate limits.
- [Capability-based sandboxes start with no authority](../concepts/capability-based-sandboxes-start-with-no-authority.md) - generated-code runtimes should receive explicit task-scoped capabilities instead of broad ambient access.
- [Encode agent intent into server-side tools](../concepts/encode-agent-intent-into-server-side-tools.md) - tools can hide multi-call service choreography behind a more reliable agent intent.
- [Filter MCP tools by scopes and step-up authorization](../concepts/filter-mcp-tools-by-scopes-and-step-up-authorization.md) - scopes and OAuth challenges can shrink tool exposure while preserving workflow continuity.
- [Stateless remote MCP servers rebuild allowed tools per request](../concepts/stateless-remote-mcp-servers-rebuild-allowed-tools-per-request.md) - remote MCP servers can scale by deriving the allowed tool set on each request.
- [Treat prompts as distributed harness surfaces](../concepts/treat-prompts-as-distributed-harness-surfaces.md) - rules, skills, lints, PR comments, and tests can act as agent-steering tool surfaces.
- [Deep research agents need planning, grounded evidence, and pivot loops](../concepts/deep-research-agents-need-planning-grounded-evidence-and-pivot-loops.md) - research tools should support search, inspection, citation, and synthesis.
- [Split exploratory research agents from constrained writing workflows](../concepts/split-exploratory-research-agents-from-constrained-writing-workflows.md) - Markdown artifacts can be the tool boundary between agentic and deterministic phases.

## Open Questions

- When should a workflow be encoded as an MCP tool description, a skill, a local script, or a combination of these?
- When is server-controlled command prompting a better product surface than visible UI controls?
- What telemetry is needed to decide that a skill or tool is unused, stale, or actively harmful?
- When should a context engine expose the same capability through MCP, CLI, API, or a messaging integration?
- What security checks should run before a registry skill or context package is loaded by an agent?
- Which agent operations should be implemented as deterministic scripts rather than LLM tool calls?
- Which personal-agent tool calls need visible progress, cancellation, or capability toggles before users will trust them?
- How should tool descriptions be tested when they act as prompts for high-risk actions?
- How small should a realtime voice agent's tool surface be before handoff delegation becomes necessary?
- How should product teams test APIs, CLIs, and MCP servers as user interfaces for agents rather than just integrations for humans?
- Which agent tools are safe to expose directly in a generic loop, and which need deterministic policy checks before execution?
- Which file types should never be exposed through raw read tools, even when an agent needs to edit them?
- When should a visual agent be limited to structured editor APIs, and when is sandboxed code execution against the runtime justified?
- Which plugin bundles are coherent enough to install as a unit, and which should remain separate skills, apps, or MCP servers?
- Which MCP servers need IdP-mediated cross-app access before they are safe to roll out across an enterprise team?
- Which gateway primitives should be mandatory before an enterprise lets teams publish their own MCP servers?
- Which tool calls should be collapsed into intent-level server tools instead of exposed as separate low-level operations?
- When should a large API prefer CLI discovery, tool search, typed code mode, or hand-authored MCP tools?
- Which generated-code actions are safe enough for code mode, and which require a fixed tool or approval gate?
- Which image and video controls should appear as explicit user-facing tool parameters rather than hidden prompt instructions?
- Which research artifacts should be preserved as files so later tools can audit provenance?
- Which open-model runtimes and fine-tuning tools need first-class support before a model release is usable by the target developer community?
- Which MCP applications need web-client rendering support before they are useful, and which should remain tool-only integrations?
- Which guidance belongs in server-authored skills over MCP instead of client-local skills?
- Which lint messages or CI comments are important enough to be treated as first-class prompt surfaces?

## Sources

- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md)
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md)
- [I Gave an AI Agent the Keys to My Life (Here's What Happened) - Radek Sienkiewicz (@velvetshark-com)](../sources/20260502_sJ2jc7leKBk.md)
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md)
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md)
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md)
- [Agents on the Canvas in tldraw - Steve Ruiz, tldraw](../sources/20260501_sPUjIBH5Cwg.md)
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md)
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md)
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md)
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md)
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md)
- [One Login to Rule Them All: Cross-App Access for MCP - Garrett Galow, WorkOS](../sources/20260428_EmhRyw6xeT0.md)
- [Scaling GitHub for your Agents — Sam Morrow, GitHub](../sources/20260427_0n3MKk7r60w.md)
- [Gateways are All You Need - Karan Sampath, Anthropic](../sources/20260427_CD6R4Wf3jnY.md)
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md)
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md)
- [The End of Apps - Kitze, Sizzy.co](../sources/20260423_4fntwuOoedA.md)
- [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../sources/20260422_XNtkiQJ49Ps.md)
- [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @pragmaticengineer](../sources/20260421_CS5Cmz5FssI.md)
- [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../sources/20260420_mYSRn6PC1mc.md)
- [The New Application Layer - Malte Ubl, CTO Vercel](../sources/20260420_XKup1pj-34M.md)
- [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](../sources/20260420__gVFUEdhCyI.md)
- [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX - Adrien Grondin, Locally AI](../sources/20260420_a2muGkT4WD4.md)
- [The Future of MCP - David Soria Parra, Anthropic](../sources/20260419_v3Fr2JR47KA.md)
- [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](../sources/20260419_8txf05vVVl4.md)
- [Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI](../sources/20260417_am_oeAoUhew.md)
- [State of the Claw - Peter Steinberger](../sources/20260417_zgNvts_2TUE.md)
