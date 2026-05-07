# Low-false-positive bug finding is required for coding-agent trust

Summary: Bug-finding agents need precision, not only volume. False-positive-heavy reports create alert fatigue, consume review capacity, and can make teams ignore the real defects the agent was supposed to prevent.

Use when:
- Evaluating coding agents that report vulnerabilities or defects.
- Deciding whether automated bug reports should be trusted, routed to review, or blocked until better validated.

Details:
- Bismuth's benchmark found low true-positive rates for several popular agents; the talk cites cases around 10% or lower and one task where an agent reported 70 issues that were all false. (00:33-01:36)
- False positives create an operational failure, not just a metric problem: no developer will review unbounded piles of bad issues, so trust drops and real bugs can still reach production. (01:36-01:59)
- For vibe coding, poor bug-finding precision is especially risky because agents can quickly add unintended bugs while lacking enough reliable detection ability to find and fix them later. (00:48-00:58)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Make Code Review the Bottleneck Skill for AI-Generated Code](make-code-review-the-bottleneck-skill-for-ai-generated-code.md)
- [Evaluate agent loops with correctness, cost, latency, and step counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)

Sources:
- [How to Improve your Vibe Coding - Ian Butler](../sources/20250803_g03m-WFEu1U.md), 00:33-01:59

