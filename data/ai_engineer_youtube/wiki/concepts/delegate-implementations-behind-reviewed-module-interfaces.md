# Delegate Implementations Behind Reviewed Module Interfaces

Summary: Agent delegation is safer when humans retain the system shape: module boundaries, interfaces, behavior, and tests. Agents can then implement inside those boundaries without forcing reviewers to understand every internal line.

Use when:
- Designing codebase architecture that lets agents work without eroding human understanding.
- Reviewing whether an autonomous coding task has enough module and test boundaries.

Details:
- The source warns that heavy delegation can make engineers know the codebase less well, effectively handing the system's shape to AI. (01:19:43-01:19:59)
- The proposed mitigation is to design module interfaces and behavioral contracts, then delegate implementation details behind those interfaces. (01:20:19-01:20:38)
- Review can focus on whether a module behaves under specified conditions instead of inspecting every internal detail. (01:20:36-01:21:07)
- End-to-end module tests can expose a complete flow to the agent; the example wraps browser video-editor behavior so the agent can see, change, and test the whole path. (01:22:16-01:23:02)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)

Sources:
- [Full Walkthrough: Workflow for AI Coding - Matt Pocock](../sources/20260424_-QFHIoCo-Ko.md), 01:19:43-01:23:02

