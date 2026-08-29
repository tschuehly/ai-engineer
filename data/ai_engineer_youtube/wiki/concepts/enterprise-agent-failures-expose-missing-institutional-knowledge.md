# Enterprise Agent Failures Expose Missing Institutional Knowledge

Summary: Enterprise agents often fail not because they lack general reasoning, but because the task depends on organizational knowledge that is stale, duplicated, undocumented, or held in people's heads.

Use when:
- Diagnosing why capable coding or operations agents do not move real delivery work.
- Separating model capability gaps from enterprise context gaps.

Details:
- The source distinguishes three kinds of task knowledge: green general knowledge that models already know, orange knowledge that can be taught through skills or instructions, and red institutional knowledge that sits inside a company and its people, 05:40-06:37.
- AI can generate code, review PRs, and help with incident management, yet enterprise delivery metrics may not improve when Jira work depends on missing domain context, 04:36-05:21.
- A knowledge base with outdated, unreliable, duplicated, and tribal information makes broad connector coverage insufficient; the missing or low-quality knowledge must be repaired, 10:11-11:59.
- **The same discovery mechanism run deliberately, with the papercuts treated as the product.** Shenoy's flywheel puts agents alongside employees on real work specifically to harvest what breaks: the traces capture "tool calls, the hiccups, the papercuts, everything that goes wrong with doing real work," and the point of collecting them is that the missing institutional knowledge is only visible at the moment the agent fails to have it. His framing of the terrain is the reason the failures are the signal rather than noise: against the demo's smooth slope, "there are hills and ravines. There's death by a thousand paper cuts… The exceptions are the job." ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 10:52-11:08, 13:04-13:43)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)

Sources:
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md), 04:36-11:59
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 10:52-13:43
