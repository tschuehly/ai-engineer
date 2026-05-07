# Evaluate Support Coding Agents by Staged Failure Modes

Summary: Support-oriented coding agents should be evaluated by the distinct decisions they make before and after code generation, not only by whether a final merge request exists.

Use when:
- Designing evals for an agent that triages tickets, decides whether to act, generates code, and asks humans to review.
- Turning production support feedback into regression cases for a coding agent.

Details:
- Scout Agent separates the ticket workflow into categorization, fixability assessment, merge-request generation, support review and test, adjustment requests, and engineering review. (10:09-11:05)
- Zapier's implementation runs plan, execute, and validate phases in a GitLab CI/CD pipeline after diagnosis and fixability checks decide that a ticket should move forward. (11:19-11:55)
- Zapier tracks three questions separately: whether Scout categorized the ticket correctly, whether the ticket was actually fixable, and whether the generated code fix was accurate. (12:39-12:50)
- Early categorization and fixability evals were reported around 75% accuracy, and feedback from processed tickets becomes future test cases for improving Scout. (12:50-13:04)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)
- [Split LLM judges into narrow binary metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)

Sources:
- [Your Support Team Should Ship Code - Lisa Orr, Zapier](../sources/20251216_RmJ4rTLV_x4.md), 10:09-13:04
