# Use Reviewer Agents and Lints to Turn Review Lessons Into Guardrails

Summary: Repeated review findings should become harness guardrails that run automatically. Reviewer agents, CI checks, and bespoke lints can turn reliability and security lessons into recurring constraints instead of relying on humans to remember every non-functional requirement.

Use when:
- A team repeatedly catches the same reliability, security, or interface-quality issue in agent-written code.
- Designing CI and review automation for coding-agent workflows.

Details:
- Lopopolo describes security and reliability reviewer agents that run on pushes and CI, read documentation plus the proposed patch, and ask whether code satisfies local expectations. (12:00-12:20)
- Concrete review prompts include checking whether network code has retries and timeouts and whether new interfaces are secure and hard to misuse. (12:20-12:30)
- A recurring outage lesson can become a bespoke lint, such as checking every `fetch` call for retry and timeout handling, making the lesson durable across future agent output. (12:32-13:21)
- The talk argues that accepting short-term velocity hits to understand where agents struggle and add guardrails lets humans step back to higher-leverage work later. (09:36-10:07)
- Ankit Jain (Aviator) runs the same conversion retrospectively and in bulk rather than incident by incident: "mine your last 1,000 review comments and build out a[n] AI slo[p] register for the things which are repeatable," because "a vast majority of the comments that you're providing in your code review are something that we repeat over and over again." The corpus of past reviews already contains the rules, so mining precedes waiting for the next incident, and the two approaches compose. He also states the cost Lopopolo's velocity-hit framing implies: adoption "does follow a J curve. So, pain is real." (YgEv7IQzGdM 06:53-07:57, 14:12-15:08)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)
- [Agent rules should emerge from observed off-rail behavior](agent-rules-should-emerge-from-observed-off-rail-behavior.md)
- [Use agent hooks to automate session rituals](use-agent-hooks-to-automate-session-rituals.md)
- [Mine Recurring Review Comments Into an Invariant Registry](mine-recurring-review-comments-into-an-invariant-registry.md)

Sources:
- [Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI](../sources/20260417_am_oeAoUhew.md), 09:36-13:21
- [How to Kill the Code Review — Ankit Jain, Aviator](../sources/20260817_YgEv7IQzGdM.md), 06:53-07:57, 14:12-15:08
