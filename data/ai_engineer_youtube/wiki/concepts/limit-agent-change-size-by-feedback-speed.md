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

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Delegate implementations behind reviewed module interfaces](delegate-implementations-behind-reviewed-module-interfaces.md)

Sources:
- ["Software Fundamentals Matter More Than Ever" - Matt Pocock](../sources/20260423_v4F1gFy-hqg.md), 10:28-12:15
