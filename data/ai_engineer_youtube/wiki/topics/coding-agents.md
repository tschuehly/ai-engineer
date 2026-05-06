# Coding Agents

## Overview

Coding agents work best when their autonomy is constrained by small work items, visible checks, isolated workspaces, and explicit handoff rules. The Ralph loop pattern favors a simple repeated cycle over elaborate orchestration: pick one ticket, implement it, validate it, update status, and let the next run continue with the improved prompt, skill, or work queue. This reduces the coordination burden that appears when many agents attempt a large dependency graph at once. As agents write more of the implementation, human effort shifts toward planning, reviewing, QA, and shepherding changes. The right balance depends on task shape: specifiable back-end, refactor, migration, and maintenance work can be plan-heavy and test-driven, while exploratory front-end work may require tighter review loops. Productized codegen agents also need protection against model rot and runaway variation: serve fresh documentation, provide small exemplar projects that show the desired architecture, and breadcrumb the agent through discovery, event planning, and implementation rather than asking for the final integration in one jump. Even a minimal coding agent still needs a disciplined tool loop: file and shell tools should be explicitly declared, model-required actions should be checked against the available tool map, and destructive or unsupported operations should not be executed just because the model or user suggests them. Parallel coding can be made more useful when project worktrees isolate feature or bugfix threads, when custom subagents receive task-appropriate models, tools, and permissions, and when a parent agent compares or synthesizes outputs. Prompt-enforced workspace isolation still needs explicit evals because a model can drift back into the primary checkout. Parallel orchestration also needs observability beyond terminal logs: spatial maps can show which files each agent touches, heat maps can surface collisions, quest queues can keep background work flowing, and review bundles can attach task summaries plus screenshots or videos to each output. Hooks add another workflow layer for setup, logging, and continuation rituals, while privilege approval gates keep sensitive filesystem, server, or network-exposure actions from becoming all-access defaults. Context engines add another reliability layer by giving the agent system-specific decisions, reviewers, owners, and expert signals before it spends tokens rediscovering them from the repository.

## Key Concepts

- [Ralph loops process one ticket at a time with fresh context](../concepts/ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md) - simple repeated ticket execution can ship more reliably than broad multi-agent plans.
- [Unified coding-agent harnesses combine models, tools, environments, and safety](../concepts/unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md) - model capability needs an execution harness that manages tools, environments, and safety.
- [Isolate parallel coding work with project worktrees](../concepts/isolate-parallel-coding-work-with-project-worktrees.md) - separate work streams reduce interference between concurrent feature, bugfix, and investigation tasks.
- [Customize subagents by task, model, tools, and permissions](../concepts/customize-subagents-by-task-model-tools-and-permissions.md) - specialist subagents should receive only the capabilities their role needs.
- [Use agent hooks to automate session rituals](../concepts/use-agent-hooks-to-automate-session-rituals.md) - lifecycle hooks can automate setup, logging, and final validation passes.
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](../concepts/feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md) - review outputs, tests, and generated critiques become inputs to the next run.
- [Use independent validation contexts to reduce agent confirmation bias](../concepts/use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md) - separate validation contexts can catch defects the producing agent misses.
- [Coding agents shift engineering work toward planning and review](../concepts/coding-agents-shift-engineering-work-toward-planning-and-review.md) - agent-written code increases the importance of task definition, review, QA, and change shepherding.
- [Choose plan-heavy or review-heavy agent workflows by task shape](../concepts/choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md) - task type should determine whether humans invest more in upfront specification or iterative review.
- [Parallel coding-agent queues need focus-preserving review interfaces](../concepts/parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md) - long-running agent work benefits from queueing, diffs, previews, and focused review handoffs.
- [Spatial agent maps expose filesystem-level lineage and collisions](../concepts/spatial-agent-maps-expose-filesystem-level-lineage-and-collisions.md) - spatial repository projections make parallel agent edits easier to inspect and deconflict.
- [Let agents propose quest queues for parallel work](../concepts/let-agents-propose-quest-queues-for-parallel-work.md) - agent-discovered missions turn maintenance and follow-up work into selectable queues.
- [Review bundles compress parallel agent output into evidence](../concepts/review-bundles-compress-parallel-agent-output-into-evidence.md) - review artifacts should summarize task intent, changed work, rationale, and visual proof.
- [Prompt-coded product behavior reduces code but weakens hard guarantees](../concepts/prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md) - prompt-backed coding workflows reduce product code but may lose hard workspace constraints.
- [Fresh Markdown context mitigates model rot in codegen](../concepts/fresh-markdown-context-mitigates-model-rot-in-codegen.md) - current docs reduce hallucinated keys, APIs, and setup patterns.
- [Model airplanes give coding agents token-efficient exemplars](../concepts/model-airplanes-give-coding-agents-token-efficient-exemplars.md) - thin reference projects show successful integration shape without full app complexity.
- [Breadcrumb coding agents through staged discovery and implementation](../concepts/breadcrumb-coding-agents-through-staged-discovery-and-implementation.md) - staged prompts reduce improvisation while preserving agent flexibility.
- [Evaluate workspace isolation with positive and negative filesystem scorers](../concepts/evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md) - isolation evals should check both intended edits and forbidden checkout changes.
- [Use parent agents to compare and merge parallel subagent outputs](../concepts/use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md) - parallel subagent work becomes easier to review when a parent compares and combines results.
- [Use social and expert graphs to personalize coding-agent context](../concepts/use-social-and-expert-graphs-to-personalize-coding-agent-context.md) - reviewer and ownership graphs can tell agents whose conventions and decisions matter for a change.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - context engines reduce irrelevant exploration before a coding task.
- [Agent tool loops turn model-required actions into executable results](../concepts/agent-tool-loops-turn-model-required-actions-into-executable-results.md) - coding-agent file and shell access needs validated tool execution and loop termination.
- [Agent software factories need runnable, contextual, and verifiable primitives](../concepts/agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md) - autonomous coding work depends on repository structure, setup commands, external context, and validation.
- [Agent rules should emerge from observed off-rail behavior](../concepts/agent-rules-should-emerge-from-observed-off-rail-behavior.md) - repository rules should encode concrete repeated failures and sensitive boundaries.
- [Cloud agents turn coding work into asynchronous VM-backed queues](../concepts/cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md) - VM-backed agents turn implementation into background work that still needs review and context routing.
- [Align teams before agents implement](../concepts/align-teams-before-agents-implement.md) - unaligned agentic speed can create wrong features, duplicated work, and late PR rejection.
- [Shared cloud workspaces make agent sessions collaborative](../concepts/shared-cloud-workspaces-make-agent-sessions-collaborative.md) - shared micro-VM sessions let teammates inspect and continue agent work without local checkout friction.
- [Collaborative plans become executable agent context](../concepts/collaborative-plans-become-executable-agent-context.md) - plan mode should be shareable and editable before the coding agent starts implementation.
- [Social context dashboards keep agentic teams oriented](../concepts/social-context-dashboards-keep-agentic-teams-oriented.md) - team summaries help reviewers and collaborators keep up with high-volume agentic work.

## Open Questions

- What ticket sizes and dependency patterns are small enough for unattended coding-agent loops?
- Which validation responsibilities should stay in deterministic tests versus independent review agents?
- Which workspace boundaries must be enforced by the runtime rather than by prompt instructions?
- Which integration examples are thin enough to remain token-efficient while still giving agents the right architectural shape?
- What repository activity signals are reliable enough to infer code ownership or expertise for agent context?
- Which front-end QA capabilities are strong enough to move visual and interaction review out of human back-and-forth?
- Which file or shell operations should a minimal coding-agent runtime refuse even when the user prompt asks for them?
- Which session hooks are useful enough to automate, and which create hidden agent behavior that should remain explicit?
- Which repository-readiness checks predict whether a cloud agent can run without human setup intervention?
- What shared planning artifact is sufficient before multiple teammates or agents start related work?
- How should agent-suggested work queues be prioritized so they create useful leverage rather than review backlog?

## Sources

- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [Software Engineering Is Becoming Plan and Review - Louis Knight-Webb, Vibe Kanban](../sources/20260502_W76woOYHlvY.md)
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md)
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md)
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md)
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md)
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md)
- [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment - Maggie Appleton, GitHub](../sources/20260426_ClWD8OEYgp8.md)
- [AgentCraft: Putting the Orc in Orchestration - Ido Salomon](../sources/20260425_kR64LOqBBCU.md)
