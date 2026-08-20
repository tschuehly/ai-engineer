# Triage Agent Issues by Onset and Share of Users

Summary: An agent will produce effectively unbounded issues, so the useful question is not what is broken but what is worth acting on. Two numbers per issue answer that: when it started, and what fraction of users it hits. Onset turns a report into a causal question; share decides whether to care at all.

Use when:
- Reports of odd agent behavior arrive faster than the team can investigate them.
- Designing what an agent observability tool must record per issue, before choosing how it detects issues.
- Deciding whether a quality signal deserves a fix, a watch, or nothing.
- Evaluating a trace-analysis approach: if it cannot produce these two numbers, it is analysis, not monitoring.

Details:
- The premise that forces triage: "your agent will have issues that potentially you can't solve or not exactly worth solving," because "agents will have an infinite number of problems. That's sort of like the the great and terrible thing about them… they're like these little stochastic, you know, crazy things exploring everywhere." So the root question is "how do you make your agent better," not "what issues does your agent have." ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 07:12-07:29, 14:06-14:17)
- The requirement, stated flatly: "for each issue, you really need to know two things. You need to know when it actually started, and you need to know how many people it affects." (13:20-13:27)
- **Onset is the causal handle.** "The first thing is like, 'Is this new?' Cuz if it's not new… I'm going to care about it less. If I tell you like, 'Hey, look, this issue started yesterday'… suddenly like your mind starts turning and you're like, 'Oh, what did I do? Like, what what what changed, right? Did we change model? Did we change something else um downstream?'" A dated onset converts an unfalsifiable complaint into a diff to inspect. (13:38-13:58)
- **Share is the priority handle.** "Knowing that it happened to three users versus 100,000 users just is critical." Note the asymmetry with severity: three users is a reason to deprioritize only when the floor consequence is small — a five-user internal app can invert this ([Match the Quality Method to Your User Count](match-the-quality-method-to-your-user-count.md)). (13:58-14:06)
- Both numbers are ordinary telemetry requirements, which is the point. "If you think about like normal telemetry… when you're building software, you need to know like when something started, you need to know how much it's grown. Those things really matter." The claim is that agent observability regressed below the bar its own industry already meets for exceptions. (16:40-17:02)
- The practical filter this gives you: any candidate issue-detection mechanism has to produce a stable object that persists across days so onset and growth are meaningful. That is exactly what ad-hoc clustering does not give you ([Clusters Are Not Issues](clusters-are-not-issues.md)). (18:04-18:08)
- Same speaker, thirteen months earlier, framed the discovery half of this: AI failures often throw no exception, so you need explicit and implicit signals plus intent to know something broke at all ([AI Product Issues Need Signals and Intents](ai-product-issues-need-signals-and-intents.md)). This page is the layer after: given a candidate issue, what do you have to know about it to act.
- Caveat: no figures are given for how often onset changes a triage decision at Raindrop, and both numbers are easier to state than to compute — attributing onset requires a stable issue identity across time, which the same talk describes as the hard part.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Clusters Are Not Issues](clusters-are-not-issues.md)
- [Raise the Floor Before Maxing the Benchmark](raise-the-floor-before-maxing-the-benchmark.md)
- [AI Product Issues Need Signals and Intents](ai-product-issues-need-signals-and-intents.md)
- [Run a Production AI Incident Playbook](run-a-production-ai-incident-playbook.md)
- [Hand Agents Anomalies to Investigate, Not to Detect](hand-agents-anomalies-to-investigate-not-to-detect.md)
- [Portfolio-Allocate Eval Failures With a Triage Agent](portfolio-allocate-eval-failures-with-a-triage-agent.md)

Sources:
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 07:12-07:29, 13:20-14:24, 16:40-17:02
