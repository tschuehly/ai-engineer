# Keep Agents Off the Customer Channel and Treat Inbound Forms as Untrusted Input

Summary: Deciding that no agent speaks directly to a customer is usually argued as a quality or brand policy, but it is also the control that keeps a trust boundary intact: anything a prospect types into a public form is attacker-controlled text that will reach an agent, and a human approving every outbound message is what stops that text from turning into an action.

Use when:
- Designing an agentic workflow where some input originates from people outside the organization.
- Arguing about whether an agent may send email, chat, or form replies without review.
- Enumerating trust boundaries in a system where an agent sits between untrusted input and a privileged action.

Details:
- The policy is stated first and without hedging: "we deliberately chose not to let an agent talk directly to a customer. For sales-assist workflows, humans stay in the loop by default and approve anything the agents do. The agents do the busy work." ([Liu](../sources/20260826_L4I7WgiEquo.md), 07:27-07:43)
- **The security argument is presented as a second, independent reason for the same decision.** "That decision also has a security dimension too. If a prospect fills out a contact sales form online, we treat that as untrusted user input. And so trust boundaries don't break down, especially because there is an agent in the middle." (07:43-07:58)
- The classification is the useful part: a contact-sales form is normally treated as a lead record, and naming it untrusted input puts it in the same category as a web page an agent browses or a document it ingests — with the difference that a form is addressed *to* the pipeline, so a submitter can write directly to whatever prompt consumes it.
- Human approval is scoped by risk rather than applied uniformly. The takeaway is "let humans stay in the loop where there are risky possibilities," and the paired implementation is the reactive workflow, where a Gong transcript is parsed into a grounded follow-up draft that lands in a rep's task box for review. (14:24-14:52, 16:14-16:41, 19:55-20:01)
- The stance is explicitly a current position on a trajectory, not a permanent one: "right now, humans are the primary consumer of GTM data and agents are helping at the edges. Soon, agents will become primary first-class consumers within the system, moving from drafting to acting within guardrails." The guardrails that would replace the human are not described. (20:30-20:49)
- **Limit.** This is a design decision with a rationale, not a tested control. No injection attempt, filter, classifier, sanitization step, or incident is described, and nothing is said about what the agent may still do with untrusted text on the read side — research, enrichment, and scoring all consume it before a human sees the draft. (07:43-07:58)

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Filter Untrusted Context Before It Reaches the Agent](filter-untrusted-context-before-it-reaches-the-agent.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [LLM Guardrails Need Checkpoints at Every Untrusted Boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Browser Agents Sit in the Prompt-Injection Lethal Trifecta](browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md)
- [Human Approval Can Hide Tool Description and Parameter Risk](human-approval-can-hide-tool-description-and-parameter-risk.md)
- [Reduce Every Workflow to Know, Decide, Act, and Learn](reduce-every-workflow-to-know-decide-act-and-learn.md)
- [Scope a Person-Cloned Agent by Caller, With Drafts as the Shared Capability](scope-a-person-cloned-agent-by-caller-with-drafts-as-the-shared-capability.md)

Sources:
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 07:23-07:58, 16:14-16:41, 19:55-20:01, 20:30-20:49
