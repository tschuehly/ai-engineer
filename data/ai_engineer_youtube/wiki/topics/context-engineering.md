# Context Engineering

## Overview

Personal-agent context can be made visible through nested topic descriptions and explicit attachments rather than only opaque memory. When a workspace lets the user attach the relevant document, knowledge base, password, or skill to the current task, the context contract is easier to inspect and debug than a hidden retrieval decision.

Context engineering treats prompts, skills, memory, retrieval, and documentation as an engineered substrate for agent work. It needs a lifecycle similar to software delivery: generate context, evaluate it, distribute it, observe its use, and adapt it from feedback. Demand-driven context adds a practical enterprise workflow: rather than predicting every context need upfront, assign real work to agents, observe failures, and convert missing institutional knowledge into reusable context blocks. Personal knowledge bases show the same pattern at individual scale: Markdown notes, bookmarks, project records, search, and memory become useful agent context when ingestion flows add tags, connections, and surfacing rather than merely storing links. Read-only personal intelligence adds a useful variant: emails, journals, tasks, browser history, notes, and relationship data can be synthesized into reflection artifacts without mutating source systems. A context engine is the selection and reasoning layer for this substrate: it should combine task relevance, user and team signals, source relationships, permissions, and conflict handling rather than relying on generic RAG, many MCP servers, or larger context windows alone. For productized codegen, current Markdown docs, shared domain glossaries, and compact exemplar projects can offset stale model knowledge and weak architectural priors; context can be generated from a service into skill references and loaded only when the task requires it. Conversational-agent state adds a related context-management concern: server-side interaction IDs can simplify continuation and branching, but retention, retrieval, and compaction limits remain part of the application design. Small-model preprocessing can further manage context by filtering, classifying, extracting, or reranking data before it reaches the agent. Skills and context packages distribute reusable workflow guidance, but package-like reuse also creates versioning, dependency, quality, and security concerns; volatile API facts should often stay in current documentation that skills point to rather than being copied into every skill.

Product engineering adds a customer-context layer to this problem. If AI handles more of the mechanical implementation, engineers need searchable customer conversations, tagged feedback, recorded calls, and direct customer channels so product judgment is grounded in real needs rather than abstract feature requests.

Prompt-learning workflows show a narrower context loop: when traces or datasets include explanatory feedback from subject-matter experts or evaluators, that text becomes context for improving the next system prompt. Bare labels are less reusable because they do not identify the missed instruction, missing context, or rule violation that future prompts should address.

Agentic context optimization should not be treated as one universal loop. Meta-adaptive context engineering frames context reflection as one strategy among several: a task profile can choose minimal context for simple work, AC-style reflection for incremental context updates, structured memory retrieval for hard tasks, or verification and extra compute when feedback is weak. That framing challenges a context-only optimization instinct: sometimes the right fix is less context, more execution checking, or a different resource allocation.

For coding agents, the same loop can target repository or agent rule files directly: benchmark traces, unit-test results, and judge explanations can be fed into a meta-prompt that writes learned instructions for the next run. AI-native company workflows add a team-level version of the context loop. Lessons from delegated agent work can be codified into `CLAUDE.md`-style files, subagents, slash commands, prompt libraries, and onboarding guidance so tacit conventions become reusable agent-readable context rather than private memory.

Long context should be treated as temporary working memory, not durable knowledge. Large prompts can keep a model from outright lacking a document, but attention cost, latency, and context-rot behavior mean "fits in the window" is weaker than "the model can reason over it reliably." For stable long-tail knowledge, the design choice may move from prompt stuffing to retrieval, contextual embeddings, or model adaptation.

Context platform engineering adds an inference-side complement to context selection. Agentic coding sessions often resend system prompts, tool calls, and tool responses far more than direct user text, so context engineering should consider which repeated regions become KV-cache working sets and how cache time-to-live interacts with human pauses and fast tool loops.

Tool-heavy agent sessions also need active cleanup inside the working window. Memory can keep durable patterns and preferences outside the prompt until they are relevant, while context editing removes stale tool outputs that otherwise crowd out current task context. Knowledge graphs add a structured memory option when relationships matter: semantic and procedural learnings can become nodes, relationships, properties, embeddings, and access overlays that agents can traverse and humans can inspect.

Coding-agent subagents are another context-management lever. Instead of forcing one agent to spend its main window on broad repository search, deep reasoning, dependency lookup, or codemod planning, a specialist can consume context in a separate window and return only the useful result.

Context compression for coding agents is not just about fitting files into a smaller prompt. Nations' Netflix example shows that a multi-million-token codebase can be reduced into a research document and implementation plan only after humans select relevant architecture, diagrams, interfaces, requirements, and sometimes a manual migration seed. The goal is to distinguish intended design constraints from accidental local patterns before generation preserves both as if they were requirements.

Proactive agents add a timing constraint to context engineering. A background coding agent needs current project observation, personalized preferences, repository and environment knowledge, editable memory, and just-in-time task context so it can consult the right guidance before interrupting the user. Context that arrives too soon becomes noise, while context that arrives too late misses the intervention window.

AI code review turns context quality into a trust issue. Review and generation tools need access to the relevant standards, best practices, version history, PR history, organizational logs, and current code context; otherwise developers can distrust the LLM's judgment even when the model is capable.

Frequent intentional compaction is a coding-specific context-engineering workflow. It treats the active context window as a limited, trajectory-sensitive working area: preserve correct current facts and intent in reviewed Markdown artifacts, start fresh sessions from those artifacts, and prefer on-demand compressed context from current code over broad static onboarding docs that grow stale. Per-feature context packaging adds a planning-artifact variant of the same idea: after a master specification, feature inventory, specifications, dependencies, and implementation plan exist, the implementation agent should receive only the sections relevant to the current atomic feature plus its dependencies and validation strategy.

Architecture copilots add a system-map version of context engineering. Instead of relying on stale architecture docs, they normalize current cloud, Kubernetes, service, logging, dependency, drift, business-objective, and standards context into a live model that an AI can use for architecture recommendations.

Repository architecture can turn context engineering into the adoption bottleneck for coding agents. In PR telemetry, highly distributed codebases did not show the same AI-adoption-to-throughput lift as centralized or balanced codebases, plausibly because tools and agents operate best inside one repository while product, service, and ownership relationships span many repositories and remain undocumented.

## Key Concepts

- [Keep agent context small, fresh, and task-specific](../concepts/keep-agent-context-small-fresh-and-task-specific.md) - context should be externalized, selected, summarized, and isolated so stale or excessive history does not degrade agent work.
- [Frequent intentional compaction keeps coding agents in the smart zone](../concepts/frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md) - source-backed compaction controls size, correctness, completeness, and trajectory in coding-agent sessions.
- [Assemble Per-Feature Context Packages for Coding Agents](../concepts/assemble-per-feature-context-packages-for-coding-agents.md) - planning artifacts should be sliced into feature-specific context packages before implementation.
- [Proactive agent systems need observation, personalization, timing, and workflow embedding](../concepts/proactive-agent-systems-need-observation-personalization-timing-and-workflow-embedding.md) - proactive agents need context selected for the current moment and workflow surface.
- [Use subagents to isolate context-heavy subtasks](../concepts/use-subagents-to-isolate-context-heavy-subtasks.md) - separate context windows can preserve the main agent's working memory.
- [Agent swarms create reusable KV-cache working sets](../concepts/agent-swarms-create-reusable-kv-cache-working-sets.md) - repeated prompt and tool regions in agent swarms should be treated as cacheable context infrastructure.
- [Offload long-horizon agent state outside the context window](../concepts/offload-long-horizon-agent-state-outside-the-context-window.md) - files, plans, docs, memories, and scoped subagents can hold state until it is relevant.
- [Context window editing clears stale tool results](../concepts/context-window-editing-clears-stale-tool-results.md) - old tool outputs should be pruned when they stop helping the current task.
- [Enterprise agent failures often expose missing institutional knowledge](../concepts/enterprise-agent-failures-expose-missing-institutional-knowledge.md) - agent failures can indicate missing or stale enterprise knowledge rather than weak model reasoning.
- [Encode domain judgment in node-level agent skills](../concepts/encode-domain-judgment-in-node-level-agent-skills.md) - skills can carry expert contingencies into the specific work-tree node where they apply.
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - real tasks reveal the exact context that needs to be documented.
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](../concepts/context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md) - reusable knowledge units make enterprise context easier for agents to retrieve and apply.
- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - connector output should be judged by its contribution to task completion.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - preprocessing, filtering, and extraction can reduce context rot before context reaches the agent.
- [Agent skills package progressive-disclosure context for repeatable workflows](../concepts/agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) - skill metadata can keep initial context small while making deeper instructions discoverable.
- [Skills turn procedural feedback into transferable agent memory](../concepts/skills-turn-procedural-feedback-into-transferable-agent-memory.md) - skill updates can preserve repeatable procedural lessons without treating all context as memory.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - context engines should personalize and narrow organizational context for the current task.
- [Active repos per engineer exposes context architecture drag](../concepts/active-repos-per-engineer-exposes-context-architecture-drag.md) - repository distribution can make cross-repo context the blocker for AI coding gains.
- [Live architecture digital twins ground architecture copilots](../concepts/live-architecture-digital-twins-ground-architecture-copilots.md) - architecture context should reflect deployed reality, not only documentation.
- [Surface unresolved context conflicts to agents and users](../concepts/surface-unresolved-context-conflicts-to-agents-and-users.md) - unresolved contradictions should become explicit handoff points rather than hidden guesses.
- [Do not cache context-engine answers as durable truth](../concepts/do-not-cache-context-engine-answers-as-durable-truth.md) - generated answers can become stale or self-reinforcing if reused as canonical context.
- [Use social and expert graphs to personalize coding-agent context](../concepts/use-social-and-expert-graphs-to-personalize-coding-agent-context.md) - reviewer and contribution graphs can help route context to likely owners and experts.
- [Product engineers need direct customer context](../concepts/product-engineers-need-direct-customer-context.md) - customer feedback, calls, and channels are product context for AI-assisted engineering decisions.
- [Context development lifecycle treats context as an engineered artifact](../concepts/context-development-lifecycle-treats-context-as-an-engineered-artifact.md) - context should move through generate, evaluate, distribute, observe, and adapt loops.
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](../concepts/evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md) - prompt and skill changes need validation because small context edits can change generated behavior.
- [Route agent optimization by task profile, not one fixed loop](../concepts/route-agent-optimization-by-task-profile-not-one-fixed-loop.md) - context reflection should be chosen only when the task profile calls for it.
- [Package reusable context as skills, libraries, and registries](../concepts/package-reusable-context-as-skills-libraries-and-registries.md) - shared context needs package, registry, dependency, and security practices.
- [Treat complex skills like software artifacts](../concepts/treat-complex-skills-like-software-artifacts.md) - executable and dependency-heavy skills need eval, version, and lineage practices.
- [Use agent logs and review feedback as context observability signals](../concepts/use-agent-logs-and-review-feedback-as-context-observability-signals.md) - logs, reviews, and production failures should feed durable context improvements.
- [Filter untrusted context before it reaches the agent](../concepts/filter-untrusted-context-before-it-reaches-the-agent.md) - repository and marketplace context needs screening before model ingestion.
- [Aggregated personal context creates mosaic and exfiltration risk](../concepts/aggregated-personal-context-creates-mosaic-and-exfiltration-risk.md) - aggregated read-only sources can still reveal sensitive composites and leak through remaining communication paths.
- [Personal knowledge bases become agent context substrates](../concepts/personal-knowledge-bases-become-agent-context-substrates.md) - personal notes and saved links become active context when agents connect them to current work.
- [Cognitive exhaust gains value through cross-source synthesis](../concepts/cognitive-exhaust-gains-value-through-cross-source-synthesis.md) - low-value personal byproducts become useful context when combined across tools.
- [Explicit context attachments can outperform opaque agent memory](../concepts/explicit-context-attachments-can-outperform-opaque-agent-memory.md) - selected topic descriptions and attachments can be easier to inspect and debug than hidden memory lookup.
- [Code-backed content can replace fragile CMS workflows for agents](../concepts/code-backed-content-can-replace-fragile-cms-workflows-for-agents.md) - structured content in code can give agents a reviewable operational source of truth.
- [Server-side interaction state simplifies branching conversational agents](../concepts/server-side-interaction-state-simplifies-branching-conversational-agents.md) - state APIs can reduce context plumbing while preserving explicit retention and compaction responsibilities.
- [Agent skills should point to current docs instead of embedding every API detail](../concepts/agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md) - skills should avoid stale copies of fast-changing documentation.
- [Fresh Markdown context mitigates model rot in codegen](../concepts/fresh-markdown-context-mitigates-model-rot-in-codegen.md) - runtime-selected documentation can update model knowledge without retraining.
- [Context quality determines AI code review trust](../concepts/context-quality-determines-ai-code-review-trust.md) - generation and review tools need broader software-development context to produce trustworthy quality feedback.
- [Model airplanes give coding agents token-efficient exemplars](../concepts/model-airplanes-give-coding-agents-token-efficient-exemplars.md) - flattened reference projects can act as reusable, searchable skill context.
- [Encode non-functional requirements as agent-visible context](../concepts/encode-non-functional-requirements-as-agent-visible-context.md) - durable quality expectations help agents reproduce team judgment.
- [Treat prompts as distributed harness surfaces](../concepts/treat-prompts-as-distributed-harness-surfaces.md) - long-running work needs context refreshed through multiple instruction channels.
- [Agent harnesses combine model, tools, prompts, filesystem, skills, hooks, and memory](../concepts/agent-harnesses-combine-model-tools-prompts-filesystem-skills-hooks-and-memory.md) - files, scripts, tools, hooks, and memory are part of the agent context substrate.
- [Use hooks for deterministic agent verification and live context injection](../concepts/use-hooks-for-deterministic-agent-verification-and-live-context-injection.md) - event hooks can refresh an agent with changed state or enforce recurring context rules.
- [Guard AI-assisted platform contributions with policy and context](../concepts/guard-ai-assisted-platform-contributions-with-policy-and-context.md) - platform contribution guidance belongs in agent-readable Markdown when hard policy alone is not enough.
- [Collaborative plans become executable agent context](../concepts/collaborative-plans-become-executable-agent-context.md) - shared plans and discussion can become prompt context once teammates agree on intent.
- [Social context dashboards keep agentic teams oriented](../concepts/social-context-dashboards-keep-agentic-teams-oriented.md) - code-adjacent conversations and teammate activity can orient agents and humans.
- [Use PRDs to align agents on the design concept](../concepts/use-prds-to-align-agents-on-the-design-concept.md) - generated plans are useful when they capture current shared intent and decisions.
- [Spec-driven development turns prompts into requirements, design, and tasks](../concepts/spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md) - structured spec artifacts can become compact task context for coding agents.
- [Keep spec artifacts feature-scoped, mutable, and context-backed](../concepts/keep-spec-artifacts-feature-scoped-mutable-and-context-backed.md) - specs should be scoped and refreshed so they do not become stale context.
- [Maintain ubiquitous language for AI coding](../concepts/maintain-ubiquitous-language-for-ai-coding.md) - a shared glossary is compact context for domain terms used by humans, code, and agents.
- [Retire completed planning docs before they become agent doc rot](../concepts/retire-completed-planning-docs-before-they-become-agent-doc-rot.md) - stale planning artifacts can become harmful context for later agents.
- [Surface existing company information before redesigning processes](../concepts/surface-existing-company-information-before-redesigning-processes.md) - scattered Slack, meeting, issue, and update signals can be made usable as agent context.
- [Use explanatory feedback to optimize prompts](../concepts/use-explanatory-feedback-to-optimize-prompts.md) - failure explanations become context for prompt revisions.
- [System prompt learning updates agent rules from eval explanations](../concepts/system-prompt-learning-updates-agent-rules-from-eval-explanations.md) - eval explanations can become durable agent-visible rules.
- [Use Compounding Engineering Loops](../concepts/use-compounding-engineering-loops.md) - agent-work lessons should be captured into files, commands, subagents, and onboarding context.
- [Do not treat long context as durable model memory](../concepts/do-not-treat-long-context-as-durable-model-memory.md) - full-context prompting has latency and reasoning limits even when the window is large enough.
- [Knowledge graphs make agent memory traversable and explainable](../concepts/knowledge-graphs-make-agent-memory-traversable-and-explainable.md) - graph memory can preserve relationships, provenance, and access rules outside the raw context window.
- [Long AI coding conversations compound accidental complexity](../concepts/long-ai-coding-conversations-compound-accidental-complexity.md) - stale conversational history can carry wrong architectural turns into later code.
- [Manual migration seeds teach agents the hidden constraints](../concepts/manual-migration-seeds-teach-agents-the-hidden-constraints.md) - manual examples can become high-signal context for later agent research.
- [Treat embeddings as recoverable sensitive data](../concepts/treat-embeddings-as-recoverable-sensitive-data.md) - embeddings are derived context artifacts that still need data-protection controls.
- [Train long-tail knowledge into weights with curated synthetic data](../concepts/train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md) - stable niche knowledge may belong in model adaptation rather than repeated prompt context.

## Open Questions

- What minimum metadata should each context block include so retrieval systems can select it reliably for future tasks?
- How often should teams rescan or revalidate context blocks when source systems change?
- Which context-management tasks should be implemented with deterministic code, retrieval, or small-model inference?
- How should teams decide what belongs in `SKILL.md` versus referenced files or tool descriptions?
- Which parts of a context engine can be cached safely as source-backed structure, and which generated answers must be recomputed from current sources?
- What metadata should context packages expose so teams can evaluate provenance, version compatibility, dependencies, and security risk before installation?
- How should personal knowledge-base agents avoid amplifying stale notes or noisy bookmarks into future context?
- Which personal-agent context should be injected from explicit topic hierarchy versus retrieved from memory?
- When should operational content be moved from a CMS into code so agents can manage it with diffs and review?
- What conversation state should be summarized into durable memory before server-side interaction records expire?
- How should context services decide which examples belong in a generated skill reference versus separate documentation?
- Which team conversations are durable enough to preserve as agent context rather than transient chat?
- Which customer conversations are durable enough to become agent-visible product context without overfitting to one account?
- How should repositories distinguish current implementation guidance from historical planning artifacts?
- Which non-functional requirements are durable enough to become default context for every coding-agent run?
- Which failure explanations should become durable prompt context instead of staying as one-off annotations?
- When should stable long-tail knowledge move from context or retrieval into model weights?
- Which architectural seams require human-written context because raw code makes technical debt look like intended convention?
- When should codebase onboarding context be prewritten, generated on demand, or avoided because source code is the better source of truth?
- Which repeated prompt, tool-call, and tool-response regions should be engineered for KV-cache reuse rather than summarized or regenerated?

## Sources

- [Context Platform Engineering to Reduce Token Anxiety - Val Bercovici, WEKA](../sources/20251124_NTBX-wxUhHs.md)
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases - Dex Horthy, HumanLayer](../sources/20251202_rmvDxxNubIg.md)
- [The Cure for the Vibe Coding Hangover - Corey J. Gallon, Rexmore](../sources/20251124_JsKTQbT58BY.md)
- [Agentic Engineering: Working With AI, Not Just Using It - Brendan O'Leary](../sources/20260407_BEKc4P87XKo.md)
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](../sources/20251208_CEvIs9y1uog.md)
- [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro](../sources/20260109_HY_JyxAZsiE.md)
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md)
- [I Gave an AI Agent the Keys to My Life (Here's What Happened) - Radek Sienkiewicz (@velvetshark-com)](../sources/20260502_sJ2jc7leKBk.md)
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md)
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md)
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md)
- [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment - Maggie Appleton, GitHub](../sources/20260426_ClWD8OEYgp8.md)
- [Full Walkthrough: Workflow for AI Coding - Matt Pocock](../sources/20260424_-QFHIoCo-Ko.md)
- [The End of Apps - Kitze, Sizzy.co](../sources/20260423_4fntwuOoedA.md)
- ["Software Fundamentals Matter More Than Ever" - Matt Pocock](../sources/20260423_v4F1gFy-hqg.md)
- [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../sources/20260422_XNtkiQJ49Ps.md)
- [Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer](../sources/20260421_wjk0ulMAkbc.md)
- [The New Application Layer - Malte Ubl, CTO Vercel](../sources/20260420_XKup1pj-34M.md)
- [Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI](../sources/20260417_am_oeAoUhew.md)
- [Platforms for Humans and Machines: Engineering for the Age of Agents - Juan Herreros Elorza](../sources/20260408_cCRO3ChaYhM.md)
- [Cognitive Exhaust Fumes, or: Read-Only AI Is Underrated - Simon Podhajsky, Head of AI, Waypoint](../sources/20260408_u0TOSBbAw7c.md)
- [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](../sources/20260106_SbcQYbrvAfI.md)
- [The Unreasonable Effectiveness of Prompt Learning - Aparna Dhinakaran, Arize](../sources/20251223_pP_dSNz_EdQ.md)
- [Claude Agent SDK [Full Workshop] - Thariq Shihipar, Anthropic](../sources/20260105_TqC1qOfiVcQ.md)
- [Jack Morris: Stuffing Context is not Memory, Updating Weights is](../sources/20251229_Jty4s9-Jb78.md)
- [Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code](../sources/20251222_gvIAkmZUEZY.md)
- [The 3 Pillars of Autonomy - Michele Catasta, Replit](../sources/20251222_MLhAA9yguwM.md)
- [The Infinite Software Crisis - Jake Nations, Netflix](../sources/20251220_eIoohUmYpGI.md)
- [Dispatch from the Future: building an AI-native Company - Dan Shipper, Every, AI & I](../sources/20251218_MGzymaYBiss.md)
- [Proactive Agents - Kath Korevec, Google Labs](../sources/20251213_v3u8xc0zLec.md)
- [The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo](../sources/20251211_rgjF5o2Qjsc.md)
- [Katelyn Lesse - Evolving Claude APIs for Agents, Anthropic](../sources/20251204_aqW68Is_Kj4.md)
- [Context Engineering: Connecting the Dots with Graphs - Stephen Chin, Neo4j](../sources/20251124_LLuKshphGOE.md)
- [AI Copilots for Tech Architecture: The Highest-ROI Use Case You're Not Building - Boris B., Catio](../sources/20251124_QRWdapxMdSY.md)
- [What Data from 20m Pull Requests Reveal About AI Transformation - Nick Arcolano, Jellyfish](../sources/20251124_WqZq8L-v9pA.md)
- [The Unbearable Lightness of Agent Optimization - Alberto Romero, Jointly](../sources/20251124_zfvEMNmVlNY.md)
