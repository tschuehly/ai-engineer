# AI Product Issues Need Signals and Intents

Summary: AI product failures often do not throw exceptions, so teams need ground-truth-like signals combined with user intent to define what actually broke.

Use when:
- An AI app produces bad or frustrating behavior without a conventional stack trace.
- Product teams need to discover emerging failure patterns from production usage.

Details:
- The talk contrasts conventional Sentry-style errors with AI failures: AI apps may have no concrete exception, so teams need performance signals rather than only error logs. (11:09-11:30)
- Useful signals can be explicit analytics-style events such as thumbs up/down, copied text, preference choices, marked-correct results, or marked-wrong results. (11:30-12:53)
- Implicit signals detect behavior such as refusals, task failure, and user frustration; clustering those signals can expose issue classes such as users failing to search for tweets. (12:55-13:15)
- Intent changes the meaning of a signal, so the talk frames an AI issue as a signal plus the user's intent, explored through metadata such as properties, models, keywords, and intents. (13:17-13:39)
- **Thirteen months later the same speaker adds what a signal cluster still is not.** Hylak's 2026 talk keeps this page's premise — agent failures throw no exception and arrive as thousands of "I saw this weird thing" reports — but sharpens what has to be attached before any of it is actionable: onset and share of users, "when it actually started, and… how many people it affects" ([Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)). He also narrows where clustering belongs, arguing that clustering raw traces is one-off analysis rather than issue detection ([Clusters Are Not Issues](clusters-are-not-issues.md)). Read as a refinement rather than a reversal: clustering a pre-filtered, intent-annotated signal stream, as this page describes, is a narrower operation than clustering everything — but the talk does not draw that distinction itself, so treat any cluster here as a discovery output that still needs a declared identity before it can be tracked. ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 13:20-14:17, 16:00-18:08)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Cluster conversation outputs to prioritize AI product work](cluster-conversation-outputs-to-prioritize-ai-product-work.md)
- [Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)
- [Clusters Are Not Issues](clusters-are-not-issues.md)

Sources:
- [Building AI Products That Actually Work - Ben Hylak (Raindrop), Sid Bendre (Oleve)](../sources/20250724_eSvXbb2EBYc.md), 11:09-13:39
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 13:20-14:17, 16:00-18:08
