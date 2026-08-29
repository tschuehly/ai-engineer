# Structure an Agent Plan With a Frozen Why and Reviewer-Sized Phases

Summary: Four structural rules make a plan document something an agent can execute unattended overnight: a "why" at the top the agent may not rewrite, phases sized to a pull request you would review in one sitting, a validation gate on every phase so later work never rests on unverified earlier work, and enough detail per phase to hand it to a subagent. The rules are about the artifact, not the loop — once the plan holds, any execution harness can run it.

Use when:
- Writing a plan an agent will implement without supervision, and deciding what has to be in it.
- An unattended run came back having quietly redefined the goal partway through.
- Deciding how finely to decompose a large piece of agent work.
- Reviewing someone else's agent plan and needing criteria beyond "looks thorough."

Details:
- **Rule 1 — a frozen why at the top.** "Really important to start with a why at the top. It really helps preventing agent drift… like when you write a design doc, you want to have the executive summary. Put that in there for the agent. Otherwise, they'll start drifting over time — and make sure that the agent[s] don't go back and change that because they feel like it." Two things are being asked for and they are separable: the goal statement is present, and the goal statement is immutable. The second half is the unusual one — the plan is a working document the agent edits as it progresses, and the rule carves out one section it may not touch. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 08:38-09:01)
- **Rule 2 — phases sized to a reviewable PR.** "Make sure that the plan can be broken down into small parts that can each be verified independently. And my personal way of knowing what is a good size[:] would I want to review the PR that will correspond to that part? If it's going to be too big for me to want to review in one sitting… 'I'm going to need to get a cup of coffee before I read this' — that means it's too big." The test is worth keeping in its concrete form because it is checkable in advance, at plan-writing time, by the person who will actually do the reviewing. Compare [Limit Agent Change Size by Feedback Speed](limit-agent-change-size-by-feedback-speed.md), which sizes changes by how fast the check returns; this sizes them by human reading stamina, and the two can disagree. (09:01-09:27)
- **Rule 3 — a validation gate per phase.** "What I don't want to have is… five stages and then the first one is written but not validated, and then everything else is built on top of all the assumptions. So, having… a validation gate or an ex[it] criteria for each phase really helps and make[s] the plan resilient to drift." The failure being prevented is compounding rather than local: an unvalidated phase one does not produce one bad phase, it produces four phases resting on an assumption nobody checked. (09:27-09:52)
- **Rule 4 — phase detail sized to a subagent.** "The executive summary at the top, the phases break it down, and then each one of them I would go into lots of details so that I can just fit it into a sub agent, and the sub agent can independently work on that and not have to worry about it." This gives the "how detailed?" question a concrete stopping condition: detailed enough that the phase can be handed to a fresh context that will see nothing else. (10:07-10:26)
- **The rules are loop-agnostic, and that is the point.** "There's all kind of technique[s] on how to manage the context[] and doing a software factory on top of that. But once you have the plan, you can use whatever loop you want or whatever workflow you want in order to implement it." That is what separates this page from the wiki's process pages: [Use research-plan-implement loops for coding agents](use-research-plan-implement-loops-for-coding-agents.md) says what phases the *workflow* passes through, and this says what the plan *document* must contain for any of them to survive an unattended run. (09:52-10:07)
- **The output these rules were tuned against.** One plan produced "probably 20 PRs… some of them would be maybe 10 lines, and some of them would be 100 lines. There's probably nothing bigger than that," sent to an agent overnight after a week of writing and cross-team alignment. Rules 2 and 4 are visible in that shape: nothing over ~100 lines is a one-sitting review, and twenty independently detailed phases is a subagent fan-out. (11:00-11:35)
- **Rules 1 and 3 both name drift, and they catch different halves of it.** Rule 1 protects the destination from being rewritten; rule 3 protects the route from being built on sand. An agent can hold the goal perfectly and still compound an unchecked assumption, and it can validate every phase and still be validating the wrong thing.
- **Caveats.** No measurement supports any of the four rules — they are one engineer's working practice, and the "5x speed up" attached to the example is self-estimated against a self-estimated pre-AI baseline, on work the speaker says is "probably from two plans, not one." The coffee test is explicitly personal ("my personal way of knowing"), so it calibrates to one reviewer's stamina rather than to a team's. Nothing is said about how the frozen-why rule is *enforced* — whether it is an instruction in the plan, a harness constraint, or a convention the author checks afterward — which is the difference between a rule and a hope.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Use research-plan-implement loops for coding agents](use-research-plan-implement-loops-for-coding-agents.md)
- [Collaborative Plans Become Executable Agent Context](collaborative-plans-become-executable-agent-context.md)
- [Limit Agent Change Size by Feedback Speed](limit-agent-change-size-by-feedback-speed.md)
- [Review coding-agent work at task, plan, and code checkpoints](review-coding-agent-work-at-task-plan-and-code-checkpoints.md)
- [Reduced Developer Agency Is an Adoption Cost, and Planning Is Its Remedy](reduced-developer-agency-is-an-adoption-cost-and-planning-is-its-remedy.md)
- [Write the Test First So the Agent Cannot Fit It to the Code](write-the-test-first-so-the-agent-cannot-fit-it-to-the-code.md)

Sources:
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 08:38-10:26, 11:00-11:35
