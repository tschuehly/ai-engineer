# Do not treat long context as durable model memory

Summary: Long context windows can increase what a model can see, but they are not the same as reliable model memory. Larger prompts add latency, cost, and reasoning degradation, so teams should distinguish temporary activations from knowledge the model can retrieve or use efficiently across tasks.

Use when:
- Deciding whether to paste a whole corpus into a prompt, build retrieval, or adapt a model.
- Evaluating claims that million-token context windows make memory, RAG, or knowledge adaptation unnecessary.

Details:
- The source distinguishes full context, RAG, and weight updates as separate ways to inject knowledge into a model. Full context is the easiest path for bounded data, but it keeps knowledge in transient activations rather than durable model behavior. (02:35-03:16, 03:30-04:07)
- Full context has a serving cost: the talk cites a drop from roughly 10,000 output tokens per second with 1,000 context tokens to roughly 130 tokens per second with 128k context tokens. (04:11-05:08)
- Self-attention creates a quadratic pressure because tokens need to attend to one another; this becomes a memory and latency bottleneck as the prompt grows. (05:16-05:54)
- A long window can avoid hard failure while still failing to reason well. The speaker separates "not breaking" at many tokens from actually reasoning across large chunks, and cites context-rot behavior where performance worsens as extra context grows. (06:18-07:51)
- A measured qualification, not a refutation: Towards AI probed *single-fact* recall across a growing session transcript and found distinctive facts recovered consistently out to 800k tokens with no visible rot, while ambiguous facts (no distinguishing surface form) degraded to about half that. Within one session, on this model class, keeping the full history recalled specific details 95% of the time against 32% after summarizing — so for retrieval of distinctive details, the window outperformed the alternative rather than rotting. The claim this page makes still holds where it was made: across sessions the model is stateless, the serving cost of long prompts is real, and reasoning *across* a large span is a different task from pulling one fact out of it. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 50:53-51:56, 53:16-54:33)

- What the flagship consumer products actually do with this constraint is instructive: neither ChatGPT nor Claude carries raw history into a new conversation. Each prepends a small synthesized profile — ~4,000 and ~1,000 tokens respectively — because that artifact enters the context window of *every* conversation, making its length a permanent per-turn serving cost rather than a one-off. Asked what an unconstrained design would look like, Shlok Khemani answers 400,000 tokens updated after every conversation, and immediately notes "we live in a GPU constrained world." ([Lessons from Studying Every Memory System](../sources/20260812_5ZGyKWjQDr0.md), 12:08-13:37)

- **The boundary measured from both sides in one experiment.** A memory-harness ablation ran the same harness on two tasks and got opposite verdicts. On a literature review whose whole corpus fit in the window — including a deliberately hard needle, a retracted Nature claim about 742,000 materials where "the retraction… is a much smaller haystack needle in that corpus than the headlines and the citations" — memory produced "the same performance with memory and without memory, and it only added more cost." On an xbench question whose answer sat at step 124 while the question arrived at step 500, "completely outside of the context window," the harness became the only route to the answer. That is the operational form of this page's claim: inside the window, external memory is overhead; outside it, the window is not memory at all and the harness is the whole mechanism. ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 05:29-07:33)

- **What the same speaker moved on to, which sharpens what this page is actually recommending.** Eight months after the talk this page was built from, Morris's framing is no longer "context versus RAG versus weights" but "which scaling axis is even available." Against a private corpus you cannot make more data and will not train from scratch, so compute is the only lever left ([Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)). That reframes the choice this page opens: pasting the corpus into the window is not a weaker version of adapting the model, it is a decision to spend nothing on the one axis you have. The counterweight is that spending on it does not scale indefinitely either ([The Synthetic Data Wall](the-synthetic-data-wall-caps-every-define-then-train-loop.md)), and that the in-window techniques closest to "memory" — compressing the corpus into cache state — still "only appl[y] to things that are in context" ([KV Compaction Reaches Only What Already Fits in Context](kv-compaction-reaches-only-what-already-fits-in-context.md)). ([Engram](../sources/20260812_WiqDvX6isc4.md), 07:26-08:11, 13:00-13:10, 16:23-16:57)

- **The strongest qualification yet, and it is about the alternatives rather than about long context.** On a benchmark built to require learning across instances, "vanilla in context learning where you just put the experience in the context and you don't do any of the fancy context management" topped the leaderboard on reward *and* on gain — that is, growing context learned more from experience than the memory and context-management systems it was compared against, at lower cost. This does not make the window durable memory; the same talk's whole argument is that state has to be carried deliberately, and simply growing the context is counted as one legitimate way to carry it. What it does is set the bar: an architecture that externalizes memory has to beat "keep appending" on a gain-versus-cost plot, and on medium-horizon tasks it did not. See [Plain In-Context Learning Topped a Continual-Learning Benchmark](plain-in-context-learning-topped-a-continual-learning-benchmark.md). ([Evaluating Continual Learning](../sources/20260812_iqloyWCGYQQ.md), 09:36-09:46, 13:52-14:52)

- **The organizational-corpus version of the same point, with the size claim made explicit.** Asked why not load the codebase and every architecture document at once, Werry gives a capacity answer and a behavioural one: "you've got way more organizational context than can fit into a context window, even one that's a million tokens in size," and even where it fits, "it causes the agent to get distracted." The durable framing is that a window is a working set chosen per task, not a place to keep what the organization knows. ([Werry](../sources/20260827_qdAkxLoYNI8.md), 05:34-06:20)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [RAG stacks need modular baselines instead of one fixed recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)
- [Train long-tail knowledge into weights with curated synthetic data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)
- [Full History Recalls Details That Summaries Delete](full-history-recalls-details-that-summaries-delete.md)
- [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md)
- [Profile Synthesis Is Continual Learning Outside the Weights](profile-synthesis-is-continual-learning-outside-the-weights.md)
- [A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md)
- [Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)
- [KV Compaction Reaches Only What Already Fits in Context](kv-compaction-reaches-only-what-already-fits-in-context.md)
- [Plain In-Context Learning Topped a Continual-Learning Benchmark](plain-in-context-learning-topped-a-continual-learning-benchmark.md)

Sources:
- [Jack Morris: Stuffing Context is not Memory, Updating Weights is](../sources/20251229_Jty4s9-Jb78.md), 02:35-07:51
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 50:53-51:56, 53:16-54:33
- [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../sources/20260812_5ZGyKWjQDr0.md), 12:08-13:37
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 05:29-07:33
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 07:26-08:11, 13:00-13:10, 16:23-16:57
- [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../sources/20260812_iqloyWCGYQQ.md), 09:36-09:46, 13:52-14:52
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 05:34-06:20
