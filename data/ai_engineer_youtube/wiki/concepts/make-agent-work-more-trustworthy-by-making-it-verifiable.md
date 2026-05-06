# Make Agent Work More Trustworthy by Making It Verifiable

Summary: Agent autonomy is safer when work is decomposed into steps with cheap checks, proxy evaluations, or hard guardrails. If a task is easy to solve but hard to verify, humans should keep judgment-heavy choices while agents handle verifiable subwork.

Use when:
- Deciding whether a complex vertical workflow is ready for agent autonomy.
- Turning vague review burden into concrete tests, proxies, or guardrails.
- Explaining why some domains advance faster with agents than others.

Details:
- The talk applies the verifier's rule to agents: when a task is solvable and easy to verify, an agent can be run in a loop, corrected, and improved; when verification is weak, autonomy should be limited. 03:20-03:55
- Legal examples show the spectrum: checking contract definitions is easy to verify, drafting contract language is easy to generate but hard to verify, and litigation strategy may have no objective answer because experts disagree. 04:03-05:13
- Trust can be raised by adding verifiable scaffolding, such as browser access and TDD for coding, golden-contract similarity checks for legal drafting, and decomposition that leaves risk profile, precedent selection, or negotiation stance to humans while agents handle formatting and definition linting. 05:51-07:09
- Guardrails also raise trust by narrowing allowed files, directories, websites, or actions instead of relying on broad "YOLO mode" access for high-impact work. 07:12-07:49

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)

Sources:
- [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../sources/20260422_XNtkiQJ49Ps.md), 03:20-07:49
