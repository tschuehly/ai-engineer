# Plan Asynchronous Authorization for Background Agents

Summary: Background agents can outlive the user's original browser consent moment, so authorization UX needs asynchronous reauthorization paths. Agents should be able to request additional access through channels such as push notifications or SMS when work continues unattended.

Use when:
- Designing long-running or background agent workflows that may need step-up access later.
- Evaluating OAuth user interaction assumptions for autonomous agents.

Details:
- OAuth often assumes a user is sitting in front of a browser during the authorization flow, but agent work may continue after the user walks away. 17:13-17:25
- A background agent may need to ask for more access than it was originally permissioned for, so the system needs a way to reach the user after the initial interaction. 17:25-17:31
- Real-time channels such as SMS or push notifications are suggested as authorization interaction paths beyond browser-only flows. 17:31-17:39
- **A deployed instance of the reach-back channel, used for confirmation rather than for scope.** Resolve AI's background agents have Slack DM access, and an agent that is unsure whether to answer a question in a public channel will "DM you to say, 'I think I know the answer to this, but I'm not sure. Can you confirm this for me before I, you know, respond back?'" This is the same asynchronous pattern — the agent is running long after anyone was watching, and it reaches the human on a channel they already read — applied to whether an action is *correct* rather than whether it is *permitted*. Two notes: the DM channel doubles as an authorization surface only if the messages are authenticated as coming from the agent, which is not discussed, and Smith describes the behavior as "emergent" rather than as a designed control. See [Answer Unaddressed Questions Behind a Confidence Gate](answer-unaddressed-questions-behind-a-confidence-gate.md). ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 16:52-17:09)
- **The other resolution: decide the authorization before the run, so nothing has to be asked mid-flight.** GitHub Next's position on scheduled automations is that the absence of a supervisor is the design premise rather than a gap to be bridged — "if we're going to be not supervising agents doing things, then we're going to need much stronger guardrails" — so permissions, tools, destinations and permitted writes are all fixed in the workflow's front matter at authoring time. That trades expressiveness for availability: an asynchronous approval channel can grant a one-off exception at 3am, while a manifest can only fail closed. The two are complementary, and which one a job needs follows from whether its exceptional cases are worth waking someone for. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 07:10-08:34)

Related topics:
- [Agents](../topics/agents.md)
- [Security](../topics/security.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Filter MCP Tools By Scopes And Step-Up Authorization](filter-mcp-tools-by-scopes-and-step-up-authorization.md)
- [Treat Long Waits as Logical Workflow State](treat-long-waits-as-logical-workflow-state.md)
- [Control Long-Running Workflow Agents Through Run Lifecycle Operations](control-long-running-workflow-agents-through-run-lifecycle-operations.md)
- [Answer Unaddressed Questions Behind a Confidence Gate](answer-unaddressed-questions-behind-a-confidence-gate.md)
- [Bound What an Unattended Automation May Emit, Including Emitting Nothing](bound-what-an-unattended-automation-may-emit.md)

Sources:
- [How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)](../sources/20250730_blmAkayzE8M.md), 17:13-17:39
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 16:52-17:09
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 07:10-08:34
