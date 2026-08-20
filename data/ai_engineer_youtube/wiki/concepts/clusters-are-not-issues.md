# Clusters Are Not Issues

Summary: Clustering all your traces produces a useful one-off picture of your data and a poor issue tracker. Three structural properties break it as a monitoring primitive: cluster boundaries are not yours to set, they do not stay stable enough to track over time, and what counts as "the same issue" is specific to your product in a way no general clusterer can know.

Use when:
- A trace-analysis tool or in-house pipeline proposes clustering as the issue-detection layer.
- A cluster label like "price issues" is being treated as a work item.
- Deciding what to build on top of an error-analysis pass so its findings persist.
- Reviewing why an issue count moved and finding that the clustering changed, not the product.

Details:
- The critique is aimed at a specific naive default: "you just take all the traces and you just cluster it… and you get these like clusters." ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 16:04-16:15)
- What clustering *is* good for is conceded up front: "it could be like useful from like an analysis… like error analysis… It could be useful to see like, well, what's going on in your data… Going from like a bunch of logs to like something." The limit is scope, not validity — "it's useful for one-off analysis, but it just doesn't really scale well." (16:16-16:38)
- **Reason one — temporal instability.** "With clusters, it's very, very hard to reliably track over time… it's like called like temporal clustering and there's like research in this, but it's pretty hard to do reliably." If the partition shifts between runs, an issue's history is not comparable to itself. (17:03-17:17)
- **Reason two — you do not control boundaries.** "You also just like don't have control of boundaries." The granularity is emergent from the embedding and the algorithm, so you cannot declare that two behaviors are one problem or that one behavior is two. (17:17-17:20)
- **Reason three — issue identity is product-specific.** "This also changes a lot depending on your product. Like what you consider to be like the same issue or not is actually very, very unique to every company." (17:21-17:34)
- The worked failure: a cluster surfaces as "price issues," bundling "wrong price quoted" and "wrong refund calculated." Semantically adjacent, operationally unrelated — "these could have like extremely different root causes." A single owner, a single fix, and a single trend line for that bucket are all wrong. (17:34-18:03)
- The decisive objection is that a cluster cannot supply the two numbers triage runs on: it "doesn't doesn't really tell you the things that we talked about needing" — onset and share of users ([Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)). (18:04-18:08)
- The analogy that makes the point concrete: "there's a reason why you don't sort of like take all of your, you know, normal logs and just like start clustering it." Conventional telemetry groups by an identity the *author* declared — an exception type, a route, an error code — not by post-hoc similarity. (16:40-16:52)
- **This qualifies rather than cancels the wiki's clustering pages.** [Cluster Conversation Outputs to Prioritize AI Product Work](cluster-conversation-outputs-to-prioritize-ai-product-work.md) uses clusters for roadmap allocation, which is exactly the one-off analysis use conceded here. [Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md) survives the objection for a different reason: its human validation-and-promotion step converts a cluster into a named, owned regression test with a stable identity, which is precisely the thing a raw cluster is not. Read together, the rule is that clustering is a discovery pass whose output must be *promoted into something you named* before it can be tracked.
- The same speaker recommended clustering thirteen months earlier, on a different object: explicit and implicit *signals* joined to user intent, not raw traces ([AI Product Issues Need Signals and Intents](ai-product-issues-need-signals-and-intents.md)). The shift is worth reading as a refinement — clustering a pre-filtered, intent-annotated signal stream is a narrower operation than clustering everything — but the talk does not draw the distinction itself.
- Caveat: this is a vendor arguing against what "customers or also, sometimes competitors" do, immediately after telling competitors in the room to pay attention. No measurement of clustering's failure rate is offered and no alternative mechanism is described; only the requirements the alternative must meet.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)
- [Cluster Conversation Outputs to Prioritize AI Product Work](cluster-conversation-outputs-to-prioritize-ai-product-work.md)
- [Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md)
- [AI Product Issues Need Signals and Intents](ai-product-issues-need-signals-and-intents.md)
- [Run Trace Classifiers as Code Mode in a Sandbox](run-trace-classifiers-as-code-mode-in-a-sandbox.md)

Sources:
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 16:00-18:08
