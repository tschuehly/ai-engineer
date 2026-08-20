# Define Continual Learning as Adaptive Compression of Experience

Summary: "Continual learning" names a cross-product, not a technique: adaptive compression of *experience* into *reusable structures* for *future behavior*. Pinning down which experience, which compression, which structure, and which use turns a confusing label into four concrete design decisions — and explains why two teams saying "continual learning" often mean unrelated systems.

Use when:
- Two proposals both called continual learning need to be compared.
- Specifying a memory, profile, skills, or fine-tuning loop and the requirements are still vague.
- Auditing an existing learning loop for the axis nobody chose deliberately.

Details:
- The definition, offered because the term "is such a confusing term" and an earlier speaker at the same event had already given "like 10 different names" for it: continual learning is "adaptive compression of experience into reusable structures for future behavior." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 10:27-11:08)
- **Experience — what goes in.** "Is it more like episodes of experience, or is like these semantic facts or procedures or feedback from human or in environments?" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 11:06-11:20)
- **Compression — how it is reduced.** "We embed them into vectors, or we index them into some symbolic structure, we distill them into model parameters, or do some kind of a reinforcement learning." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 11:20-11:34)
- **Adaptive — the qualifier that rules out a one-shot pipeline.** "It's not just like one-time compression. It needs to be adaptive compression. Like what you have learned, what you have compressed so far should largely influence how you compress further." A pass that treats every item identically regardless of what is already stored does not satisfy the definition. ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 11:34-11:48)
- **Structure — what it is stored as.** "Is just like parameters like adapters of your language models, or is vectors, graphs, or skills, or even [world] models?" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 11:48-11:59)
- **Use — what the structure is for.** "Is like you use it just to recall these facts, or you use it for prediction of like future states? You use it for better planning, or even for the control like actuation layer of the agent, or as a value function for potential states." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 11:59-12:18)
- Why the taxonomy earns its place: "if different aspects can be instantiated in different ways, that makes this field so confusing" — the confusion is combinatorial, not conceptual, and naming the four axes is what makes two systems comparable. ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 12:18-12:41)
- Applied to systems already in this wiki, the axes separate designs that share a label. ChatGPT's and Claude's running profiles compress *conversations* into a *text artifact* used for *recall and framing* ([Profile Synthesis Is Continual Learning Outside the Weights](profile-synthesis-is-continual-learning-outside-the-weights.md)). RELAI's loop compresses *production failures* into *replayable environments and regression tests* used for *verified repair* ([Verifiable Continual Learning](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)). Skills compress *procedural feedback* into *files the agent reads* used for *planning and execution* ([Skills Turn Procedural Feedback Into Transferable Agent Memory](skills-turn-procedural-feedback-into-transferable-agent-memory.md)). Distillation compresses *traces* into *weights*. All four are continual learning under this definition and share almost no machinery.
- **The naming problem this definition answers, itemized by another speaker at the same event.** Jack Morris lists what the field calls the same thing: "sleep time compute, continual learning, neural memory, write time compute, note taking, dreaming, studying, machine studying. In classical AI, maybe it's called amortized inference" — plus his own term, scaling compute on context. His diagnosis is not that the terms mean different things but that "the paradigm is like very early and hasn't been solidified the way, for example, pre-training or post-training have." That is the complementary half of the account above: Su explains the confusion as *combinatorial* (four axes instantiated differently), Morris as *chronological* (no vocabulary has won yet). Both point at the same remedy — describe the four axes rather than reaching for a label. ([Engram](../sources/20260812_WiqDvX6isc4.md), 04:33-05:05)
- Morris's own instantiation is worth reading through the axes as a check on their coverage: the *experience* is a fixed unstructured corpus (emails, meeting transcripts), the *compression* is gradient-based training, the *structure* is model parameters, and the *use* is answering and generating in the domain. His central complaint — that this loop saturates because the dataset is defined once — is precisely a failure of Su's "adaptive" qualifier, and the escape he points at is a curriculum that gets harder as the model improves ([Seek the AlphaGo Property](seek-the-alphago-property-so-added-compute-keeps-buying-depth.md)). ([Engram](../sources/20260812_WiqDvX6isc4.md), 16:23-16:57, 17:35-18:05)
- Provenance: a definitional contribution from a conceptual talk, by the COO of a company focused on continual learning. It is not validated against anything; its value is as a specification checklist, and the fourth axis (use) is the one most often left implicit in the systems above.

- **One cell of this taxonomy needs two more axes, which is a result about the taxonomy's resolution rather than a correction to it.** Applied Compute's whole talk lives in a single cell — experience = agent traces, compression = distillation into parameters — and inside it distinguishes two independent dimensions that appear nowhere in Su's four: how on-policy the traces are, and whether the supervising hint is a static prior or constructed against the rollout just produced ([Place a Continual-Learning Setup on Two Axes](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)). Two systems can match on all four of Su's axes and still differ on both of Denton's, with different infrastructure prerequisites and, by Applied Compute's account, different ceilings. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 01:24-05:33)
- The addition also puts a name to something the "experience" axis leaves implicit: experience alone is not supervision. A trace records what the policy did, so distilling from it requires a second input carrying what it should have done ([Distill Without a Golden Answer](distill-without-a-golden-answer-using-privileged-information.md)). Auditing a learning loop for "which axis did nobody choose deliberately" should include this one — where the corrective signal comes from — alongside Su's four. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 03:43-04:07, 09:49-10:36)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Models](../topics/models.md)

Related concepts:
- [Place a Continual-Learning Setup on Two Axes: Trace Policyness and Hint Provenance](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)
- [Distill Without a Golden Answer by Giving the Teacher Privileged Information](distill-without-a-golden-answer-using-privileged-information.md)
- [Separate Intelligence From Expertise When Diagnosing an Agent](separate-intelligence-from-expertise-when-diagnosing-agents.md)
- [Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md)
- [Profile Synthesis Is Continual Learning Outside the Weights](profile-synthesis-is-continual-learning-outside-the-weights.md)
- [Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Skills Turn Procedural Feedback Into Transferable Agent Memory](skills-turn-procedural-feedback-into-transferable-agent-memory.md)
- [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md)
- [Seek the AlphaGo Property So Added Compute Keeps Buying Depth](seek-the-alphago-property-so-added-compute-keeps-buying-depth.md)
- [The Synthetic Data Wall Caps Every Define-Then-Train Loop](the-synthetic-data-wall-caps-every-define-then-train-loop.md)

Sources:
- [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 10:27-12:41
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 04:33-05:05, 16:23-16:57, 17:35-18:05
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 01:24-05:33, 09:49-10:36
