# Classify the Assistant Question Log to Find Feature and Content Gaps

Summary: The question log of a widely used assistant is a continuously refreshed demand signal. Classify it with an LLM into a topic taxonomy and it replaces user interviews for finding feature gaps, quality problems, and missing organizational content — with repeated questions and profanity serving as free negative labels.

Use when:
- An assistant has enough traffic that reading traces one by one is no longer possible.
- Deciding what to build next and wanting demand rather than opinion to rank it.
- Enablement, documentation, or support content is stale and nobody knows which parts.
- Looking for a signal that a specific answer was unsatisfactory without asking the user.

Details:
- The framing: "I would really recommend investing in your logs, because they create the feedback loop." The scale is what forces automation — 1.2 million questions total, 40,000 a week — and the interesting engineering is doing it "at scale without breaking the bank" using LLMs to classify. ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 14:11-14:37)
- The output is a taxonomy, not a metric: a top-level categorization broken down into subcategories, with detailed example questions per category, so "we are able to track what kind of questions they are asking." (14:37-15:00)
- **Two failure signals fall out for free, and both are behavioral rather than solicited.** "I'm clearly seeing what people are asking and we are not able to answer, or where we have a quality issue, where they are swearing at the agent or repeating their question, so that we see where to improve." A repeated question is a self-labeled unsatisfactory answer, and it requires no thumbs-up widget, no survey, and no annotation budget — which matters because explicit feedback is sparse and biased toward the users who already care. (15:00-15:20)
- **The strongest use is content gaps rather than product gaps, because it replaces a research method outright.** "For sales enablement it's a goldmine. Let's say that we launch a new product. Usually they would need to interview maybe 100 sellers a week to understand how the topics are changing, where there's gaps in terms of knowledge documents, battle cards. I see that in real time in a minute or two by just asking a question." (15:20-15:37)
- And the fix path closes in the same loop: "we can connect to Confluence, we can connect to Jira, we can connect to Slack channels, we can ingest the PRDs, and in a couple of minutes we can generate battle cards, sales enablement documents, and then feed it back into the agent. You cannot do that kind of feedback loop with humans." Gap detection and gap remediation are both automated, and the artifact produced is retrievable content the agent will use on the next question. (15:37-15:57)
- A second-order use that only exists because one system sees everyone's questions: "within the sales organization, there will be different teams that are trying to target maybe similar accounts from different angles. They don't know about each other. We do. We are now able to ping them and do matchmaking." The log is a cross-team index, not only a per-user record. (15:58-16:11)
- His claim about the payoff curve: "the first features are difficult to get out. The next ones are easy. And then once you start tapping into your logs, this hockey stick exponential thing actually starts happening." (16:15-16:32)
- **The precondition is adoption, which makes this the back half of a loop the front half must seed.** A 40,000-question weekly log is a product of a rollout that reached its population ([Separate the Did-Not-Try Problem From the Did-Not-Return Problem](separate-the-did-not-try-problem-from-the-did-not-return-problem.md)); before that traffic exists, demand has to be written down by hand from the business process instead ([Write the Question Set From the Business Process Before the Data Is Connected](write-the-question-set-from-the-business-process-before-the-data-is-connected.md)).
- Limits: the pipeline is described only by its output. No model, prompt, sampling rate, taxonomy design, cost figure, or classification accuracy is given, despite cost being named as the hard part; nor is any validation that LLM-assigned categories match what users meant. Privacy and consent for reading employee questions at this scale are not discussed at all. The generated battle cards are not reported as reviewed by anyone before being fed back into the agent. ([Provenance and Limits](../sources/20260826_DrTdD-ttjCY.md))
- **The mirror instrument, for when the assistant is not yours.** This page's signal depends on owning the log. A vendor whose product is discussed inside someone else's assistant has no log to classify, so Jarmak synthesizes the demand signal instead: write the prompts your ICP would actually type at their moment of need, run them against the assistants, and count mentions. The finding that comes back is the same class of gap — the pain-shaped prompt ("we keep breaking downstream services when we change shared libraries because we can't see all the consumers") produced zero mentions and a suggestion to write a wiki page, while the comparison-shopping prompt produced 65%. A content gap, discovered without a log. See [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 08:18-09:50)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Business Intelligence](../topics/business-intelligence.md)
- [Retrieval](../topics/retrieval.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)
- [Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md)
- [Mine Agent Conversation History to Generate Missing Skills](mine-agent-conversation-history-to-generate-missing-skills.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Write the Question Set From the Business Process Before the Data Is Connected](write-the-question-set-from-the-business-process-before-the-data-is-connected.md)
- [Separate the Did-Not-Try Problem From the Did-Not-Return Problem](separate-the-did-not-try-problem-from-the-did-not-return-problem.md)
- [Schema-first classification turns LLMs into enterprise categorization tools](schema-first-classification-turns-llms-into-enterprise-categorization-tools.md)
- [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md)

Sources:
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 14:11-16:32
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 08:18-09:50
