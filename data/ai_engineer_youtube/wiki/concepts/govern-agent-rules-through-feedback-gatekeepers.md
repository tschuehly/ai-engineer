# Govern Agent Rules Through Feedback Gatekeepers

Summary: Shared agent instructions should have an explicit owner or group that receives feedback, maintains the rules, and keeps system prompts aligned with current engineering practice.

Use when:
- Establishing ownership for `AGENTS.md`, Cursor rules, system prompts, or other agent-control files.
- Deciding how to update shared prompt context after recurring model failures or stale framework guidance.

Details:
- The talk groups system prompts, Cursor rules, and agent Markdown as mainstream mechanisms for controlling model and agent behavior. (11:18-11:31)
- A Spring Boot example illustrates why rule files need maintenance: models may keep suggesting older framework patterns when the organization wants current Spring Boot 3 guidance. (11:36-11:46)
- Reock recommends a gatekeeper or group that receives feedback and understands how to maintain and continuously improve shared system prompts. (11:48-11:58)
- The reason for governance is organization-wide effect: shared prompts shape how assistants, models, and agents behave across the business. (11:58-12:04)
- The same section cautions that generation settings such as temperature should be chosen by use case, with more deterministic settings for repeatability and higher settings for divergent creative solutions. (12:07-13:25)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [System prompt learning updates agent rules from eval explanations](system-prompt-learning-updates-agent-rules-from-eval-explanations.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)

Sources:
- [Leadership in AI Assisted Engineering - Justin Reock, DX (acq. Atlassian)](../sources/20251219_PmZDupFP3UM.md), 11:18-13:25
