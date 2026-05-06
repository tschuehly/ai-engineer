# Browser agents sit in the prompt-injection lethal trifecta

Summary: Browser-based agents are especially exposed to prompt injection because they combine private user data, untrusted web content, and channels that can communicate or act externally.

Use when:
- Designing AI browser features such as page summarization, autofill, email drafting, scheduling, or computer use.
- Threat-modeling prompt injection in agents that read web pages and can use private context or take actions.

Details:
- A hidden prompt injection in webpage HTML can redirect a summarization task into opening a new website and exfiltrating personal information through URL parameters. (13:14-13:40)
- The browser sits in a "lethal trifecta": it has access to private data, it reads untrusted content, and it can communicate externally by opening websites, sending emails, scheduling events, or similar actions. (13:40-14:05)
- Wrapping untrusted context in tags is weak because attackers can escape it; separating instructions and third-party content into roles with random tags can help but does not guarantee safety. (14:08-15:01)
- Product design must assume prompt injections will still happen, blending technical controls with user experience. Dia's autofill pattern asks users to inspect and confirm generated data in plain text before writing to a form, and similar confirmations are used for scheduling and email actions. (15:01-16:14)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [LLM guardrails need checkpoints at every untrusted boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Human approval can hide tool-description and parameter risk](human-approval-can-hide-tool-description-and-parameter-risk.md)

Sources:
- [From Arc to Dia: Lessons learned building AI Browsers - Samir Mody, The Browser Company of New York](../sources/20251219_o4scJaQgnFA.md), 12:50-16:14
