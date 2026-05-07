# Authorize High-Impact Agent Actions Transactionally

Summary: Broad OAuth scopes are often too coarse for agents that initiate commercial, financial, or otherwise high-impact actions. Transaction-level authorization should bind permission to the specific action, amount, budget, or context the agent is about to execute.

Use when:
- Granting agents access to payments, procurement, trading, infrastructure changes, or other sensitive actions.
- Deciding whether read/write OAuth scopes are enough for an autonomous workflow.

Details:
- OAuth scopes are an improvement over passwords because they can distinguish coarse permissions such as read and write access, but they can still be too broad or too long-lived for agent workflows. 14:59-15:27
- Financial or commercial agent transactions may need authorization on a per-transaction basis with specific amounts or budgets, rather than only a standing scope. 15:27-15:47
- Rich Authorization Requests are named as an OAuth specification to evaluate or adopt when agent actions need more dynamic, transaction-specific authorization. 15:47-16:02

Related topics:
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Filter MCP Tools By Scopes And Step-Up Authorization](filter-mcp-tools-by-scopes-and-step-up-authorization.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)

Sources:
- [How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)](../sources/20250730_blmAkayzE8M.md), 14:59-16:02
