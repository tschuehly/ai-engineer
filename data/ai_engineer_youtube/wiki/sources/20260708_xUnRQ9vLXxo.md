# Everything we knew about software has changed — Theo Browne, @t3dotgg

Source: [Everything we knew about software has changed — Theo Browne, @t3dotgg](https://www.youtube.com/watch?v=xUnRQ9vLXxo)
Uploaded: 2026-07-08
Transcript: `raw/20260708_xUnRQ9vLXxo/xUnRQ9vLXxo.en-orig.vtt`

## Summary

Closing keynote of AIEWF2026. Theo Browne argues that recent model jumps aren't just "better at coding" — they change what scope of product a builder can attempt. He frames three model eras: Sonnet 3.5 as the tool-call era (first reliable multi-step tool use in a real codebase), Opus 4.5 as the long-running-task era (tests and completes hour-scale work without losing track), and Mythos as the orchestration era (the model "understands itself," spawns and verifies subagents, and does so just from a prompt — no custom "software factory" needed). His thesis: to benefit from these gains you must "go bigger," which requires shedding legacy developer habits (terminals, Git conventions, Vim, language identity, sunk-cost attachment to code) that are skeuomorphic holdovers optimized for familiarity, not utility. Concretely, the tiers of ambition have each dropped one level — what was a startup is now a side project, and a whole class of former services collapses to a "markdown file on a cron" piped to an agent. Finally, he reframes "bigger" as "wider": AI collapses the cost of breadth, so small teams can now span the surface area of an AWS or Salesforce by architecting products for user-driven extensibility (users build the missing vertical features themselves, as happened accidentally with Slack). "If your idea doesn't feel stupid, it's cuz your idea's not big enough."

## Extracted Concepts

- [Rescope Ambition Down a Tier as Models Improve](../concepts/rescope-ambition-down-a-tier-as-models-improve.md) - the tiers of buildable ambition each dropped a level, and a new bottom tier is executable natural language on a cron.
- [Think Wider, Not Bigger: Compete on Breadth via User Extensibility](../concepts/think-wider-not-bigger-compete-on-breadth-via-extensibility.md) - AI collapses the cost of breadth, so architect for user-built extensions instead of matching a giant's depth.
- [Reject Skeuomorphic Dev Tooling and Legacy Workflow Constraints](../concepts/reject-skeuomorphic-dev-tooling-and-legacy-constraints.md) - our terminals, Git conventions, and language identity are familiarity-driven holdovers to question in the AI era.
- [Coding-Agent Capability Tiers Change the Bottleneck](../concepts/coding-agent-capability-tiers-change-the-bottleneck.md) - independent field framing of model eras: tool-call → long-running task → prompt-native orchestration.

## Topic Links

- [Product Strategy](../topics/product-strategy.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

## Notes

- Model eras (00:54-03:03): Sonnet 3.5 = the first model to do tool calls consistently and reliably enough for day-to-day codebase work; Opus 4.5 = long-running tasks (tests its own work, completes hour-scale tasks without losing track, needs no step-by-step handholding); Mythos = orchestration — "the first model that doesn't just understand your code base, but it understands itself," spawns additional models and breaks up work to be completed more reliably and verified afterward, and "you don't need some custom tooling, some fancy software factory. You just need to prompt it to go a little further" (02:39-03:01).
- The capability gain doesn't help unless you scale ambition to match it: "Most of the Jira tickets I closed in my previous job could be trivially solved with a model like Opus 4.5. My previous work would not benefit from a model like Mythos" (02:59-03:22). "The models are getting better faster than we are... instead we have to go bigger" (03:22-03:34).
- Skeuomorphism analogy (04:09-06:41): iOS 6→7 dropped skeuomorphic textures once Apple no longer had to *convince* users a phone could replace a physical compass/book; the flatter iOS 7 compass is objectively more useful (clear target vs current-heading, big numeric readout). "We're currently in our skeuomorphic phase as software developers... We're pretending our terminals are the ultimate interface when they're not even good interfaces... Natural language has no place in a terminal, but we pretend it does because the terminal's familiar" (06:08-06:36).
- Legacy constraints to question (07:00-09:28): qualifying yourself by languages you know; "why can't we commit our environment files?" — an arbitrary Git default that "took over our brains"; sunk-cost attachment and "guilt merging" a PR that isn't the right solution because a teammate spent a week on it. "One of the nice things about a[gents] — you don't have to feel bad when you shut down their work" (09:12-09:18).
- Tier shift (09:29-11:02): three of his own projects — a Reddit meme scraper (2-3 day *side project*), Ping/"Zoom for streamers" (a YC *startup*), and a full-stack cloud ("Vercel but with auth and databases built in," *too big*). "Now that the models are bigger, the tiers have shifted. Everything is now one tier lower." What was a startup is now a side project.
- The new bottom tier (11:02-12:20): "the G brain tier. It's a markdown file." "The fact that you can now execute markdown by just piping it to Codex or Claude is unbelievable." His PR-triage service is now a markdown file: it tells the agent to read open PRs across four repos, assess status, prioritize, then write a static HTML file and push it to S3 and return the URL — run on a cron every morning at 9:00 a.m., producing his work list by ~9:15-9:20. "You'd be amazed how many of these types of things can exist that are literally just a markdown file running on a cron."
- "Too big" is now undefined (12:22-13:05): "I don't know what too big means anymore. Is it training your own model from scratch? ... building your own operating system? ... compete with NPM and Node directly? I don't know."
- Think wider (13:06-15:42): breadth (range of things covered) vs depth (features per area). Old rule: you couldn't out-*breadth* AWS with a small team, so you competed on depth in a narrow space (Vercel = deep front-end-leaning full-stack, "so much so that even the agents prefer it"). New rule: breadth is viable — "you can build a database platform into your product in a day or two of work with enough prompting" — if you architect for extensibility so users build the vertical features you don't support. Slack "accidentally did this" — "the platform people run their agents in half the time... it's the right shape for people to build the features they want into it." Closing line: "If your idea doesn't feel stupid, it's cuz your idea's not big enough."
