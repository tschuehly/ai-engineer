# Alert on Account Change Events, Including the Ones That Are Absences

Summary: A world model earns its keep when something changes in it, so the action layer over customer data should be an event stream on state transitions — and the transition set has to include stopping, which no threshold alert on activity will ever fire.

Use when:
- Building the layer that turns a customer or usage database into work a human or agent picks up.
- Deciding between a periodic report, a dashboard, and an event trigger for account signals.
- Reviewing an alerting rule set and checking whether disappearance is representable in it.

Details:
- The design is stated as a general trigger over the customer model rather than a set of specific reports: "anytime something significant happens with any of our customers, we're alerted." ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 07:02-07:10)
- The four named triggers cover three different event shapes: an entity event ("someone signed up"), a positive rate change ("someone used a ton of searches"), a negative rate change to zero ("someone stopped using searches"), and a watchlist match ("someone showed up that we really really care about"). (07:10-07:18)
- The stop is the interesting member of the set. Surges and signups are things that appear in a log; a stop is the absence of rows, which means the detector has to run over expected activity rather than over observed activity — a structurally different query from the other three, and the one a naive "alert when metric exceeds X" system cannot express.
- The output contract is explicit and modest: these "are signals that we are notified about and that our team can act on." The system routes attention; it does not decide or act. (07:18-07:27)
- The event layer sits on top of the same joined data as the market classification and the internal agents, which is what makes "something significant happens" computable at all — the alert is a diff against a model, not a metric on a single source. (03:53-04:42, 05:22-07:27)
- **Limit.** No definition of "significant," no thresholds, no volume, no false-positive rate, and no evidence about what the team did with the alerts. The tool is named (Request Lens) and demonstrated only as a concept slide. (07:02-07:27)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Proactive Agent Systems Need Observation, Personalization, Timing, and Workflow Embedding](proactive-agent-systems-need-observation-personalization-timing-and-workflow-embedding.md)
- [Run a Signal Layer to Triage Comms and Protect Focus](run-a-signal-layer-to-triage-comms-and-protect-focus.md)
- [Incident Agents Turn Alerts Into RCA and Operational Memory](incident-agents-turn-alerts-into-rca-and-operational-memory.md)

Sources:
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 03:53-04:42, 07:02-07:27
