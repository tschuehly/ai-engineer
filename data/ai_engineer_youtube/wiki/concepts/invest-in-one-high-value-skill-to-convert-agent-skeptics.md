# Invest in One High-Value Skill to Convert Agent Skeptics

Summary: Rather than distributing agent enablement across many small skills, put the investment into one skill that carries a complete, universally shared, universally disliked segment of the workflow end to end. Its value is legible without an explanation, and its long unattended runtime is the evidence of trust rather than a defect.

Use when:
- Choosing where to spend the first serious chunk of harness-engineering effort on a team.
- Trying to convert engineers who have used agents and were unimpressed.
- Deciding how to respond to "the agent has been running for an hour."

Details:
- The choice and its scope: "there's one high value skill that we invested in. In our case it was this thing called ship it. What it did was the moment you're done with your code, it takes care of everything from code done to PR ready for review. Which means you got to open a PR, figure out your [description], handle all the comments… handle all the PR descriptions, the merge comments, everything. It handles CI failures. It basically runs through these loops." ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 09:47-10:14)
- Why this segment is a good wedge, from the properties of the choice rather than from the talk's claims: it is work every engineer does, none enjoys, whose success criteria are external and checkable (does CI pass, is the PR ready), and whose failure is cheap and visible. It also sits *after* the part engineers are protective of, so adopting it does not require them to give up authorship of the code.
- The runtime is the argument, not the objection: "often the skill was running for over an hour. And that scared people, but once… they saw the value, they get invested… it's one skill which tells them, 'Okay, this AI thing can actually work for me. I don't need to constantly baby sit it. I can trust it.'" (10:14-10:32)
- Long runtime is therefore reframed as an expectation-setting problem: "Agents are taking too long. This is actually one of those expectation setting things. It's good if agents take too long. That means you can actually go off and do other things and you have confidence that they're doing the right thing." (12:28-12:51)
- Read that against the wiki's own diagnostic list, which does *not* include long runtime: what indicts a setup is the intervention rate, not the duration. A one-hour run nobody watches is the goal state; a ten-minute run that needs three nudges is the failure. See [Read a Broken Agent Setup From Babysitting, Context Burn, and Slop](read-a-broken-agent-setup-from-babysitting-context-burn-and-slop.md).
- Skepticism has a one-strike failure mode that has to be absorbed by the skill rather than argued with: "as soon as people saw like, 'Oh, this isn't working perfectly or the way I expected it.' There is super easy for them to say, 'You know what? I'm just going to go back to babysitting my agent.' You don't want that. You want to actually take their feedback and put it back into the skill and improve the skill." A shared skill's complaint channel is its improvement channel — the same loop recorded in [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md), with the added organizational point that the reverting engineer is the signal. (12:11-12:28)
- Caveats, and they are substantial:
  - The skill is described only by what it does. No prompt, no file layout, no tool set, no error handling, no cost per run, and no measure of how often its PRs needed human rework. Nothing establishes that the hour of runtime bought output worth an hour.
  - The generalization Khandelwal offers for long runtimes — "the moment we hit this reasoning paradigm, the longer the agent like thought, the better its output," extended to "a similar mindset for your entire code base and for your skills" — is an analogy with no measurement behind it, and it is the most attractive unsupported claim in the talk. Longer runs are not uniformly better; the trust argument stands on its own without this one.
  - A single high-value skill is also a single point of failure and a governance surface: everyone's PRs flow through it, so a regression in it is a team-wide outage, and the ~100-line cap that keeps it maintainable becomes load-bearing (see [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md)).
- **A competing answer to the same problem: hand skeptics the roadmap instead of a wedge.** This page converts skeptics by building one thing so useful they adopt it. Blum inverts the direction — "just make sure to bring them in rather than trying to figure out how to make them use the AI. Just… let's have them be in charge of the road map to make AI safe [in] your organization, and they will come along once they see that the improvement that they're making [is] actually making their life better." Both sources agree on the channel — the complaint is the improvement signal — and differ on who owns the backlog it feeds. They compose in sequence: the skeptics' roadmap tells you which wedge is worth building. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 11:45-12:33)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Map Agent Adoption on Fear and Utilization Axes](map-agent-adoption-on-fear-and-utilization-axes.md)
- [Read a Broken Agent Setup From Babysitting, Context Burn, and Slop](read-a-broken-agent-setup-from-babysitting-context-burn-and-slop.md)
- [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Treat Complex Skills Like Software Artifacts](treat-complex-skills-like-software-artifacts.md)
- [Human Ownership Keeps Agent Pull Requests From Bypassing Review](human-ownership-keeps-agent-pull-requests-from-bypassing-review.md)
- [The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap](the-best-engineers-adopt-agents-last-and-their-objections-are-the-roadmap.md)

Sources:
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 09:47-10:32, 12:11-12:51
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 11:45-12:33
