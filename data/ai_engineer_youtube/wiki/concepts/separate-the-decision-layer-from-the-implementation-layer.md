# Separate the Decision Layer From the Implementation Layer

Summary: Once agents own implementation, the human work above it — deciding what matters and what the system should become — is a distinct layer, not the front end of coding. Treating it as a layer has a tooling consequence (the IDE and the chat were built for the layer you no longer work in) and a personal one (the skill is noticing which gear you are in and whether your current tool serves it).

Use when:
- Deciding whether planning deserves its own surface rather than a mode inside the coding tool.
- Explaining why an engineer feels unproductive in a tool that used to work well.
- Auditing a session that started as design work and quietly became implementation.

Details:
- The shape of the work changed, not just its speed. Before: "planning up front… sit down and build. We'd implement… But largely we're sitting down building in isolation… And at the end we sort of polish it up and ship it out the door." After: plan, then "an agent takes that idea and… implements it. This is like arguably should not even be on this slide cuz it's not our human work anymore," then polish — "we take back that thing the agent has made for us and we… say, is this what I wanted?" ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 06:39-08:20)
- The tooling mismatch is stated as a historical fact rather than a complaint: "all our history of coding tools were built for this style of work. Um our IDE, our workhorse… it was built for implementation and polish to be done by an individual, to be heads down building as a software engineer writing code… That's a tool built for how we used to work." (07:03-07:27)
- What remains is characterized by a property, which is the reason it needs different tooling: the two surviving human phases are "the two creative and collaborative parts of our work as engineers," where "we express our craft" — as opposed to implementation, which was individual and heads-down. Tools optimized for solo focus are the wrong shape for collaborative, exploratory work. (08:07-08:20)
- The layer's actual job description: "This is the decision layer. This is where we're thinking through what are the key decisions, doing that like craft of engineering… and expressing our taste as engineers, ultimately a different thing than implementation." Concretely, "I have this vague idea. I have this complex system. I need to understand the contours of this system, apply this idea… And I need to pull out what's relevant and express my taste as an engineer. As to like, where do I want this system to go?" (08:21-09:40)
- **The gear check.** "it's a different gear as an engineer. The skill now is what gear am I in? Am I using the appropriate tools for the gear that I'm… trying to accomplish right now." The actionable form is drift detection *within* one session: "notice when you're in a single session and you're doing both of these in one session. Notice when you drift from the planning phase into the polish phase and is your tool serving you for what you're trying to do at that moment?" This is the part that costs nothing to adopt — it is an observation habit, not a tool purchase. (09:40-09:55, 18:43-19:16)
- The durable version of the layer is organizational, not personal: "we're always going to have this thing where we have a group of people responsible for managing a complex system and it's sort of deciding the future of that system. And that's this planning work." That framing is what makes the layer survive changes in model capability — it is about who is accountable for the system's direction, not about what the model cannot do yet.
- Scope boundaries the speaker draws himself. This is not plan mode, which is "largely… a rich chat message… But it's still in this isolated ephemeral environment," and it is not spec-driven development, which "operate[s] at the like product level [and] is a little far away from the engineering reality." He is after "something in the middle" — "more durable, more shared, more long-lived that you and your team are spending time on." (12:03-12:52)
- Relationship to the wiki's existing displacement claim. [Coding Agents Shift Engineering Work Toward Planning and Review](coding-agents-shift-engineering-work-toward-planning-and-review.md) establishes that human time moves *into* planning and review. This page adds the consequence that follows: displaced time inherits the wrong tools, and the two remaining phases have different requirements from each other — planning is exploratory and shared, polish is evaluative and local — so "plan and review" is two gears, not one new job.
- Caveat: the layer separation is argued, not measured, and it is argued by a vendor selling a decision-layer tool. No comparison of a decision-layer tool against plan mode or a spec-driven toolchain is offered anywhere in the talk, and the gear-drift claim rests on the speaker's observation of users rather than on any instrumentation.

- **What happens to the ratio between the two layers once implementation is cheap.** "Often I find that frontier engineering teams spend more time making decisions than they do writing code," which inverts the proportion most engineering processes were sized for and makes the decision layer's own latency the thing worth optimizing: "the more that you can make fast decisions, especially ones that are easy to be reversed, the better." The reversibility qualifier is the operative part — the argument is for sorting decisions by cost-to-undo and refusing a heavyweight review on the cheap ones, not for removing governance. Liguori's evidence is the arithmetic of Amazon's own timelines rather than any measurement of decision latency. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 19:37-19:56)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Coding Agents Shift Engineering Work Toward Planning and Review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Make the Doc the State and the Agent the Action](make-the-doc-the-state-and-the-agent-the-action.md)
- [Velocity Sickness Is Output Without Impact](velocity-sickness-is-output-without-impact.md)
- [Choose Plan-Heavy or Review-Heavy Agent Workflows by Task Shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Collaborate With Complex Agents Through High-Bandwidth Artifacts](collaborate-with-complex-agents-through-high-bandwidth-artifacts.md)
- [Spec-driven development is a tool-portable pattern, not a single product](spec-driven-development-is-a-tool-portable-pattern.md)
- [When Code Stops Being the Long Pole, Approvals Become It](when-code-stops-being-the-long-pole-approvals-become-it.md)

Sources:
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 06:39-09:55, 12:03-12:52, 18:43-19:16
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 19:37-19:56
