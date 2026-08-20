# Ceding a Critical Decision Transfers Ownership of the Code

Summary: Ownership of code is lost at the decision, not at the line. An engineer who lets an agent make a critical decision has ceded control of that code — the agent is now its owner — and when a whole team does it, the company no longer owns its product. The remedy is not reading more diff; it is making sure the decisions that matter are surfaced and made by a human before implementation.

Use when:
- Setting a policy for what an agent may decide on its own versus what it must ask about.
- Arguing why line-by-line review of a large agent diff does not restore ownership.
- Explaining what is actually at risk when a team accepts every recommended option.

Details:
- The claim, stated at the individual and the organizational scale: "if you as an engineer are letting an agent make a critical decision, you are [ceding] control of your code. You are no longer the owner of that code. The agent is. And if you imagine that at scale at your company, if the engineers across your team are… giving up ownership of the code, you no longer own the product." ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 03:16-03:43)
- The positive statement of the same rule: "humans own the decisions. Like, that's what we're solving for. Humans need to own the decisions. That's how we retain ownership of our software and our products and make it like a true expression of what we're trying to create in the world." (17:10-17:27)
- **How the transfer actually happens is mundane, not dramatic** — it happens through the approval UI. "the agent [is] saying, Okay, this is what I want to do. Is that okay? Let's go. Or… it'll ask you a question and it'll be like, you know, this is the recommended option and then you're like, great. I don't even think about this. I'll just hit that one and we keep going." A decision was surfaced, an answer was recorded, and no human made it. (10:55-11:10)
- The setting makes the collapse likelier: chat is "default isolated and ephemeral and… brain off" — a medium built for getting things done, entered in execution posture, which is the worst posture in which to be handed a design question. (11:11-11:35)
- **This is a different loss from the one the wiki already records.** [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md) bounds generated volume by what humans can read and insists on reading every line of critical code. That protects against code you do not understand. It does not protect against code you understand perfectly whose shape someone else chose: you can read every line of an approach you never picked. The two controls are complementary — read the critical lines, and own the critical decisions — and only the second one survives the diff getting larger.
- It is also different from ownership as *accountability routing*. [Human Ownership Keeps Agent Pull Requests From Bypassing Review](human-ownership-keeps-agent-pull-requests-from-bypassing-review.md) is about whose name is on the PR and who is responsible for the failing test. Dailey's claim is upstream of that: a human can be correctly named as the owner of a change whose every real decision was made by the model.
- The operational consequence is a surfacing problem rather than a gating problem. Blocking the agent more often does not help if the decisions arrive as recommended options inside an execution session; what helps is extracting the decisions into a place where they are visible as decisions before implementation begins — see [Make the Doc the State and the Agent the Action](make-the-doc-the-state-and-the-agent-the-action.md) and [Separate the Decision Layer From the Implementation Layer](separate-the-decision-layer-from-the-implementation-layer.md).
- Corroboration on the failure of the in-session gate comes from an unrelated source. OpenAI's Codex team reports the same degradation from the vendor side — approval prompts produced fatigue, "we saw people would just start clicking yes," and users migrated to full-access mode — which is why they moved the judgment to an automatic reviewer rather than relying on the human ([Escalate Risky Actions to a Read-Only Review Subagent](escalate-risky-actions-to-a-read-only-review-subagent.md)). Note the two responses point in opposite directions: automate the judgment, or move the judgment out of the session entirely.
- Caveats: "critical decision" is never defined in the talk, so the boundary between what an agent may decide and what it may not is left to the reader; no evidence is offered that teams using a decision layer retain ownership in any measurable sense; and the speaker sells a decision-layer product.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Velocity Sickness Is Output Without Impact](velocity-sickness-is-output-without-impact.md)
- [Make the Doc the State and the Agent the Action](make-the-doc-the-state-and-the-agent-the-action.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Human Ownership Keeps Agent Pull Requests From Bypassing Review](human-ownership-keeps-agent-pull-requests-from-bypassing-review.md)
- [Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md)
- [Escalate Risky Actions to a Read-Only Review Subagent](escalate-risky-actions-to-a-read-only-review-subagent.md)
- [Scope Coding-Agent Autonomy by User Decision Authority](scope-coding-agent-autonomy-by-user-decision-authority.md)

Sources:
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 03:16-03:43, 10:55-11:35, 17:10-17:27
