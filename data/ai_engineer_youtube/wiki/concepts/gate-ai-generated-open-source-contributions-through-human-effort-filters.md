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
- **Where the filter goes when it stops paying for itself.** Zechner's allowlist keeps the channel open at a price; Rizwan documents four projects that stopped paying it. Zig's code of conduct bans AI on pull requests, issues "or even comments"; tldraw auto-closes every pull request "whether they're AI generated or not"; curl is "considering shutting down their bug bounty program for the first time in decades"; and GitHub shipped a switch to disable third-party pull requests entirely. Two things follow for anyone tuning a filter. Each escalation is cheaper to operate than the one before it, so drift toward closure is the default rather than a decision. And the thing the filter is protecting may not be review time: Rizwan reports Zig's reason as an ordering of values — the team "value contributors more than they do the contributions," because review is how they "grow new contributors who can become trusted over time," which an AI-authored patch does not do regardless of its quality. See [Closing the Contribution Channel Is Where Slop Filtering Ends](closing-the-contribution-channel-is-where-slop-filtering-ends.md). ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 02:22-03:56)
- **The opposite response to the same influx: absorb it instead of narrowing the channel.** Every mitigation on this page reduces what arrives — a human-voiced issue first, an allowlist, an auto-close, a bug bounty shut down. Warp went the other way after open sourcing took it from about 20,000 GitHub stars to over 60,000 with "thousands of PRs" from "hundreds of contributors": an agent triages every filed issue and researches the repo before a maintainer sees it, and "all PRs that get contributed to Warp go through an agent-managed review process… we don't actually ping any of the human reviewers on our team until an agent has approved," so "the things that humans actually have to manage are only the high-signal, high-quality ones" ([Put an Agent Approval Gate in Front of Maintainer Attention](put-an-agent-approval-gate-in-front-of-maintainer-attention.md)). The cost moves from maintainer attention to compute. Which response is right turns on what the project believes review is *for*, and Rizwan already supplied that test on this page: Zig's stated reason for banning AI contributions is that review is how they "grow new contributors who can become trusted over time," which an agent gate does not do at all — it qualifies patches, not people. A project short of attention should absorb; a project short of trusted contributors should filter. ([Abdalla](../sources/20260822_L173Z8DpaJg.md), 10:30-12:45)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI-generated security reports need maintainer triage](ai-generated-security-reports-need-maintainer-triage.md)
- [Plugin architectures let agent systems absorb experiments](plugin-architectures-let-agent-systems-absorb-experiments.md)
- [Closing the Contribution Channel Is Where Slop Filtering Ends](closing-the-contribution-channel-is-where-slop-filtering-ends.md)
- [Put an Agent Approval Gate in Front of Maintainer Attention](put-an-agent-approval-gate-in-front-of-maintainer-attention.md)

Sources:
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md), 10:46-11:58
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 02:22-03:56
- [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../sources/20260822_L173Z8DpaJg.md), 10:30-12:45
