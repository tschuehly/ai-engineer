# Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI

Source: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew)
Uploaded: 2026-04-17
Transcript: `raw/20260417_am_oeAoUhew/am_oeAoUhew.en-orig.vtt`

## Summary

Ryan Lopopolo frames harness engineering as the work of making abundant coding-agent output useful by shifting human effort toward systems design, delegation, durable context, guardrails, and review automation. The talk argues that teams should make non-functional requirements legible to agents through documentation, rules files, lints, reviewer agents, and prompt surfaces embedded throughout the development workflow.

## Extracted Concepts

- [Harness engineering shifts scarcity from code production to control surfaces](../concepts/harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md) - this source frames implementation as abundant while human time, attention, and context remain scarce.
- [Encode non-functional requirements as agent-visible context](../concepts/encode-non-functional-requirements-as-agent-visible-context.md) - this source explains how quality expectations, QA plans, ADRs, and review history become durable agent guidance.
- [Use reviewer agents and lints to turn review lessons into guardrails](../concepts/use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md) - this source gives concrete examples of CI reviewer agents and bespoke lints for reliability and security checks.
- [Treat prompts as distributed harness surfaces](../concepts/treat-prompts-as-distributed-harness-surfaces.md) - this source identifies rules files, skills, lint messages, PR comments, and tests as places where teams inject guidance into agent trajectories.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

## Notes

- Lopopolo argues that when coding agents can produce code at high volume, the engineering role shifts toward productively deploying that capacity through systems thinking, system design, and delegation. (02:09-03:09)
- The talk identifies human time, human/model attention, and model context window as the scarce resources, with synchronous human implementation time moved toward higher-leverage activities. (05:10-05:37)
- Durable process artifacts such as breadcrumbs, documentation, ADRs, persona-oriented documentation, historical tickets, and code reviews are described as the process evidence agents need to reproduce team-quality work. (06:54-07:25)
- The source stresses that teams should write down underspecified non-functional requirements so agents can see what counts as acceptable merged code, then refine outputs when agents miss that bar. (08:28-09:57)
- Reviewer agents can run during pushes and CI, using documentation plus proposed patches to ask whether network code includes retries and timeouts or whether an interface is secure and hard to misuse. (12:00-12:30)
- Bespoke lints can make reliability lessons durable, such as checking every `fetch` call for retry and timeout handling after a class of outages. (12:56-13:21)
- The talk treats rules files, skills, lint errors, reviewer-agent PR comments, and agent SDK checks in tests as prompt surfaces that keep agent work aligned without changing model weights. (15:10-16:15)
