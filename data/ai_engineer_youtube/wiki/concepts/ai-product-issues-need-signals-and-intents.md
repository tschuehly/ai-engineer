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

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Cluster conversation outputs to prioritize AI product work](cluster-conversation-outputs-to-prioritize-ai-product-work.md)

Sources:
- [Building AI Products That Actually Work - Ben Hylak (Raindrop), Sid Bendre (Oleve)](../sources/20250724_eSvXbb2EBYc.md), 11:09-13:39
