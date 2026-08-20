# KV Compaction Reaches Only What Already Fits in Context

Summary: Compressing a corpus into a small set of key/value cache entries — the same mechanism coding agents use to survive long sessions — makes a model behave as though the data were in its prompt, cheaply. Its two limits are that it can only compress what fits in the window in the first place, and that it never takes a gradient, so it inherits none of the generalization that training buys.

Use when:
- Evaluating cache-compression or "context distillation into KVs" as a substitute for adapting a model to a private corpus.
- Deciding whether a compaction technique that works inside a coding agent will scale to a whole document store.
- Separating serving-cost optimizations from knowledge-acquisition techniques that look similar on a slide.

Details:
- What it is, anchored to shipping products: compaction is "similar to the way that, you know, Claude code or Codex or open code, what have you, does compaction. You take this really long context, which is D, and then you try to compress it into some set of KVs that can represent the data to the model in like a very succinct way." ([Engram](../sources/20260812_WiqDvX6isc4.md), 12:16-12:38)
- It can be learned rather than heuristic — the talk points at "a very cute paper that has like a kind of greedy algorithm for approximating KV compaction" — and the effect is that "if your data is small enough to fit into context, there are some interesting ways to like compress it to something very small and like pretend like your model knows this." ([Engram](../sources/20260812_WiqDvX6isc4.md), 12:38-13:00)
- **Limit one — the reach is the window.** "It only applies to things that are in context." A technique whose input is a filled context window cannot be the answer for a corpus that does not fit in one; it compresses what you already had, it does not acquire what you did not. ([Engram](../sources/20260812_WiqDvX6isc4.md), 13:00-13:05)
- **Limit two — no gradients.** It "misses, I think, some of the magic that you can get from… taking gradients." This is the sharper objection and the one that separates compaction from every training-based method on the same slide: cache state is an encoding of the text, while a weight update is an encoding of what the text implies. ([Engram](../sources/20260812_WiqDvX6isc4.md), 13:05-13:10)
- The practical read: compaction is a *serving* technique that borrows the vocabulary of a *learning* technique. It belongs in the same bucket as prompt caching and context management, not in the bucket with distillation and continued pre-training — which is why the next family in the same talk keeps the "make the model think the data is in context" goal but takes gradients to get there ([Distill Behaving as if the Corpus Were in Context](distill-behaving-as-if-the-corpus-were-in-context.md)).
- **Boundary against the wiki's compaction material.** The coding-agent pages treat compaction as a working practice — [frequent intentional compaction keeps agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md), and [prompt caching sets the break-even bar](prompt-caching-sets-the-break-even-bar-for-compaction.md) for when it pays. Nothing here contradicts that. The claim is narrower: those results are about surviving a session whose material already passed through the window, and they say nothing about whether the same mechanism can substitute for adapting a model to a corpus it has never seen.
- The motivation behind the whole family is worth keeping: "we know models are really good when you paste stuff into context. Like, in-context learning is is magical." The goal of every technique in this group is to buy that behavior without paying the window. ([Engram](../sources/20260812_WiqDvX6isc4.md), 12:03-12:16)
- Provenance: characterized in one paragraph of a framing talk by a competitor building a different approach; the cited paper is shown on a slide and not named in audio, and no comparison or measurement is offered. Read the referenced work before treating either limit as settled. ([Engram](../sources/20260812_WiqDvX6isc4.md), 12:38-13:10)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Distill Behaving as if the Corpus Were in Context, Not the Documents](distill-behaving-as-if-the-corpus-were-in-context.md)
- [Frequent, intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Prompt caching sets the break-even bar for compaction](prompt-caching-sets-the-break-even-bar-for-compaction.md)
- [Externalize agent state to files and reset instead of compact](externalize-agent-state-to-files-and-reset-instead-of-compact.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)

Sources:
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 12:01-13:10
