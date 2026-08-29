# Push the Narrative Because Dashboard Adoption Is Always Uneven

Summary: Metric adoption inside a company is a distribution, not a rollout — some people live in dashboards and some will never open one — so the reliable delivery mechanism for an automatically generated insight is a pushed narrative, with the dashboard demoted to the drill-down surface for whoever wants it.

Use when:
- Deciding whether an analytics investment should ship as a dashboard, a digest, or both.
- Explaining why a well-built dashboard has low usage and the numbers still are not landing.
- Designing the delivery layer for a recurring agent-generated analysis.

Details:
- The thesis is stated as an obligation rather than a feature: "there's a story in the data and they really shouldn't have to search for it." ([Joyce](../sources/20260826_Qw_tC68KKes.md), 08:57-09:04)
- **The justification is a fact about people, not a preference about interfaces:** "there's different level of adoption of the KPI metrics at any given company. You're going to have people who love dashboards, people are never going to look at them. So I think you really need to have a way to scaffold that across the business." A dashboard is a pull surface, and a pull surface cannot reach the tail of that distribution at all.
- The pushed artifact has a fixed structure: a weekly summary "which highlights how the business is doing, how they're pacing to their goals, and then highlighting trends, standouts, as well as watches." Pacing-to-goal, trends, standouts, and watches are four different reader questions, and enumerating them is what keeps the generated prose from drifting into narration. (09:04-09:18)
- **The dashboard is kept and reclassified rather than replaced:** "if they do need to look at some of the reports or dashboards, they can to drill in, but we bring the story to them." The push carries the interpretation; the dashboard carries the evidence for anyone who wants to check it. (09:30-09:42)
- The stated design analogy is the phone's morning briefing — you open it and see "your notes for the day or the things that you need to do" — which sets the expectation of a glanceable artifact arriving on a schedule rather than a report to be worked through. (09:18-09:30)
- **The pushed narrative does a second job the talk names separately:** it gets teams "aligning with source of truth on performance." One generated summary read by everyone removes the divergent-spreadsheet problem that a self-serve query surface reintroduces. (15:02-15:15)
- This is the aggregate-performance case of a broader proactive pattern; the account-level case is an event stream over customer state, where the hardest trigger is an absence ([Alert on Account Change Events, Including the Ones That Are Absences](alert-on-account-change-events-including-absences.md)). The stated next step here is exactly that move: extending the summary "beyond just what I've shown you for multiple teams, but also down to the customer level." (11:55-12:03)
- **Limit.** No open rate, read rate, or behavior change is reported for the weekly summary, and the screen shown is synthetic data. The uneven-adoption claim is asserted from experience, not measured, and the talk does not address the failure mode a push surface has and a dashboard does not — a scheduled digest nobody reads is indistinguishable from one that arrived.

Related topics:
- [Business Intelligence](../topics/business-intelligence.md)
- [Go To Market](../topics/go-to-market.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Proactive Agent Systems Need Observation, Personalization, Timing, and Workflow Embedding](proactive-agent-systems-need-observation-personalization-timing-and-workflow-embedding.md)
- [Alert on Account Change Events, Including the Ones That Are Absences](alert-on-account-change-events-including-absences.md)
- [Layer Ask, Push, and Self-Serve Because Teams Interface Differently](layer-ask-push-and-self-serve-because-teams-interface-differently.md)
- [Split a Generated Narrative Into Drafter, Fact-Checker, and Tone Agents](split-generated-narrative-into-drafter-checker-and-tone-agents.md)
- [Close the Eval-to-Action Loop So Signal Survives the Dashboard](close-the-eval-to-action-loop-so-signal-survives-the-dashboard.md)
- [Choose AI coworker form factors by interaction mode](choose-ai-coworker-form-factors-by-interaction-mode.md)
- [Crystallize the UI for Repeated Use Cases and Generate It for Novel Ones](crystallize-the-ui-for-repeated-use-cases-and-generate-it-for-novel-ones.md)

Sources:
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 05:50-06:11, 08:57-10:04, 11:55-12:03, 15:02-15:15
