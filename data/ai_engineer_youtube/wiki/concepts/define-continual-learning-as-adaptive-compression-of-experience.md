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
- Provenance: a definitional contribution from a conceptual talk, by the COO of a company focused on continual learning. It is not validated against anything; its value is as a specification checklist, and the fourth axis (use) is the one most often left implicit in the systems above.

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Models](../topics/models.md)

Related concepts:
- [Separate Intelligence From Expertise When Diagnosing an Agent](separate-intelligence-from-expertise-when-diagnosing-agents.md)
- [Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md)
- [Profile Synthesis Is Continual Learning Outside the Weights](profile-synthesis-is-continual-learning-outside-the-weights.md)
- [Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Skills Turn Procedural Feedback Into Transferable Agent Memory](skills-turn-procedural-feedback-into-transferable-agent-memory.md)
- [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md)

Sources:
- [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 10:27-12:41
