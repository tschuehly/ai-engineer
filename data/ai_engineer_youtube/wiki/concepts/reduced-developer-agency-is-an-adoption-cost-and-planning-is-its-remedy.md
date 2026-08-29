# Reduced Developer Agency Is an Adoption Cost, and Planning Is Its Remedy

Summary: A cost of coding-agent adoption that no throughput metric reports is the collapse of the engineer's role into a prompt cycle — issue a request, wait on output, respond to output — which removes the flow state people took pleasure in and produces burnout. The proposed remedy is not less agent use but a relocation of the craft: the human keeps the design decisions and writes the plan, and the agent gets the typing.

Use when:
- Adoption metrics are healthy and morale is not, and the two facts are not obviously connected.
- An engineer says agent work is "not as much fun" and you are tempted to treat that as a preference rather than a signal.
- Choosing between prompting workflows and planning workflows for reasons other than output quality.
- Justifying a week of human planning time against a manager who reads planning as delay.

Details:
- **The cost, stated plainly.** "Reduced developer agency causes engineers to lose some of their job satisfaction. So, if a lot of people used to take a lot of pride and enjoyment in writing code and getting into the flow… a lot of people feel like that's been lost… getting into more of a prompt cycle where they just wait on output from AI and then speak to the AI that['s] like not as much fun as they used to have and they're getting burned out." ([Blum](../sources/20260828_5Bn0xro2ol8.md), 02:53-03:25)
- **The distinguishing word is agency, not workload.** The engineer in a prompt cycle is not necessarily busier; the decisions have moved. What is lost is being the one who chooses, in a state of uninterrupted attention. That makes this a different failure from attention exhaustion — see [Treat Human Attention as the Bottleneck for Agentic Work](treat-human-attention-as-the-agentic-bottleneck.md), where the mechanism is load and context switching. Both end in burnout by different routes, and a fix for one does not address the other: reducing parallel agents restores attention but not authorship.
- **The remedy is a relocation, not a retreat.** "This is really tied into the giving agency back to developers and finding a replacement to the craft of writing code… spending a lot of time writing the plan and then sending [it] to the agent basically as an implementation that can be done automatically is something that we find to really… reintroduce the joy of building back into the process." (07:34-08:07)
- **What the relocated craft looks like in hours.** "It's not uncommon to spend a week writing a very detailed plan, making all the decisions, fl[esh]ing it out, iterating, sending it out to teammates to review. And then only when it's ready and you've fl[eshe]d out all the decision[s], you can send it to the agent. The agent will send it back to you when it's implemented." A week of human deliberation against an overnight run is the asymmetry that makes the claim non-trivial — the human's time did not shrink, it moved. (08:07-08:26)
- **Why the relocation is plausible on its own terms.** In a prompt cycle the decisions are made incrementally by whoever is holding the keyboard at the time, which in practice is the model; in a planning workflow they are made deliberately, in advance, by the human, and reviewed by teammates before anything is built. That is the same content the engineer used to decide while typing, extracted into an artifact. Whether it feels like craft is an empirical question this talk answers only for its author.
- **The counterweight this page needs.** Planning workflows are not universally better — [Choose Plan-Heavy or Review-Heavy Agent Workflows by Task Shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md) argues that stateful, visual, and exploratory work resists specification and does better with interactive iteration. If that is right, the agency remedy is unavailable exactly where the work is least specifiable, and front-end engineers get the prompt cycle whether they want it or not. Nothing in either source resolves this.
- **A second remedy appears elsewhere in the same talk, unlabelled**: giving the strongest skeptics ownership of the verification roadmap is also an agency restoration, aimed at a different population. See [The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap](the-best-engineers-adopt-agents-last-and-their-objections-are-the-roadmap.md).
- **Caveats.** This is self-report from one engineer about one org, with no survey, retention figure, or before/after satisfaction measure. "Burned out" is used colloquially. The claim that planning restores joy is offered as the speaker's experience and his team's, and it is worth noticing that the person reporting it is the one who writes the plans — the engineers who receive a week-old plan and review its 20 resulting PRs may be in a different position, which the talk does not examine.

- **A second remedy for the same injury, aimed at the people the planning answer does not reach.** Debois reports the identical complaint in different words — "we didn't sign up for better prompting, writing better specs. We're engineers. We're technical" — and adds that context engineering, the wiki's usual reply, did not close it: developers "felt empty just working with a prompt and a specification as such." What worked was building the harness. "All of a sudden, we were helping the agent with tooling, building tooling for the agent, and that kind of reignited some of the developers who kind of felt that it wasn't for them." That is a different relocation of the craft from this page's: planning restores authorship over the product, harness work restores programming as an activity. The distinction matters operationally, because an engineer whose objection is that spec-writing is not engineering has already declined the planning remedy — a plan is a document. See [Building the Harness Is the Engineering Path That Prompting Took Away](building-the-harness-is-the-engineering-path-that-prompting-took-away.md). ([Debois](../sources/20260822_zCJtYuqwm7E.md), 02:39-04:24)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat Human Attention as the Bottleneck for Agentic Work](treat-human-attention-as-the-agentic-bottleneck.md)
- [Structure an Agent Plan With a Frozen Why and Reviewer-Sized Phases](structure-an-agent-plan-with-a-frozen-why-and-reviewer-sized-phases.md)
- [Choose Plan-Heavy or Review-Heavy Agent Workflows by Task Shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Coding Agents Shift Engineering Work Toward Planning and Review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap](the-best-engineers-adopt-agents-last-and-their-objections-are-the-roadmap.md)
- [Create Psychological Safety for AI Adoption](create-psychological-safety-for-ai-adoption.md)
- [Building the Harness Is the Engineering Path That Prompting Took Away](building-the-harness-is-the-engineering-path-that-prompting-took-away.md)

Sources:
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 02:53-03:25, 07:34-08:26
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 02:39-04:24
