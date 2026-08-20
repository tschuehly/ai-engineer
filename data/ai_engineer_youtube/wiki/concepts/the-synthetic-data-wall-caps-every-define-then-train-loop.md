# The Synthetic Data Wall Caps Every Define-Then-Train Loop

Summary: Every method for teaching a model your private corpus has the same shape — define a dataset, train on it, saturate — and unless the model is under-parameterized it eventually absorbs everything you generated. That gives a synthetic version of the data wall: adding compute stops buying depth, and the real design question is not which technique to use but what the *second* stage of training looks like.

Use when:
- A domain-adaptation roadmap assumes that more compute or more synthetic data keeps improving the model.
- Comparing continued training, distillation, and RL-on-generated-environments and finding no clear winner.
- Deciding what to build next after a first adaptation run stops improving.

Details:
- The requirement none of the methods meets: "the thing that we're really after is like to give the model more knowledge of D, or to get better depth of your domain. We want to be able to add compute arbitrarily in a way that makes the model better… I think none of the approaches I proposed do this." ([Engram](../sources/20260812_WiqDvX6isc4.md), 16:06-16:23)
- The reason, given as elementary rather than exotic — "basically for classical machine learning reasons, which is that whatever you do, you have to define the data set, and then you train on the data set, and eventually things saturate. So, even if it's like really hard, unless your model is under parameterized, eventually it will learn all the data." Note the corollary hidden in "unless under-parameterized": a model too small to fit your data would keep having something to learn, which is not the trade anyone wants. ([Engram](../sources/20260812_WiqDvX6isc4.md), 16:23-16:39)
- The name and the loop it implies: "this doesn't give… the beautiful scaling properties that we see out of pre-training. It's kind of like a data wall in in the synthetic sense, where when you create synthetic data from D and train on it, you eventually hit this upper bound where like you've learned all of the synthetic data. And then you have to do it again." ([Engram](../sources/20260812_WiqDvX6isc4.md), 16:39-16:57)
- **The open question this reframes into, which is the practical takeaway:** "a lot of the missing components here are… how do you do it again? Like what's this second stage of training look like?" Any of the techniques can fill either stage — "the attention matching, or some type of self-study thing, or some continued pre-training" — so the unsolved part is the *sequencing and the escalation*, not the ingredient list. ([Engram](../sources/20260812_WiqDvX6isc4.md), 16:57-17:14)
- Why iterating naively does not escape it: "eventually you will fit the data and you'll know some about D, but you won't know everything and you'll no longer have this property where you can add compute and give the model more depth." Two distinct losses land at once — you plateau *and* you plateau short of knowing the corpus. ([Engram](../sources/20260812_WiqDvX6isc4.md), 17:14-17:26)
- The speaker's own reported evidence, and it is a negative result about his own company: "when we started the company, we we generated curves that look just like this blue curve where no matter sort of how much data we generate or how much we train, we kind of do plateau because there's this almost like natural upper bound to how much you can learn in one go from D." He claims "more sophisticated things you can do that make the training gradually harder" exist without describing them. ([Engram](../sources/20260812_WiqDvX6isc4.md), 18:05-18:32)
- What the wall does *not* say: it is not an argument against adapting models to private corpora. It is an argument against budgeting for one as if it scaled — the first pass has a bounded return that you should estimate before committing, and the plan needs an explicit answer for what happens after it saturates. The escape route the talk points at is [the AlphaGo property](seek-the-alphago-property-so-added-compute-keeps-buying-depth.md), and the other lever is enlarging the corpus itself ([Treat the Corpus Boundary as Negotiable, Not Fixed](treat-the-corpus-boundary-as-negotiable-not-fixed.md)).
- **How this qualifies existing wiki guidance.** [Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md) recommends expanding a small corpus into a diverse synthetic dataset — good advice that this page bounds rather than contradicts. The expansion fixes generalization; it does not create an unbounded axis, because the expanded set is still a set you defined and will eventually finish learning.
- Provenance and limits: asserted as a theoretical argument in a framing talk by a founder-adjacent researcher, with one unpublished negative curve as the only evidence and no numbers on it. The argument's premise — a fixed dataset is eventually memorized by a sufficiently large model — is standard; the strength of the conclusion depends on how much a smarter generation procedure can keep enlarging the effective dataset, which the talk asserts is possible and does not demonstrate.

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Seek the AlphaGo Property So Added Compute Keeps Buying Depth](seek-the-alphago-property-so-added-compute-keeps-buying-depth.md)
- [A Perfect Training Loss on Your Corpus Is Not Knowledge](a-perfect-training-loss-on-your-corpus-is-not-knowledge.md)
- [Continued Pre-Training on a Private Corpus Owes a Post-Training Debt](continued-pretraining-on-a-private-corpus-owes-a-post-training-debt.md)
- [Distill Behaving as if the Corpus Were in Context, Not the Documents](distill-behaving-as-if-the-corpus-were-in-context.md)
- [Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)
- [Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)
- [Treat the Corpus Boundary as Negotiable, Not Fixed](treat-the-corpus-boundary-as-negotiable-not-fixed.md)

Sources:
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 16:00-17:26, 18:05-18:32
