# Codebase Hygiene Amplifies AI Productivity Gains

Summary: AI coding tools appear to deliver more value in clean engineering environments with tests, types, documentation, modularity, and maintainable code. Tool rollout without hygiene work can accelerate codebase entropy and make future AI assistance less trustworthy.

Use when:
- Explaining why the same AI coding tools produce different gains across teams.
- Planning platform, testing, documentation, or code-quality investments before scaling coding agents.

Details:
- The source describes an experimental "environment cleanliness index" built from tests, types, documentation, modularity, and code quality, then reports a stronger correlation with AI productivity lift than raw token usage. (04:02-04:49)
- Clean code is framed as an amplifier for AI gains because more tasks become suitable for AI help or completion when the codebase is easier to understand and validate. (04:51-05:27)
- Unchecked AI use can increase codebase entropy and push cleanliness down, so humans need to invest in hygiene to keep receiving AI benefits. (05:27-05:50)
- Engineers also need judgment about when not to use AI: rejected or heavily rewritten AI output can reduce trust and collapse later usage gains. (05:50-06:13)
- Jellyfish's PR data adds an architecture-specific version of this caveat: highly distributed repositories showed little or no positive throughput correlation with AI adoption, plausibly because cross-repo context is harder for humans and tools to assemble. (13:23-15:26)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Agent-legible codebases reduce generated-code entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [Active repos per engineer exposes context architecture drag](active-repos-per-engineer-exposes-context-architecture-drag.md)
- [Treat agent readiness as verification infrastructure](treat-agent-readiness-as-verification-infrastructure.md)
- [Standardize development environments around common model priors](standardize-development-environments-around-common-model-priors.md)

Sources:
- [Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) - Yegor Denisov-Blanch, Stanford](../sources/20251211_JvosMkuNxF8.md), 04:02-06:13
- [What Data from 20m Pull Requests Reveal About AI Transformation - Nick Arcolano, Jellyfish](../sources/20251124_WqZq8L-v9pA.md), 13:23-15:26
