# Treat AI Coding as Safe Software Change

Summary: AI coding should be evaluated as the ability to change production software safely, not as the amount of code a model can emit. Generated code still carries operational, security, maintenance, and incident-response obligations.

Use when:
- Evaluating whether AI coding belongs in a production engineering workflow.
- Challenging line-count or percentage-of-code-generated claims about AI productivity.

Details:
- Code is an artifact of software engineering, while the engineering job includes decisions about behavior, architecture, dependencies, tradeoffs, availability, data safety, and production operations. (04:11-04:45)
- Every generated line creates maintenance and debugging responsibility; maximizing code volume can make the system worse if the code is not needed, understandable, or supportable. (04:47-05:20)
- Complex production systems fail through emergent behavior that is not visible in isolated lines of code, so humans still need enough system understanding to diagnose and repair failures. (02:00-02:32)
- Vibe coding, defined here as letting AI write and reason through code without examining it, is not enough for software with high availability, many users, large data sets, or security obligations. (03:14-04:08)
- Safe change still depends on engineering practices such as codebase knowledge, version control, tests, type systems, deployment strategies, and context. (06:38-07:35)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Treat slop as a quality failure, not an AI provenance label](treat-slop-as-a-quality-failure-not-an-ai-provenance-label.md)
- [Reliability thresholds determine whether coding agents save time](reliability-thresholds-determine-whether-coding-agents-save-time.md)

Sources:
- [Vibes won't cut it - Chris Kelly, Augment Code](../sources/20250803_Dc3qOA9WOnE.md), 02:00-07:35
