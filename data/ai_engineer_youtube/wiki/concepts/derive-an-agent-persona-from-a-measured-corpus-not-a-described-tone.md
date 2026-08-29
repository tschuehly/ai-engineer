# Derive an Agent Persona From a Measured Corpus, Not a Described Tone

Summary: When an agent has to write as a specific person, the persona prompt should be measured off that person's own output — length distributions, sign-offs, recurring constructions — rather than assembled from adjectives, because a corpus produces checkable facts and self-description produces aspiration.

Use when:
- Building a drafting agent that writes in a named individual's voice rather than a brand's.
- A persona prompt is full of adjectives ("concise, warm, direct") and the output still does not sound right.
- You have an accessible archive of the person's prior output and are only using it for retrieval, not for style.

Details:
- The method is a measurement pass over the person's own archive: "analyze like 760 of my emails to figure out what my email voice is." ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 08:52-08:58)
- The extracted features are specific and low-level, which is the point — "I use 18 words on average per email and I like to end emails with best and not sincerely." A length statistic and a sign-off convention are things a person rarely reports about themselves accurately, and both are directly checkable in generated output. (08:58-09:06)
- The corpus size is worth noting for feasibility: 760 emails is one person's ordinary archive, not a curated dataset, and the analysis was done inside a one-week personal project. (08:23-09:09)
- Voice is only one of three components in the clone described here; the other two are a judgment calibration built from past decisions and a data-access grant. Persona measurement handles *how it sounds*, and does nothing about *what it decides* — see [Mine Chat History for Past Decisions and Turn Them Into Judgment Evals](mine-chat-history-for-past-decisions-and-turn-them-into-judgment-evals.md). (09:10-09:47)
- The features double as an evaluation surface, which is the practical advantage over adjective prompts: average length and sign-off can be measured on generated drafts without a judge model.
- **Limit.** No claim is made that matching the measured features improves acceptance, and no comparison against a described-tone prompt is reported. The statistics are presented as derived facts about the corpus, not as a validated recipe. (08:52-09:09)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Mine Chat History for Past Decisions and Turn Them Into Judgment Evals](mine-chat-history-for-past-decisions-and-turn-them-into-judgment-evals.md)
- [Layer Brand Voice Into Four Composable Prompt Tiers](layer-brand-voice-into-composable-prompt-tiers.md)
- [Prompt Voice Agents for Persona, Prosody, and Brand Fit](prompt-voice-agents-for-persona-prosody-and-brand-fit.md)
- [Scope a Person-Cloned Agent by Caller, With Drafts as the Shared Capability](scope-a-person-cloned-agent-by-caller-with-drafts-as-the-shared-capability.md)
- [Personal Knowledge Bases Become Agent Context Substrates](personal-knowledge-bases-become-agent-context-substrates.md)

Sources:
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 08:23-09:47
