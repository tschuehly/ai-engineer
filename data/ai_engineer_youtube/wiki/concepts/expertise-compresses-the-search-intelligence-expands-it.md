# Expertise Compresses the Search; Intelligence Expands It

Summary: Treating problem solving as search makes the intelligence/expertise split operational. Intelligence brute-forces — spin up a hundred parallel attempts against the context you were handed. Expertise compresses the search space because the shortcuts are already learned, and it decides which context to bring in the first place. This is a direct account of why capable agents are token-inefficient.

Use when:
- Agent cost is dominated by parallel attempts, retries, and exploration rather than by the final answer.
- Choosing between "run more samples" and "learn from the last run" as the way to improve a deployment.
- Designing what a memory or learning layer should actually store: shortcuts and context-selection policy, not just facts.

Details:
- The framing: "every problem solving is a search problem. So intelligence tends to brute force it — try to spin up like 100 different parallel ways to try to solve the problem. Well, expertise will actually try to compress the search space because expertise has learned the essential shortcuts for the problem space. So that whenever you have a problem, you know the most plausible ways to solve it." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 09:49-10:27)
- The context half of the same slide, which is the part most relevant to context engineering: "intelligence is about, hey, when we have the context, how to solve the problem through the context. But expertise actually will bring you the right context. Given any problem, we know what context [to] bring in are important for this problem and bring it in to solve the problem." Retrieval quality is framed here as an expertise property, not a retriever property. ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 09:20-09:49)
- The talk opens on token inefficiency as one of its two motivating puzzles — agents "so token inefficient… to the degree that every company right now is like coming out and try to curb their [token spend]" — and this slide is the proposed explanation: a system with no accumulated expertise has nothing to prune the search with, so every episode pays full exploration cost. ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 00:57-01:19, 13:01-13:26)
- What this implies about what to store. A memory layer that only recalls facts leaves the search uncompressed; the compression comes from procedures, shortcuts, and priors over where the answer usually is — which is why the same talk lists "skills" and "world models" alongside vectors and adapters as candidate reusable structures ([Define Continual Learning as Adaptive Compression of Experience](define-continual-learning-as-adaptive-compression-of-experience.md)).
- Where it meets an existing wiki tension: parallel sampling and wide exploration are real levers with measured wins in several sources, and nothing here says to stop using them. The claim is narrower — that their cost is the price of missing expertise, so a deployment that repeats the same class of task should expect the search width to fall over time rather than stay flat.
- Provenance and limits: no measurement. Neither the "100 parallel ways" figure nor the compression effect is quantified anywhere in the talk, and no experiment separates a shorter search from a worse one. Treat it as a design frame, not an efficiency result.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Separate Intelligence From Expertise When Diagnosing an Agent](separate-intelligence-from-expertise-when-diagnosing-agents.md)
- [Define Continual Learning as Adaptive Compression of Experience](define-continual-learning-as-adaptive-compression-of-experience.md)
- [Digital Work Is Millions of Microworlds With Local Physics](digital-work-is-millions-of-microworlds-with-local-physics.md)
- [Memory Quality Is Capped by the Context It Can Reach](memory-quality-is-capped-by-the-context-it-can-reach.md)
- [Skills Turn Procedural Feedback Into Transferable Agent Memory](skills-turn-procedural-feedback-into-transferable-agent-memory.md)
- [Rank Agent Memory by Outcome Utility, Not Just Similarity](rank-agent-memory-by-outcome-utility-not-just-similarity.md)

Sources:
- [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 00:57-01:19, 09:20-10:27, 13:01-13:26
