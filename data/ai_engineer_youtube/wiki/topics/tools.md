# Tools

## Overview

Personal-agent tools need visible orchestration controls. Users should be able to see and collapse tool calls, stop runs, inspect scheduled messages, switch workspaces, attach exact context, and adjust the active agent's capabilities without relying on generic chat commands or hidden execution state. For read-only observers, the tool surface should make source mutability explicit: source connectors can feed an analysis workspace and reviewable outputs without granting write-back authority.

Agent tools are most useful when their execution surface is paired with clear context about when and how to use them. MCP can expose service-backed integrations and remote actions, while skills can package the workflow guidance, domain instructions, references, and scripts that help an agent choose and use those integrations correctly. Visual automation tools can expose service nodes such as Gmail or calendar actions directly as agent tools, but the tool names and descriptions become part of the prompt surface and need the same care as any other instruction. Tool loops also need a strict runtime contract: when a model requests a function call, the client should validate that the tool exists, execute it, return the structured result, and continue only until final text. Tool design should also narrow sensitive authority: if an agent needs to update a secret-bearing file, a purpose-built operation such as key existence and key write is safer than raw file reads that may send secrets through inference or logs. Skill-like command prompts can function as product surfaces: they are loaded only when invoked, can be updated server-side, and can encode advanced workflows that would otherwise require heavy UI and orchestration code. API-focused skills should avoid embedding every volatile detail; stable guidance plus links to current Markdown docs gives agents a better chance of avoiding stale model names or outdated method signatures. Browser runtimes are becoming tool surfaces too: Chrome DevTools MCP can expose navigation, screenshots, console errors, network requests, Lighthouse, network throttling, and performance traces to coding agents, while DevTools AI can analyze selected runtime evidence and apply browser-tested CSS changes back to source. Canvas tools add a different surface: agents can use structured editor objects as prompt context and produce editor-native shapes, diagrams, and UI elements that remain inspectable and editable. Voice agents are another place where tool restraint matters: a realtime conversational agent should start with a small tool surface and delegate complex work through specialist handoffs that preserve conversation state. Realtime multimodal APIs can expose audio buffers, visual frames, transcriptions, and grounding tools over a single stateful stream, which makes tool timing and latency part of the UX. Some workflows should bypass LLM judgment entirely: deterministic scripts, explicit approval gates, and subworkflows are a better fit for known conditional actions, while the LLM handles judgment-heavy interpretation and connection-making. On edge devices, guidance must be especially compact: a skill registry can expose short descriptions first, then load full instructions, JavaScript, native intents, or API calls only when needed. Context packages can also be distributed through libraries and registries, which makes tool guidance reusable across projects but requires evaluation, provenance, dependency management, and context filtering before installation. A context engine can be exposed through MCP, CLI, API, dashboard, or messaging surfaces; the tool surface is the access path, while the engine still needs source relationships, personalization, permissions, and conflict handling behind it. Runtime and browser/editor APIs can turn an agent into a much more capable tool user, but direct code execution against a live app should be treated as executable authority with sandboxing, local/offline constraints, or explicit permission boundaries. Product teams should also treat APIs, CLIs, and MCP servers as first-class user interfaces when agents or bots are the callers; dashboards alone are insufficient for agent experience. AI-product teams need internal behavior tools as well: prompt, context, model, tool, parameter, memory, and computer-use controls are more useful when they live in the product's real working context rather than an engineer-only sandbox. Agent-readable web conventions extend that rule to public sites: `llms.txt` can guide agents to relevant documentation, and WebMCP-style tools can expose intended app operations rather than forcing browser agents to infer buttons from screenshots, DOM text, and coordinates. Enterprise MCP tools add an authentication layer: Cross-App Access can reduce repeated OAuth consent by letting the identity provider mediate trust between an MCP client and server, but authorization scopes still need their own policy design. A gateway can generalize that control plane by placing auth, authorization, observability, secure connectivity, routing, deployment, and credential primitives between MCP clients and many servers, so domain teams focus on tool workflow while security teams bless one root of trust. At production scale, the tool catalog itself becomes an operational surface: defaults, output payloads, descriptions, and scope filters should be tuned so agents see enough capability to act without burning context or selecting hazardous tools. Very large APIs should use progressive discovery rather than eager endpoint dumps; CLIs, tool search, and typed code-mode surfaces each reduce upfront context in different ways. Code mode is especially useful when generated SDK types can make thousands of endpoints available through model-written code, but that moves safety work into capability-based sandboxes, network policy, secret isolation, observability, and API rate limits. The safest shape starts with no ambient authority and grants only the APIs or network access required for the current task. Treat generated code as an untrusted tool implementation: short-lived tool calls and transformations can run in isolate-style runtimes, while generated apps that install packages or start servers need container sandboxes with tenant isolation and cleanup.

Domain skills can act as node-level controls by supplying expert handling for specific work-tree contingencies after the agent discovers them. Persistent artifacts such as documents, comments, and tables can also be tool surfaces because they let the user scope an instruction to the exact clause, row, or review finding instead of relying on a linear chat correction. Research agents especially need tool and artifact discipline: source gathering, YouTube analysis, compilation, and writing can be split into explicit tools or files so downstream workflows consume grounded evidence instead of hidden conversation state.

Agent-facing products should treat APIs and CLIs as primary interfaces once agents become meaningful users. Dashboards still matter for humans, but agent experience asks whether a feature can be automated, called from a CLI, or used through a stable machine surface. Open model families add a model-tooling version of the same rule: release success depends on meeting developers in their existing runtimes, fine-tuning libraries, quantization paths, and product integrations. Environment tooling applies the same lesson to research workflows: shared Python environment projects, registries, rubrics, async tool definitions, and managed execution make evals and RL artifacts reusable instead of one-off lab infrastructure. For Apple local apps, MLX Swift LM and Hugging Face model IDs form a compact tooling path, while curated app model catalogs prevent users from selecting weights that are available but poor on the target phone.

MCP is one part of the agent connectivity stack, not a universal replacement for every surface. Skills carry reusable domain knowledge, CLIs and computer use fit local sandboxed environments, and MCP fits remote semantics, authorization, governance, resources, long-running tasks, and cross-client application surfaces. MCP applications and skills over MCP point to a richer server-authored surface where an integration can ship UI, tools, and current usage guidance together.

Task-management tools need the same product shape. Backlog.md uses MCP resources to teach agents the task lifecycle and MCP tools to let them search, view, create, update, and complete repo-local Markdown tasks; the resource/tool split keeps workflow guidance explicit while preserving a constrained operation surface.

RAG stacks are another tool surface when their internals are inspectable and editable. OpenRAG's LangFlow layer exposes ingestion, retrieval, guardrails, parsers, URL ingestion, calculators, prompt templates, and OpenSearch tools as flow components; its API keys and MCP server let other applications or agents call the same retrieval system instead of duplicating it.

LLM programming frameworks can make prompt format itself a tool layer. DSPy signatures and modules describe the workflow intent, while adapters choose how that intent is rendered to the model, so teams can compare JSON, BAML, compressed formats, or model-specific formatting without rewriting the program.

Open-source agent tools need extension points as well as integrations. Plugin architecture can keep memory, wiki, dreaming, and other experimental capabilities installable without forcing every idea into core or overloading maintainers with unrelated pull requests. Ordinary package-manager distribution can be enough for harness extensions when extensions are just code modules that add tools, commands, events, providers, or compaction behavior. Routine systems are another tool layer: they package repeated prompts as scheduled or manually parameterized workflows, often invoking skills for specialized domain guidance while keeping the trigger, variables, and project or agent ownership explicit.

Tool metadata is also a security boundary. MCP and function-calling systems should treat full tool descriptions, hidden parameters, and approval summaries as prompt and policy surfaces, because a model may act on instructions the reviewer never saw. High-risk tools need approval UI that exposes the effective action and guardrails that inspect the full model-visible metadata.

Durable workflow tools add another tool boundary: LLM calls, sandbox operations, and external API calls should be wrapped as steps so the tool run has cached inputs and outputs, retry behavior, spans, and event logs. The workflow engine gives observability and resumability, but sandboxing and permission control still belong to the agent's underlying tool and VM boundaries.

Production MCP servers should be designed as agent-facing interfaces, not as dumps of existing API endpoints. Fewer outcome-oriented tools, constrained schemas, unambiguous descriptions, minimal response payloads, read-only annotations, and resource-level scoping all reduce prompt-injection and oversharing risk before OAuth enters the picture. Remote MCP also changes tool authorization: long-lived API keys in config files or headers are weak production credentials, while OAuth 2.1 flows, PKCE, token exchange, and CIMD-based client identity give shared MCP servers a path toward short-lived scoped access. Governance still needs per-tool policy and traces that show which agent called which tool, which parameters were used, and what data came back. Public MCP servers often need an adaptation layer before they fit a production agent workflow: filter irrelevant tools, rewrite descriptions for the local task, validate sensitive arguments before invocation, compose intent-specific tools from generic ones, and call mandatory brittle setup steps directly when no agent decision is needed. Tool outputs need the same model-facing design: a verbose API-native payload can be worse agent context than a compact serialization shaped for analysis.

Agent-native MCP design is product design, not endpoint publishing. A useful server starts from the workflow outcome an agent should achieve, then curates tools around agent discovery, iteration, and context limits. Auto-generated REST mirrors can bootstrap experiments, but they should be reduced into agent stories before production: known multi-call choreography belongs behind a server-side tool, while the model should be reserved for judgment-heavy steps where the algorithm is not already known.

Enterprise tool ecosystems also need registry metadata once many teams publish MCP servers and A2A agents. A private registry can start from public MCP catalog conventions, add approved internal and public servers, and enrich each entry with owner, environment, authentication, cost attribution, and use-case links. A paired A2A registry can use agent cards as the discoverable contract for agent identity, endpoint, capabilities, modalities, and auth requirements. These registries should be connected to DevOps pipelines so publishing an MCP server or agent updates both the runtime artifact and the governance catalog.

Internal platform tools should be designed so agents can call the same intended paths humans use. APIs are the base layer, while CLIs or MCP servers can wrap those APIs for agent use; logs, metrics, traces, and relevant documentation should also be exposed through machine-friendly surfaces instead of only dashboards or full HTML pages.

For coding agents, tool boundaries should be chosen by what needs hard semantics. Read tools can control token load, grep/glob can support exact codebase search, edit tools can enforce read-before-write and diff-shaped changes, Bash can compose project commands inside a sandbox, and brittle edge cases can be moved into versioned tools that are easier to evaluate than broad prompt guidance. When an action can be exposed as a CLI or API, that text-native surface is usually a better agent tool than browser automation, especially when accuracy matters.

Agent-first IDEs show how browser and editor tools can be combined without hiding their authority. Antigravity gives the agent a Chrome browser for authenticated context retrieval, UI interaction, JavaScript execution, DOM inspection, and screen recording, while keeping terminal-command approvals and editor handoff visible in the agent manager.

The post-IDE direction adds another tool-design constraint: putting every request through one all-purpose coding agent wastes context and model budget. A better tool surface can route trivial checks, product exploration, implementation, review, tests, and merges through narrower roles and interfaces, while the human sees orchestration state and evidence instead of a raw terminal transcript.

Amp Code adds that generic integration availability is not the same as a good core tool surface. A coding agent may need custom search, reasoning, dependency-lookup, and codemod tools tuned to the exact feedback loops it must close; otherwise tool descriptions and calls become context overhead and irrelevant choices become failure modes.

Zapier's Scout work reinforces that useful tools still need to live where the work happens. A separate API playground added another window and saw weak engagement, while the same capabilities gained traction when embedded into support ticket creation, Cursor through MCP, Jira, GitLab CI/CD, and GitLab comment-based iteration.

Prompt-to-app builders are also tool surfaces. AI Studio shows a compact version: model and API feature chips can attach Search grounding, Maps grounding, Live API, and model choices to a generated app, while one-shot builders can clone UI screenshots or explore export flows before a team commits to production implementation. Full-stack app builders extend that surface by inferring packages, backend services, storage, payments, and first- or third-party API integrations from application intent.

Coding agents can also become programmable tools inside other products. Codex is described as callable through SDKs, GitHub Actions, CI/CD, and MCP-connected product agents, which lets an outer product delegate code-writing, connector creation, merge-conflict handling, or bug fixing without rebuilding the full coding-agent harness. The tool-design burden then shifts to the product boundary: expose the coding agent where the work already happens and reserve the surrounding UI, policy, and workflow decisions for the product.

Shell wrappers can also act as local harness tools. A wrapper around Codex CLI can accept file-backed task inputs, launch a child `codex exec`, and print the child output to stdout so the parent agent receives a compact result. This uses Bash as a composable tool surface, but it also turns command shape, sandbox mode, credentials, rollout logging, output files, and timeouts into explicit tool-design concerns.

Model-client wrappers are another tool-surface pattern. When a compiled local model can be invoked through the same `embeddings.create`-style call shape as a hosted model, application and agent code can stay stable while runtime-specific resolution, FFI loading, and output shaping move behind the client boundary.

AI coworker products add tool surfaces that are neither plain chat nor backend APIs. A tool can be invisible background work, ambient affordances in a workspace, inline transformation controls, or a conversational builder. When an agent acts inline, the tool UX should show what it is doing, ask for alignment at meaningful checkpoints, keep snapshots and rollback paths visible, and hand control back to the user when the model cannot safely complete the work.

## Key Concepts

- [Abstract LLM inference behind one routing API](../concepts/abstract-llm-inference-behind-one-routing-api.md) - model-routing platforms can normalize tool calling, provider edge cases, caching, and observability.
- [Run coding agents through a simple master loop](../concepts/run-coding-agents-through-a-simple-master-loop.md) - compact tool loops can be the core architecture for coding agents.
- [Choose AI coworker form factors by interaction mode](../concepts/choose-ai-coworker-form-factors-by-interaction-mode.md) - agent tool surfaces can be invisible, ambient, inline, or conversational rather than only chat.
- [Prototype AI UX by feeling the model material](../concepts/prototype-ai-ux-by-feeling-the-model-material.md) - runnable tools reveal whether a model fits the proposed interaction surface.
- [Design agent presence with visual alignment and handoff](../concepts/design-agent-presence-with-visual-alignment-and-handoff.md) - inline tools need visible progress, alignment, rollback, and handoff.
- [Use coding agents as programmable subagents inside products](../concepts/use-coding-agents-as-programmable-subagents-inside-products.md) - coding agents can be called through SDKs, CI/CD, and MCP as product-internal tools.
- [Headless coding-agent servers make agents callable infrastructure](../concepts/headless-coding-agent-servers-make-agents-callable-infrastructure.md) - terminal coding agents become workflow tools when exposed through a server API and packaged tool environment.
- [Use stable agent harnesses as model-evolution boundaries](../concepts/use-stable-agent-harnesses-as-model-evolution-boundaries.md) - maintained harnesses keep model and tool churn behind a stable integration surface.
- [Task-tuned tool sets beat generic integration surfaces for core coding loops](../concepts/task-tuned-tool-sets-beat-generic-integration-surfaces-for-core-coding-loops.md) - core agent tools should be selected and described for the local workflow.
- [Role-specialized agent systems beat one giant coding agent](../concepts/role-specialized-agent-systems-beat-one-giant-coding-agent.md) - tool and model routing should follow role-specific work rather than one universal worker.
- [Embed agent tools in existing work surfaces](../concepts/embed-agent-tools-in-existing-work-surfaces.md) - standalone tools can fail when they force users out of their normal IDE, ticket, or review flow.
- [Use subagents to isolate context-heavy subtasks](../concepts/use-subagents-to-isolate-context-heavy-subtasks.md) - subagents can be tool-like specialists for search, reasoning, dependency lookup, and codemods.
- [Shell-wrapped subagents can retrofit harness capabilities](../concepts/shell-wrapped-subagents-can-retrofit-harness-capabilities.md) - wrapper scripts can add child-agent behavior to a CLI harness.
- [Permission-stable command wrappers reduce approval friction](../concepts/permission-stable-command-wrappers-reduce-approval-friction.md) - wrappers can keep approved command text stable while task inputs change through files.
- [Design coding-agent editors as review surfaces](../concepts/design-coding-agent-editors-as-review-surfaces.md) - review-oriented UI is part of the tool surface for agent-heavy coding.
- [Put brittle edge cases behind rigorous tools](../concepts/put-brittle-edge-cases-behind-rigorous-tools.md) - high-risk or specific behaviors should become testable tool boundaries.
- [Build RL environments as software artifacts](../concepts/build-rl-environments-as-software-artifacts.md) - Verifiers-style packages combine parsers, rewards, rollout execution, and trainer integration for model environments.
- [Optimize Judge Prompts With Diagnostic Feedback](../concepts/optimize-judge-prompts-with-diagnostic-feedback.md) - prompt-optimization tools such as GEPA need evaluator diagnostics and ground-truth annotations to improve judge rubrics.
- [Sandboxed code execution turns model reasoning into inspectable computation](../concepts/sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md) - sandboxed execution gives models computation tools while limiting local side effects.
- [DSPy programs keep LLM intent separate from prompt strings](../concepts/dspy-programs-keep-llm-intent-separate-from-prompt-strings.md) - typed LLM-backed functions keep workflow logic in code instead of hand-managed prompt strings.
- [DSPy adapters make prompt format a swappable runtime layer](../concepts/dspy-adapters-make-prompt-format-a-swappable-runtime-layer.md) - adapters make JSON, BAML, and compressed model-facing formats testable implementation choices.
- [Route heterogeneous documents through multimodal LLM pipelines](../concepts/route-heterogeneous-documents-through-multimodal-llm-pipelines.md) - multimodal document classifiers and page-image tools can route mixed files through specialized processing paths.
- [Reusable Routines Turn Prompts Into Operational Agent Workflows](../concepts/reusable-routines-turn-prompts-into-operational-agent-workflows.md) - routines turn repeated prompts into explicit tool workflows with schedules, variables, and skill references.
- [Repository skills and AGENTS.md encode repeatable web-agent workflows](../concepts/repository-skills-and-agents-md-encode-repeatable-web-agent-workflows.md) - repo-local instructions can make browser proof, preview sharing, and confirmation gates part of every web-agent change.
- [Browser DevTools MCP turns runtime debugging into agent tools](../concepts/browser-devtools-mcp-turns-runtime-debugging-into-agent-tools.md) - DevTools MCP turns live browser state, traces, and diagnostics into agent-callable tools.
- [Autonomous browser verification finds painted-door failures](../concepts/autonomous-browser-verification-finds-painted-door-failures.md) - browser, DOM, log, API, database, screenshot, and Playwright surfaces give agents verification feedback.
- [Agent managers orchestrate editor, browser, and background agents](../concepts/agent-managers-orchestrate-editor-browser-and-background-agents.md) - agent products can coordinate editor, browser, approvals, and notifications as one tool surface.
- [Dynamic artifacts make agent work reviewable and reusable](../concepts/dynamic-artifacts-make-agent-work-reviewable-and-reusable.md) - generated plans, recordings, diagrams, and comments are tool outputs for supervision and memory.
- [Browser-native AI APIs bring local models into web apps](../concepts/browser-native-ai-apis-bring-local-models-into-web-apps.md) - browser-managed local models can become product APIs for summarization, proofreading, and multimodal prompts.
- [Agent-readable web surfaces guide browsing agents](../concepts/agent-readable-web-surfaces-guide-browsing-agents.md) - `llms.txt` and WebMCP-style surfaces make sites easier for agents to read and operate.
- [Expose task workflow guidance through MCP resources and tools](../concepts/expose-task-workflow-guidance-through-mcp-resources-and-tools.md) - resources can teach a task workflow while tools mutate task state through the intended interface.
- [Build internal AI engineering platforms when off-the-shelf tools lack enterprise context](../concepts/build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md) - enterprise tool platforms may need custom context and integrations around existing engineering systems.
- [Make internal platforms self-service for agent users](../concepts/make-internal-platforms-self-service-for-agent-users.md) - platform tools should remove person-dependent handoffs from agent workflows.
- [Expose observability as agent-readable feedback](../concepts/expose-observability-as-agent-readable-feedback.md) - operational signals should be available through APIs, CLIs, or MCP.
- [Collaborate with complex agents through high-bandwidth artifacts](../concepts/collaborate-with-complex-agents-through-high-bandwidth-artifacts.md) - documents, tables, and comments can be tool surfaces for precise human-agent collaboration.
- [Encode domain judgment in node-level agent skills](../concepts/encode-domain-judgment-in-node-level-agent-skills.md) - skills can provide contextual guidance at the work node where a special case appears.
- [Use hosted model playgrounds to prototype before owning infrastructure](../concepts/use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md) - playgrounds can be a temporary integration surface before production runtime ownership.
- [Treat agent APIs as asynchronous task lifecycles](../concepts/treat-agent-apis-as-asynchronous-task-lifecycles.md) - long-running agent APIs need task handles, state inspection, callbacks, and error paths.
- [Map external conversation threads to agent task IDs](../concepts/map-external-conversation-threads-to-agent-task-ids.md) - channel integrations need correlation records between visible threads and provider task state.
- [Prototype agent workflows in the UI before hardening the API path](../concepts/prototype-agent-workflows-in-the-ui-before-hardening-the-api-path.md) - richer UI surfaces can reveal the context and permissions an API integration must encode.
- [Open model families need ecosystem-compatible tooling](../concepts/open-model-families-need-ecosystem-compatible-tooling.md) - open models need toolchain support where developers already run, fine-tune, and integrate them.
- [Environment registries make AI research more accessible](../concepts/environment-registries-make-ai-research-more-accessible.md) - environment registries package eval and training tasks as discoverable, versioned projects.
- [Treat environments as eval, data, and training substrates](../concepts/treat-environments-as-eval-data-and-training-substrates.md) - environment tools preserve reuse across evaluation, data creation, and training.
- [Use MLX Swift LM for Apple local model integration](../concepts/use-mlx-swift-lm-for-apple-local-model-integration.md) - MLX Swift LM turns Hugging Face model IDs into a native Apple local-inference tool path.
- [Realtime multimodal models should plan over specialized local actuators](../concepts/realtime-multimodal-models-should-plan-over-specialized-local-actuators.md) - embodied tool use should separate conversational planning from local action execution.
- [Use skills for workflow guidance and MCP for integrations](../concepts/use-skills-for-workflow-guidance-and-mcp-for-integrations.md) - separates the integration layer from the contextual guidance layer.
- [Agentic GraphRAG uses schema-aware multi-step graph queries](../concepts/agentic-graphrag-uses-schema-aware-multi-step-graph-queries.md) - graph MCP tools can expose schema, Cypher queries, traversal, and supporting chunks to agents.
- [Context window editing clears stale tool results](../concepts/context-window-editing-clears-stale-tool-results.md) - tool runtimes should remove stale outputs before they crowd out current context.
- [General agents need skills for domain expertise](../concepts/general-agents-need-skills-for-domain-expertise.md) - tool-capable agents still need skills that encode domain procedures.
- [Customize subagents by task, model, tools, and permissions](../concepts/customize-subagents-by-task-model-tools-and-permissions.md) - specialist agents should receive scoped tool and MCP access that matches their role.
- [Configure agent modes, rules, and permissions as the workflow evolves](../concepts/configure-agent-modes-rules-and-permissions-as-the-workflow-evolves.md) - modes, AGENTS.md, skills, worktrees, MCP servers, and approval controls shape how tools are used.
- [Keep spec artifacts feature-scoped, mutable, and context-backed](../concepts/keep-spec-artifacts-feature-scoped-mutable-and-context-backed.md) - MCP servers and steering files can enrich specs without bloating every task prompt.
- [Use agent hooks to automate session rituals](../concepts/use-agent-hooks-to-automate-session-rituals.md) - event hooks can automate setup, audit, and continuation actions around tool use.
- [Prompt-coded product behavior reduces code but weakens hard guarantees](../concepts/prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md) - command or skill prompts can carry advanced behavior, but they should not be confused with hard enforcement.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - a tool surface alone does not make a context engine useful.
- [Edge agent skills need progressive disclosure to preserve small-model reliability](../concepts/edge-agent-skills-need-progressive-disclosure-to-preserve-small-model-reliability.md) - small local models need tool context to be discoverable without all details being preloaded.
- [Constrained decoding makes small-model tool calls production-usable](../concepts/constrained-decoding-makes-small-model-tool-calls-production-usable.md) - tool runtimes can improve small-model reliability by constraining calls to valid tools.
- [Package reusable context as skills, libraries, and registries](../concepts/package-reusable-context-as-skills-libraries-and-registries.md) - tool guidance can be shared as installable context packages.
- [Treat complex skills like software artifacts](../concepts/treat-complex-skills-like-software-artifacts.md) - executable skills need tests, dependency metadata, and version lineage.
- [Filter untrusted context before it reaches the agent](../concepts/filter-untrusted-context-before-it-reaches-the-agent.md) - tool and skill ecosystems need controls for unsafe context before execution sandboxes apply.
- [Aggregated personal context creates mosaic and exfiltration risk](../concepts/aggregated-personal-context-creates-mosaic-and-exfiltration-risk.md) - read-only tool access still needs privacy analysis when many personal sources are combined.
- [Ambient agents need self-maintenance and memory hygiene](../concepts/ambient-agents-need-self-maintenance-and-memory-hygiene.md) - operational jobs and deterministic scripts keep always-on agent systems reliable.
- [Scope personal and team agents by reachable authority](../concepts/scope-personal-and-team-agents-by-reachable-authority.md) - shared agent tools need authority boundaries tied to who can invoke them.
- [Plugin architectures let agent systems absorb experiments](../concepts/plugin-architectures-let-agent-systems-absorb-experiments.md) - plugins let agent capabilities evolve without bloating the core tool surface.
- [Let agent harnesses extend through ordinary code packages](../concepts/let-agent-harnesses-extend-through-ordinary-code-packages.md) - package-manager extensions can add harness capabilities without core forks or bespoke marketplaces.
- [Own agent context instead of accepting hidden harness mutation](../concepts/own-agent-context-instead-of-accepting-hidden-harness-mutation.md) - tool and prompt surfaces should be inspectable when they affect agent behavior.
- [Minimal coding-agent harnesses can outperform feature-heavy surfaces](../concepts/minimal-coding-agent-harnesses-can-outperform-feature-heavy-surfaces.md) - the default tool surface should stay small unless extra capability proves useful.
- [Personal knowledge bases become agent context substrates](../concepts/personal-knowledge-bases-become-agent-context-substrates.md) - note search, memory, tagging, and link ingestion are tool surfaces for personal context.
- [Purpose-built agent workspaces make orchestration visible](../concepts/purpose-built-agent-workspaces-make-orchestration-visible.md) - visible tool calls, cron labels, stop controls, and capability panels make personal-agent tool use easier to supervise.
- [Read-only personal AI observers are a distinct product category](../concepts/read-only-personal-ai-observers-are-a-distinct-product-category.md) - tool systems can produce insight without exposing write tools.
- [Explicit context attachments can outperform opaque agent memory](../concepts/explicit-context-attachments-can-outperform-opaque-agent-memory.md) - explicit document, skill, and knowledge-base mentions make task context a user-controlled tool surface.
- [Visual agent workflows make tool use observable and adjustable](../concepts/visual-agent-workflows-make-tool-use-observable-and-adjustable.md) - visual nodes expose the trigger, memory, model, tool, and approval surfaces behind an agent.
- [Canvas-native agents turn spatial work surfaces into prompt context](../concepts/canvas-native-agents-turn-spatial-work-surfaces-into-prompt-context.md) - canvas objects and annotations can serve as the tool context for agent edits.
- [Structured canvas outputs make agent edits inspectable and editable](../concepts/structured-canvas-outputs-make-agent-edits-inspectable-and-editable.md) - structured editor objects keep visual agent outputs modifiable rather than flattened into pixels.
- [Hackable agent runtimes need tight safety boundaries](../concepts/hackable-agent-runtimes-need-tight-safety-boundaries.md) - executable editor or browser access needs stricter controls than ordinary shape or API tools.
- [Route high-impact agent actions through explicit human approval gates](../concepts/route-high-impact-agent-actions-through-explicit-human-approval-gates.md) - approval steps keep sensitive tool execution outside model-only control.
- [Use tool names and descriptions as operational prompts](../concepts/use-tool-names-and-descriptions-as-operational-prompts.md) - clear tool metadata improves selection and enables local tool-specific guidance.
- [Evaluate tool definitions and outputs as context](../concepts/evaluate-tool-definitions-and-outputs-as-context.md) - agent-facing tools need model-shaped schemas and output formats.
- [VoiceVision agents wrap visual RAG with retrieval, image-reading, and speech tools](../concepts/voicevision-agents-wrap-visual-rag-with-retrieval-image-reading-and-speech-tools.md) - retrieval, image-reader, and speech tools can keep visual-document workflows inspectable inside an agent.
- [Build AI product iteration tools into the product context](../concepts/build-ai-product-iteration-tools-into-the-product-context.md) - behavior tooling should run where real user and teammate context is available.
- [Browser agents sit in the prompt-injection lethal trifecta](../concepts/browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md) - browser tool design must account for private data, untrusted content, and external action channels.
- [Human approval can hide tool-description and parameter risk](../concepts/human-approval-can-hide-tool-description-and-parameter-risk.md) - tool approval UX should reveal hidden instructions and sensitive parameters.
- [LLM guardrails need checkpoints at every untrusted boundary](../concepts/llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md) - tool descriptions and tool calls are guardrail checkpoints, not trusted implementation detail.
- [Expose explicit control signals for generative media models](../concepts/expose-explicit-control-signals-for-generative-media-models.md) - image and video tools should expose structured controls when text alone is too imprecise.
- [Use LLMs to generate compiler lowerings under verification](../concepts/use-llms-to-generate-compiler-lowerings-under-verification.md) - LLM code generation is safer when constrained to reusable compiler primitives and checked by the compiler pipeline.
- [Expose local and open-source models through familiar API clients](../concepts/expose-local-and-open-source-models-through-familiar-api-clients.md) - familiar client contracts reduce tool churn across local, remote, and compiled model runtimes.
- [Split large automation surfaces into specialized subagents and subworkflows](../concepts/split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md) - subworkflows and specialist agents keep large tool surfaces manageable.
- [Delegate complex voice-agent tasks through specialist tools and handoffs](../concepts/delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md) - voice systems should route harder tool or policy decisions to specialists while preserving context.
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](../concepts/agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md) - agent-facing products need machine-friendly control surfaces, not only human dashboards.
- [Separate agent harnesses from generated-code execution](../concepts/separate-agent-harnesses-from-generated-code-execution.md) - generated code should execute away from the trusted agent harness.
- [Agent tool loops turn model-required actions into executable results](../concepts/agent-tool-loops-turn-model-required-actions-into-executable-results.md) - tool runtimes need to turn model-selected functions into validated execution and structured results.
- [Use Bash as a composable code-mode tool for agents](../concepts/use-bash-as-a-composable-code-mode-tool-for-agents.md) - command-line access can compose existing software and verification artifacts.
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](../concepts/layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md) - powerful tools need guardrails at model, harness, parser, and sandbox layers.
- [Use hooks for deterministic agent verification and live context injection](../concepts/use-hooks-for-deterministic-agent-verification-and-live-context-injection.md) - event hooks can check tool effects and add changed state.
- [Model LLM calls and tools as durable activities](../concepts/model-llm-calls-and-tools-as-durable-activities.md) - tool calls that touch LLMs or external APIs need retry, timeout, and persistence boundaries in production.
- [Use resumable streams as the UI boundary for durable agents](../concepts/use-resumable-streams-as-the-ui-boundary-for-durable-agents.md) - streaming tool output should remain connected to inspectable backend step traces.
- [Keep workflow orchestration deterministic and put side effects in steps](../concepts/keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md) - tool side effects should be isolated from rerunnable workflow code.
- [Agent skills should point to current docs instead of embedding every API detail](../concepts/agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md) - skills should stay stable while fast-changing API detail stays in current docs.
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](../concepts/realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md) - streaming sessions can combine live input, transcriptions, and grounding tools.
- [Constrain sensitive file access with purpose-built tools](../concepts/constrain-sensitive-file-access-with-purpose-built-tools.md) - narrow operations keep secrets out of model context and logs.
- [Agent rules should emerge from observed off-rail behavior](../concepts/agent-rules-should-emerge-from-observed-off-rail-behavior.md) - rules, checks, and hooks are tool-context controls that should be grounded in local agent failures.
- [Cross-app access centralizes MCP authentication through the identity provider](../concepts/cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md) - IdP-mediated trust can make enterprise MCP access less repetitive and more governable.
- [Short-lived IdP-derived tokens reduce standing MCP access](../concepts/short-lived-idp-derived-tokens-reduce-standing-mcp-access.md) - short token lifetimes tie MCP access to active SSO sessions.
- [Identify the human subject behind agent actions](../concepts/identify-the-human-subject-behind-agent-actions.md) - tool policy needs a subject to bind delegated actions and audit records.
- [Vault and exchange tokens for scoped upstream agent access](../concepts/vault-and-exchange-tokens-for-scoped-upstream-agent-access.md) - token vaults keep delegated API scopes managed outside model context.
- [Model MCP servers as OAuth clients in downstream API chains](../concepts/model-mcp-servers-as-oauth-clients-in-downstream-api-chains.md) - MCP servers may need their own OAuth client identity when mediating upstream APIs.
- [Cross-app access does not replace authorization policy](../concepts/cross-app-access-does-not-replace-authorization-policy.md) - authentication centralization should not be mistaken for fine-grained tool authorization.
- [MCP gateways create an enterprise root of trust](../concepts/mcp-gateways-create-an-enterprise-root-of-trust.md) - a gateway gives enterprise MCP a shared auth, authorization, observability, connectivity, and deployment layer.
- [Enterprise AI asset registries connect governance to runtime lineage](../concepts/enterprise-ai-asset-registries-connect-governance-to-runtime-lineage.md) - registries link use cases to MCP servers, A2A agents, models, owners, environments, auth, and cost.
- [A2A agent registries make deployed agents discoverable through agent cards](../concepts/a2a-agent-registries-make-deployed-agents-discoverable-through-agent-cards.md) - agent cards provide a standard discovery contract for reusable deployed agents.
- [Blueprint repositories standardize MCP and A2A service delivery](../concepts/blueprint-repositories-standardize-mcp-and-a2a-service-delivery.md) - templates and CI/CD can package platform requirements while publishing registry metadata.
- [Gateway platform primitives let teams focus on MCP business logic](../concepts/gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md) - shared platform primitives let domain teams build workflow-specific servers without reimplementing the control plane.
- [Decouple agent harnesses from enterprise data layers](../concepts/decouple-agent-harnesses-from-enterprise-data-layers.md) - gateways keep new agent clients from binding directly to every internal MCP server and data source.
- [MCP tool surfaces need default context budgets](../concepts/mcp-tool-surfaces-need-default-context-budgets.md) - broad tool catalogs need context-aware defaults and compact outputs.
- [Design MCP servers as agent products](../concepts/design-mcp-servers-as-agent-products.md) - product thinking keeps MCP surfaces focused on agent workflows rather than transport mechanics.
- [Translate API endpoints into agent stories](../concepts/translate-api-endpoints-into-agent-stories.md) - server-side outcome tools prevent agents from acting as brittle glue over low-level endpoints.
- [Secure MCP servers by shrinking the agent-visible surface](../concepts/secure-mcp-servers-by-shrinking-the-agent-visible-surface.md) - production MCP security starts with fewer tools, constrained inputs, clear descriptions, minimal outputs, and scoped permissions.
- [Adapt third-party MCP servers to the agent workflow](../concepts/adapt-third-party-mcp-servers-to-the-agent-workflow.md) - generic public MCP servers need local curation before they become reliable agent product surfaces.
- [Wrap generic tool descriptions with use-case guidance](../concepts/wrap-generic-tool-descriptions-with-use-case-guidance.md) - wrappers can keep upstream tool behavior while replacing generic descriptions with local workflow guidance.
- [Enforce deterministic guardrails around sensitive tool calls](../concepts/enforce-deterministic-guardrails-around-sensitive-tool-calls.md) - tool wrappers should enforce hard boundaries before invoking sensitive operations.
- [Move mandatory brittle tool steps outside the agent loop](../concepts/move-mandatory-brittle-tool-steps-outside-the-agent-loop.md) - fixed setup steps can be direct function calls instead of model-selected actions.
- [Move production MCP from API keys to scoped OAuth token flows](../concepts/move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md) - remote MCP should move away from long-lived unscoped API keys toward OAuth 2.1, PKCE, token exchange, and CIMD.
- [Govern MCP tool calls with tool-level policy and end-to-end traces](../concepts/govern-mcp-tool-calls-with-tool-level-policy-and-end-to-end-traces.md) - enterprise MCP needs tool/resource-level policy, masking, interaction logs, and traces across the full request path.
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](../concepts/agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md) - agent connectivity choices should match local execution, remote semantics, governance, and guidance needs.
- [MCP applications ship UI and tools together](../concepts/mcp-applications-ship-ui-and-tools-together.md) - MCP can expose both human-rendered interfaces and model-callable tools from the same server.
- [Ship skills over MCP for server-authored tool guidance](../concepts/ship-skills-over-mcp-for-server-authored-tool-guidance.md) - large MCP servers can ship updatable usage guidance with the integration.
- [Discover large API tool surfaces progressively](../concepts/discover-large-api-tool-surfaces-progressively.md) - broad API surfaces should be discovered on demand instead of loaded as one huge MCP context payload.
- [Expose large APIs through typed code mode](../concepts/expose-large-apis-through-typed-code-mode.md) - generated SDK types can make many endpoints available through compact code-oriented context.
- [Treat AI-generated code as untrusted code](../concepts/treat-ai-generated-code-as-untrusted-code.md) - generated tool implementations need runtime boundaries because model intent is not a security boundary.
- [Run agent-written API code inside programmable sandboxes](../concepts/run-agent-written-api-code-inside-programmable-sandboxes.md) - code-mode tools need isolation, network controls, secret boundaries, and rate limits.
- [Capability-based sandboxes start with no authority](../concepts/capability-based-sandboxes-start-with-no-authority.md) - generated-code runtimes should receive explicit task-scoped capabilities instead of broad ambient access.
- [Choose isolates or containers by generated-code workload](../concepts/choose-isolates-or-containers-by-generated-code-workload.md) - runtime choice should follow whether a generated tool needs only bindings or a full OS-like environment.
- [Encode agent intent into server-side tools](../concepts/encode-agent-intent-into-server-side-tools.md) - tools can hide multi-call service choreography behind a more reliable agent intent.
- [Filter MCP tools by scopes and step-up authorization](../concepts/filter-mcp-tools-by-scopes-and-step-up-authorization.md) - scopes and OAuth challenges can shrink tool exposure while preserving workflow continuity.
- [Stateless remote MCP servers rebuild allowed tools per request](../concepts/stateless-remote-mcp-servers-rebuild-allowed-tools-per-request.md) - remote MCP servers can scale by deriving the allowed tool set on each request.
- [Treat prompts as distributed harness surfaces](../concepts/treat-prompts-as-distributed-harness-surfaces.md) - rules, skills, lints, PR comments, and tests can act as agent-steering tool surfaces.
- [Deep research agents need planning, grounded evidence, and pivot loops](../concepts/deep-research-agents-need-planning-grounded-evidence-and-pivot-loops.md) - research tools should support search, inspection, citation, and synthesis.
- [Split exploratory research agents from constrained writing workflows](../concepts/split-exploratory-research-agents-from-constrained-writing-workflows.md) - Markdown artifacts can be the tool boundary between agentic and deterministic phases.
- [Agentic retrieval lets models plan search steps](../concepts/agentic-retrieval-lets-models-plan-search-steps.md) - retrieval can be exposed as tools an agent chooses and sequences.
- [Structure-aware document parsing improves RAG chunk quality](../concepts/structure-aware-document-parsing-improves-rag-chunk-quality.md) - document parsing settings are practical tool controls for retrieval quality.
- [Standardize development environments around common model priors](../concepts/standardize-development-environments-around-common-model-priors.md) - conventional toolchains give agents more reliable operational patterns.
- [Make validation fast, local, deterministic, and actionable](../concepts/make-validation-fast-local-deterministic-and-actionable.md) - validation commands are agent tools when they produce fast repairable feedback.
- [Use one-shot app builders for product ideation](../concepts/use-one-shot-app-builders-for-product-ideation.md) - prompt-to-app surfaces can make UI and workflow ideas runnable quickly.
- [Infer full-stack app infrastructure from user intent](../concepts/infer-full-stack-app-infrastructure-from-user-intent.md) - app builders can hide backend and integration choices behind user intent.
- [Ground generated media with current search context](../concepts/ground-generated-media-with-current-search-context.md) - search grounding can be a media-generation tool, not only a text-answering tool.

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
- Which agent-facing MCP tools should be collapsed into coarse-grained outcome operations before the server is exposed remotely?
- Which MCP deployments should prefer DCR, CIMD, or an enterprise gateway for client identity management?
- Which fields in MCP tool responses should be masked, summarized, or withheld from model context by default?
- Which tool calls should be collapsed into intent-level server tools instead of exposed as separate low-level operations?
- When should a large API prefer CLI discovery, tool search, typed code mode, or hand-authored MCP tools?
- Which generated-code actions are safe enough for code mode, and which require a fixed tool or approval gate?
- Which image and video controls should appear as explicit user-facing tool parameters rather than hidden prompt instructions?
- Which research artifacts should be preserved as files so later tools can audit provenance?
- Which open-model runtimes and fine-tuning tools need first-class support before a model release is usable by the target developer community?
- Which MCP applications need web-client rendering support before they are useful, and which should remain tool-only integrations?
- Which guidance belongs in server-authored skills over MCP instead of client-local skills?
- Which lint messages or CI comments are important enough to be treated as first-class prompt surfaces?
- Which browser-controlled workflows should be replaced by direct CLIs or APIs for agent accuracy?
- Which registry metadata fields should be mandatory before an MCP server or A2A agent can be discovered by production agents?
- Which RAG internals should be editable in visual flows, and which should remain fixed behind a stable API or MCP server?
- Which prompt-format decisions belong in DSPy adapters versus task signatures or higher-level program logic?

## Sources

- [The Next Unicorns: 7 Top AI startups from the HF0 Residency](../sources/20250821_L8-5ezsoI5A.md)
- [Form factors for your new AI coworkers - Craig Wattrus, Flatfile](../sources/20250822_CiMVKnX-CNI.md)
- [Your Support Team Should Ship Code - Lisa Orr, Zapier](../sources/20251216_RmJ4rTLV_x4.md)
- [Compilers in the Age of LLMs - Yusuf Olokoba, Muna](../sources/20251124_q2nHsJVy4FE.md)
- [Hacking Subagents Into Codex CLI - Brian John, Betterup](../sources/20251124_5eJqXtevlXg.md)
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md)
- [Agentic Engineering: Working With AI, Not Just Using It - Brendan O'Leary](../sources/20260407_BEKc4P87XKo.md)
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](../sources/20251208_CEvIs9y1uog.md)
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
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md)
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md)
- [Paperclip: Open Source Human Control Plane for AI Labor - Dotta Bippa](../sources/20260415_h403btjldDQ.md)
- [One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca](../sources/20260410_VXfRt_H-V08.md)
- [Developer Experience in the Age of AI Coding Agents - Max Kanat-Alexander, Capital One](../sources/20251223_rT2Del5pwg4.md)
- [Judge the Judge: Building LLM Evaluators That Actually Work with GEPA - Mahmoud Mabrouk, Agenta AI](../sources/20260410_X4dEHRzBLmc.md)
- [AI Didn't Kill the Web, It Moved in! - Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)](../sources/20260410_XZ0boOjtbNo.md)
- [OpenRAG: An open-source stack for RAG - Phil Nash](../sources/20260408_4TxOBhDRRCM.md)
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md)
- [Why, and how you need to sandbox AI-Generated Code? - Harshil Agrawal, Cloudflare](../sources/20260408_AHtGAgQ0Q_Q.md)
- [Building in the Gemini Era - Kat Kampf & Ammaar Reshi, Google DeepMind](../sources/20251215_fgkXEIbZpGc.md)
- [Your Insecure MCP Server Won't Survive Production - Tun Shwe, Lenses](../sources/20260408_BurJvbqFr4c.md)
- [Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz](../sources/20260408_U00AOI1eJUE.md)
- [Platforms for Humans and Machines: Engineering for the Age of Agents - Juan Herreros Elorza](../sources/20260408_cCRO3ChaYhM.md)
- [Cognitive Exhaust Fumes, or: Read-Only AI Is Underrated - Simon Podhajsky, Head of AI, Waypoint](../sources/20260408_u0TOSBbAw7c.md)
- [DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](../sources/20260108_-cKUW6n8hBU.md)
- [Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0](../sources/20260114_VSdV-AdSlis.md)
- [Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect](../sources/20260112_96G7FLab8xc.md)
- [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](../sources/20260112_k8cnVCMYmNc.md)
- [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro](../sources/20260109_HY_JyxAZsiE.md)
- [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](../sources/20260106_kmV-qg4uoNI.md)
- [Claude Agent SDK [Full Workshop] - Thariq Shihipar, Anthropic](../sources/20260105_TqC1qOfiVcQ.md)
- [Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)](../sources/20251230_xz0-brt56L8.md)
- [Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code](../sources/20251222_gvIAkmZUEZY.md)
- [The 3 Pillars of Autonomy - Michele Catasta, Replit](../sources/20251222_MLhAA9yguwM.md)
- [From Arc to Dia: Lessons learned building AI Browsers - Samir Mody, The Browser Company of New York](../sources/20251219_o4scJaQgnFA.md)
- [RL Environments at Scale - Will Brown, Prime Intellect](../sources/20251209__IzZWeuTx7I.md)
- [2026: The Year The IDE Died - Steve Yegge & Gene Kim, Authors, Vibe Coding](../sources/20251206_7Dtu2bilcFs.md)
- [VoiceVision RAG - Integrating Visual Document Intelligence with Voice Response - Suman Debnath, AWS](../sources/20251206_hwCmfThIiS4.md)
- [Future-Proof Coding Agents - Bill Chen & Brian Fioca, OpenAI](../sources/20251205_wVl6ZjELpBk.md)
- [Defying Gravity - Kevin Hou, Google DeepMind](../sources/20251202_HN-F-OQe6j0.md)
- [Katelyn Lesse - Evolving Claude APIs for Agents, Anthropic](../sources/20251204_aqW68Is_Kj4.md)
- [Context Engineering: Connecting the Dots with Graphs - Stephen Chin, Neo4j](../sources/20251124_LLuKshphGOE.md)
- [Five hard earned lessons about Evals - Ankur Goyal, Braintrust](../sources/20250823_a4BV0gGmXgA.md)
- [Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents - Alex Gavrilescu, Funstage](../sources/20251124_zMXKhhwiCIc.md)

- [Infra that fixes itself, thanks to coding agents - Mahmoud Abdelwahab, Railway](../sources/20251124_Q5IVm_CxN2w.md)
