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

- If hygiene is the amplifier, one team automates the upkeep rather than scheduling it as human cleanup: "We have like a code gardener that actually goes back and looks through… every night it'll run and look at the code and check if something like not organized correctly. What does correct organization mean will depend on your code base." The design choice worth noting is that the rubric is repo-specific rather than a generic linter — it encodes the team's own organization conventions, which is exactly the part a linter cannot express and the part that decays fastest under agent-written code. Reported as practice, with no measure of what it caught or what it cost. ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 10:32-10:53)
- **Voluntary cross-area contribution as the hygiene signal.** After consolidating more than ten repositories, WiseDocs reports a result that no velocity dashboard produces: "beyond just shipping velocity, developers actually want to work in this codebase. So, everybody comes along and says, 'Hey, can I work in this codebase? It's much cleaner compared to the other ones.'" It became measurable as reach — "now almost every developer within the company is committing to this new mono repo even though it might not be their area of expertise, but they might need to make changes to schemas, API calls, and other parts of the stack" — against a prior estate where "nobody actually wants to touch the code. It's not a fun experience." The patterns then propagated on their own: "a lot of the patterns we have adopted here have spread to other repos within the company." ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 00:38-00:45, 11:22-11:35, 14:09-14:28)

- **The temporal counterpart to this correlation, and the cost it hides.** Amazon's 50-team pilot ran entirely on "existing systems with existing code bases. Nothing green field," and reports the same dispersion this page describes — half the teams under 3x, the other half a median of 4.5x — with the tool roughly held constant ("90% of these teams used Kiro"). But the interviews add what a cross-sectional correlation cannot: getting from the dirty state to the clean one costs output first. "In almost every team that was interviewed, they reported that their productivity actually went down as they intentionally adopted a new way of working," because "we have to do real work in our code base first for agents to be successful there, especially in brownfield existing code bases." The named work is specific — build agent context, "improve existing tools error messages so that the model knew what was going on when it failed," build "new tools, new MCP servers," restructure for navigability, and at the extreme change the language away from Python or JavaScript because "there's no compiler errors. So the model kind of guesses." See [Budget the Productivity Dip That Precedes the Agent Speedup](budget-the-productivity-dip-that-precedes-the-agent-speedup.md). Self-reported internal figures with no defect or rework adjustment. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 06:04-07:34, 09:39-11:08)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Read a Broken Agent Setup From Babysitting, Context Burn, and Slop](read-a-broken-agent-setup-from-babysitting-context-burn-and-slop.md)
- [Agent-legible codebases reduce generated-code entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [Active repos per engineer exposes context architecture drag](active-repos-per-engineer-exposes-context-architecture-drag.md)
- [Treat agent readiness as verification infrastructure](treat-agent-readiness-as-verification-infrastructure.md)
- [Standardize development environments around common model priors](standardize-development-environments-around-common-model-priors.md)
- [Audit a Refactor Against Having Waited for Better Models](audit-a-refactor-against-having-waited-for-better-models.md)
- [Budget the Productivity Dip That Precedes the Agent Speedup](budget-the-productivity-dip-that-precedes-the-agent-speedup.md)

Sources:
- [Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) - Yegor Denisov-Blanch, Stanford](../sources/20251211_JvosMkuNxF8.md), 04:02-06:13
- [What Data from 20m Pull Requests Reveal About AI Transformation - Nick Arcolano, Jellyfish](../sources/20251124_WqZq8L-v9pA.md), 13:23-15:26
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 10:32-10:53
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 11:22-11:35, 14:09-14:28
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 06:04-07:34, 09:39-11:08
