# Limit Agent Change Size by Feedback Speed

Summary: Agent coding work should move no faster than its feedback loops can verify. Tests, type checks, and small deliberate changes prevent the agent from producing a large unverified diff before discovering basic failures.

Use when:
- An agent is generating large code changes before running checks.
- Designing prompts, skills, or workflow gates for test-driven agent implementation.

Details:
- Pocock observes that agents often produce too much code before type-checking, testing, or otherwise using available feedback. (10:28-10:50)
- He applies the "outrunning your headlights" metaphor: the rate of feedback is the speed limit, so the workflow should force small steps and frequent checks. (10:50-11:11)
- TDD helps by making the agent create a test first, make it pass, then refactor with design in mind. (11:11-11:29)
- Testing remains a design problem: teams must choose unit size, mocks, and behaviors, and large flaky units can weaken the feedback loop. (11:33-12:15)
- **A second sizing rule that binds before any code exists.** Blum sizes a plan's phases by the reviewer rather than by the check: "would I want to review the PR that will correspond to that part? If it's going to be too big for me to want to review in one sitting… 'I'm going to need to get a cup of coffee before I read this' — that means it's too big and I'm going to want to have it broken down into pieces." Feedback speed sizes a change by how fast the loop closes; this sizes it by human reading stamina, and it is applied at plan-writing time rather than at execution time. The two can disagree — a change with a two-second test suite can still be a 600-line diff — and where they do, the human bound governs whether the change actually gets reviewed rather than skimmed. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 09:01-09:27)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Delegate implementations behind reviewed module interfaces](delegate-implementations-behind-reviewed-module-interfaces.md)
- [Structure an Agent Plan With a Frozen Why and Reviewer-Sized Phases](structure-an-agent-plan-with-a-frozen-why-and-reviewer-sized-phases.md)

Sources:
- ["Software Fundamentals Matter More Than Ever" - Matt Pocock](../sources/20260423_v4F1gFy-hqg.md), 10:28-12:15
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 09:01-09:27
