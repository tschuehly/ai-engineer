# Workflows

## Overview

Personal-agent workflows need domain separation and proactive task flow once they move beyond one recurring pain. A single chat can collapse unrelated work and life contexts; multi-topic workspaces preserve context boundaries, show tool progress, and let the agent ask the human for decisions or missing artifacts while background work continues.

Agent workflows become more reliable when they expose a tight loop between work execution, failure observation, missing-context discovery, and documentation updates. Demand-driven context uses that loop to grow enterprise context from real tasks rather than from speculative upfront curation. Production AI application workflows add another loop: stage the agent, trace it, evaluate it on golden cases, deploy managed prompts/tools/scores, monitor production traces, replay failures, and rerun regression checks before promoting fixes. Personal-agent workflows apply the same idea to permissions and trust: start from one recurring pain, add one simple workflow, watch it fail or succeed, then add guardrails before expanding autonomy. Human-in-the-loop automations make those guardrails concrete by pausing sensitive actions for explicit approval, keeping credentials scoped, and logging waiting or resumed executions. Voice-agent workflows need a similar staged design: start with a narrow realtime conversation path, add tools sparingly, preserve context across handoffs, and validate both transcript behavior and audio delivery before expanding coverage. Coding-agent loops apply the same principle to implementation work: keep each run small, make progress observable, and feed defects or process lessons into the next prompt or skill. Product codegen workflows can reduce variation by breadcrumbing the agent through discovery, candidate event design, shared vocabulary, and then implementation, and can use post-run self-interrogation to discover missing tools or contradictory context. AI-amplified product work also needs explicit quality routines: recurring quality reviews train engineers to find small regressions, and zero-bug policies turn defect inflow into immediate triage rather than postponed cleanup. For agentic software work, workflow design should deliberately trade upfront planning against later review effort, should make feedback speed the limit on change size, and should use parallel queues only when the interface preserves human focus around completed work. Parent-agent comparison workflows can run multiple models or strategies in isolated workspaces, then help the user review, rank, and combine the results. Spatial orchestration workflows add filesystem visibility, collision heat maps, agent-discovered quest queues, containerized decomposition, and evidence-rich review bundles so many agent runs can be supervised without constant babysitting. When that workflow is encoded as prompts rather than runtime code, its eval loop must verify both desired work and absence of forbidden side effects. Outside coding, agents are useful when they shorten feedback cycles for collaborators who can hand over natural artifacts, and when they absorb the prerequisite work that otherwise blocks progress. Canvas-native workflows strengthen that artifact handoff by letting users draw, annotate, select, and revise directly on the same surface the agent reads and edits. Multi-agent canvas workflows can also make shared state, leader/follower delegation, overlapping work, and completion review visible rather than hidden in logs. Context-engine workflows should also surface unresolved source conflicts, recompute from current sources when answers may be stale, and route clarification back into durable context. Skill and context-package workflows should be developed like library workflows: define expected behavior, package guidance, evaluate changes, distribute reusable context, observe use through logs and review, then update shared packages when the workflow changes. Ambient-agent workflows add a maintenance loop: overnight indexing, backups, memory refreshes, update validation, cleanup, and notification filtering keep the system ready without forcing the user to watch every operation.

Complex vertical workflows add another design dimension: make ambiguous work more verifiable through decomposition, proxy checks, and guardrails; when uncertainty remains, let agents record reversible decisions instead of blocking on low-context chat questions. Artifact-native surfaces help humans review the specific branch of the work tree where their judgment is needed. AI adoption workflows should also avoid Goodharted usage goals: visible token counts and spend leaderboards can reward performative usage, while effective adoption requires hands-on experimentation against real work.

## Key Concepts

- [Use hosted model playgrounds to prototype before owning infrastructure](../concepts/use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md) - hosted playgrounds can compress the path from idea to model, API, app, and cloud deployment experiment.
- [Do not use token volume as a developer productivity metric](../concepts/do-not-use-token-volume-as-a-developer-productivity-metric.md) - workflow metrics should not reward token generation over useful delivery.
- [AI-amplified shipping speed needs stronger product taste](../concepts/ai-amplified-shipping-speed-needs-stronger-product-taste.md) - AI-assisted workflows need explicit no-saying and root-problem discovery before implementation.
- [Quality Wednesdays train engineers to notice small regressions](../concepts/quality-wednesdays-train-engineers-to-notice-small-regressions.md) - recurring quality review turns product polish into team practice.
- [Zero-bug policies turn bug inflow into immediate work](../concepts/zero-bug-policies-turn-bug-inflow-into-immediate-work.md) - bug workflow should prevent passive backlog accumulation.
- [Product engineers need direct customer context](../concepts/product-engineers-need-direct-customer-context.md) - customer feedback surfaces help engineers steer AI-assisted product work.
- [Practice-driven AI tool fluency beats theory-only adoption](../concepts/practice-driven-ai-tool-fluency-beats-theory-only-adoption.md) - AI workflow competence comes from repeated real-use experimentation.
- [Make agent work more trustworthy by making it verifiable](../concepts/make-agent-work-more-trustworthy-by-making-it-verifiable.md) - workflow design should turn hard-to-review autonomy into checked or constrained subwork.
- [Use decision logs to keep uncertain agents moving](../concepts/use-decision-logs-to-keep-uncertain-agents-moving.md) - decision logs preserve assumptions for review without stopping the entire work tree.
- [Collaborate with complex agents through high-bandwidth artifacts](../concepts/collaborate-with-complex-agents-through-high-bandwidth-artifacts.md) - artifact-native workflows let humans steer local parts of complex agent work.
- [Isolate parallel coding work with project worktrees](../concepts/isolate-parallel-coding-work-with-project-worktrees.md) - worktrees let concurrent coding-agent runs proceed without colliding in one checkout.
- [Customize subagents by task, model, tools, and permissions](../concepts/customize-subagents-by-task-model-tools-and-permissions.md) - decomposed agent work needs role-specific models, tools, and authority.
- [Use agent hooks to automate session rituals](../concepts/use-agent-hooks-to-automate-session-rituals.md) - event hooks can encode repeated setup, audit, and final-validation steps.
- [Compare models by task, thinking budget, cost, and latency](../concepts/compare-models-by-task-thinking-budget-cost-and-latency.md) - workflow design should include model routing and thinking-budget choices.
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - failed work items become the driver for context improvements.
- [Ralph loops process one ticket at a time with fresh context](../concepts/ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md) - narrow repeatable work units reduce orchestration complexity.
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](../concepts/feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md) - each run can improve the instructions that shape later runs.
- [Choose plan-heavy or review-heavy agent workflows by task shape](../concepts/choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md) - workflow design should match planning depth to whether a task can be specified and tested.
- [Parallel coding-agent queues need focus-preserving review interfaces](../concepts/parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md) - long-running agent workflows need queueing and review handoffs that reduce context switching.
- [Spatial agent maps expose filesystem-level lineage and collisions](../concepts/spatial-agent-maps-expose-filesystem-level-lineage-and-collisions.md) - spatial activity maps help operators understand where parallel agents are acting.
- [Let agents propose quest queues for parallel work](../concepts/let-agents-propose-quest-queues-for-parallel-work.md) - queues of agent-suggested missions can move ideation and maintenance discovery into the workflow.
- [Review bundles compress parallel agent output into evidence](../concepts/review-bundles-compress-parallel-agent-output-into-evidence.md) - compact evidence artifacts keep parallel work reviewable.
- [Prompt-coded product behavior reduces code but weakens hard guarantees](../concepts/prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md) - workflow behavior can move into prompts when teams accept the new evaluation and guarantee tradeoffs.
- [Evaluate workspace isolation with positive and negative filesystem scorers](../concepts/evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md) - prompt-enforced workspace workflows need scorers for both intended and forbidden edits.
- [Use parent agents to compare and merge parallel subagent outputs](../concepts/use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md) - parent agents can coordinate subagent results into a reviewable comparison and synthesis loop.
- [Agent skills package progressive-disclosure context for repeatable workflows](../concepts/agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) - repeated workflows can be packaged as skills with deeper references loaded on demand.
- [Evaluate agent skills with task scenarios and comparative conditions](../concepts/evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md) - workflow changes can be tested by comparing runs with and without the skill.
- [Validate eval harnesses before trusting skill scores](../concepts/validate-eval-harnesses-before-trusting-skill-scores.md) - workflow evals need checks for evaluator mistakes, not just agent mistakes.
- [Surface unresolved context conflicts to agents and users](../concepts/surface-unresolved-context-conflicts-to-agents-and-users.md) - context workflows should turn unresolved contradictions into explicit clarification points.
- [Do not cache context-engine answers as durable truth](../concepts/do-not-cache-context-engine-answers-as-durable-truth.md) - workflows should avoid carrying stale generated answers forward as if they were source truth.
- [Context development lifecycle treats context as an engineered artifact](../concepts/context-development-lifecycle-treats-context-as-an-engineered-artifact.md) - context work should follow a generate, evaluate, distribute, observe, and adapt loop.
- [Use agent logs and review feedback as context observability signals](../concepts/use-agent-logs-and-review-feedback-as-context-observability-signals.md) - workflow failures should feed shared context updates rather than repeated local fixes.
- [Package reusable context as skills, libraries, and registries](../concepts/package-reusable-context-as-skills-libraries-and-registries.md) - reusable workflow context can be installed and maintained across projects.
- [Grow personal-agent permissions incrementally from recurring pain](../concepts/grow-personal-agent-permissions-incrementally-from-recurring-pain.md) - personal automation should expand through small, trusted, reversible steps.
- [Single-chat personal agents collapse mixed life domains](../concepts/single-chat-personal-agents-collapse-mixed-life-domains.md) - personal-agent workflows need domain separation when one thread becomes too broad.
- [Purpose-built agent workspaces make orchestration visible](../concepts/purpose-built-agent-workspaces-make-orchestration-visible.md) - visible orchestration state helps users supervise multi-topic personal workflows.
- [Local OS agents can invert the prompt flow](../concepts/local-os-agents-can-invert-the-prompt-flow.md) - proactive agents can prompt the human for decisions while ordinary work proceeds in the background.
- [Ambient agents need self-maintenance and memory hygiene](../concepts/ambient-agents-need-self-maintenance-and-memory-hygiene.md) - recurring maintenance jobs keep always-on workflows reliable.
- [Visual agent workflows make tool use observable and adjustable](../concepts/visual-agent-workflows-make-tool-use-observable-and-adjustable.md) - workflow graphs provide an inspectable path from trigger to model, memory, tool call, and approval state.
- [Route high-impact agent actions through explicit human approval gates](../concepts/route-high-impact-agent-actions-through-explicit-human-approval-gates.md) - review steps should be implemented as workflow control points, not model self-approval.
- [Use tool names and descriptions as operational prompts](../concepts/use-tool-names-and-descriptions-as-operational-prompts.md) - workflow tuning includes improving the prompt-like metadata attached to each tool.
- [Split large automation surfaces into specialized subagents and subworkflows](../concepts/split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md) - reusable subflows and specialist agents reduce complexity as automations expand.
- [Prompt voice agents for persona, prosody, and brand fit](../concepts/prompt-voice-agents-for-persona-prosody-and-brand-fit.md) - voice workflows need spoken delivery guidance in addition to task instructions.
- [Stage complex AI applications into inspectable deterministic and agentic steps](../concepts/stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md) - staged workflows make production agent behavior easier to trace and debug.
- [Replay production failures before promoting prompt fixes](../concepts/replay-production-failures-before-promoting-prompt-fixes.md) - remediation workflows should turn production failures into replayable regression tests before changes ship.
- [Agents reduce dependency-chain chores through parallel execution](../concepts/agents-reduce-dependency-chain-chores-through-parallel-execution.md) - workflows gain leverage when agents clear prerequisite setup and integration work.
- [Non-technical collaborators can steer agents with natural work artifacts](../concepts/non-technical-collaborators-can-steer-agents-with-natural-work-artifacts.md) - operational workflows can accept existing work artifacts instead of forcing collaborators into developer-shaped tools.
- [Canvas-native agents turn spatial work surfaces into prompt context](../concepts/canvas-native-agents-turn-spatial-work-surfaces-into-prompt-context.md) - users can steer workflows through drawings, annotations, selections, and prior generated artifacts.
- [Shared canvases expose multi-agent state and coordination](../concepts/shared-canvases-expose-multi-agent-state-and-coordination.md) - shared visual state makes delegation, progress, and overlap visible during parallel agent work.
- [Hackable agent runtimes need tight safety boundaries](../concepts/hackable-agent-runtimes-need-tight-safety-boundaries.md) - richer runtime workflows need sandboxing before they can safely affect user artifacts.
- [Code-backed content can replace fragile CMS workflows for agents](../concepts/code-backed-content-can-replace-fragile-cms-workflows-for-agents.md) - repository-backed structured content lets agents make reviewable operational updates.
- [Server-side interaction state simplifies branching conversational agents](../concepts/server-side-interaction-state-simplifies-branching-conversational-agents.md) - workflow branches can reuse prior interaction state without duplicating full history client-side.
- [Agent tool loops turn model-required actions into executable results](../concepts/agent-tool-loops-turn-model-required-actions-into-executable-results.md) - tool workflows should explicitly execute required actions and loop until final output.
- [Agent skills should point to current docs instead of embedding every API detail](../concepts/agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md) - reusable workflow guidance should avoid stale copies of fast-moving API docs.
- [Breadcrumb coding agents through staged discovery and implementation](../concepts/breadcrumb-coding-agents-through-staged-discovery-and-implementation.md) - sequence agent context to reduce inconsistent codegen paths.
- [Maintain ubiquitous language for AI coding](../concepts/maintain-ubiquitous-language-for-ai-coding.md) - workflow artifacts should reuse shared domain terms across prompts, code, and tests.
- [Limit agent change size by feedback speed](../concepts/limit-agent-change-size-by-feedback-speed.md) - workflow gates should keep agent changes small enough for available checks.
- [Use deep modules to make agent work testable](../concepts/use-deep-modules-to-make-agent-work-testable.md) - module boundaries let humans validate agent work through stable interfaces.
- [Ask agents after each run what blocked their success](../concepts/ask-agents-after-each-run-what-blocked-their-success.md) - post-run feedback helps turn failures into workflow and context fixes.
- [Agent software factories need runnable, contextual, and verifiable primitives](../concepts/agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md) - workflow readiness starts with runnable projects, accessible context, and agent-executable checks.
- [Cloud agents turn coding work into asynchronous VM-backed queues](../concepts/cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md) - synchronous planning and asynchronous execution can increase throughput when review remains focused.
- [Align teams before agents implement](../concepts/align-teams-before-agents-implement.md) - workflow design should prevent agentic speed from bypassing shared direction.
- [Shared cloud workspaces make agent sessions collaborative](../concepts/shared-cloud-workspaces-make-agent-sessions-collaborative.md) - shared sessions combine execution, review, and collaboration surfaces.
- [Collaborative plans become executable agent context](../concepts/collaborative-plans-become-executable-agent-context.md) - team-edited plans turn discussion into prompt context.
- [Social context dashboards keep agentic teams oriented](../concepts/social-context-dashboards-keep-agentic-teams-oriented.md) - summarized work streams help teams resume, review, and coordinate agentic work.
- [Automation loops convert repeated review and triage into factory improvements](../concepts/automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md) - repeated Slack, PR, transcript, and review work can become process feedback.
- [Gateway platform primitives let teams focus on MCP business logic](../concepts/gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md) - workflow teams can build domain-specific MCP behavior on shared platform controls.
- [Use PRDs to align agents on the design concept](../concepts/use-prds-to-align-agents-on-the-design-concept.md) - planning artifacts turn ambiguous requirements into shared agent-ready intent.
- [Run parallel issue agents in sandboxes with review and merge loops](../concepts/run-parallel-issue-agents-in-sandboxes-with-review-and-merge-loops.md) - parallel workflow needs explicit isolation, review, and integration stages.

## Open Questions

- How should teams decide when a failure-driven context update is durable enough to enter the shared knowledge base?
- How should a loop decide when to stop, ask for human review, or continue to the next ticket?
- How should teams retire or rewrite skills that are no longer loaded or no longer match the current workflow?
- How should context-engine clarification from users be converted into durable, source-backed memory without preserving bad generated answers?
- How should organizations decide when an individual prompt improvement is mature enough to publish as shared team context?
- When does parallel agent execution improve throughput, and when does it merely create review backlog?
- What minimum evidence should each autonomous agent run produce before it is eligible for human review?
- When should a prompt-coded workflow be promoted back into native product code?
- What evidence is enough to promote a personal-agent workflow from playground testing into daily ambient operation?
- When should a personal-agent workflow move from generic messaging into a purpose-built workspace?
- Which actions should require a hard approval gate even when the user has already granted the agent broad tool access?
- How should synthetic voice conversations be promoted from exploratory testing into durable workflow eval cases?
- When should a production AI workflow add another stage, and when does the extra stage add more operational risk than debugging value?
- Which non-engineering workflows become better when agents accept natural artifacts, and which need stricter data-entry constraints?
- How should shared-canvas agents prevent duplicate or conflicting edits while still letting multiple agents work in parallel?
- How should interaction-state retention, retrieval, and compaction be built into long-running conversational workflows?
- Which codegen steps should be breadcrumbs in the workflow, and which should remain flexible local agent judgment?
- Which lifecycle hooks should be mandatory for auditability, and which should stay opt-in to avoid surprising users?
- Which domain workflows are ready for team-owned MCP servers once a gateway supplies the shared controls?
- How much team conversation should become agent-visible context, and what should remain private?
- When does PRD optimization stop adding value compared with investing the same effort in tests and QA?
- Which feedback loops are fast enough to let an agent continue autonomously, and which require human review before the next change?
- Which agent uncertainties should be logged as reversible decisions, and which should block for immediate human input?
- Which adoption metrics encourage real workflow learning rather than performative AI usage?
- Which recurring quality rituals remain useful when agents can generate most of the underlying fix?

## Sources

- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md)
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md)
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md)
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md)
- [Software Engineering Is Becoming Plan and Review - Louis Knight-Webb, Vibe Kanban](../sources/20260502_W76woOYHlvY.md)
- [I Gave an AI Agent the Keys to My Life (Here's What Happened) - Radek Sienkiewicz (@velvetshark-com)](../sources/20260502_sJ2jc7leKBk.md)
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md)
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md)
- [Shipping complex AI applications - Braintrust & Trainline](../sources/20260501_ZdheJTfLu-s.md)
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md)
- [Agents on the Canvas in tldraw - Steve Ruiz, tldraw](../sources/20260501_sPUjIBH5Cwg.md)
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md)
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md)
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md)
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md)
- [Gateways are All You Need - Karan Sampath, Anthropic](../sources/20260427_CD6R4Wf3jnY.md)
- [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment - Maggie Appleton, GitHub](../sources/20260426_ClWD8OEYgp8.md)
- [AgentCraft: Putting the Orc in Orchestration - Ido Salomon](../sources/20260425_kR64LOqBBCU.md)
- [Full Walkthrough: Workflow for AI Coding - Matt Pocock](../sources/20260424_-QFHIoCo-Ko.md)
- [The End of Apps - Kitze, Sizzy.co](../sources/20260423_4fntwuOoedA.md)
- ["Software Fundamentals Matter More Than Ever" - Matt Pocock](../sources/20260423_v4F1gFy-hqg.md)
- [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../sources/20260422_XNtkiQJ49Ps.md)
- [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @pragmaticengineer](../sources/20260421_CS5Cmz5FssI.md)
- [Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer](../sources/20260421_wjk0ulMAkbc.md)
