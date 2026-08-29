# Map Agent Adoption on Fear and Utilization Axes

Summary: Plot each engineer's adoption state on two independent axes — how threatened they feel by agents, and how much they actually use them — and treat the goal as the low-fear, high-utilization corner. The axes move independently, which is why usage mandates and shipped slop can each move one axis in a way that looks like progress and is not.

Use when:
- Deciding what intervention a specific engineer or team needs next, rather than pushing usage uniformly.
- Interpreting an adoption metric that went up without anything getting better.
- Explaining why the same rollout produces enthusiasm in one group and compliance in another.

Details:
- The two axes: "there is the fear axis where people lie on the spectrum… Is it coming for my job? Like am I going to be out of a job? Or is it like a really handy tool?… Versus like the confidence they have in how much they're executing it. So, they can either use it a lot or they can use it… not that much because they don't really know how to use it that well." ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 02:17-02:39)
- The observed trajectory is not a straight line to the goal corner, and each leg is worth recognizing separately:
  - **Start: high fear, low utilization.** "people said, 'Oh, you know, what is this? Is this the end? Like am I needed?' And fear was pretty high. Utilization was pretty low cuz people didn't really know how to use it." (02:39-02:50)
  - **Early adopters move utilization, via self-interest.** "when a few people got outsized leverage… people said, 'Okay, well, it looks like I'm still kind of needed if I figure out how to use this thing. So, let me actually try using it.'" The persuasive fact is that the leverage went to a *person*, not to the tool. (02:50-03:04)
  - **Mandates move utilization without moving confidence.** "we saw… mandates and token maxing, and people kind of got a little skeptical. Like confidence stayed the same, but people tried to use it a lot more." This is the leg where a usage metric rises and nothing underneath it does. (03:04-03:14)
  - **Shipped slop lowers fear for the wrong reason.** "there's a bunch of slop shipping, there's [sev twos], and… it's like I'm not really that scared cuz, you know, it just ships slop. Like I'm going to still be needed." Fear falls because expectations fell, which is a worse state than the fear it replaced, because it also suppresses the motive to learn. (03:14-03:25)
- The goal is stated as both axes at once: "get people from all the way wherever they are on the spectrum to where they're not fearful and they're actually using it a whole lot more." (03:29-03:39)
- Position is per-person and not stable: "realize people vary on the spectrum… And depending on the day, depending on like what they're going through, they're going to vary on the spectrum. You have to be able to talk to them." A single skeptical experience can move someone back — see the failure mode where one imperfect run sends an engineer back to babysitting. (12:11-12:28, 13:15-13:34)
- Using the map: high fear plus low usage is a safety and demonstration problem (the psychological-safety material applies); low fear plus low usage is a fluency problem; high usage plus low confidence is where mandates leave people and where a single trustworthy skill does the most work (see [Invest in One High-Value Skill to Convert Agent Skeptics](invest-in-one-high-value-skill-to-convert-agent-skeptics.md)); low fear from disappointment is the trap, and the counter is a demonstration that the setup, not the model, was the problem.
- Caveat on evidence: this is a framing device from one talk, drawn on a slide with no data behind either axis. No instrument is proposed for measuring either fear or utilization, and the trajectory is a narrative of the industry as the speaker experienced it. It is useful as a diagnostic vocabulary, not as a measurement.
- **A three-act time axis runs underneath the two spatial ones.** Blum describes adoption as a sequence rather than a position: something simple works and it is "10x faster"; the same practices applied to bigger problems fail badly, giving "lots of bugs, and the trust that you build breaks down"; only then comes "learning how to use AI correctly and put the right guardrails and the right prompting and the right context." The act-two trust collapse is a distinct route into low fear and low utilization that this map's trajectory does not name — arrived at from an early success rather than from disappointment — and it is why one org contains teams in different acts that "all need to work together in order to ship our product… they need to coexist." ([Blum](../sources/20260828_5Bn0xro2ol8.md), 01:04-02:44)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Uneven Agent Adoption Loads Review Onto the Slowest Adopters](uneven-agent-adoption-loads-review-onto-the-slowest-adopters.md)
- [Invest in One High-Value Skill to Convert Agent Skeptics](invest-in-one-high-value-skill-to-convert-agent-skeptics.md)
- [Create Psychological Safety for AI Adoption](create-psychological-safety-for-ai-adoption.md)
- [Stage Agentic-Engineering Adoption With a Delegation Maturity Model](stage-agentic-engineering-adoption-with-a-delegation-maturity-model.md)
- [Measure AI Coding Adoption With PR Telemetry and Guardrails](measure-ai-coding-adoption-with-pr-telemetry-and-guardrails.md)
- [The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap](the-best-engineers-adopt-agents-last-and-their-objections-are-the-roadmap.md)

Sources:
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 02:17-03:39, 12:11-12:28, 13:15-13:34
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 01:04-02:44
