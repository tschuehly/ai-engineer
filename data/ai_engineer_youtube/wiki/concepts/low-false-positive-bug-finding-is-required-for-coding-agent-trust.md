# Low-false-positive bug finding is required for coding-agent trust

Summary: Bug-finding agents need precision, not only volume. False-positive-heavy reports create alert fatigue, consume review capacity, and can make teams ignore the real defects the agent was supposed to prevent.

Use when:
- Evaluating coding agents that report vulnerabilities or defects.
- Deciding whether automated bug reports should be trusted, routed to review, or blocked until better validated.

Details:
- Bismuth's benchmark found low true-positive rates for several popular agents; the talk cites cases around 10% or lower and one task where an agent reported 70 issues that were all false. (00:33-01:36)
- False positives create an operational failure, not just a metric problem: no developer will review unbounded piles of bad issues, so trust drops and real bugs can still reach production. (01:36-01:59)
- For vibe coding, poor bug-finding precision is especially risky because agents can quickly add unintended bugs while lacking enough reliable detection ability to find and fix them later. (00:48-00:58)

- **The same conclusion reached from the opposite mechanism, once the reader is an agent rather than a person.** This page's argument is that false positives destroy trust and developers stop reading. Uber's inner-loop finding is that agents never stop reading: "with the inner loop, our accuracy needs actually need to go up, or else we can result in… cavitation of an agent where it fixes something, goes back, gets another code review, and has to kind of like fix backwards because the quality of the comment was low." Alert fatigue is self-limiting — a person who ignores the tool stops paying for its errors. Obedient rework is not, because the agent will act on every wrong finding, repeatedly. The mirror-image observation completes the inversion: "agents are more than happy to go through and fix 100 nits on a pull request where your engineers really get frustrated in situations like that," so precision matters more for agent readers and relevance matters more for human ones. See [Review Comments Have Two Audiences With Inverted Error Costs](review-comments-have-two-audiences-with-inverted-error-costs.md). ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 12:14-12:47)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Make Code Review the Bottleneck Skill for AI-Generated Code](make-code-review-the-bottleneck-skill-for-ai-generated-code.md)
- [Evaluate agent loops with correctness, cost, latency, and step counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Review Comments Have Two Audiences With Inverted Error Costs](review-comments-have-two-audiences-with-inverted-error-costs.md)

Sources:
- [How to Improve your Vibe Coding - Ian Butler](../sources/20250803_g03m-WFEu1U.md), 00:33-01:59
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 12:14-12:47

