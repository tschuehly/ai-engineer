# Workflows

## Overview

Agent workflows become more reliable when they expose a tight loop between work execution, failure observation, missing-context discovery, and documentation updates. Demand-driven context uses that loop to grow enterprise context from real tasks rather than from speculative upfront curation. Coding-agent loops apply the same principle to implementation work: keep each run small, make progress observable, and feed defects or process lessons into the next prompt or skill.

## Key Concepts

- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - failed work items become the driver for context improvements.
- [Ralph loops process one ticket at a time with fresh context](../concepts/ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md) - narrow repeatable work units reduce orchestration complexity.
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](../concepts/feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md) - each run can improve the instructions that shape later runs.

## Open Questions

- How should teams decide when a failure-driven context update is durable enough to enter the shared knowledge base?
- How should a loop decide when to stop, ask for human review, or continue to the next ticket?

## Sources

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md)
