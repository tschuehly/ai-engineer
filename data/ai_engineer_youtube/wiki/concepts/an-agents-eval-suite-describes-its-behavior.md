# An Agent's Eval Suite Describes Its Behavior

Summary: Show someone the evals an agent was measured against and you have largely described how it behaves, because the agent was iteratively altered until those evals passed — which makes the eval suite a disclosure artifact and makes every gap in it a blind spot the agent was never pushed to cover.

Use when:
- Assessing someone else's agent and you can see their evals but not their prompts.
- Deciding what to put in an eval suite, knowing the suite is also the behavioral target.
- Explaining why an agent is excellent on the measured axis and unremarkable everywhere else.

Details:
- The claim, offered as a hot take: "you can basically define agent behavior by showing the evals that you ran on it. Like, if someone showed me all the things that they're trying to test their agent on, I think I would have a rough idea about how that agent is going to behave." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 11:43-12:00)
- The mechanism is hill climbing, stated without euphemism: "it literally like hill climbs those evals, and you alter the behavior of the agent to make the evals pass. Like, the purpose of evals is roughly to try to make them pass. So, I update my agent so that they essentially pass." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 12:00-12:15)
- The context in which it appears matters: generating evals and environments is listed as one of the three products of mining a trace corpus, alongside distillation datasets and human-readable reports. Evals in this frame are *derived from observed behavior* and then become the target for future behavior, closing a loop between what the agent did and what it will be pushed to do. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 11:08-12:46)
- **The corollary is the uncomfortable half.** If the suite is the behavioral description, everything absent from it is undescribed and unoptimized. The wiki records the same boundary from the failure side: [Evals only cover known AI product failures](evals-only-cover-known-ai-product-failures.md). Reading the two together gives a sharper diagnostic than either alone — an agent's competence profile is the shape of its eval suite, including the holes.
- This is the descriptive inverse of the wiki's existing prescriptive framing. [Use evals as durable AI system specifications](use-evals-as-durable-ai-system-specifications.md) argues you should write evals to state what the system must do so that models, prompts, and optimizers can churn beneath them; this observes that whether or not you intended it, the suite is already functioning as that specification, because it is what the improvement loop optimizes against.
- Practical uses of the claim: when evaluating a vendor or an open agent, ask for the eval suite before asking for the architecture; when writing your own, treat adding an eval as adding a behavioral requirement rather than adding a measurement.
- The reward-hacking hazard sits directly on this claim. In the same talk: "if you have some sort of score that you can make number go up, agents are pretty good at making that number go up. They might cheat a little bit and you need to like check them on some stuff." An eval suite describes behavior only to the extent that passing it requires the behavior you meant ([Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)). ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 14:33-14:51)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Use Evals As Durable AI System Specifications](use-evals-as-durable-ai-system-specifications.md)
- [Evals only cover known AI product failures](evals-only-cover-known-ai-product-failures.md)
- [Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)
- [Treat evals as the home of domain knowledge](treat-evals-as-the-home-of-domain-knowledge.md)
- [Densify Agent Feedback Because Pass/Fail Is Not Actionable](densify-agent-feedback-because-pass-fail-is-not-actionable.md)

Sources:
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 11:08-12:46, 14:33-14:51
