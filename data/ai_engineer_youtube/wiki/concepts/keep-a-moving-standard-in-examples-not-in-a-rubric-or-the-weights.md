# Keep a Moving Standard in Examples, Not in a Rubric or the Weights

Summary: Judgment you cannot fully articulate has exactly three places to live — a specification you write up front, model weights you train, or a corpus of examples you retrieve from. When the standard is tacit, contextual, and still moving, the first two lose it and the third keeps it: adding one judged case makes it live on the next call, and you can point at which case moved the score.

Use when:
- Choosing between a longer rubric, a fine-tune, and a retrieval corpus for encoding domain quality.
- Your rubric keeps growing, keeps getting edited after every review meeting, and still misses cases.
- The standard of good in your domain changes with guidelines, model behavior, or which expert you ask.
- A score has to be explainable to a regulator, a customer, or the expert who disagrees with it.

Details:
- **The precedent for learning a standard rather than writing it.** "RLHF exists because you can't write the reward function for good. You learn it from examples by showing it. The only question is where you keep what you've learned. And there's three places." ([Fox](../sources/20260822_yqF6XhzbWBk.md), 12:36-12:56)
- **Option one — specify it up front:** "stuff the prompt, write the perfect rubric. We just watched that fail." The bound is structural rather than about effort: "a rubric that you pre-specify is only the taste you could write down. The taste that matters is the part that you couldn't." (11:36-11:56, 12:36-12:56)
- **Option two — bake it into the weights** by fine-tuning or continual learning. Rejected on three specific grounds rather than on cost: "for a standard that's still moving and a score that has to be explainable, the weights, I think, are the wrong place to keep that. They go stale, they can't tell you why, and you can't change them without a retrain." Staleness, unexplainability, and update latency are the axes; a stable, unexplained standard would not fail this test. (12:56-13:19)
- **Option three — keep the standard as the examples themselves:** "past judgments, expert corrections, references, and for each output you retrieve the ones that bear on it into the judge's context. Add one and it's live on the next call. You can point at exactly what moved the score. For this problem, it's both better and also cheaper to do." (13:19-13:36)
- **The three properties that select option three.** The standard is tacit ("your domain experts have it, but they can't fully write it down"), contextual ("the same detail is critical in one note, noise in the next"), and moving ("the model changes, guidelines change, two good doctors disagree, different hospitals have different definitions"). Each maps to one failure of the other options: tacit defeats specification, contextual defeats a single global rubric, moving defeats weights. (07:15-07:34)
- **The residual that still belongs in the rubric.** Fox does not discard written criteria; he demotes them. "The generic part of this you can write down once easily. For example, be faithful, or don't drop anything important. But what you can't write down is what counts as a serious miss for this specific note." A working system keeps a short universal rubric and puts the case-specific standard in retrieval. (14:59-15:18)
- **What this costs, which the talk does not price.** Nothing in the source specifies the index, the embedding, retrieval depth, per-judgment token cost, or latency; nor what happens when the retrieved precedent is itself a bad judgment, since expert corrections enter the corpus with no described review step. A retrieved-precedent standard has the failure mode that a rubric does not — one wrong case can propagate to every case that resembles it — and this source does not address it.
- **Position against the wiki's other reference-construction procedure.** [Build Judge References From Independently Written, Adjudicated Expert Rubrics](build-judge-references-from-adjudicated-expert-rubrics.md) spends four physicians per case producing a rubric of required elements — a specification, built carefully and pinned to one case. That is option one applied per case rather than globally, and it survives Fox's critique of global rubrics while inheriting the cost he is trying to avoid: four experts per reference item, fixed at authoring time. The reconciling variable is how fast the standard moves. Abridge's element lists for a clinical question are stable enough to adjudicate once; Fox's claim is that materiality judgments are not, so his corpus is designed for cheap continuous appending rather than for careful one-time construction.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Assemble the Judging Standard Per Output From Retrieved Precedent](assemble-the-judging-standard-per-output-from-retrieved-precedent.md)
- [Build Judge References From Independently Written, Adjudicated Expert Rubrics](build-judge-references-from-adjudicated-expert-rubrics.md)
- [A Judge Without Taste Is a Second Silent Failure](a-judge-without-taste-is-a-second-silent-failure.md)
- [Capture Expert Reasoning and Corrections, Not Just a Score](capture-expert-reasoning-and-corrections-not-just-a-score.md)
- [Share Taste Packages Across Teams and Domains](share-taste-packages-across-teams-and-domains.md)
- [Treat Evals as the Home of Domain Knowledge](treat-evals-as-the-home-of-domain-knowledge.md)

Sources:
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 07:15-07:34, 11:36-13:36, 14:59-15:18
