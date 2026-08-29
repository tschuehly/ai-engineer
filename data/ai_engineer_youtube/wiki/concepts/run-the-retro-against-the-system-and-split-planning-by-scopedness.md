# Run the Retro Against the System and Split Planning by Scopedness

Summary: Two existing team rituals get repointed once agents do the implementation. The retro stops reviewing what went wrong in the code and starts asking where the agent hit the same wall repeatedly, which turns it into a harness backlog. Planning stops producing one queue and starts producing two: work scoped tightly enough to hand to an agent, and work that is still a conversation.

Use when:
- Agent adoption is real but the team's ceremonies still assume humans wrote the code.
- Looking for a recurring, low-cost mechanism that generates harness and context work without a separate program.
- Deciding what to do with the backlog items agents keep failing on.
- Sprint planning keeps producing tickets agents cannot start.

Details:
- **The retro's new question.** In the more advanced teams, "their rituals of 'we're doing a planning, and we're doing a retro' — they weren't about 'hey, we had issues with the code,' but 'we had issues with the system.' So, on the retro part: 'the agent went over and over hit this problem. Can we fix the system?' That's something you'll learn in the retro." ([Debois](../sources/20260822_zCJtYuqwm7E.md), 06:54-07:31)
- **Why the retro is the right place for it.** Repetition is the signal, and repetition is only visible across a period and across people — one engineer hitting a wall once is noise. The retro already has the cadence and the attendance; it just needed a different subject. This makes it a cheap, standing generator of the harness work that [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md) says has to be funded as a standing line rather than a project.
- **Planning splits on whether the work is scoped, not on who does it.** "Things that were sufficiently scoped enough were easy to pick up by agents because they were well-defined, and what still was left for the humans were the things that weren't scoped out well. So, we were like a split in the planning where we said, these things can straight go into agents, well-defined, and the harness is getting better, and this is conversational things that we need to decide as a team." (07:31-08:00)
- **The split moves as the harness improves, which is the point.** "The harness is getting better" is doing real work in that quote: the boundary between the two piles is a property of the system on that date, not of the ticket. Read alongside the retro, the two rituals form a loop — the retro moves the boundary, planning re-measures it every cycle.
- **The lead paces the ladder rather than letting it emerge.** "There's a certain kind of cycle that developers go through… prompting, they get better, specs, context, harness loop… But the lead of the team can say, 'Well, stop prompting. Make the context reusable.' Now, we got that. Now, we jump to the next. So, part of the team lead is putting that pace and almost that constraint and that directive in the team, where it does[n't] work where you just say, 'Go figure it out and do something on your own.'" (08:00-08:48) This is a directive, and Debois is explicit that laissez-faire fails — the same conclusion [Stage Agentic-Engineering Adoption With a Delegation Maturity Model](stage-agentic-engineering-adoption-with-a-delegation-maturity-model.md) reaches from measurement rather than from ritual.
- **Relation to the wiki's planning material.** [Coding Agents Shift Engineering Work Toward Planning and Review](coding-agents-shift-engineering-work-toward-planning-and-review.md) and [Structure an Agent Plan With a Frozen Why and Reviewer-Sized Phases](structure-an-agent-plan-with-a-frozen-why-and-reviewer-sized-phases.md) both describe how to write a plan an agent can execute. This page is upstream of both: it is the triage step that decides which items get a plan written at all, and it names the residue — genuinely undecided work — as the human's, rather than treating under-specification as a defect to be fixed before every ticket.
- **Engineering practice does not get relaxed on the way through.** "We're also instructing this: 'Please do it with tests. Please update the documentation.' All the things that we're saying to good engineers, we're now asking the agents to do. So, if you still have people who are yoloing their way into this… engineering practices still matter for you to maintain the system, and also for the agent to keep getting better at this." (06:00-06:54) The second reason is the interesting one: the practices are inputs to the agent's next run, not just outputs for humans.
- **Caveats.**
  - This is an observation of unnamed "more advanced teams," with no count and no before-and-after. Nothing here has been measured.
  - Neither ritual has a stated failure mode. A retro that produces harness items every cycle can become a backlog nobody funds, and the talk does not say who takes the items or how they are prioritized against feature work.
  - "Sufficiently scoped" is undefined, and the wiki's own material suggests it is not a single threshold — see [Make the Triage Agent Ask the Reporter for the Missing Context](make-the-triage-agent-ask-the-reporter-for-the-missing-context.md), where under-specification is treated as a state the system can resolve by asking rather than a fixed property that routes work to a human.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Coding Agents Shift Engineering Work Toward Planning and Review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Structure an Agent Plan With a Frozen Why and Reviewer-Sized Phases](structure-an-agent-plan-with-a-frozen-why-and-reviewer-sized-phases.md)
- [Stage Agentic-Engineering Adoption With a Delegation Maturity Model](stage-agentic-engineering-adoption-with-a-delegation-maturity-model.md)
- [Demand-Driven Context Pulls Knowledge From Failed Work](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Measure Enablement by Human Touches and Share of Fixes Reused](measure-enablement-by-human-touches-and-share-of-fixes-reused.md)
- [Building the Harness Is the Engineering Path That Prompting Took Away](building-the-harness-is-the-engineering-path-that-prompting-took-away.md)
- [Make the Triage Agent Ask the Reporter for the Missing Context](make-the-triage-agent-ask-the-reporter-for-the-missing-context.md)

Sources:
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 06:00-08:48
