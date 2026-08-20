# Reliability and Plasticity Conflict in Continually Learning Agents

Summary: An agent that keeps learning is an agent that keeps changing, and the two properties users want — dependable behavior and rapid adaptation — pull against each other by construction: stable systems resist change, plastic systems invite it. No source in this wiki resolves the tension; the useful moves are to make the trade explicit and to bound where change is allowed.

Use when:
- Designing a loop that writes to memory, skills, prompts, or weights while the system is serving users.
- A stakeholder asks for an agent that both "learns from us" and "behaves consistently."
- Deciding how much of a system should be frozen between releases.

Details:
- The tension, stated as an open question rather than a solved trade: "we want these agents to be both reliable and plastic. But they are inherently conflicting with each other. Reliable systems or stable systems, they resist the change. But the plastic systems likes change. So how do we reconcile that?" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 15:46-16:12)
- The grounds offered for thinking it is solvable at all: "we do have a living existence proof, which is us ourselves, humans, that we are incredibly plastic, but also manage to be dependable most of the time." This is an existence argument, not a mechanism. ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 16:12-16:26)
- The companion open question on the same slide is measurement: "how do you even define and measure expertise? And this is probably environment-specific." Without a measure of the thing being accumulated, there is no way to tell an update that increased expertise from one that merely changed behavior. ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 15:35-15:46)
- The one concrete discipline this wiki holds against the problem is verification: RELAI's loop requires every improvement drawn from experience to be "proven to help and proven to break nothing that already worked," via a replayable failure test, a measured before/after delta, and a regression suite ([Verifiable Continual Learning](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)). That does not dissolve the conflict — it makes plasticity affordable by pricing each change against the stability it might cost, and it requires that the past be replayable.
- A second partial answer already in the wiki is scope rather than verification: constrain *where* the system is allowed to change. A closed tag vocabulary, a fixed schema, or a bounded skills directory keeps the plastic surface small enough that reliability lives in the parts that do not move.
- The related design axis the same talk raises: "when we talk about learning, largely they are like this two forms of learning, parametric or non-parametric… my belief here is that both are really needed for this type of continual learning to actually work. But how do we synergize the two?" Plasticity and reliability may sit on different substrates — fast, cheap, inspectable, reversible text updates against slow, expensive, opaque weight updates — but the talk leaves the combination unspecified. ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 16:32-16:49)
- Provenance: stated as an unsolved research question by the COO of a continual-learning company. No measurement, no proposed algorithm, and no evidence about how bad the trade actually is in deployed systems.

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)
- [Define Continual Learning as Adaptive Compression of Experience](define-continual-learning-as-adaptive-compression-of-experience.md)
- [Constrain Agent-Generated Tags to a Reference Vocabulary](constrain-agent-generated-tags-to-a-reference-vocabulary.md)
- [Ambient Agents Need Self-Maintenance and Memory Hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)
- [Profile Synthesis Is Continual Learning Outside the Weights](profile-synthesis-is-continual-learning-outside-the-weights.md)

Sources:
- [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 15:35-16:49
