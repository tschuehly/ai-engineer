# Create Psychological Safety for AI Adoption

Summary: AI-assisted engineering rollouts need psychological safety, transparent intent, and protected learning time so engineers can experiment, report failures, and build useful habits without treating adoption as a threat.

Use when:
- Planning AI enablement for engineering organizations.
- Diagnosing why an AI rollout produced compliance behavior but little durable practice change.

Details:
- The talk rejects top-down mandates such as 100% adoption because engineers can satisfy them through low-value ritual usage without improving delivery. (03:27-03:46)
- Reock links AI adoption to Google's Project Aristotle lesson that psychological safety was the strongest indicator of team performance, then applies that to current AI rollouts. (06:13-06:41)
- Leaders should communicate that AI is being used to augment engineers and improve developer experience, not to replace them, before fear blocks honest experimentation. (06:44-07:25)
- Enablement needs both education and adequate time to learn; useful guidance can come from surveying high-value users, stack-ranking use cases, and publishing concrete code and prompting examples. (13:32-14:17)
- The talk identifies stack-trace analysis as a top valuable use case, showing that useful AI practice may be interpretive rather than purely generative. (14:20-14:32)

- Khandelwal states the same premise as a design constraint on the rollout — "treat it like a human problem… Fear is real. Human emotions are real. We should recognize it" — against the alternative he rejects by name: "people will figure it out. Let's just mandate our way through life. Like, that's just not going to work." He adds two refinements. First, dismissing a skeptic as merely frightened is a mistake: "It's really easy to say like the skeptic is just someone who's scared. It's really hard to get them to buy in, but if you can get them to buy in, you know you're doing something right." Second, fear and usage move independently, so a rollout can lower fear the wrong way — after slop shipped, engineers stopped worrying because expectations dropped ("I'm not really that scared cuz… it just ships slop. Like I'm going to still be needed"), which is a worse state than the fear it replaced because it also removes the motive to learn. See [Map Agent Adoption on Fear and Utilization Axes](map-agent-adoption-on-fear-and-utilization-axes.md). ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 03:14-03:25, 08:33-08:50, 10:56-11:15)
- **A concrete safety failure with a one-sentence fix, told from the sender's side.** Blum sent an AI-skeptic senior engineer a model-written analysis without marking it as generated, and was told: "I did not expect somebody that I respect this much to send me something that's clearly this sloppy." His repair states both the boundary and the ask — "this is what I wrote. This is what the AI wrote and I need your feedback on that because I don't have the context to know if it is sloppy or not." The dynamic this page describes runs through artifacts as well as meetings: an unlabelled generated document reads as a claim about quality the sender never made, and the skeptic's reaction is about respect rather than tooling. Blum's conclusion is that "chang[ing] the culture is just as important as some [of] the engineering challenges." ([Blum](../sources/20260828_5Bn0xro2ol8.md), 14:22-15:28)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Map Agent Adoption on Fear and Utilization Axes](map-agent-adoption-on-fear-and-utilization-axes.md)
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Practice-driven AI tool fluency beats theory-only adoption](practice-driven-ai-tool-fluency-beats-theory-only-adoption.md)
- [AI adoption depends on incentive design as much as tool access](ai-adoption-depends-on-incentive-design-as-much-as-tool-access.md)
- [Mark Which Lines a Human Wrote So Readers Can Budget Attention](mark-which-lines-a-human-wrote-so-readers-can-budget-attention.md)

Sources:
- [Leadership in AI Assisted Engineering - Justin Reock, DX (acq. Atlassian)](../sources/20251219_PmZDupFP3UM.md), 03:27-03:46, 06:13-07:25, 13:32-14:32
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 03:14-03:25, 08:33-08:50, 10:56-11:15
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 14:22-15:28
