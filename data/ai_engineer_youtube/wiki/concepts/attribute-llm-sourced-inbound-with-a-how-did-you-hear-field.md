# Attribute LLM-Sourced Inbound With a How-Did-You-Hear Field

Summary: Assistant recommendations arrive with no referrer, so the ordinary analytics stack cannot see them. A free-text "how did you hear about us?" question on onboarding can — it detected a dated spike and ranked assistant recommendation as one library's largest single inbound source, which is the cheapest available instrument for a channel that is otherwise invisible.

Use when:
- You want to know whether agent-experience work is producing adoption, not just better scores.
- Deciding what to measure first for generative-engine optimization, before building a prompt harness.
- A team asserts that "LLMs are sending us users" with nothing behind it.

Details:
- **The instrument and the finding.** "We had an onboarding [form] that said, 'How did you hear about this?' And we started to get spikes from April 13th. Now it is our number one source of inbound is Claude, ChatGPT, Codex, that is ChatGPT, Gemini recommending us." Nothing was built for this; an existing signup field turned into channel attribution when the answers changed. ([Burns](../sources/20260826_V_5bn4q-vAI.md), 02:17-02:39)
- **Why the usual analytics miss it.** A recommendation made inside an assistant produces no referrer, no UTM parameter, and often no click at all — the agent installs the package on the user's machine. Self-report is not a fallback here; it is the only place the event surfaces.
- **What the date buys you.** A named start date turns a level into an event. It gives a before/after boundary to line changes up against — a release, a docs change, a model version — which a rolling percentage does not. Record the date the spike began, not just the current share.
- **This is the downstream half of a two-instrument pair.** [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md) measures the assistant's behavior directly by running prompt sets and counting mentions — controllable, repeatable, and synthetic. This measures the real population, uncontrolled and unrepeatable. Neither substitutes: a prompt harness can show a mention rate rising while nobody installs anything, and an inbound spike cannot tell you which prompt shape produced it. The same talk that supplies the prompt-set method also names the distinction that matters on this side — mentions versus recommendations — and only the second one shows up in a signup form.
- **A distinction the free-text field will not draw for you.** "An LLM told me to install it" covers at least two different events: an assistant answering a question in chat, and a coding agent installing the package unattended during a task. They imply different work — the first is a content and retrieval problem, the second a package-and-docs problem ([Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)). If you are adding the field deliberately rather than inheriting it, make that separation askable.
- **Known biases, since this is self-report.** Only users who complete onboarding answer, so it measures converted inbound rather than reach; free-text answers require grouping, and the grouping is a judgment; naming an assistant is more memorable than "I saw it in a blog post," which plausibly inflates the assistant category relative to diffuse channels. The wiki's own caution about vendor-reported numbers applies — treat "number one source" as a ranking one team observed, not a share.
- **Context for the size of the claim.** The library reports 3 million npm downloads, 45% month-on-month growth, and 2,800 production sites, from 1,200 downloads at an earlier conference talk (01:20-01:53). None of that growth is attributed to the channel with a method; the attribution field establishes that the channel exists and leads, not how much of the curve it explains.
- **Limit.** One vendor, one product category — consent banners, which a coding agent is unusually likely to be asked for by name — one free-text field, no volumes, no time window, and no comparison against other channels beyond the ranking.
- **The general form of the lesson: capture fields before you can use them.** This field worked because it was already on the form when the channel appeared. Rosenthal reports the inverse from OpenAI's inbound wave — "I would have added way more fields to our sign-up form, like phone number, because eventually when we did catch up and we built all the automation… I didn't have a lot of information to go follow up with people" — with the mitigation that extra fields can be optional so they cost little. A signup form is the one place where an uncollected field is permanently unrecoverable, which argues for over-capturing against uses that do not exist yet, including attribution. See [Reply to Every Inbound and Over-Capture at Signup](reply-to-every-inbound-and-over-capture-at-signup.md). ([Rosenthal](../sources/20260826_wdTRsfw0KG0.md), 04:31-05:04)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Product Strategy](../topics/product-strategy.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md)
- [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md)
- [The Install Handoff Is Now a Prompt](the-install-handoff-is-now-a-prompt.md)
- [Distribution Is the New Bottleneck for Developer Tools](distribution-is-the-new-bottleneck-for-devtools.md)
- [Score Agent-Readiness Against a Moving Baseline](score-agent-readiness-against-a-moving-baseline.md)
- [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md)
- [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)
- [Reply to Every Inbound and Over-Capture at Signup](reply-to-every-inbound-and-over-capture-at-signup.md)

Sources:
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 01:20-02:39
- [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../sources/20260826_wdTRsfw0KG0.md), 04:31-05:04
