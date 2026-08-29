# Start with augmentation when autonomous reliability is not ready

Summary: Full automation is not always the fastest path to revenue or trust. In many domains, a strong copilot or augmentation surface is more usable because human tolerance for failures drops as latency, task stakes, and uncertainty increase.

Use when:
- Choosing between a copilot, human-in-the-loop workflow, or fully autonomous agent for a vertical AI product.
- Evaluating agent startup claims that skip directly to full automation before reliability is proven.

Details:
- Guo notes that agent startup interest is rising, but the revenue data she sees still makes copilots underrated rather than obsolete. 17:44-18:18
- Her Iron Man analogy frames the product as augmentation first: the system helps a human do more, can perform some basic tasks independently, and can expand autonomy as capability improves. 18:18-19:04
- The caveat is reliability: human tolerance for hallucination and failure falls dramatically as latency increases, so long-running autonomous work needs a higher trust bar than quick interactive assistance. 18:35-18:49
- **A second reason to start low that is about the customer rather than the model.** Shenoy's ladder — copilot, synchronous agent, asynchronous agent, long-running agent, AI coworker — is presented with the coworker rung as the one "everyone wants to sell you," and his rule is "you have to earn the right to do more." He gives two reasons, and only the first is the reliability argument this page makes: "for certain tasks, the models might not quite be there yet," and separately, you have to iterate with the organization in the field "so that they understand that this is the beginning of AI, and you can work up the rungs over time." The second is a claim about the customer's expectations rather than the system's failure rate, and it does not resolve as models improve. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 06:48-07:33)
- **A third reason to hold autonomy back, and it never resolves.** Garvin's caution is neither about model reliability nor about customer expectations: it is about what the system does. Billing is "business critical, has deep business logic behind it," so the recommendation is to let the coding agent "accelerate your work and get into a test mode and test environment" and stop — "we're not expecting to ship into production." Where the reliability argument predicts its own expiry, this one does not: a more capable model does not make a wrong invoice cheaper. Note also the direction of interest, since it is unusual — this is the vendor of the product arguing against unattended use of it. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 07:19-07:47)

Related topics:
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Choose autonomy level by task uncertainty and control needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md)
- [Make agent work more trustworthy by making it verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)
- [Measure AI intensity by human input to valuable output](measure-ai-intensity-by-human-input-to-valuable-output.md)
- [Async Agents Need a Forking Substrate and a User Who Tolerates Out-of-Order Completion](async-agents-need-a-forking-substrate-and-a-tolerant-user.md)
- [Let the Agent Reach a Test Environment, Not Production, When the Domain Carries Money](let-the-agent-reach-a-test-environment-not-production.md)

Sources:
- [State of Startups and AI 2025 - Sarah Guo, Conviction](../sources/20250802_3MZS5gNElZM.md), 17:44-19:04
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 06:48-07:33
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 07:19-07:47
