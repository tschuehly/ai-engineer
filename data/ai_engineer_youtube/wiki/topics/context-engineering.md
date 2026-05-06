# Context Engineering

## Overview

Personal-agent context can be made visible through nested topic descriptions and explicit attachments rather than only opaque memory. When a workspace lets the user attach the relevant document, knowledge base, password, or skill to the current task, the context contract is easier to inspect and debug than a hidden retrieval decision.

Context engineering treats prompts, skills, memory, retrieval, and documentation as an engineered substrate for agent work. It needs a lifecycle similar to software delivery: generate context, evaluate it, distribute it, observe its use, and adapt it from feedback. Demand-driven context adds a practical enterprise workflow: rather than predicting every context need upfront, assign real work to agents, observe failures, and convert missing institutional knowledge into reusable context blocks. Personal knowledge bases show the same pattern at individual scale: Markdown notes, bookmarks, project records, search, and memory become useful agent context when ingestion flows add tags, connections, and surfacing rather than merely storing links. Read-only personal intelligence adds a useful variant: emails, journals, tasks, browser history, notes, and relationship data can be synthesized into reflection artifacts without mutating source systems. A context engine is the selection and reasoning layer for this substrate: it should combine task relevance, user and team signals, source relationships, permissions, and conflict handling rather than relying on generic RAG, many MCP servers, or larger context windows alone. For productized codegen, current Markdown docs, shared domain glossaries, and compact exemplar projects can offset stale model knowledge and weak architectural priors; context can be generated from a service into skill references and loaded only when the task requires it. Conversational-agent state adds a related context-management concern: server-side interaction IDs can simplify continuation and branching, but retention, retrieval, and compaction limits remain part of the application design. Small-model preprocessing can further manage context by filtering, classifying, extracting, or reranking data before it reaches the agent. Skills and context packages distribute reusable workflow guidance, but package-like reuse also creates versioning, dependency, quality, and security concerns; volatile API facts should often stay in current documentation that skills point to rather than being copied into every skill.

Product engineering adds a customer-context layer to this problem. If AI handles more of the mechanical implementation, engineers need searchable customer conversations, tagged feedback, recorded calls, and direct customer channels so product judgment is grounded in real needs rather than abstract feature requests.

## Key Concepts

- [Enterprise agent failures often expose missing institutional knowledge](../concepts/enterprise-agent-failures-expose-missing-institutional-knowledge.md) - agent failures can indicate missing or stale enterprise knowledge rather than weak model reasoning.
- [Encode domain judgment in node-level agent skills](../concepts/encode-domain-judgment-in-node-level-agent-skills.md) - skills can carry expert contingencies into the specific work-tree node where they apply.
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - real tasks reveal the exact context that needs to be documented.
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](../concepts/context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md) - reusable knowledge units make enterprise context easier for agents to retrieve and apply.
- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - connector output should be judged by its contribution to task completion.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - preprocessing, filtering, and extraction can reduce context rot before context reaches the agent.
- [Agent skills package progressive-disclosure context for repeatable workflows](../concepts/agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) - skill metadata can keep initial context small while making deeper instructions discoverable.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - context engines should personalize and narrow organizational context for the current task.
- [Surface unresolved context conflicts to agents and users](../concepts/surface-unresolved-context-conflicts-to-agents-and-users.md) - unresolved contradictions should become explicit handoff points rather than hidden guesses.
- [Do not cache context-engine answers as durable truth](../concepts/do-not-cache-context-engine-answers-as-durable-truth.md) - generated answers can become stale or self-reinforcing if reused as canonical context.
- [Use social and expert graphs to personalize coding-agent context](../concepts/use-social-and-expert-graphs-to-personalize-coding-agent-context.md) - reviewer and contribution graphs can help route context to likely owners and experts.
- [Product engineers need direct customer context](../concepts/product-engineers-need-direct-customer-context.md) - customer feedback, calls, and channels are product context for AI-assisted engineering decisions.
- [Context development lifecycle treats context as an engineered artifact](../concepts/context-development-lifecycle-treats-context-as-an-engineered-artifact.md) - context should move through generate, evaluate, distribute, observe, and adapt loops.
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](../concepts/evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md) - prompt and skill changes need validation because small context edits can change generated behavior.
- [Package reusable context as skills, libraries, and registries](../concepts/package-reusable-context-as-skills-libraries-and-registries.md) - shared context needs package, registry, dependency, and security practices.
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
- [Model airplanes give coding agents token-efficient exemplars](../concepts/model-airplanes-give-coding-agents-token-efficient-exemplars.md) - flattened reference projects can act as reusable, searchable skill context.
- [Encode non-functional requirements as agent-visible context](../concepts/encode-non-functional-requirements-as-agent-visible-context.md) - durable quality expectations help agents reproduce team judgment.
- [Treat prompts as distributed harness surfaces](../concepts/treat-prompts-as-distributed-harness-surfaces.md) - long-running work needs context refreshed through multiple instruction channels.
- [Guard AI-assisted platform contributions with policy and context](../concepts/guard-ai-assisted-platform-contributions-with-policy-and-context.md) - platform contribution guidance belongs in agent-readable Markdown when hard policy alone is not enough.
- [Collaborative plans become executable agent context](../concepts/collaborative-plans-become-executable-agent-context.md) - shared plans and discussion can become prompt context once teammates agree on intent.
- [Social context dashboards keep agentic teams oriented](../concepts/social-context-dashboards-keep-agentic-teams-oriented.md) - code-adjacent conversations and teammate activity can orient agents and humans.
- [Use PRDs to align agents on the design concept](../concepts/use-prds-to-align-agents-on-the-design-concept.md) - generated plans are useful when they capture current shared intent and decisions.
- [Maintain ubiquitous language for AI coding](../concepts/maintain-ubiquitous-language-for-ai-coding.md) - a shared glossary is compact context for domain terms used by humans, code, and agents.
- [Retire completed planning docs before they become agent doc rot](../concepts/retire-completed-planning-docs-before-they-become-agent-doc-rot.md) - stale planning artifacts can become harmful context for later agents.
- [Surface existing company information before redesigning processes](../concepts/surface-existing-company-information-before-redesigning-processes.md) - scattered Slack, meeting, issue, and update signals can be made usable as agent context.

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

## Sources

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
