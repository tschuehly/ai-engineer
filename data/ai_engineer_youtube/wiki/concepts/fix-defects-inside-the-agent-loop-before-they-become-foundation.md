# Fix Defects Inside the Agent Loop Before They Become Foundation

Summary: The argument for verifying inside the agent's loop rather than at PR time is not that CI is slow — it is that a multi-loop agent build keeps going. An unfixed defect becomes the code the next loop reads, extends, and imitates, so issues surfaced during generation "can then be fixed immediately by the agent so they don't propagate into future agentic loops." The same verification regime then runs again in the outer CI/CD loop; in-loop checking replaces neither the gate nor review.

Use when:
- Deciding where quality checks belong in an agentic pipeline, and the existing argument for moving them earlier is only about feedback latency.
- An agent builds a feature across many loops or sessions and later work is visibly shaped by earlier mistakes.
- Justifying an in-loop verification tool call against the objection that CI already catches this.
- Designing the exit condition for an agent's turn.

Details:
- **The propagation argument.** The agent "can call in to us and… get a list of issues that we are finding in real time in the code that's being written and the great thing about that is those issues can then be fixed immediately by the agent so they don't propagate into future agentic loops that are going to run in order to fully build out the software project." The cost of a late catch is not one delayed fix but every subsequent loop that built on the defect. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 17:41-17:59)
- **Both loops, not one.** Stated as a requirement: "The verification needs to run in both the inner agentic loop and also in the outer loop for CICD." The outer loop keeps the blocking role — a PR "won't… go past into production unless it gets a passing grade" — so the in-loop layer is a way to arrive at the gate clean, not a way to skip it. (18:25-19:04)
- **The turn's exit condition becomes the verifier's verdict.** In the demo, Cursor is given a task, calls a context tool up front, writes, and on completing "the initial write, it's going to call into our verification process to get a list of issues." It fixes them, reruns the analysis, "and then it will not proceed until it actually is able to get a passing grade from us on the verification pass." That makes passing verification a precondition for advancing rather than a report the agent may read and ignore. Integrations are named for Cursor, Claude Code, Codex, and Antigravity. (19:05-19:57)
- **Remediation belongs to the agent, which is what makes the loop close.** The Solve phase is described as "allowing the agent to have the agency to do so itself by providing access to the tools it needs to… find the issues and fix them itself and then just repeat the loop" — findings routed to a human queue do not stop propagation, because the agent keeps building while the queue waits. Restated in the closing takeaways as "use agents to solve their own mistakes. Empower them to do that." (11:39-11:55, 21:33-21:38)
- **What this adds to the wiki's shift-left thread.** [Shift Code Quality Left With a Pre-Commit Analysis and Remediation Loop](shift-code-quality-left-with-precommit-analysis-loop.md) records the same vendor's earlier account, where the argument for moving left was latency — 1-5 seconds pre-commit against 1-5 minutes in CI. Latency argues for a faster check anywhere; propagation argues specifically for *inside the loop*, and it is the argument that survives if CI ever becomes fast. Read alongside [Limit Agent Change Size by Feedback Speed](limit-agent-change-size-by-feedback-speed.md): both make the unit of agent work the unit at which correctness is established.
- **A related caution the talk raises about the loop's other end.** Guidance quality bounds what in-loop verification can do, and the guidance must be served rather than dumped: "you can't just throw your entire code base at the agent up front. It's going to spend a lot of time thrashing and exploring and burning tokens." Note that this reverses the same vendor's earlier position of pushing the whole codebase into context; the narrower position is the one recorded here, and neither talk acknowledges the change. (17:19-17:35)
- Caveat: no measurement of the in-loop layer appears anywhere in the talk — no defect-rate comparison against PR-time-only checking, no latency figure for the verification call, no false-positive rate, and no cost for running analysis on every loop. The demo was a pre-recorded video. The propagation claim is a mechanism argument, not a result.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Shift Code Quality Left With a Pre-Commit Analysis and Remediation Loop](shift-code-quality-left-with-precommit-analysis-loop.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md)
- [Run Verify-Fix-Review Loops for Agentic Refactors](run-verify-fix-review-loops-for-agentic-refactors.md)
- [Limit Agent Change Size by Feedback Speed](limit-agent-change-size-by-feedback-speed.md)
- [AI Code Quality Needs Full-SDLC Workflows](ai-code-quality-needs-full-sdlc-workflows.md)

Sources:
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 11:39-11:55, 17:19-17:59, 18:25-19:57, 21:33-21:38
