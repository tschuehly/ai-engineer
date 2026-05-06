# Workflows

## Overview

Agent workflows become more reliable when they expose a tight loop between work execution, failure observation, missing-context discovery, and documentation updates. Demand-driven context uses that loop to grow enterprise context from real tasks rather than from speculative upfront curation. Production AI application workflows add another loop: stage the agent, trace it, evaluate it on golden cases, deploy managed prompts/tools/scores, monitor production traces, replay failures, and rerun regression checks before promoting fixes. Personal-agent workflows apply the same idea to permissions and trust: start from one recurring pain, add one simple workflow, watch it fail or succeed, then add guardrails before expanding autonomy. Human-in-the-loop automations make those guardrails concrete by pausing sensitive actions for explicit approval, keeping credentials scoped, and logging waiting or resumed executions. Voice-agent workflows need a similar staged design: start with a narrow realtime conversation path, add tools sparingly, preserve context across handoffs, and validate both transcript behavior and audio delivery before expanding coverage. Coding-agent loops apply the same principle to implementation work: keep each run small, make progress observable, and feed defects or process lessons into the next prompt or skill. For agentic software work, workflow design should deliberately trade upfront planning against later review effort, and should use parallel queues only when the interface preserves human focus around completed work. Outside coding, agents are useful when they shorten feedback cycles for collaborators who can hand over natural artifacts, and when they absorb the prerequisite work that otherwise blocks progress. Context-engine workflows should also surface unresolved source conflicts, recompute from current sources when answers may be stale, and route clarification back into durable context. Skill and context-package workflows should be developed like library workflows: define expected behavior, package guidance, evaluate changes, distribute reusable context, observe use through logs and review, then update shared packages when the workflow changes. Ambient-agent workflows add a maintenance loop: overnight indexing, backups, memory refreshes, update validation, cleanup, and notification filtering keep the system ready without forcing the user to watch every operation.

## Key Concepts

- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - failed work items become the driver for context improvements.
- [Ralph loops process one ticket at a time with fresh context](../concepts/ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md) - narrow repeatable work units reduce orchestration complexity.
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](../concepts/feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md) - each run can improve the instructions that shape later runs.
- [Choose plan-heavy or review-heavy agent workflows by task shape](../concepts/choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md) - workflow design should match planning depth to whether a task can be specified and tested.
- [Parallel coding-agent queues need focus-preserving review interfaces](../concepts/parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md) - long-running agent workflows need queueing and review handoffs that reduce context switching.
- [Agent skills package progressive-disclosure context for repeatable workflows](../concepts/agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) - repeated workflows can be packaged as skills with deeper references loaded on demand.
- [Evaluate agent skills with task scenarios and comparative conditions](../concepts/evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md) - workflow changes can be tested by comparing runs with and without the skill.
- [Validate eval harnesses before trusting skill scores](../concepts/validate-eval-harnesses-before-trusting-skill-scores.md) - workflow evals need checks for evaluator mistakes, not just agent mistakes.
- [Surface unresolved context conflicts to agents and users](../concepts/surface-unresolved-context-conflicts-to-agents-and-users.md) - context workflows should turn unresolved contradictions into explicit clarification points.
- [Do not cache context-engine answers as durable truth](../concepts/do-not-cache-context-engine-answers-as-durable-truth.md) - workflows should avoid carrying stale generated answers forward as if they were source truth.
- [Context development lifecycle treats context as an engineered artifact](../concepts/context-development-lifecycle-treats-context-as-an-engineered-artifact.md) - context work should follow a generate, evaluate, distribute, observe, and adapt loop.
- [Use agent logs and review feedback as context observability signals](../concepts/use-agent-logs-and-review-feedback-as-context-observability-signals.md) - workflow failures should feed shared context updates rather than repeated local fixes.
- [Package reusable context as skills, libraries, and registries](../concepts/package-reusable-context-as-skills-libraries-and-registries.md) - reusable workflow context can be installed and maintained across projects.
- [Grow personal-agent permissions incrementally from recurring pain](../concepts/grow-personal-agent-permissions-incrementally-from-recurring-pain.md) - personal automation should expand through small, trusted, reversible steps.
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
- [Code-backed content can replace fragile CMS workflows for agents](../concepts/code-backed-content-can-replace-fragile-cms-workflows-for-agents.md) - repository-backed structured content lets agents make reviewable operational updates.

## Open Questions

- How should teams decide when a failure-driven context update is durable enough to enter the shared knowledge base?
- How should a loop decide when to stop, ask for human review, or continue to the next ticket?
- How should teams retire or rewrite skills that are no longer loaded or no longer match the current workflow?
- How should context-engine clarification from users be converted into durable, source-backed memory without preserving bad generated answers?
- How should organizations decide when an individual prompt improvement is mature enough to publish as shared team context?
- When does parallel agent execution improve throughput, and when does it merely create review backlog?
- What evidence is enough to promote a personal-agent workflow from playground testing into daily ambient operation?
- Which actions should require a hard approval gate even when the user has already granted the agent broad tool access?
- How should synthetic voice conversations be promoted from exploratory testing into durable workflow eval cases?
- When should a production AI workflow add another stage, and when does the extra stage add more operational risk than debugging value?
- Which non-engineering workflows become better when agents accept natural artifacts, and which need stricter data-entry constraints?

## Sources

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
