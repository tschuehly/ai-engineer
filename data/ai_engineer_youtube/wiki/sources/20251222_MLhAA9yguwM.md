# The 3 Pillars of Autonomy - Michele Catasta, Replit

Source: [The 3 Pillars of Autonomy - Michele Catasta, Replit](https://www.youtube.com/watch?v=MLhAA9yguwM)
Uploaded: 2025-12-22
Transcript: `raw/20251222_MLhAA9yguwM/MLhAA9yguwM.en-orig.vtt`

## Summary

Michele Catasta frames coding-agent autonomy around Replit's non-technical-user problem: agents must make technical decisions, verify their own work, manage context without relying only on huge context windows, and use parallelism carefully enough that users are not left to decompose tasks or resolve merge conflicts.

## Extracted Concepts

- [Scope coding-agent autonomy by user decision authority](../concepts/scope-coding-agent-autonomy-by-user-decision-authority.md) - autonomy should mean taking technical decisions inside a scoped task, especially when users cannot supervise implementation.
- [Autonomous browser verification finds painted-door failures](../concepts/autonomous-browser-verification-finds-painted-door-failures.md) - browser-level feedback catches broken UI paths, mock data, missing handlers, and hallucinated completion claims.
- [Offload long-horizon agent state outside the context window](../concepts/offload-long-horizon-agent-state-outside-the-context-window.md) - files, plans, documentation, and scoped subagents can preserve coherence without stuffing all state into context.
- [Let the core agent loop orchestrate parallel subtasks](../concepts/let-the-core-agent-loop-orchestrate-parallel-subtasks.md) - parallel coding needs agent-led decomposition and conflict-aware task shaping, not only user-dispatched threads.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Replit's target user is a non-technical knowledge worker, so the agent must offload technical decisions while keeping the user's control focused on what they are building rather than how it is implemented. 01:59-03:01
- The talk distinguishes supervised autonomy, where the user still needs the equivalent of a driving license, from a back-seat experience where the agent handles technical execution for users without that expertise. 02:01-02:59
- Autonomy is not the same as long runtime: narrow tasks can be autonomous and fast, while broad tasks naturally create longer gaps between user interactions. 04:18-05:31
- The proposed autonomy target is reducible runtime: spans where the user does not need to make technical decisions while the agent plans, implements, and tests. 05:55-06:46
- Verification is one of the pillars because untested agents create "painted doors" such as clickable-looking buttons without handlers or UI backed by mock data rather than real state. 08:31-09:24
- Replit found that more than 30% of individually generated features were broken on the first attempt, implying that almost every generated app could contain at least one broken feature if the agent does not test. 09:10-09:24
- Autonomous testing should gather feedback from the environment because non-technical users cannot reliably provide the technical feedback needed for agent progress. 09:48-10:33
- Browser verification spans static analysis, code execution, unit tests, API tests, computer use, DOM-based browser use, and Playwright scripts; Replit favors Playwright because LLMs can write expressive reusable tests. 11:12-14:56
- Context management can support long trajectories without 10M or 100M token windows by using code, docs, plans, task lists, file-system memory, and scoped subagents as state surfaces. 15:13-16:35
- Subagents start from fresh context, receive only the subset needed for their concern, return outputs to the main loop, and reduce context pollution. 17:00-18:16
- Parallel agents trade extra compute for time and UX, but duplicate shared context and create merge-conflict burden when humans manually dispatch and reconcile threads. 20:00-23:13
- Replit's next parallelism direction is to make the core loop the orchestrator so the agent decomposes subtasks on the user's behalf and shapes them to reduce collisions. 23:14-24:16
