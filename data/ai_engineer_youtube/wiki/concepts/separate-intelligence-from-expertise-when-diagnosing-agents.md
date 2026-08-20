# Separate Intelligence From Expertise When Diagnosing an Agent

Summary: Intelligence — reasoning through an unfamiliar problem from the context you were handed — and expertise — accumulated, situated competence in one environment — are roughly orthogonal, so an agent can be failing on either axis and the fixes are different. Scaling only the first produces "the world's smartest novice": brilliant at whatever is put in front of it, accumulating nothing between episodes.

Use when:
- An agent is failing and the reflex is to upgrade the model.
- Deciding whether to spend on a stronger model or on a mechanism that lets the deployment accumulate competence.
- Explaining why a system that benchmarks well still makes "brittle and silly errors" in one customer's environment.

Details:
- The working definitions, given as a deliberate conceptual split. Intelligence is "the capacity to reason through unfamiliar problems from available context. This is what the frontier models are increasingly good at. You give it the problem statement, the context, the tools, and it can reason through this even if it's a [thing] done for the first time" — and crucially, "every episode is more or less independent from each other here." Expertise is "accumulated and situated competence… the ability to act reliably, efficiently, and with judgment to achieve [reproducibly superior] performance in a particular domain." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 06:33-07:19; the phrase inside brackets is garbled in the captions and reconstructed.)
- The orthogonality claim, from the slide the speaker calls "maybe the most important figure in this talk": plot raw intelligence on x and expertise on y and "I think we'll find that they are largely orthogonal to each other." Position on one axis predicts little about the other. ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 12:41-13:01)
- The failure mode of scaling one axis alone: "if you don't have continual learning, all you do is scaling your model to get better raw intelligence, then what we will get is what I call the world's smartest novice. Like super smart, it can try to attack at any problem given to it, but it doesn't accumulate expertise, so it ends up as just like brute forcing its way at every problem." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 13:01-13:26)
- What expertise contains, itemized — this is the checklist for what a deployment is missing when the model is already smart enough. **Pattern recognition**: an expert reading "a gigantic bug report… can immediately locate the most plausible places where things could go wrong." **Deep structure**: scheduling a meeting "is actually a constraint optimization problem over everyone's authority, the priorities, the urgency." **Conditionality**: "every rule has like the preconditions where it applies, but then we also know when we can bend the rules when exceptions happen." **Judgment and taste**: what counts as high quality and "very importantly, when to stop, when it's good enough." Together these amount to "a world model of their environments." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 07:25-09:20)
- The diagnostic use: if the agent reasons correctly once it has the right facts but keeps rediscovering the environment, the deficit is expertise, and a stronger model will re-solve the same problem from scratch at higher cost. If it holds the right context and still reasons wrongly, that is the intelligence axis.
- Scope and provenance: this is a position talk with no measurement behind it. The orthogonality figure is drawn conceptually, not plotted from data, and the speaker is COO of a company whose stated focus is agents and continual learning. The distinction is useful as a diagnostic frame; the "largely orthogonal" claim is an assertion, not a result.

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Expertise Compresses the Search; Intelligence Expands It](expertise-compresses-the-search-intelligence-expands-it.md)
- [Define Continual Learning as Adaptive Compression of Experience](define-continual-learning-as-adaptive-compression-of-experience.md)
- [Scale Expertise Once Intelligence Is Abundant](scale-expertise-once-intelligence-is-abundant.md)
- [Digital Work Is Millions of Microworlds With Local Physics](digital-work-is-millions-of-microworlds-with-local-physics.md)
- [Last-Mile Domain Context Beats Model Chasing](last-mile-domain-context-beats-model-chasing.md)
- [General Agents Need Skills for Domain Expertise](general-agents-need-skills-for-domain-expertise.md)
- [Route Agent Repairs to the Right Layer With the Smallest Durable Change](route-agent-repairs-to-the-right-layer-smallest-durable-change.md)

Sources:
- [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 06:33-09:20, 12:41-13:26
