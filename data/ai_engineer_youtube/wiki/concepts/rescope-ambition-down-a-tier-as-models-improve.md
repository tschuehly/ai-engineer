# Rescope Ambition Down a Tier as Models Improve

Summary: Each jump in model capability doesn't just make you faster at the same work — it shifts what scope of product a solo builder or small team can own down one tier, so the durable move is to rescope your ambition up (attempt what was "too big") rather than pocket the gain on unchanged work.

Use when:
- Deciding what a small team or solo builder should attempt now versus a year ago.
- Explaining why a stronger model doesn't help work that was already trivial for the previous model.
- Scoping automation: recognizing that a former "service" or "startup" may now be a smaller artifact.

Details:
- Theo Browne's tier ladder: what he'd have called a *side project* (a Reddit meme scraper, 2-3 days), a *startup* (a YC company, Ping/"Zoom for streamers"), and *too big* (a full-stack cloud with auth and databases) — "Now that the models are bigger, the tiers have shifted. Everything is now one tier lower." What was a startup is now a side project. 09:29-11:02
- A new bottom tier appears below "side project": executable natural language. "The fact that you can now execute markdown by just piping it to Codex or Claude is unbelievable." A PR-triage service became a single markdown file that tells an agent to read open PRs across repos, prioritize, and write a static HTML report to S3 — run on a cron at 9 a.m., producing the day's work list by ~9:15. 11:02-12:20
- The gain is wasted if you don't scale ambition to match: "Most of the Jira tickets I closed in my previous job could be trivially solved with Opus 4.5. My previous work would not benefit from Mythos." Since models improve faster than humans do, the response is to "go bigger," not to get better at the old tier. 02:59-03:34
- Caveat: the old ceiling has genuinely blurred — "I don't know what too big means anymore" (training your own model? an OS? competing with NPM directly?) — so finding the new limit requires deliberately attempting projects that feel oversized. 12:22-13:05
- The tier collapse rests on the orchestration-era model handling large implementations from a prompt with no custom "software factory" — see the model-eras framing in the related capability-tiers concept.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Think Wider, Not Bigger: Compete on Breadth via User Extensibility](think-wider-not-bigger-compete-on-breadth-via-extensibility.md)
- [Coding-Agent Capability Tiers Change the Bottleneck](coding-agent-capability-tiers-change-the-bottleneck.md)
- [Repo-Local Markdown Tasks Give Agents Durable Scoped Work Units](repo-local-markdown-tasks-give-agents-durable-scoped-work-units.md)
- [Agentic Coding Collapses Coordination Tax for Small Valuable Changes](agentic-coding-collapses-coordination-tax-for-small-valuable-changes.md)

Sources:
- [Everything we knew about software has changed — Theo Browne, @t3dotgg](../sources/20260708_xUnRQ9vLXxo.md), 02:59-13:05
