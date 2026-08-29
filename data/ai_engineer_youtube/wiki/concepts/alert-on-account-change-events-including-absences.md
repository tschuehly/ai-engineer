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
- **A second account-event layer that carries the design one step further: it assigns the work instead of notifying.** Notion defines the unit by consequence — "a signal is a single customer event that's important enough to change what should happen next for a customer" — and its service "decides whether a single action is available, decides who should own that action, and then it emits a concrete task" for a human or an agent. Its trigger set is user-driven events (an AI limit hit, a contact-sales submission) plus external ones nobody at the company can observe in a log — funding rounds, hiring, tech-stack shifts — which are credited with making the system "proactive instead of reactive." The absence case is handled differently than in Wang's set: rather than detecting a stop, the no-signal path falls through to a predictive engine that picks relevant features and sends lifecycle messages. ([Liu](../sources/20260826_L4I7WgiEquo.md), 11:20-12:53)
- **The aggregate-performance precursor, and the stated path from it to the account level.** Cloudflare pushes a weekly narrative about how teams are pacing — "trends, standouts, as well as watches" — before pushing anything about individual customers, and names the account-level version as the next step: extending the pipeline "beyond just what I've shown you for multiple teams, but also down to the customer level." The generalization is not free. A performance summary is computed from a fixed slice grid where every cell exists; an account event stream has to notice that a cell stopped producing rows, which is the failure this page is about. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 09:04-09:18, 11:55-12:03)
- **The account state that a signal is a diff against, enumerated from three directions.** Berry's account of why the model never settles gives the change sources their own taxonomy: the company acts ("a company gets acquired, opens offices, ships products"), you act on it ("you're marketing at them, you're selling towards them, you're trying to book meetings. That's changing the state of the account"), and it emits observable events ("hiring people and firing people and doing things that provide signals for you"). The middle one matters for alert design and is easy to omit: your own outreach changes the state, so a naive change detector will fire on the consequences of its own actions. ([Berry](../sources/20260826_UhCY231d0FQ.md), 03:00-03:42)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Proactive Agent Systems Need Observation, Personalization, Timing, and Workflow Embedding](proactive-agent-systems-need-observation-personalization-timing-and-workflow-embedding.md)
- [Run a Signal Layer to Triage Comms and Protect Focus](run-a-signal-layer-to-triage-comms-and-protect-focus.md)
- [Incident Agents Turn Alerts Into RCA and Operational Memory](incident-agents-turn-alerts-into-rca-and-operational-memory.md)
- [Emit Owner-Assigned Tasks From Signals, With a Marketing Default When None Fire](emit-owner-assigned-tasks-from-signals-with-a-marketing-default-when-none-fire.md)
- [Push the Narrative Because Dashboard Adoption Is Always Uneven](push-the-narrative-because-dashboard-adoption-is-always-uneven.md)
- [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md)

Sources:
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 03:53-04:42, 07:02-07:27
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 11:20-12:53
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 09:04-09:18, 11:55-12:03
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 03:00-03:42
