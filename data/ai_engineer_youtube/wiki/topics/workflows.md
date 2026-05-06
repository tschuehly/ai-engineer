# Workflows

## Overview

Agent workflows become more reliable when they expose a tight loop between work execution, failure observation, missing-context discovery, and documentation updates. Demand-driven context uses that loop to grow enterprise context from real tasks rather than from speculative upfront curation. Coding-agent loops apply the same principle to implementation work: keep each run small, make progress observable, and feed defects or process lessons into the next prompt or skill. Skill workflows should be developed the same way: define expected behavior, package guidance, run task scenarios, inspect failures, and update the skill when the workflow changes.

## Key Concepts

- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - failed work items become the driver for context improvements.
- [Ralph loops process one ticket at a time with fresh context](../concepts/ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md) - narrow repeatable work units reduce orchestration complexity.
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](../concepts/feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md) - each run can improve the instructions that shape later runs.
- [Agent skills package progressive-disclosure context for repeatable workflows](../concepts/agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) - repeated workflows can be packaged as skills with deeper references loaded on demand.
- [Evaluate agent skills with task scenarios and comparative conditions](../concepts/evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md) - workflow changes can be tested by comparing runs with and without the skill.
- [Validate eval harnesses before trusting skill scores](../concepts/validate-eval-harnesses-before-trusting-skill-scores.md) - workflow evals need checks for evaluator mistakes, not just agent mistakes.

## Open Questions

- How should teams decide when a failure-driven context update is durable enough to enter the shared knowledge base?
- How should a loop decide when to stop, ask for human review, or continue to the next ticket?
- How should teams retire or rewrite skills that are no longer loaded or no longer match the current workflow?

## Sources

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md)
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
