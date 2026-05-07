# Measure AI Coding Adoption With PR Telemetry and Guardrails

Summary: AI coding adoption should be measured as developer behavior tied to engineering outcomes, not as generated lines or raw tool exposure. PR throughput and cycle time can show delivery lift, but they need PR-size and quality guardrails to avoid rewarding volume alone.

Use when:
- Designing engineering dashboards for AI coding rollouts.
- Explaining why adoption and productivity claims need outcome metrics plus quality checks.

Details:
- Jellyfish defines developer AI adoption rate as the fraction of coding time where a developer uses AI tools, then averages those rates to compute company-level adoption. (03:00-03:37)
- Generated lines of code are treated as a weak metric; developer adoption better captures the behavior change the organization wants to create. (02:23-03:15)
- In Jellyfish's PR data, higher AI adoption correlates with about 2x PR throughput and about a 24% decrease in median cycle time from first commit to merge. (06:54-08:30)
- The same analysis found PRs about 18% larger in net lines added, with similar file counts, so AI-assisted throughput should be watched alongside review size and verbosity risk. (08:46-09:39)
- Quality guardrails matter: Jellyfish looked at bug tickets created and PR reverts and did not find a statistically significant relationship with AI adoption, while bug-resolution rates increased because teams used AI on well-scoped backlog bugs. (09:41-10:54)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Do not use token volume as a developer productivity metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)
- [Measure AI engineering impact across utilization, impact, and cost](measure-ai-engineering-impact-across-utilization-impact-and-cost.md)
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)

Sources:
- [What Data from 20m Pull Requests Reveal About AI Transformation - Nick Arcolano, Jellyfish](../sources/20251124_WqZq8L-v9pA.md), 02:23-10:54
