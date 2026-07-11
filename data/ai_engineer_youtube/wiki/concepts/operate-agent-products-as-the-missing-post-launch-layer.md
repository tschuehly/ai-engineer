# Operate Agent Products as the Missing Post-Launch Layer

Summary: Shipping an agent is now the easy part; operating it in production is a distinct engineering discipline because agent failures are *silent* — they live in the conversation, not the stack trace — so you must build a feedback "loop" layer that watches, judges, and improves the live system.

Use when:
- You have launched a non-deterministic agent product and need to know whether it is actually working across many real sessions.
- Deciding how much to invest in post-launch operations vs new features.
- Reasoning about why classical software safety nets (unit tests, CI, dashboards) feel insufficient for agents.

Details:
- "Shipping is the moment when the real work begins"; you can build a whole product in days, but you must close the loop as soon as possible, and the loop is "at least as important as the product itself, sometimes even more." (00:31-01:26)
- Agent ops is genuinely new: an agent has no predefined, pre-testable flow, its coverage is endless (like Claude Code/Codex it can do a giant range of things), and "you cannot write all the conversations in advance"; LLMs are non-deterministic so the same input can take a different trajectory. (01:50-03:00)
- The scariest failure is silent: a long-running agent struggles mid-task but "was lucky," recovers with workarounds, and finishes green with "no red alerts, no problems on a dashboard" — a hidden defect that "lives in your code base," because reliable agents "shouldn't depend on the luck." Cites Anthropic's point that agents "love to make [mark] features as complete without checking they actually worked." (03:44-04:36)
- Finished ≠ helpful: the agent built a trip itinerary and the answer "looks successful," but it used the wrong service and mispriced it — "technically successful but still failing the task." (05:07-05:37)
- Normal safety nets are only "one slice": unit tests, regex, and simulated-customer scripts help but customers "always do something different," so "green CI means nothing for a non-deterministic agent," and "production is the place where you learn what you need to test in the first place." (02:41-03:06, 05:37-05:48)
- The differentiator is not the model or the harness everyone can copy — it is the internal operations system that closes the loop, detects problems, and gives you a felt sense of the system's health. (19:00-19:31)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Staff Agent Operations With a Team of Agents](staff-agent-operations-with-a-team-of-agents.md)
- [Score Every Production Conversation to Judge Agent Health](score-every-production-conversation-to-judge-agent-health.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)

Sources:
- [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](../sources/20260705_kZsf_Sfm7RU.md), 00:31-05:48, 19:00-19:31
