# Continued Pre-Training on a Private Corpus Owes a Post-Training Debt

Summary: Simulating pre-training — generating synthetic data conditioned on your corpus and continuing to train on it — is the approach with the best pedigree, because pre-training is where knowledge acquisition actually works. It carries three costs that are usually left off the plan: it overwrites some of the pre-training, it is hard to scale, and it leaves you owing a post-training pass that most teams cannot pay because they started from an instruct model, not a base model.

Use when:
- Scoping a continued-pre-training project on internal documents and estimating what "done" costs.
- Choosing a starting checkpoint, and deciding whether a post-trained model is acceptable.
- Explaining why a technique that works in a lab's pipeline is hard to reproduce outside one.

Details:
- Why the approach is attractive at all: "pre-training is amazing for knowledge acquisition. Like I can ask Claude what… result I got in a paper that I've written and it actually knows this, which is incredible… it more or less is knowledge that's acquired through pre-training." If you want a model to know things the way it knows public things, imitate the process that produced that knowledge. ([Engram](../sources/20260812_WiqDvX6isc4.md), 14:35-14:56)
- The recipe: "craft synthetic data conditioned on D and then train… for longer on the synthetic data as if you're continuing pre-training." Three papers are shown as instances; none is named in audio. ([Engram](../sources/20260812_WiqDvX6isc4.md), 14:56-15:13)
- **Cost one — you overwrite what you started with.** "You sort of overwrite some of the pre-training." The capability you are borrowing is the thing the run erodes; this is the same reliability/plasticity trade the wiki records elsewhere ([Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md)), arriving at the weights level. ([Engram](../sources/20260812_WiqDvX6isc4.md), 15:13-15:17)
- **Cost two — "I think it's difficult to scale."** Stated without elaboration, so treat it as a flag to price rather than a finding. ([Engram](../sources/20260812_WiqDvX6isc4.md), 15:17-15:20)
- **Cost three — the post-training debt, and the prerequisite it exposes.** "Maybe like one blocker is you then have to post-train the model after doing this. So, a lot of people don't actually start with good pre-trained base models. They have post-trained models, which makes this hard." Continuing pre-training on an already-instruction-tuned model damages the tuning, and restoring it means owning a post-training pipeline — the capability most teams outsourced by starting from an instruct checkpoint in the first place. ([Engram](../sources/20260812_WiqDvX6isc4.md), 15:20-15:32)
- The practical consequence of cost three is a checkpoint-selection rule that has to be made *before* the project starts: if you cannot post-train, an open base model plus a post-training pass is a different project from fine-tuning an instruct model, and this technique quietly requires the former. It also explains why this approach reads as more available to labs than to application teams.
- The RL variant is the same shape with a different loss and inherits the same accounting: "you can craft unsupervised reinforcement learning environments and do RL. It's pretty similar to the previous suggestion, except instead of doing some type of distillation, you're just using like RL loss like GRPO or whatever." The wiki's [environments as software artifacts](build-rl-environments-as-software-artifacts.md) and [environments as eval data and training substrates](treat-environments-as-eval-data-and-training-substrates.md) pages describe what building that half actually involves. ([Engram](../sources/20260812_WiqDvX6isc4.md), 15:41-15:58)
- The ceiling is shared with every other option in the same talk: however good the synthetic data, the loop still terminates ([The Synthetic Data Wall](the-synthetic-data-wall-caps-every-define-then-train-loop.md)).
- Provenance and limits: a 90-second characterization in a framing talk, with no measurements, no named papers in audio, and a stated overall verdict of "pretty promising." The three costs are the durable part; the promise is the speaker's judgment. ([Engram](../sources/20260812_WiqDvX6isc4.md), 14:19-15:38)

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [The Synthetic Data Wall Caps Every Define-Then-Train Loop](the-synthetic-data-wall-caps-every-define-then-train-loop.md)
- [Distill Behaving as if the Corpus Were in Context, Not the Documents](distill-behaving-as-if-the-corpus-were-in-context.md)
- [Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)
- [Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Decide When to Fine-Tune From Three Business Signals](decide-when-to-fine-tune-from-three-signals.md)
- [Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)

Sources:
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 14:19-15:58
