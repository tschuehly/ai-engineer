# Frequency, Not Volume, Drives Web-Context Cost

Summary: Web-sourced context decays fast enough that it is never a snapshot, so the cost driver is how often you re-ask about the same entities rather than how many entities you have. Every repeated query costs what the first one did — even when nothing changed and the answer comes back identical — so a per-record price must be multiplied by refresh cadence, not by row count.

Use when:
- Budgeting a research, monitoring, enrichment, or due-diligence agent that revisits the same entities over time.
- A cost model built from "N records × price per record" is about to be signed off.
- Deciding refresh cadence for web-derived context, or explaining why a pilot's economics do not survive production.
- Arguing about whether long context windows or bigger batches change the bill.

Details:
- The decay premise: a chart from Bright Data's own team measuring "how long after a new page, a new piece of content goes live, it is no longer relevant" puts social media at "far less than a day" and news, finance, and retail at "30 days later, data that was collected mostly no longer relevant." No methodology for the chart is given, so treat the shape (fast, domain-dependent decay) as the durable claim rather than the specific curve. (02:47-03:09)
- The consequence: "extracting context from the web or relying on the web is not a snapshot. It's not a one-time effort. It's not even a monthly effort… an ongoing process." (03:09-03:28)
- The reinterpretation of scale is the core move. Asked "what happens with a million?", the answer is not a context-window problem: "a million records will not fit in a context… You can think about a million in terms of the frequency." (14:05-14:16)
- The worked case is private-equity due diligence: "I revisit these companies all the time. I ask more questions about them as the time goes by. Was there any new news about them? Was there anything that changed? Did somebody join? Did somebody leave? Do they have new hires? I keep on asking the same thing… It's not just about the number of companies. It's the frequency in which I'm asking it." (14:16-14:38)
- The pricing property that makes this bite: "Frequency is the cost killer… Every repeated query costs the same as the first. Even if it brought back the exact same answers. Nothing changed? Pay up." Noise and false positives are billed identically. (14:38-15:02)
- Volume discounts do not rescue it: token cost "doesn't shrink well over time. There's always some volume element in terms of the cost, but it's not the same as flatlining." (15:02-15:14)
- Practical consequences: quote a rented-context path as *price × entities × refreshes per period over the horizon you actually intend to run*, not price × entities; and treat cadence as a first-class design parameter, because it is the term the vendor bill is most sensitive to and the one teams silently reduce under pressure (see [Cost Pressure Silently Shrinks Research Scope](cost-pressure-silently-shrinks-research-scope.md)).
- This is the failure mode that inverts under ownership: once the pipeline is yours, the marginal query is effectively free, so re-asking becomes cheap exactly where it was most expensive. That is the argument for [finding the crossover point](find-the-crossover-point-between-renting-and-owning-context.md), and the reason the speaker's closing framing is "owned context compounds while rented decays." (19:46-20:16, 21:32-21:44)
- **The same economics with a per-field rather than per-source granularity.** Purchased account data makes continuous refresh unaffordable — "it's incredibly expensive to update data all the time, especially if you're purchasing it. So, I can't just update all the fields" — and the ranking signal is how fast each field moves: "employee count change[s] all the time. Other data points like headquarters location change very rarely." Frequency drives the bill here too, but the unit that carries the frequency decision is the field, not the corpus, which makes the policy a table rather than a schedule. ([Berry](../sources/20260826_UhCY231d0FQ.md), 05:38-05:50, 07:44-07:54)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Find the Crossover Point Between Renting and Owning Context](find-the-crossover-point-between-renting-and-owning-context.md)
- [Cost Pressure Silently Shrinks Research Scope](cost-pressure-silently-shrinks-research-scope.md)
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)
- [Context as a Service Is Vertical Search for Agents](context-as-a-service-is-vertical-search-for-agents.md)
- [Do not cache context-engine answers as durable truth](do-not-cache-context-engine-answers-as-durable-truth.md)
- [Agents Punish Bad Data and Need Question and Tracking Data Foundations](agents-punish-bad-data-and-need-question-and-tracking-data-foundations.md)
- [Refresh Record Fields Selectively by Volatility and Price](refresh-record-fields-selectively-by-volatility-and-price.md)

Sources:
- [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../sources/20260814_Ot4OPrPH4xY.md), 02:47-03:28, 14:05-15:14, 19:46-21:44
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 05:38-05:50, 07:44-07:54
