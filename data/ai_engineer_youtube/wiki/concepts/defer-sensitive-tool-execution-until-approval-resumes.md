# Defer Sensitive Tool Execution Until Approval Resumes

Summary: Human approval workflows should pause the sensitive tool call itself, persist enough state to resume it, and guard against duplicate side effects when approval notifications arrive.

Use when:
- Designing finance, provisioning, account, or customer-facing actions that need explicit human approval.
- Connecting agent workflows to notification systems, webhooks, or approval providers.

Details:
- Kozlov's credit-card provisioning example wraps the `issueCard` action in a required-human-input tool so card issuance always waits for approval instead of trusting the model to decide approval occurred. 15:58-16:44
- The workflow delegates approval notification to Knock, defers the tool call until approval, routes the approval webhook back to the correct user-scoped durable object, then resumes the paused tool call. 16:44-18:07
- The workflow must store status so asynchronous or repeated webhook events cannot approve or provision the same card twice. 18:08-18:44

Related topics:
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Treat long waits as logical workflow state](treat-long-waits-as-logical-workflow-state.md)
- [Keep Fixed Business Logic Outside the Model](keep-fixed-business-logic-outside-the-model.md)

Sources:
- [Building Agents (the hard parts!) - Rita Kozlov, Cloudflare](../sources/20250723_j_TKDweOsYE.md), 14:32-18:44
