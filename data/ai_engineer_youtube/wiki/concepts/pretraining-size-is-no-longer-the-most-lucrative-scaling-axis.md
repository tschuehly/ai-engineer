# Pre-Training Size Is No Longer the Most Lucrative Scaling Axis

Summary: The argument that the current architecture is saturated on size: recent size increases have not delivered the stepwise jumps their predecessors did, small models keep beating large ones, and the practical consequence is that no lab is expected to supersize again on this architecture. Where the returns moved is a broader action space and post-training pushed further back — not a bigger model.

Use when:
- Planning a model roadmap and deciding whether to wait for a bigger base model or invest in recipe, post-training, and harness work.
- Interpreting a capability plateau as an architecture ceiling versus a data or method problem.
- Arguing a budget between pre-training compute and post-training/agentic compute.
- Reading "scaling is dead" claims and wanting the specific version of the claim that is being made.

Details:
- The claim, scoped precisely to size: "empirically, we do now know that… pre-training size in particular is not your most lucrative axis of scale." It is a claim about one axis, not about scaling generally. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 10:52-10:59)
- The stated cause: "we know it's not giving the same returns largely because our architecture is saturated," sharpened in Q&A into "the architecture determines your ceiling, and I'm saying we are probably at the ceiling of size, which means that… it's what you innovate within that." A new architecture would reset the ceiling; nothing in the talk claims one is coming. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 11:31-11:36, 18:52-19:03)
- Two pieces of evidence are offered, and they are different in kind. Observational: "most recent models that have severely… played with just increasing model size haven't provided the same stepwise change… as their predecessors" (11:54-12:08). Quantitative-ish: the Open LLM leaderboard's "daily submission of… the best small model under 13B versus all the larger models," where "over time that ratio totally flips" (11:36-11:53). The second is a self-selected sample of what people chose to submit rather than a controlled size comparison — see [Do Not Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md).
- The predictive form, which is the actionable one: "no frontier AI lab is going to [supersize] their model again for pre-training." If that holds, the capability you can buy from a future base model is bounded by an architecture that already exists, and waiting is not a strategy.
- **Where the lever moved.** Two answers are given. Within pre-training: "data quality in general means you use capacity a lot more. So… what you will see in pre-training is instead of the size people are just moving post-training further back, which is very fascinating and a bigger lever" (19:24-19:39). Outside it: "where the most returns for performance are now are on a broader action space" — "we move from an algorithm to we are expanding optimization space in new places" (12:08-12:24).
- The explicit non-claim, which the page should carry with the claim: "size does matter… I'm not advocating everyone use a 0.8B, but I am saying that we now have a more equal… playing field at the top" (19:08-19:20). And on distillation, asked whether small models still depend on large teachers: "I agree distillation is helpful. It's just that again we've hit the ceiling and so it's almost like no one is going to supersize their model or if they do it's not clear it's beneficial except for small size of the distribution, which is very much the long tail" — so extra pre-training compute is argued to still pay, but only for tail coverage (19:40-20:03).
- Read alongside the same-event argument that [only the compute axis is available on your own corpus](only-the-compute-axis-is-available-on-your-own-corpus.md): that talk removes data and size as levers for *your* private domain; this one argues size is running out as a lever for *everyone*, which is what makes recipe, algorithm, and post-training the contested ground. It also supplies a mechanism for the conjecture that [expertise, not intelligence, is what to scale next](scale-expertise-once-intelligence-is-abundant.md) — if the size ceiling is real, "maybe they're already good enough" stops being only a preference about where to spend.
- Provenance: asserted by a founder whose company sells per-domain training, citing her own paper ("Slow Death of Scaling") without detail and one leaderboard exhibit. The architecture-ceiling claim is a prediction about lab behavior, not a measurement. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 10:47-11:08)

Related topics:
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Distributable Compute Lowers the Barrier to Frontier Work](distributable-compute-lowers-the-barrier-to-frontier-work.md)
- [Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)
- [Scale Expertise Once Intelligence Is Abundant](scale-expertise-once-intelligence-is-abundant.md)
- [Distill reasoning traces into small models](distill-reasoning-traces-into-small-models.md)
- [Do Not Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md)
- [Post-Train Small Models for Narrow Capabilities](post-train-small-models-for-narrow-capabilities.md)
- [A Bigger Model Is Not Automatically a Safer or Better Agent](a-bigger-model-is-not-automatically-a-safer-or-better-agent.md)

Sources:
- [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../sources/20260812_XEd_SRVHBgU.md), 10:47-12:24, 18:25-20:03
