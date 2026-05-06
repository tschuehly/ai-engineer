# Use Deep Modules to Make Agent Work Testable

Summary: Deep modules make AI coding easier to supervise because they hide substantial functionality behind simple, testable interfaces. Shallow module sprawl forces agents and humans to navigate many small dependencies and carry too much context.

Use when:
- Refactoring a codebase so agents can work within clearer boundaries.
- Deciding where humans should retain interface control while agents implement internals.

Details:
- Pocock contrasts deep modules, which hide complexity behind simple interfaces, with shallow modules that expose many functions and little internal functionality. (12:42-13:14)
- Shallow module sprawl is difficult for agents to explore; the agent may miss the right module or fail to understand dependencies in time. (13:18-13:53)
- Deep module boundaries improve testability because the workflow can test and verify at the interface instead of reading every internal line. (14:54-15:04)
- Humans should retain control over module interfaces and design, while agents can handle internals when the boundary is testable and the module is not too critical for lighter review. (15:40-16:31)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Delegate implementations behind reviewed module interfaces](delegate-implementations-behind-reviewed-module-interfaces.md)
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)

Sources:
- ["Software Fundamentals Matter More Than Ever" - Matt Pocock](../sources/20260423_v4F1gFy-hqg.md), 12:42-16:31
