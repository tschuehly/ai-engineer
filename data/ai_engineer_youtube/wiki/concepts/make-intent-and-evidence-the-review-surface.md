# Make Intent and Evidence the Review Surface

Summary: Replace the diff as the primary review artifact with two things a human can actually judge at agent throughput: the intent (acceptance criteria derived from the coding session, plus codified invariants) and the evidence (a generated test plan executed against a live preview, producing screenshots and database snapshots). The reviewer reads the plan and the evidence; architecture arguments still happen, one level above the lines.

Use when:
- Designing what an agent-written change should present to a human reviewer.
- Building verification infrastructure for a team that can no longer read every diff.
- Deciding where human judgment goes once line-by-line review stops scaling.

Details:
- The pipeline, end to end: session → capture user responses → acceptance criteria; "the acceptance criteria then tied with your AI slo[p] register that you are now constantly maintaining finally creates a test plan"; then "the verification system… spins up a preview, takes your test plan and make[s] sure it actually works end-to-end." Stated as a formula: "the criteria plus invariant is what makes the test plan." (08:19-08:51, 10:30-10:44)
- The reframe: "this is now your review surface. You're not reviewing code line by line, but rather you're looking at the evidence of what was the intent, did the user actually implement the capability that was defined in the intent, and did the behavior actually meet the requirements that we had in the… acceptance criteria." (08:57-09:21)
- What the human keeps: "the value of human in the loop here is the governance and the review part, and the part where you're reviewing the test plan and not the code," and the conversation moves up a level to data models and service interactions rather than disappearing. (11:01-11:13, 13:48-14:04)
- The check the diff cannot perform: "Even if the code looks right, does it actually work?" Reviewing the change for plausibility is not the same as observing the behavior it was supposed to produce. (08:51-08:55)
- Evidence is concrete and reviewer-facing, not just an agent self-check. For a new payment form, "an AI agent can go and browse through your application to fill out a form and capture screenshots as evidence. And then take those screenshots as well as your database snapshots to identify whether the criteria was met… you're creating more solid evidence, which now a reviewer can look at and build more confidence that this actually works." (12:16-13:05)
- The execution rule for the verifier: "It's deterministic where it can be, but LLM where you must. Not everything can be deterministic… This is where you use LLM as a fallback." Determinism is the default and the model is the escape hatch, not the other way round. (11:47-12:16)
- Relationship to older practice, stated by the speaker: this is "closer to behavior-driven development" than to TDD — the test plan is in English and shareable with product managers and designers, "everyone can participate," while deterministic verification still checks whether each criterion was met. (11:13-11:43)
- The strongest and least-proven claim on the page: "even imagine if you're building a new feature, you don't have to maintain tests at all. This is creating tests in real time." Per-change generated test plans avoid suite maintenance, but they also give up the regression net a persistent suite provides — the talk does not address what catches a later change that breaks this one, so treat plan generation as a complement to a regression suite until someone measures the substitution. (10:44-11:01)
- Load-bearing precondition: the test plan must not be derived from the code the agent just wrote, or it inherits that agent's blind spots (see the related self-verification concept). Its independence comes from being derived from the human's session decisions.
- Caveat on provenance: this is the architecture of a vendor's product (Aviator, piloting "Verify" with design partners), presented as a design argument with a worked example rather than as measured results. No pass rates, reviewer-time savings, or escaped-defect numbers are given.
- **The same pair, reached from the opposite direction and for a different reason.** Coyle builds a critic subagent whose entire context is the claim and the evidence — "this is your claim is sort of how we're going to solve the problem. Here's the evidence, but we're not giving it the thought processes that went in to creating this claim." This page argues intent and evidence are what a reviewer *needs*; that one argues the reasoning trace is what a reviewer must *not* be given, because agents that read each other's thinking converge ([Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)). The two are compatible and the second sharpens the first: the reason to keep the surface narrow is not only reviewer attention but reviewer independence. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 13:44-15:12)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Capture the Coding Session as the Intent Record](capture-the-coding-session-as-the-intent-record.md)
- [Mine Recurring Review Comments Into an Invariant Registry](mine-recurring-review-comments-into-an-invariant-registry.md)
- [Code Review Carries Alignment, Not Just Correctness](code-review-carries-alignment-not-just-correctness.md)
- [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)
- [Autonomous Browser Verification Finds Painted-Door Failures](autonomous-browser-verification-finds-painted-door-failures.md)
- [Verify Spec Adherence With Executable, Readable BDD Scenarios](verify-spec-adherence-with-executable-readable-bdd-scenarios.md)
- [Review bundles compress parallel agent output into evidence](review-bundles-compress-parallel-agent-output-into-evidence.md)
- [Wrap agent completion in an automatic deterministic verification gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)
- [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)

Sources:
- [How to Kill the Code Review — Ankit Jain, Aviator](../sources/20260817_YgEv7IQzGdM.md), 08:19-09:30, 10:30-13:05, 13:48-14:12, 15:40-16:04
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 13:44-15:12
