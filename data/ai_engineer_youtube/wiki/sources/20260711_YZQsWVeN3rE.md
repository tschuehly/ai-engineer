# Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech

Source: [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](https://www.youtube.com/watch?v=YZQsWVeN3rE)
Uploaded: 2026-07-11
Transcript: `raw/20260711_YZQsWVeN3rE/YZQsWVeN3rE.en-orig.vtt`

## Summary

Alex Bauer (co-founder, Upside — "the data layer for GTM engineers") argues the AI hallucination problem grew up into a harder **trust problem**: asked to report revenue, an agent never says "I'm not sure," it hands you a wrong answer "that looks exactly like being right." His practical thesis is that trust patterns for AI are not new — "when in doubt, manage your agents like other humans" — and he walks three production patterns Upside runs for go-to-market (GTM) analytics, where non-engineers ("technical enough to be dangerous") now build with an "infinite supply of valedictorian interns." The patterns: (1) a **librarian** every agent consults before acting, which injects just-in-time business definitions (fiscal calendar, what "pipeline" means) and the schema of prior failed queries so the agent stops guessing; (2) a **jury-and-judge** workflow for subjective questions with no empirically correct answer (multi-touch attribution), where independent analysts each produce an evidence-cited opinion and a consensus judge weighs their reasoning quality rather than treating any as fact, escalating and expanding the jury when consensus is weak; and (3) **agent tiers** — "you can't fix stupid," so don't run important work on weak harnesses or models crowbarred into per-seat pricing that "doesn't leave enough space for an intelligent reasoning model." His one prompting tip: use **commander's intent** (tell the agent *why*), with the caveat that agents trained on human material tend to micromanage themselves.

## Extracted Concepts

- [Run a jury of analysts and a consensus judge for no-ground-truth questions](../concepts/run-a-jury-of-analysts-and-a-consensus-judge-for-no-ground-truth-questions.md) - the attribution jury-and-judge workflow: independent evidence-cited opinions weighed by a judge, escalate-and-expand on weak consensus.
- [Preflight agents through a business-definitions librarian](../concepts/preflight-agents-through-a-business-definitions-librarian.md) - a service every agent consults before querying, supplying just-in-time definitions and prior-failed-query schemas so it doesn't guess business terms.
- [Manage AI agents like humans with commander's intent](../concepts/manage-ai-agents-like-humans-with-commanders-intent.md) - reuse human-team trust patterns; prompt the *why* not the *how*, and watch for self-micromanagement.
- [Agent harnesses combine model, tools, prompts, filesystem, skills, hooks, and memory](../concepts/agent-harnesses-combine-model-tools-prompts-filesystem-skills-hooks-and-memory.md) - the "agent tiers" checklist for a tier-two harness (powerful model, sub-agents, plan mode, full MCP, file editing) and why per-seat-priced AI features starve the model.
- [Make agent work more trustworthy by making it verifiable](../concepts/make-agent-work-more-trustworthy-by-making-it-verifiable.md) - the "wrong answer that looks like right" trust problem, verified with citation/track-record cards and scaffolding before YOLO.

## Topic Links

- [Agents](../topics/agents.md)
- [Business Intelligence](../topics/business-intelligence.md)
- [Evaluation](../topics/evaluation.md)

## Notes

- The trust problem is hallucination's "older sibling": ask Claude to report on revenue and "it doesn't say 'I'm not sure,' it says 'Here you go,'" returning a wrong answer that looks exactly like being right — most dangerous for high-stakes numeric GTM outputs. (07:39-07:57)
- Age of agentic GTM: GTM teams historically were low-density builders (spreadsheets and slides) whose toolbox AI upgrades; Cloud "does for building basically what the bicycle did for mobility," turning idea-havers into builders with "an infinite supply of valedictorian interns with computer science degrees." (05:15-07:19)
- Thesis: establishing trust with AI "actually isn't new… we already know a lot about how to do this for people" — "when in doubt, manage your agents like other humans." (08:30-08:48)
- Commander's intent (from armed-forces doctrine): tell the agent *why* you want something and it performs better — "works for humans as well," and people (and models) dislike being micromanaged. Caveat: agents trained on human material like to micromanage themselves — "Don't tell Claude to improve itself, you'll get micromanagement… pull it back and say, remember we're talking about the why." (08:48-09:28)
- Scaffold before YOLO: rebuilding the company website in "YOLO mode" (even with Claude plan mode) failed; the fix is to first tell the agent how the business works via maintained **anchor assets** — a product-capabilities reference, personas, positioning. Structure first, then turn Claude loose. (09:28-11:30)
- Product-capability cards were AI-compiled and each shows what the capability does, why it matters per persona, and a **track record of citations** across every connected system so "it didn't hallucinate the important parts." Persona Bench = a set of agents inhabiting each key persona that can review work on demand. (10:33-12:12)
- Librarian (a real Upside product feature): naive agent asked "How much pipeline did we create in Q1?" would assume quarter = Jan–Mar and use created date — "probably not correct." Instead it consults the librarian first, which has documentation, a library of company knowledge items, and the **schema of prior failed queries**, giving just-in-time memory (fiscal year is Feb–Apr; "pipeline" = stage 2 or later) and returning a trustworthy answer with citations. (12:12-13:10)
- Jury-and-judge (Upside's multi-touch attribution workflow, "enabled by Opus"): for a class of GTM questions with "no empirically correct answer," the agent spins up a team of independent analysts who each examine the data independently and return an evidence-cited attribution opinion; a consensus judge treats these "not as fact… as input," weighs each analyst's reasoning quality, produces the final version, and "if there's not enough consensus, then I'll escalate and expand the jury." Mirrors trial by a jury of peers; "multiple researchers with somebody who helps at the end is better than a single person perseverating." (13:16-15:15)
- Agent tiers ("you can't fix stupid"): "friends don't let friends use really bad harnesses or low intelligent models for important work." Slackbot's new MCP-client feature was "horrifically stupid" because any AI product "crowbarred into a per-seat subscription model" lacks the margin for an intelligent reasoning model. Use at least tier two: a powerful model with sub-agents, plan mode, full MCP support, and file editing — don't hand your team the ChatGPT web interface and expect a great result. (15:15-16:34)
