# Treat the Corpus Boundary as Negotiable, Not Fixed

Summary: "We have this corpus and cannot get more" is a modeling assumption, not a fact about your deployment. A person learning a subject does not confine themselves to the one book — they find related material, search, and go ask people who know. The same moves are available to a private-corpus project, and they reopen the data axis that the formal problem statement declares closed.

Use when:
- A domain-adaptation plan has been scoped as fixed-corpus and the returns are flattening.
- Deciding where to spend before spending it all on training compute.
- Someone frames private-data adaptation as a purely algorithmic problem.

Details:
- The observation, offered as an aside inside a talk whose whole frame is the opposite: "one thing that's been beneficial for us to realize is that the amount of data isn't really fixed. There are a lot of ways that you can get more data afterwards." ([Engram](../sources/20260812_WiqDvX6isc4.md), 08:16-08:25)
- The analogy that carries the method: "if you're like studying a textbook or trying to learn a new language, it's not really like you're limited to the words of the textbook itself. There's like a lot of stuff you can do. Like you can find other textbooks, you can go on the internet and search for related things. You can even be proactive and talk to speakers of the language or people who know the thing that you're trying to learn." ([Engram](../sources/20260812_WiqDvX6isc4.md), 08:30-08:54)
- The conclusion: "So, in practice I think the data access is very interesting and not actually fixed." He then sets it aside to state the idealized problem — "from like a core idealistic standpoint… how do you scale more compute given the same data?" — which is how the constraint gets baked into everything downstream. ([Engram](../sources/20260812_WiqDvX6isc4.md), 08:54-09:10)
- Three concrete moves fall out, and they are ordered by cost rather than by sophistication: **adjacent public material** that contextualizes the private corpus (the "other textbooks" move), **targeted retrieval** of related outside information (the "search the internet" move), and **elicitation from the people who hold the knowledge** — the move that manufactures data that never existed in any corpus. The third is the one an all-algorithmic framing never proposes.
- Why it deserves its own page rather than a footnote: the entire compute-only argument in the same talk follows from "we can't create new data," so the aside undercuts a premise the talk otherwise treats as settled ([Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)). It also offers a second escape from [the synthetic data wall](the-synthetic-data-wall-caps-every-define-then-train-loop.md) alongside the algorithmic one: enlarging D is a different lever from making the training curriculum escalate, and it is available today.
- The distinction that keeps this honest: adjacent material and elicited answers are *new information*, whereas synthetic data generated from D is a reorganization of information you already had. Only the former raises the ceiling on what a model can learn about your domain; the latter changes how efficiently the model absorbs what is there.
- Where the wiki has the operational version: [Demand-Driven Context Pulls Knowledge From Failed Work](demand-driven-context-pulls-knowledge-from-failed-work.md) uses the agent's own failures to decide what to go ask for, which is this idea with a targeting mechanism attached, and [Last-Mile Domain Context Beats Model Chasing](last-mile-domain-context-beats-model-chasing.md) is the measured case for spending there rather than on the model.
- Provenance and limits: a 45-second aside with no method, no example from the speaker's own work, and no measurement, immediately set aside in favor of the fixed-data formulation. It is a useful corrective to the framing, not a validated technique — and eliciting knowledge from people has consent, cost, and confidentiality dimensions the talk does not touch.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Models](../topics/models.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)
- [The Synthetic Data Wall Caps Every Define-Then-Train Loop](the-synthetic-data-wall-caps-every-define-then-train-loop.md)
- [Demand-Driven Context Pulls Knowledge From Failed Work](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Last-Mile Domain Context Beats Model Chasing](last-mile-domain-context-beats-model-chasing.md)
- [Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)
- [Optimize Capture Bandwidth Before Note Organization](optimize-capture-bandwidth-before-note-organization.md)

Sources:
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 08:13-09:10
