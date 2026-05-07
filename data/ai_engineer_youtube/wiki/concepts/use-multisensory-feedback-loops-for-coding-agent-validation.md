# Use Multisensory Feedback Loops for Coding-Agent Validation

Summary: Coding agents need more than unit tests when validating generated software. Pair formal acceptance checks with visual, log, interaction, state, and code-structure signals so the agent can understand both what failed and why.

Use when:
- Designing validation infrastructure for autonomous or semi-autonomous coding-agent loops.
- Explaining why tests alone can miss broken rendering, incorrect state, or bad interaction behavior.

Details:
- Gallon argues that "done" should be defined before implementation through executable tests and observable success criteria, giving agents clear stop conditions and immediate feedback (09:47-10:38).
- Tests verify the specification, while sensors reveal actual behavior as the software is implemented; a feature is done when tests pass and the sensors validate expected behavior (10:41-11:16).
- The multisensory feedback loop gives agents visual signals for what renders, auditory/log signals for what the system reports, and tactile/interaction signals for how the system responds (38:52-39:19).
- Correlating sensory feedback with test results helps the agent understand both the failing acceptance criterion and the likely cause observed in the running system (39:25-39:48).
- The broader feedback system can include screenshots and layout rendering, database or configuration state, session data, code structure, logs, errors, and interaction responses; visual observation can catch broken rendering or incorrect state that logs and tests miss (51:00-52:37).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Autonomous browser verification finds painted-door failures](autonomous-browser-verification-finds-painted-door-failures.md)
- [Treat agent readiness as verification infrastructure](treat-agent-readiness-as-verification-infrastructure.md)

Sources:
- [The Cure for the Vibe Coding Hangover - Corey J. Gallon, Rexmore](../sources/20251124_JsKTQbT58BY.md), 09:47-11:16, 38:52-39:48, 51:00-52:37
