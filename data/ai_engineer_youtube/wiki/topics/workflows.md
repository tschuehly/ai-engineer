# Workflows

## Overview

Personal-agent workflows need domain separation and proactive task flow once they move beyond one recurring pain. A single chat can collapse unrelated work and life contexts; multi-topic workspaces preserve context boundaries, show tool progress, and let the agent ask the human for decisions or missing artifacts while background work continues. Read-only observer workflows are a lower-authority alternative for high-stakes personal domains: they gather signals, produce reflection artifacts, and leave outreach, scheduling, and writing decisions to the user.

Agent workflows become more reliable when they expose a tight loop between work execution, failure observation, missing-context discovery, and documentation updates. Demand-driven context uses that loop to grow enterprise context from real tasks rather than from speculative upfront curation. Production AI application workflows add another loop: stage the agent, trace it, evaluate it on golden cases, deploy managed prompts/tools/scores, monitor production traces, replay failures, and rerun regression checks before promoting fixes. Personal-agent workflows apply the same idea to permissions and trust: start from one recurring pain, add one simple workflow, watch it fail or succeed, then add guardrails before expanding autonomy. Human-in-the-loop automations make those guardrails concrete by pausing sensitive actions for explicit approval, keeping credentials scoped, and logging waiting or resumed executions. Voice-agent workflows need a similar staged design: start with a narrow realtime conversation path, add tools sparingly, preserve context across handoffs, and validate both transcript behavior and audio delivery before expanding coverage. Coding-agent loops apply the same principle to implementation work: keep each run small, make progress observable, and feed defects or process lessons into the next prompt or skill. Product codegen workflows can reduce variation by breadcrumbing the agent through discovery, candidate event design, shared vocabulary, and then implementation, and can use post-run self-interrogation to discover missing tools or contradictory context. AI-amplified product work also needs explicit quality routines: recurring quality reviews train engineers to find small regressions, and zero-bug policies turn defect inflow into immediate triage rather than postponed cleanup. For agentic software work, workflow design should deliberately trade upfront planning against later review effort, should make feedback speed and review capacity the limit on change size, and should use parallel queues only when the interface preserves human focus around completed work. Harness-oriented workflows turn repeated review lessons into durable context, lints, reviewer agents, and PR comments so non-functional requirements are refreshed throughout long-running agent work instead of relying on one initial prompt. Workflows should also reintroduce friction where it carries judgment: database migrations, permission changes, dependency additions, architecture, and reliability decisions need explicit human gates even when mechanical bugs can be sent back to the agent automatically. Parent-agent comparison workflows can run multiple models or strategies in isolated workspaces, then help the user review, rank, and combine the results. Spatial orchestration workflows add filesystem visibility, collision heat maps, agent-discovered quest queues, containerized decomposition, and evidence-rich review bundles so many agent runs can be supervised without constant babysitting. When that workflow is encoded as prompts rather than runtime code, its eval loop must verify both desired work and absence of forbidden side effects. Outside coding, agents are useful when they shorten feedback cycles for collaborators who can hand over natural artifacts, and when they absorb the prerequisite work that otherwise blocks progress. Canvas-native workflows strengthen that artifact handoff by letting users draw, annotate, select, and revise directly on the same surface the agent reads and edits. Multi-agent canvas workflows can also make shared state, leader/follower delegation, overlapping work, and completion review visible rather than hidden in logs. Context-engine workflows should also surface unresolved source conflicts, recompute from current sources when answers may be stale, and route clarification back into durable context. Skill and context-package workflows should be developed like library workflows: define expected behavior, package guidance, evaluate changes, distribute reusable context, observe use through logs and review, then update shared packages when the workflow changes. Ambient-agent workflows add a maintenance loop: overnight indexing, backups, memory refreshes, update validation, cleanup, and notification filtering keep the system ready without forcing the user to watch every operation.

Complex vertical workflows add another design dimension: make ambiguous work more verifiable through decomposition, proxy checks, and guardrails; when uncertainty remains, let agents record reversible decisions instead of blocking on low-context chat questions. Artifact-native surfaces help humans review the specific branch of the work tree where their judgment is needed. Deep-research-to-writing pipelines show the same principle in a content workflow: keep exploratory evidence gathering agentic, then hand a `research.md` artifact to a tighter writing workflow with guidelines, few-shot examples, reviewer loops, and versioned drafts. AI adoption workflows should also avoid Goodharted usage goals: visible token counts and spend leaderboards can reward performative usage, while effective adoption requires hands-on experimentation against real work.

Compressed research is a lower-risk operations pattern: keep the business event and human decision in place, but let an agent gather, classify, route, or summarize the evidence that made the work slow. This is especially useful when the source information already exists in company systems but is not available in the right place at decision time.

Open-source agent workflows have their own bottleneck: AI can generate more reports, PRs, and fixes than maintainers can safely absorb. Projects need triage loops, contribution boundaries, foundation or company support for sustained maintenance, extension points so experiments can happen without turning every idea into core-review load, and human-effort filters that require concise contributor context before maintainers spend review time.

Org-chart agent workflows add a business-operations control surface: assign work through roles, keep plans and tasks visible, route completion through reviewer and approver agents, and convert repeated prompts into scheduled or manually parameterized routines. They should grow from the smallest useful agent set because role behavior, skill use, budgets, model cost, and concurrency all need validation before fan-out.

Repository-local web-agent workflows can make implementation, verification, preview sharing, and handoff rules part of the repeatable routine. Skills can teach the agent how to inspect issues, run browser QA, record evidence, create a public preview tunnel, notify a reviewer, and wait for confirmation before closing work.

Multi-agent workflows need explicit coordination and recovery choices. Event-driven choreography works when agents can act independently and the system can trace every event; centralized orchestration works when dependencies, state, rollback, or auditability matter more than autonomy. Large refactor workflows make the dependency problem concrete: scan or visualize the code graph, form PR-sized batches, dispatch fixers only when upstream dependencies are ready, review and merge small outputs, then repeat as new batches unblock. Durable workflows should pass immutable state versions through data-contract validation and wrap agent calls with circuit breakers, graceful degradation, and compensation so partial failures do not leave hidden side effects.

Durable workflow engines also address the single-agent production loop. Agent frameworks may provide the fixed loop that calls the LLM, executes requested tools, and feeds results back, but production workflows need persisted turns, retry policy, timeout behavior, and resumable waits around that loop. Human-in-the-loop steps are a useful stress test: the workflow should pause as logical state, release active process resources when needed, and resume when a human response arrives. Workflow-like automations can still justify an agent harness when the middle of the process requires flexible exploration, repository cloning, Docker runs, tests, and structured output rather than only known deterministic steps.

Workflow-backed TypeScript agents should keep orchestration deterministic and put LLM calls, sandbox commands, and external APIs behind step boundaries. That makes the running agent easier to inspect through step spans, easier to connect to a resumable UI stream, and easier to control through scheduling, cancellation, and run-version operations when it waits beyond one request.

API-backed agent workflows should be hardened only after their task shape is understood. A practical path is to prototype the repeated work in the provider's web UI, observe which context, files, connectors, and permissions make the run succeed, then encode that stable shape as an API task lifecycle with polling or webhooks. When the workflow starts in a channel such as Slack, store the thread-to-task mapping explicitly so follow-up messages continue the same task and final results return to the user's original conversation.

Contact-center voice workflows show a concrete human-in-the-loop automation pattern: shift after-call documentation from manual memory work into a streamed extraction pipeline, but keep operators responsible for quick validation before the generated summary updates CRM fields. The workflow is only as strong as the early audio and transcript stages; speaker separation, domain STT, masking, grounded JSON extraction, and schema mapping all happen before the final human confirmation.

Platform workflows should be shaped for agent loops as well as human onboarding. Agents need local validation, clear task and success definitions, and callable platform feedback so they can iterate before remote CI or deployment; when agents contribute back to platform code, policy guardrails and repository instructions should separate hard safety boundaries from workflow guidance.

For AI app reliability work, build evals at the start of the workflow rather than after a demo already feels good. A practical loop is to define scenario-level criteria from user outcomes, generate realistic persona and wording variants, inspect failures one by one, and then use the benchmark to compare model, prompt, RAG, logic, or agentic changes while watching for regressions and cost or latency tradeoffs.

DSPy-style workflows separate program shape from prompt shape: teams can define signatures and modules, route inputs through ordinary control flow, select adapters for model-facing format, and then optimize the resulting program with datasets and metrics. This is most useful when the task has known examples and quality criteria, not when the workflow is too open-ended to score. Prompt-learning workflows should likewise be made explicit: start from examples with feedback, choose sample size and train/test split, run bounded generate/evaluate/refine loops, and review whether evaluator feedback is trustworthy enough to drive the next prompt.

For coding agents, this workflow can be attached directly to rule files: run the agent on benchmark issues, collect test and judge feedback, use a meta-prompt to draft rule changes, diff the resulting prompt context, and rerun the benchmark before adopting the rules. The same workflow pressure applies to DevEx basics: fast local validation, written external context, clear turn-taking in review, and assigned review ownership keep agent iteration from becoming slow CI loops and rubber-stamped PRs.

Anti-slop workflows should separate quality from provenance. Human and AI work can both be low-quality, inaccurate, or insecure, so the workflow should ask for evidence instead of accepting line count, engagement, or autonomous runtime as progress. AI can still be part of the anti-slop loop when it helps curate what is worth attention, creates code maps that improve codebase understanding, operates development tools through computer use, or sends commoditized work through asynchronous agents while humans keep clear design boundaries.

Agent-native organizational workflows start with supervision, dispatch, and review of agent work as a normal daily rhythm. This only works when the organization also adapts hiring and onboarding: employees need enough AI fluency to turn domain expertise into agent instructions, review artifacts, and role-specific agent setup.

Enterprise AI research workflows can be made fundable by turning each uncertain phase into a small productizable bet. For GenBI, the useful pattern is to work with production-like but controlled data, involve expert users early, ship six-week deliverables such as metadata enrichment or report discovery, and preserve stop/go decision points so leadership can keep funding tied to measurable value instead of sunk cost.

## Key Concepts

- [Run coding agents through a simple master loop](../concepts/run-coding-agents-through-a-simple-master-loop.md) - simple loops can replace over-specified DAGs when exploration is the work.
- [Use prompt-enforced todos as lightweight agent state](../concepts/use-prompt-enforced-todos-as-lightweight-agent-state.md) - lightweight task state can keep a run oriented without a full workflow graph.
- [Agent-native companies embed agents into product, operations, and culture](../concepts/agent-native-companies-embed-agents-into-product-operations-and-culture.md) - pushes workflow design beyond one-off assistant use.
- [Fund enterprise AI through incremental productizable bets](../concepts/fund-enterprise-ai-through-incremental-productizable-bets.md) - breaks uncertain enterprise AI research into short value-producing stages.
- [Start the workday by reviewing and dispatching agent work](../concepts/start-the-workday-by-reviewing-and-dispatching-agent-work.md) - provides a daily operating loop for asynchronous agent output.
- [Hire for AI fluency and agent orchestration ability](../concepts/hire-for-ai-fluency-and-agent-orchestration-ability.md) - makes candidate evaluation and onboarding part of the agent workflow.
- [Bootstrap RL with targeted SFT before reinforcement learning](../concepts/bootstrap-rl-with-targeted-sft-before-reinforcement-learning.md) - interactive post-training can teach protocol first, then optimize outcomes through RL.
- [Control environment noise for group-based RL](../concepts/control-environment-noise-for-group-based-rl.md) - RL workflows need stable seeds, difficulty ranges, batch sizing, and exploration settings.
- [Inspect rollouts before trusting RL environment scores](../concepts/inspect-rollouts-before-trusting-rl-environment-scores.md) - reward curves should be paired with trajectory inspection and real-task trials.
- [Use hosted model playgrounds to prototype before owning infrastructure](../concepts/use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md) - hosted playgrounds can compress the path from idea to model, API, app, and cloud deployment experiment.
- [Human Control Planes Turn Agent Swarms Into Manageable Organizations](../concepts/human-control-planes-turn-agent-swarms-into-manageable-organizations.md) - workflows need visible organizational state when many agents work in parallel.
- [Treat multi-agent systems as distributed systems](../concepts/treat-multi-agent-systems-as-distributed-systems.md) - workflow design must account for coordination complexity and shared-state failure modes.
- [Use durable execution for production agent loops](../concepts/use-durable-execution-for-production-agent-loops.md) - workflow durability prevents crashes or rate limits from resetting long-running agent loops.
- [Keep workflow orchestration deterministic and put side effects in steps](../concepts/keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md) - rerunnable workflow code needs side-effecting agent work isolated in steps.
- [Control long-running workflow agents through run lifecycle operations](../concepts/control-long-running-workflow-agents-through-run-lifecycle-operations.md) - recurring and waiting agents need cancellation, scheduling, and version controls.
- [Treat long waits as logical workflow state](../concepts/treat-long-waits-as-logical-workflow-state.md) - long human waits should be resumable workflow state rather than live process occupancy.
- [Treat agent APIs as asynchronous task lifecycles](../concepts/treat-agent-apis-as-asynchronous-task-lifecycles.md) - API integrations need task IDs, statuses, polling, webhooks, continuation, and errors.
- [Treat long-horizon agents as asynchronous workers with evolving interfaces](../concepts/treat-long-horizon-agents-as-asynchronous-workers-with-evolving-interfaces.md) - longer work horizons need progress, artifact, and review surfaces around the agent loop.
- [Map external conversation threads to agent task IDs](../concepts/map-external-conversation-threads-to-agent-task-ids.md) - external collaboration threads should correlate to the agent task that owns their context.
- [Prototype agent workflows in the UI before hardening the API path](../concepts/prototype-agent-workflows-in-the-ui-before-hardening-the-api-path.md) - prove the repeated work in a richer UI before freezing an integration contract.
- [Choose choreography or orchestration by complexity and autonomy](../concepts/choose-choreography-or-orchestration-by-complexity-and-autonomy.md) - workflow control should be selected by dependency complexity, autonomy need, and auditability.
- [Use immutable versioned state for agent handoffs](../concepts/use-immutable-versioned-state-for-agent-handoffs.md) - workflows become debuggable when each handoff records a sealed state version and contract check.
- [Wrap agent calls with circuit breakers and compensation](../concepts/wrap-agent-calls-with-circuit-breakers-and-compensation.md) - retry, fail-fast, degradation, and rollback behavior should be planned before production.
- [Preserve speaker channels before voice-agent transcription](../concepts/preserve-speaker-channels-before-voice-agent-transcription.md) - voice workflows should prevent speaker-attribution errors before they reach extraction or review.
- [Extract contact-center intelligence as structured JSON](../concepts/extract-contact-center-intelligence-as-structured-json.md) - after-call workflows become automatable when conversation content is converted into schema-aligned business fields.
- [Verify AI call summaries before CRM sync](../concepts/verify-ai-call-summaries-before-crm-sync.md) - human verification keeps CRM updates accountable without reverting to fully manual note-taking.
- [Use Reviewer and Approver Roles To Make Agent Workflows Reliable](../concepts/use-reviewer-and-approver-roles-to-make-agent-workflows-reliable.md) - explicit role handoffs turn validation from a reminder into a workflow path.
- [Reverse-engineer AI app evals from user outcomes](../concepts/reverse-engineer-ai-app-evals-from-user-outcomes.md) - reliability workflows should start from what users and the business need the app to accomplish.
- [Build AI app benchmarks before optimization](../concepts/build-ai-app-benchmarks-before-optimization.md) - benchmark-first workflows catch regressions while teams optimize prompts, models, retrieval, and guardrails.
- [DSPy programs keep LLM intent separate from prompt strings](../concepts/dspy-programs-keep-llm-intent-separate-from-prompt-strings.md) - program-first LLM workflows keep control flow stable while model prompts evolve.
- [Optimize LLM programs with metrics and teacher feedback](../concepts/optimize-llm-programs-with-metrics-and-teacher-feedback.md) - known examples and metrics can drive DSPy optimizer loops.
- [Use explanatory feedback to optimize prompts](../concepts/use-explanatory-feedback-to-optimize-prompts.md) - feedback-rich examples turn prompt editing into a repeatable improvement loop.
- [System prompt learning updates agent rules from eval explanations](../concepts/system-prompt-learning-updates-agent-rules-from-eval-explanations.md) - coding-agent prompt learning turns traces into rule updates.
- [Structure prompt-learning experiments with train/test splits and loop budgets](../concepts/structure-prompt-learning-experiments-with-train-test-splits-and-loop-budgets.md) - sample, split, evaluator, and iteration controls make prompt-learning runs comparable.
- [Evaluator quality is a dependency of prompt optimization](../concepts/evaluator-quality-is-a-dependency-of-prompt-optimization.md) - workflow automation should not let weak judges steer prompt changes unchecked.
- [Route heterogeneous documents through multimodal LLM pipelines](../concepts/route-heterogeneous-documents-through-multimodal-llm-pipelines.md) - mixed document workflows can classify file type and branch to specialized modules.
- [Reusable Routines Turn Prompts Into Operational Agent Workflows](../concepts/reusable-routines-turn-prompts-into-operational-agent-workflows.md) - repeated prompts can become scheduled or manually triggered routines with variables and skills.
- [Repository skills and AGENTS.md encode repeatable web-agent workflows](../concepts/repository-skills-and-agents-md-encode-repeatable-web-agent-workflows.md) - web feature work can include local QA, preview sharing, and handoff rules by default.
- [Grow Agent Organizations Incrementally By Role Quality and Cost](../concepts/grow-agent-organizations-incrementally-by-role-quality-and-cost.md) - workflow fan-out should follow observed quality and cost fit.
- [Do not use token volume as a developer productivity metric](../concepts/do-not-use-token-volume-as-a-developer-productivity-metric.md) - workflow metrics should not reward token generation over useful delivery.
- [AI-amplified shipping speed needs stronger product taste](../concepts/ai-amplified-shipping-speed-needs-stronger-product-taste.md) - AI-assisted workflows need explicit no-saying and root-problem discovery before implementation.
- [Quality Wednesdays train engineers to notice small regressions](../concepts/quality-wednesdays-train-engineers-to-notice-small-regressions.md) - recurring quality review turns product polish into team practice.
- [Zero-bug policies turn bug inflow into immediate work](../concepts/zero-bug-policies-turn-bug-inflow-into-immediate-work.md) - bug workflow should prevent passive backlog accumulation.
- [Product engineers need direct customer context](../concepts/product-engineers-need-direct-customer-context.md) - customer feedback surfaces help engineers steer AI-assisted product work.
- [Practice-driven AI tool fluency beats theory-only adoption](../concepts/practice-driven-ai-tool-fluency-beats-theory-only-adoption.md) - AI workflow competence comes from repeated real-use experimentation.
- [Treat coding agents as fast junior collaborators](../concepts/treat-coding-agents-as-fast-junior-collaborators.md) - workflow design should preserve human direction around agent execution.
- [Keep agent context small, fresh, and task-specific](../concepts/keep-agent-context-small-fresh-and-task-specific.md) - session hygiene prevents old or irrelevant context from steering later work.
- [Use research-plan-implement loops for coding agents](../concepts/use-research-plan-implement-loops-for-coding-agents.md) - separate phases make coding-agent work more reviewable.
- [Spec-driven development turns prompts into requirements, design, and tasks](../concepts/spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md) - coding-agent workflows can route from prompt to spec artifacts to task execution.
- [Translate structured requirements into property-based tests](../concepts/translate-structured-requirements-into-property-based-tests.md) - workflow completion can be tied to tests derived from acceptance criteria.
- [Keep spec artifacts feature-scoped, mutable, and context-backed](../concepts/keep-spec-artifacts-feature-scoped-mutable-and-context-backed.md) - spec workflows should amend or prune artifacts as the system evolves.
- [Configure agent modes, rules, and permissions as the workflow evolves](../concepts/configure-agent-modes-rules-and-permissions-as-the-workflow-evolves.md) - workflow configuration should adapt as the team learns what agents can do safely.
- [Make agent work more trustworthy by making it verifiable](../concepts/make-agent-work-more-trustworthy-by-making-it-verifiable.md) - workflow design should turn hard-to-review autonomy into checked or constrained subwork.
- [Harness engineering shifts scarcity from code production to control surfaces](../concepts/harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md) - workflow leverage moves to structures that steer abundant implementation capacity.
- [Encode non-functional requirements as agent-visible context](../concepts/encode-non-functional-requirements-as-agent-visible-context.md) - team quality expectations need durable workflow artifacts.
- [Use reviewer agents and lints to turn review lessons into guardrails](../concepts/use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md) - repeated review lessons should become automatic workflow checks.
- [Treat prompts as distributed harness surfaces](../concepts/treat-prompts-as-distributed-harness-surfaces.md) - workflow prompts can be injected through files, skills, lints, PR comments, and tests.
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
- [Let the core agent loop orchestrate parallel subtasks](../concepts/let-the-core-agent-loop-orchestrate-parallel-subtasks.md) - agent-led decomposition can use parallelism without making the user reconcile thread outputs.
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
- [Read-only personal AI observers are a distinct product category](../concepts/read-only-personal-ai-observers-are-a-distinct-product-category.md) - some personal workflows should stop at reflection and suggestion.
- [Cognitive exhaust gains value through cross-source synthesis](../concepts/cognitive-exhaust-gains-value-through-cross-source-synthesis.md) - observer workflows can turn scattered personal signals into reviewable Markdown.
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
- [Agent harnesses combine model, tools, prompts, filesystem, skills, hooks, and memory](../concepts/agent-harnesses-combine-model-tools-prompts-filesystem-skills-hooks-and-memory.md) - workflow agents need harness primitives around flexible middle steps.
- [Use hooks for deterministic agent verification and live context injection](../concepts/use-hooks-for-deterministic-agent-verification-and-live-context-injection.md) - hooks turn repeated verification and context refresh into workflow events.
- [Agent skills should point to current docs instead of embedding every API detail](../concepts/agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md) - reusable workflow guidance should avoid stale copies of fast-moving API docs.
- [Breadcrumb coding agents through staged discovery and implementation](../concepts/breadcrumb-coding-agents-through-staged-discovery-and-implementation.md) - sequence agent context to reduce inconsistent codegen paths.
- [Maintain ubiquitous language for AI coding](../concepts/maintain-ubiquitous-language-for-ai-coding.md) - workflow artifacts should reuse shared domain terms across prompts, code, and tests.
- [Limit agent change size by feedback speed](../concepts/limit-agent-change-size-by-feedback-speed.md) - workflow gates should keep agent changes small enough for available checks.
- [AI output speed can overwhelm review capacity](../concepts/ai-output-speed-can-overwhelm-review-capacity.md) - workflow throughput should be limited by responsible review, not only by how fast agents can produce code.
- [Treat slop as a quality failure, not an AI provenance label](../concepts/treat-slop-as-a-quality-failure-not-an-ai-provenance-label.md) - anti-slop workflows judge output quality rather than origin.
- [Do not report agent autonomy without quality accountability](../concepts/do-not-report-agent-autonomy-without-quality-accountability.md) - autonomous workflow duration needs review, safety, and maintainability evidence.
- [Keep critical code inside human understanding and review capacity](../concepts/keep-critical-code-inside-human-understanding-and-review-capacity.md) - critical workflow output should remain small enough for direct human ownership.
- [Agent-legible codebases reduce generated-code entropy](../concepts/agent-legible-codebases-reduce-generated-code-entropy.md) - workflow reliability improves when the codebase exposes clear flow, primitives, and search targets to agents.
- [Use human judgment gates for high-risk agent code changes](../concepts/use-human-judgment-gates-for-high-risk-agent-code-changes.md) - review systems should route mechanical fixes to agents while pausing risk-bearing changes for human judgment.
- [Use deep modules to make agent work testable](../concepts/use-deep-modules-to-make-agent-work-testable.md) - module boundaries let humans validate agent work through stable interfaces.
- [Ask agents after each run what blocked their success](../concepts/ask-agents-after-each-run-what-blocked-their-success.md) - post-run feedback helps turn failures into workflow and context fixes.
- [Agent software factories need runnable, contextual, and verifiable primitives](../concepts/agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md) - workflow readiness starts with runnable projects, accessible context, and agent-executable checks.
- [Local-first platform workflows shorten agent feedback loops](../concepts/local-first-platform-workflows-shorten-agent-feedback-loops.md) - platform workflows should fail early in the agent's local workspace.
- [Guard AI-assisted platform contributions with policy and context](../concepts/guard-ai-assisted-platform-contributions-with-policy-and-context.md) - contribution workflows need hard policies plus Markdown guidance.
- [Cloud agents turn coding work into asynchronous VM-backed queues](../concepts/cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md) - synchronous planning and asynchronous execution can increase throughput when review remains focused.
- [Align teams before agents implement](../concepts/align-teams-before-agents-implement.md) - workflow design should prevent agentic speed from bypassing shared direction.
- [Shared cloud workspaces make agent sessions collaborative](../concepts/shared-cloud-workspaces-make-agent-sessions-collaborative.md) - shared sessions combine execution, review, and collaboration surfaces.
- [Collaborative plans become executable agent context](../concepts/collaborative-plans-become-executable-agent-context.md) - team-edited plans turn discussion into prompt context.
- [Social context dashboards keep agentic teams oriented](../concepts/social-context-dashboards-keep-agentic-teams-oriented.md) - summarized work streams help teams resume, review, and coordinate agentic work.
- [Automation loops convert repeated review and triage into factory improvements](../concepts/automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md) - repeated Slack, PR, transcript, and review work can become process feedback.
- [Gateway platform primitives let teams focus on MCP business logic](../concepts/gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md) - workflow teams can build domain-specific MCP behavior on shared platform controls.
- [Use PRDs to align agents on the design concept](../concepts/use-prds-to-align-agents-on-the-design-concept.md) - planning artifacts turn ambiguous requirements into shared agent-ready intent.
- [Run parallel issue agents in sandboxes with review and merge loops](../concepts/run-parallel-issue-agents-in-sandboxes-with-review-and-merge-loops.md) - parallel workflow needs explicit isolation, review, and integration stages.
- [Decompose large refactors into dependency-aware agent batches](../concepts/decompose-large-refactors-into-dependency-aware-agent-batches.md) - graph- or directory-shaped batches keep large code changes reviewable and parallelizable.
- [Run verify-fix-review loops for agentic refactors](../concepts/run-verify-fix-review-loops-for-agentic-refactors.md) - refactor workflows need verifier, fixer, human review, and unblock-repeat stages.
- [Choose autonomy level by task uncertainty and control needs](../concepts/choose-autonomy-level-by-task-uncertainty-and-control-needs.md) - workflows should absorb known steps before teams add agentic planning.
- [Deep research agents need planning, grounded evidence, and pivot loops](../concepts/deep-research-agents-need-planning-grounded-evidence-and-pivot-loops.md) - open-ended research workflows need source-backed iteration.
- [Compressed research agents preserve human decision points](../concepts/compressed-research-agents-preserve-human-decision-points.md) - research automation can preserve the process's human decision boundary.
- [Surface existing company information before redesigning processes](../concepts/surface-existing-company-information-before-redesigning-processes.md) - existing internal signals can power workflow improvements before process redesign.
- [Agents expand the economically viable software surface](../concepts/agents-expand-the-economically-viable-software-surface.md) - cheaper automation changes which workflows are worth software investment.
- [Split exploratory research agents from constrained writing workflows](../concepts/split-exploratory-research-agents-from-constrained-writing-workflows.md) - artifact handoff keeps different workflow phases appropriately constrained.
- [Calibrate LLM judges like binary classifiers](../concepts/calibrate-llm-judges-like-binary-classifiers.md) - workflow judges need their own labeled validation loop.
- [Label LLM Judge Outputs Before Mapping Them to Scores](../concepts/label-llm-judge-outputs-before-mapping-them-to-scores.md) - score-bearing workflows should start from judge labels rather than raw numeric model ratings.
- [Split LLM Judges Into Narrow Binary Metrics](../concepts/split-llm-judges-into-narrow-binary-metrics.md) - judge workflows should start from trace error analysis and one pass/fail metric per failure mode.
- [Optimize Judge Prompts With Diagnostic Feedback](../concepts/optimize-judge-prompts-with-diagnostic-feedback.md) - judge-optimization workflows need diagnostic feedback, not only aggregate scores.
- [AI-generated security reports need maintainer triage](../concepts/ai-generated-security-reports-need-maintainer-triage.md) - workflow throughput should include maintainer capacity for automated reports.
- [Gate AI-generated open-source contributions through human-effort filters](../concepts/gate-ai-generated-open-source-contributions-through-human-effort-filters.md) - contribution workflows can require a short human-authored issue before accepting agent-generated PRs.
- [Human taste limits fully dark coding factories](../concepts/human-taste-limits-fully-dark-coding-factories.md) - iterative product work should keep human judgment in the loop.
- [Plugin architectures let agent systems absorb experiments](../concepts/plugin-architectures-let-agent-systems-absorb-experiments.md) - extension workflows let experiments proceed without overloading core maintainers.
- [Let agent harnesses extend through ordinary code packages](../concepts/let-agent-harnesses-extend-through-ordinary-code-packages.md) - package-based extension workflows keep optional harness behavior out of core.
- [Make validation fast, local, deterministic, and actionable](../concepts/make-validation-fast-local-deterministic-and-actionable.md) - coding-agent workflows need quick checks that can guide the next iteration.
- [Standardize development environments around common model priors](../concepts/standardize-development-environments-around-common-model-priors.md) - workflow reliability improves when agents operate in conventional local environments.
- [Use AI to scale codebase understanding against code slop](../concepts/use-ai-to-scale-codebase-understanding-against-code-slop.md) - workflows can use AI for mapping, inspecting, and routing code work instead of only generating more code.

## Open Questions

- Which repeated research phases can be compressed without changing the human decision owner?
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
- Which workflow phases should communicate through durable artifacts instead of sharing one long agent context?
- Which prompt surfaces should be refreshed during long-running agent work as context gets compacted or paged out?
- Which code-review workflow signals should explicitly mark whose turn it is to act after comments, replies, or new commits?
- Which enterprise AI research stages produce enough standalone business value to justify continued funding even if the full agent vision changes?
- Which multi-agent workflows need saga-style compensation because partial side effects are unacceptable?
- Which human-in-the-loop waits should be durable workflow state instead of application-owned queues or ad hoc jobs?
- How should teams decide when an RL run is slow-but-healthy versus stuck and worth interrupting?
- Which after-call voice fields should be reviewed by the operator versus routed directly into analytics-only data stores?
- Which LLM workflows have enough labeled examples and metrics to justify DSPy optimization instead of manual prompt iteration?
- Which prompt-learning loops need human explanations before automated optimization is safe?
- Which large-refactor batches should wait for upstream merges, and which can safely proceed speculatively in parallel?
- Which new-hire onboarding steps should be dedicated to configuring role-specific agents before ordinary execution work begins?

## Sources

- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md)
- [Agentic Engineering: Working With AI, Not Just Using It - Brendan O'Leary](../sources/20260407_BEKc4P87XKo.md)
- [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro](../sources/20260109_HY_JyxAZsiE.md)
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
- [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../sources/20260420_mYSRn6PC1mc.md)
- [The New Application Layer - Malte Ubl, CTO Vercel](../sources/20260420_XKup1pj-34M.md)
- [The Friction is Your Judgment - Armin Ronacher & Cristina Poncela Cubeiro, Earendil](../sources/20260418__Zcw_sVF6hU.md)
- [Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI](../sources/20260417_am_oeAoUhew.md)
- [State of the Claw - Peter Steinberger](../sources/20260417_zgNvts_2TUE.md)
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md)
- [AI Didn't Kill the Web, It Moved in! - Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)](../sources/20260410_XZ0boOjtbNo.md)
- [Paperclip: Open Source Human Control Plane for AI Labor - Dotta Bippa](../sources/20260415_h403btjldDQ.md)
- [Judge the Judge: Building LLM Evaluators That Actually Work with GEPA - Mahmoud Mabrouk, Agenta AI](../sources/20260410_X4dEHRzBLmc.md)
- [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik](../sources/20260408_2czYyrTzILg.md)
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md)
- [Contact Center Voice AI: Low-Latency Intelligence Extraction from Messy Audio Streams - Dippu Singh](../sources/20260408_IEF842ZEU5A.md)
- [Platforms for Humans and Machines: Engineering for the Age of Agents - Juan Herreros Elorza](../sources/20260408_cCRO3ChaYhM.md)
- [Cognitive Exhaust Fumes, or: Read-Only AI Is Underrated - Simon Podhajsky, Head of AI, Waypoint](../sources/20260408_u0TOSBbAw7c.md)
- [Practical tactics to build reliable AI apps — Dmitry Kuchin, Multinear](../sources/20250803_-T6uZYYzkWw.md)
- [DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](../sources/20260108_-cKUW6n8hBU.md)
- [Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](../sources/20260108_rcsliSIy_YU.md)
- [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](../sources/20260106_SbcQYbrvAfI.md)
- [The Unreasonable Effectiveness of Prompt Learning - Aparna Dhinakaran, Arize](../sources/20251223_pP_dSNz_EdQ.md)
- [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](../sources/20260106_kmV-qg4uoNI.md)
- [Developer Experience in the Age of AI Coding Agents - Max Kanat-Alexander, Capital One](../sources/20251223_rT2Del5pwg4.md)
- [Claude Agent SDK [Full Workshop] - Thariq Shihipar, Anthropic](../sources/20260105_TqC1qOfiVcQ.md)
- [Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)](../sources/20251230_xz0-brt56L8.md)
- [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](../sources/20260112_k8cnVCMYmNc.md)
- [AGI: The Path Forward - Jason Warner & Eiso Kant, Poolside](../sources/20251227_OGCG_QkCcZo.md)
- [Shipping AI That Works: An Evaluation Framework for PMs - Aman Khan, Arize](../sources/20251226_2HNSG990Ew8.md)
- [The Agent Native Company — Rick Blalock, Agentuity](../sources/20250603_0ZPAvzhpGjw.md)
- [No More Slop - swyx](../sources/20251222_IoiHI7p12Ao.md)
- [Small Bets, Big Impact Building GenBI at a Fortune 100 - Asaf Bord, Northwestern Mutual](../sources/20251223_LU9KgcZDRfY.md)
- [The 3 Pillars of Autonomy - Michele Catasta, Replit](../sources/20251222_MLhAA9yguwM.md)
