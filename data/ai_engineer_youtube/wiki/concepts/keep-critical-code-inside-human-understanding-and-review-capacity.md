# Keep critical code inside human understanding and review capacity

Summary: Agent-generated code should be limited by the human ability to understand, evaluate, and own the resulting system. Non-critical scoped tasks can be delegated more freely, but critical code needs direct human reading and decision ownership.

Use when:
- Deciding which coding tasks can run autonomously and which need a human in the loop.
- Reviewing proposals to scale agent output with many parallel agents, long context windows, or reviewer agents.

Details:
- Zechner warns that many agents can compound errors faster than humans can review them, and that delayed pain appears when the codebase becomes too large or inconsistent for either humans or agents to repair confidently. (12:59-16:01)
- He argues reviewer agents catch some issues but do not remove the human bottleneck because agents inherit complexity from internet-trained examples and do not learn from project pain the way humans do. (13:23-15:24)
- Good agent tasks are scoped so the agent can find all required context, have an evaluation function for the result, or are non-mission-critical work such as reproductions, boring chores, research, and rubber-ducking. (16:13-16:53)
- The final guidance is to slow down, build fewer features, keep generated code volume inside review capacity, allow more freedom for non-critical code, and read every line of critical code. (16:51-17:58)
- Volkov (ThursdAI) reframes this Zechner position as the "Z" end of a per-task continuum: route by task — non-critical, let it rip; critical, read every line. Read every line yourself of authentication, money movement, permissions, and irreversible data, and use the agent to help identify which lines and primitives are actually critical (a model is good at scanning a large repo and flagging the critical path). (ZpK5PWX2YRM 13:18-14:44)

- Matt Dailey (Ref) names a loss this control does not cover. Reading every line of critical code protects against code you do not understand; it does not protect against code whose *approach* someone else chose — "if you as an engineer are letting an agent make a critical decision, you are [ceding] control of your code. You are no longer the owner of that code." You can read every line of a design you never picked. Treat the two as complementary controls with different failure modes, and note that only the decision control keeps working as the diff gets larger. See [Ceding a Critical Decision Transfers Ownership of the Code](ceding-a-critical-decision-transfers-ownership-of-the-code.md). ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 03:16-03:43, 17:10-17:27)
- **Why the comprehension boundary is a schedule problem, not only a risk one.** Denys Linkov names the same loss and prices it in change cost: AI-native development produces "a lot of code written… with low performance or quality, and the broader problem is people don't actually understand what's happening there. So, if you have some issues within the code base or you want to adjust based on customer requirements, it's actually much harder to do so." Code that has drifted outside human understanding does not merely carry latent risk — it becomes the code you cannot modify on a customer's timeline, which is the specific way it eventually forces a refactor. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 13:03-13:32)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Route each change to the proof it needs](route-each-change-to-the-proof-it-needs.md)
- [Ceding a Critical Decision Transfers Ownership of the Code](ceding-a-critical-decision-transfers-ownership-of-the-code.md)
- [Audit a Refactor Against Having Waited for Better Models](audit-a-refactor-against-having-waited-for-better-models.md)

Sources:
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md), 12:59-17:58
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../sources/20260710_ZpK5PWX2YRM.md), 13:18-14:44
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 03:16-03:43, 17:10-17:27
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 13:03-13:32
