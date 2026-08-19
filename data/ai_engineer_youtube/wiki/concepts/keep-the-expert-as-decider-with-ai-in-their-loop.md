# Keep the Expert as Decider With AI in Their Loop

Summary: Invert the usual human-in-the-loop framing for high-stakes vertical work: instead of an agent that acts while a human reviews, build an assistant that generates candidates while the expert still makes the call. The value delivered is the expert's time, not their authority.

Use when:
- Designing the deployed shape of a vertical AI product whose decisions are expensive and slow to reverse (trades, drug candidates, deal terms, clinical selection).
- Deciding whether the product's promise is automation or throughput.
- Pushing back on a roadmap that assumes an approval checkbox turns an autonomous agent into a safe one.

Details:
- The reframing is explicit: "HITL is kind of a thing everyone is like, yeah, let's add human in the loop. I would say not yet. Finance and pharma are still those two industries where it's AITL, AI in the loop cuz everything is done by the expert, but the AI assistant really helps save time." ([Trading Desks to Clinical Trials](../sources/20260819_Yphdry8ttAQ.md), 17:45-18:03)
- The concrete shape is candidate generation. Forming trade theses takes a trader a fixed amount of time, "and AI can just give him five candidate trade theses, but which one would actually work in the market and which won't is the discussion [that] still lies with the trader." Picking drug candidates works the same way. The measured win is that "you just reduce the time of expert by a lot." (18:03-18:29)
- The prediction attached to it is that this is not a transitional stage — "it will stay this way for really long." (18:29-18:31)
- The stated blocker is a capability claim, not a policy one: "for the models to actually make good decisions, they don't need to do correlation, they need to do causation," and, citing Yann LeCun, "these are text statistics, not real-world models. You cannot just pattern match with past and use future to predict." He names the crossing point "the AGI line" — past it, "you will have vibe coded drugs." (18:32-19:02)
- This composes with the judgment gap rather than restating it: an expert who cannot be replaced as the decider is the same expert the team had to hire in order to evaluate anything at all, so AITL is the deployed form of the internal learning loop.
- The contrast worth holding is with the automation-bias failure mode. That literature warns that a human placed *after* a confident model becomes a rubber stamp; this position avoids the problem by keeping the human's decision upstream and unautomated, with the model supplying options rather than a recommendation to accept or reject.

Related topics:
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Hire the User to Own the Judgment Loop](hire-the-user-to-own-the-judgment-loop.md)
- [You Cannot Iterate on Output You Cannot Judge](you-cannot-iterate-on-output-you-cannot-judge.md)
- [Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md)
- [Start with augmentation when autonomous reliability is not ready](start-with-augmentation-when-autonomous-reliability-is-not-ready.md)

Sources:
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](../sources/20260819_Yphdry8ttAQ.md), 17:45-19:02
