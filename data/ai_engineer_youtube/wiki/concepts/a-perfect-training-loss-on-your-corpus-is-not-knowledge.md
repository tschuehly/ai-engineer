# A Perfect Training Loss on Your Corpus Is Not Knowledge

Summary: Running next-token prediction over a private document set will drive training loss to essentially zero and produce a model that reproduces the corpus perfectly and generates nothing coherent. Low loss on D measures absorption, not the capability you wanted, so it is the wrong success signal for any private-corpus adaptation run — and its failure is two independent problems, not one.

Use when:
- A continued-training run on internal documents reports excellent loss and you are about to call it working.
- Choosing the acceptance criterion for a domain adaptation experiment before starting it.
- Explaining to a stakeholder why "we trained on all our docs" did not produce a model that knows the company.

Details:
- The experiment as described: take a set of 10K financial reports, "you want it to be in the weights. You want the model to answer questions about them. You want the model to be able to create new ones… and then you just train theta on the context that you have. You can get to a loss of like 0.0001… and you can end up with a model that knows the data perfectly well. And then when you generate from it, it basically collapses." ([Engram](../sources/20260812_WiqDvX6isc4.md), 10:50-11:24)
- **Failure one — it is a bounded axis, not a scaling axis.** "There's some information in that just gets perfectly transferred into the model and then you no longer learn. So, this is like not an indefinite axis of scaling." Even in the best case, spending more compute stops buying anything once the corpus is absorbed. ([Engram](../sources/20260812_WiqDvX6isc4.md), 11:24-11:40)
- **Failure two — it does not work even inside the bound.** "It just frankly doesn't work. Like, just doing this kind of next token prediction on the data you have doesn't produce a model that has interesting generalization properties like normal models. Like, it can't answer any question unless the question is perfectly encoded in the data with its answer, which is like never the case in practice." ([Engram](../sources/20260812_WiqDvX6isc4.md), 11:40-11:59)
- The two failures are worth keeping separate because they have different implications. The first says this technique has a ceiling; the second says it does not reach the ceiling. A fix for one is not a fix for the other.
- The precondition under which it would work is stated and then dismissed: "unless you have a D that's so wide it can sort of simulate the effect of pre-training, which no one has, then this doesn't work very well." Corpus *width* — the diversity that makes pre-training generalize — is the missing property, not corpus size. ([Engram](../sources/20260812_WiqDvX6isc4.md), 10:37-10:47)
- **The same speaker reported the same failure with a different corpus eight months earlier**, and the pair is worth reading together: an earlier experiment on financial reports produced a model that "could memorize the document but failed on slightly different prompts and became overly specific" ([Stuffing Context is not Memory](../sources/20251229_Jty4s9-Jb78.md), 26:01-29:21). The 2026 restatement adds the diagnostic detail that makes it actionable — the loss number looks *excellent* at exactly the moment generation collapses, so the metric a training loop optimizes is anti-correlated with the outcome near the end of the run.
- The repair the wiki carries is not "train harder" but "train on something else": expand the corpus into a larger, diverse synthetic distribution that preserves the facts, so the model answers variants rather than reciting ([Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)). That repair has its own ceiling — see [The Synthetic Data Wall](the-synthetic-data-wall-caps-every-define-then-train-loop.md).
- Provenance and limits: no dataset description, model, eval, or baseline accompanies the numbers, and the talk is explicitly a framing talk rather than a results talk. Treat "0.0001" as illustrating "essentially zero" rather than as a measurement, and note the caption ambiguity in "10K financial reports" (ten thousand reports, or SEC 10-K filings) recorded on the source note. ([Engram](../sources/20260812_WiqDvX6isc4.md), 00:24-00:39)

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)
- [The Synthetic Data Wall Caps Every Define-Then-Train Loop](the-synthetic-data-wall-caps-every-define-then-train-loop.md)
- [Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)
- [Distill Behaving as if the Corpus Were in Context, Not the Documents](distill-behaving-as-if-the-corpus-were-in-context.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)

Sources:
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 10:29-11:59
- [Jack Morris: Stuffing Context is not Memory, Updating Weights is](../sources/20251229_Jty4s9-Jb78.md), 26:01-29:21
