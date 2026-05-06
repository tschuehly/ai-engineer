# Gate AI-generated open-source contributions through human-effort filters

Summary: Maintainers can protect open-source attention by requiring a small amount of human-authored context before accepting AI-generated issues or pull requests. The goal is to filter drive-by agent output before it consumes review time.

Use when:
- Designing contribution policy for projects receiving AI-generated issues, reports, or pull requests.
- Separating maintainer-triage workflows from agent-generated drive-by submissions.

Details:
- After pi became the agentic core inside OpenClaw, Zechner says his project received many low-signal OpenClaw-generated issues and pull requests from users who may not have realized their agents were targeting the project. (10:46-11:10)
- His mitigation is to auto-close pull requests with a request to first write a short issue in the contributor's own human voice; once the maintainer approves that issue, the contributor is allowlisted for a later pull request. (11:14-11:30)
- The filter works because low-effort agent submissions rarely return to read and satisfy the comment, while contributors willing to add concise human context can still proceed. (11:30-11:38)
- He also describes deprioritizing submissions associated with noisy agent interactions, embedding issue and pull-request text to inspect clusters, and closing trackers during "OSS vacation" periods to protect maintainer time. (11:38-11:58)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI-generated security reports need maintainer triage](ai-generated-security-reports-need-maintainer-triage.md)
- [Plugin architectures let agent systems absorb experiments](plugin-architectures-let-agent-systems-absorb-experiments.md)

Sources:
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md), 10:46-11:58
