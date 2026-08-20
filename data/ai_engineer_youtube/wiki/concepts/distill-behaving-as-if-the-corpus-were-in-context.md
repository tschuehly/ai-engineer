# Distill Behaving as if the Corpus Were in Context, Not the Documents

Summary: On-policy distillation for a private corpus does not transfer the documents — it transfers the *behavior* a model exhibits when the documents are in its prompt. That reframing decides the hard part: raw documents are the wrong distillation target, so the technique needs generated questions and answers conditioned on the corpus, which is what self-study in the cartridges paper supplies.

Use when:
- Designing a distillation run whose goal is domain knowledge rather than reasoning-trace compression.
- Deciding what data to feed a distillation pipeline over an unstructured internal corpus.
- Distinguishing on-policy distillation from ordinary SFT on documents when both are proposed.

Details:
- The trick, stated plainly: "you have text and you show it to the model and then you make the model think that the text is in context. That's more or less the trick of on policy distillation. The on policy part just means you kind of update the model throughout training." ([Engram](../sources/20260812_WiqDvX6isc4.md), 13:20-13:41)
- The verdict on the algorithm itself: "It works. It's it's a pretty good algorithm." The problem is not the optimizer. ([Engram](../sources/20260812_WiqDvX6isc4.md), 13:41-13:45)
- **The load-bearing constraint:** "maybe the main one being like what data do you actually do this with? You can't really distill the raw documents." A document is not a behavior — there is no teacher output to match if the corpus is just text sitting there. ([Engram](../sources/20260812_WiqDvX6isc4.md), 13:45-13:54)
- The fix, named: "techniques like self-study from the cartridges paper… try to generate like question and answer pairs conditioned on D and then train the model to behave as if it is seeing D in context when it's answering questions. I think this is like close to the behavior you want." ([Engram](../sources/20260812_WiqDvX6isc4.md), 13:54-14:12)
- Why this framing is worth carrying beyond the specific technique: it converts a knowledge-acquisition problem into a *behavior-cloning* problem with a teacher you can actually construct — put D in the window, let the model answer, and train the version without D to answer the same way. The corpus becomes a conditioning input for generating supervision rather than the supervision itself.
- **Contrast with the wiki's other distillation page.** [Distill reasoning traces into small models](distill-reasoning-traces-into-small-models.md) starts from a teacher that already produces the target behavior on the task; here no such teacher exists until you manufacture one by stuffing the context. The two share machinery and differ in where the supervision comes from, which is the part that dominates the engineering effort.
- The relationship to the naive baseline it replaces is direct: training next-token on D produces a model that recites, because [a perfect training loss on your corpus is not knowledge](a-perfect-training-loss-on-your-corpus-is-not-knowledge.md). Generating Q/A pairs conditioned on D is the same repair the wiki's [curated synthetic data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md) page prescribes, arriving here through a different route.
- The caveat the talk flags but does not spend: this approach "also has some properties that are not necessarily appealing" — which turn out to be the shared ceiling of the whole family, not something specific to distillation ([The Synthetic Data Wall](the-synthetic-data-wall-caps-every-define-then-train-loop.md)). ([Engram](../sources/20260812_WiqDvX6isc4.md), 14:12-14:18)
- Provenance and limits: a one-minute characterization of other people's work by a researcher at a company pursuing a different approach, with no results, no comparison, and no description of self-study beyond "question and answer pairs conditioned on D." The cartridges paper is the thing to read; the durable content here is the *framing* of what distillation transfers, not any claim about how well it performs. The transcript attributes on-policy distillation to another speaker at the same event by first name only.

Related topics:
- [Models](../topics/models.md)
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Distill reasoning traces into small models](distill-reasoning-traces-into-small-models.md)
- [Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)
- [A Perfect Training Loss on Your Corpus Is Not Knowledge](a-perfect-training-loss-on-your-corpus-is-not-knowledge.md)
- [KV Compaction Reaches Only What Already Fits in Context](kv-compaction-reaches-only-what-already-fits-in-context.md)
- [Continued Pre-Training on a Private Corpus Owes a Post-Training Debt](continued-pretraining-on-a-private-corpus-owes-a-post-training-debt.md)
- [The Synthetic Data Wall Caps Every Define-Then-Train Loop](the-synthetic-data-wall-caps-every-define-then-train-loop.md)

Sources:
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 13:10-14:18
