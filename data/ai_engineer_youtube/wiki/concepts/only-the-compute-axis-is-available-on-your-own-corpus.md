# Only the Compute Axis Is Available on Your Own Corpus

Summary: Deep learning scales along three axes — more data, more compute, bigger models — and against a private corpus two of them are already spent before you start. You cannot manufacture more of your own emails, and you are not training from scratch on them, so you begin from someone else's pre-trained model and the only lever left is how much compute you spend turning that fixed corpus into model capability.

Use when:
- Deciding what "scaling" can even mean for a domain or personal model, before choosing a technique.
- Explaining why a private-data project cannot borrow the playbook that produced the frontier models.
- Sanity-checking a proposal that implicitly assumes the data axis is still open.

Details:
- The three axes and their track record: "we can train them on more data. We can train them for longer or add compute. Or we can make the models themselves bigger, like give them more capacity to acquire new information… really the entirety of the deep learning revolution comes from these three axes of scaling." ([Engram](../sources/20260812_WiqDvX6isc4.md), 05:10-05:36)
- The elimination, stated in order: "we can't create new data. So, like the kind of data scaling axis is out the window. Um I think we also probably agree that we can't train a model from scratch on our data. So… you very likely want to start from a pre-trained model. Um, this leaves us with essentially one axis of scaling, which is compute." ([Engram](../sources/20260812_WiqDvX6isc4.md), 07:26-08:11)
- The idealized question this reduces to — and the one worth putting to any vendor in this space — is "how do you scale more compute given the same data?" ([Engram](../sources/20260812_WiqDvX6isc4.md), 09:01-09:10)
- Why this matters rather than being a bookkeeping observation: the axes that remain open are the ones that keep improving, and they only touch public material. Models keep "getting better at… coding in the way that is public on GitHub… doing math in ways that are written in public textbooks, but they're not getting more knowledge of you or your life or your work." Waiting for the next model release does not move the private axis. ([Engram](../sources/20260812_WiqDvX6isc4.md), 07:03-07:15)
- **The one axis that is less closed than it looks.** The same talk immediately qualifies its own premise: a person studying a textbook is not limited to that textbook, and in practice "the data access is very interesting and not actually fixed." Read the compute-only framing as the idealized statement of the problem, not as a description of your options — see [Treat the Corpus Boundary as Negotiable, Not Fixed](treat-the-corpus-boundary-as-negotiable-not-fixed.md). ([Engram](../sources/20260812_WiqDvX6isc4.md), 08:13-09:00)
- What "spend compute" cashes out to is the subject of the rest of that talk, and every option has a documented ceiling: [naive continued training](a-perfect-training-loss-on-your-corpus-is-not-knowledge.md), [KV compaction](kv-compaction-reaches-only-what-already-fits-in-context.md), [on-policy distillation](distill-behaving-as-if-the-corpus-were-in-context.md), and [continued pre-training on synthetic data](continued-pretraining-on-a-private-corpus-owes-a-post-training-debt.md) all hit [the same wall](the-synthetic-data-wall-caps-every-define-then-train-loop.md).
- Provenance: asserted as a first-principles argument by a researcher at a startup founded to work this axis; no measurement accompanies it, and the talk explicitly is "not… a super detail-oriented talk." The argument is structural and checkable on its own terms rather than empirical. ([Engram](../sources/20260812_WiqDvX6isc4.md), 00:24-00:39, 07:17-08:11)

Related topics:
- [Models](../topics/models.md)
- [Context Engineering](../topics/context-engineering.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Post-Training Data Is Public by Construction](post-training-data-is-public-by-construction.md)
- [Treat the Corpus Boundary as Negotiable, Not Fixed](treat-the-corpus-boundary-as-negotiable-not-fixed.md)
- [The Synthetic Data Wall Caps Every Define-Then-Train Loop](the-synthetic-data-wall-caps-every-define-then-train-loop.md)
- [Private Microworlds Are the Next Training-Data Opportunity](private-microworlds-are-the-next-training-data-opportunity.md)
- [Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)
- [Last-Mile Domain Context Beats Model Chasing](last-mile-domain-context-beats-model-chasing.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)

Sources:
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 05:10-09:10
