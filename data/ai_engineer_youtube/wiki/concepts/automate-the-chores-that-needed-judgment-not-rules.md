# Automate the Chores That Needed Judgment, Not the Ones That Needed Rules

Summary: The chores newly worth automating are not the ones a script could already do — they are the ones a script could never decide, but a human decides routinely in seconds from evidence already sitting in the repository. "Until now the only automations that we had were heuristics like make sure there's a semicolon at the end of every line"; the new set is anything requiring "some amount of basic judgment and intelligence." That test is a practical filter for which of a team's recurring annoyances are now candidates.

Use when:
- Choosing the first standing automations to add to a repository, and needing a criterion better than "what feels AI-ish."
- A recurring chore was rejected years ago as unautomatable and nobody has revisited the decision.
- Distinguishing work that should stay a deterministic script from work that needs a model in the loop.
- Justifying agent automation to people who have watched linters and bots fail at the same task.

Details:
- **The dividing line, stated as history.** Software has been "pre-industrial" because its only automations were heuristics — rules simple enough to write down completely. AI extends the automatable set to tasks that require judgment, and Gazit's argument for why this matters is an economic one rather than a novelty one: "there's no magic trick to making great software. It costs time. And we can buy that time by automating away the things that we used to need to do manually… Either you hire more people or you automate away part of what your people are currently doing." ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 02:53-03:41)
- **The canonical example, from an outside project.** The Home Assistant project's first Agentic Workflow "looks at every submitted issue, walks the Python stack trace to figure out if the bug is in first-party code or third-party code, closes the issue if it's not their issue. That's something that was not possible before AI, not possible with heuristics, but is possible now." Every property of the test is present: no rule set can classify an arbitrary stack trace by ownership, a maintainer does it in seconds, the evidence is entirely in the issue and the repo, and the output is a reversible action on a tracker. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 12:36-13:00)
- **The upgrade treadmill is the same test applied to dependencies.** Dependabot already covers the rule-shaped half — noticing that a version is behind — and stops exactly where judgment starts: "when I do these upgrades, I frequently need to make code changes." What Gazit wanted was "a kind of super Dependabot… figuring out how to upgrade me, including the code changes, the breaking changes." The demonstrated run crossed two major versions of Astro, found and fixed the broken call sites, verified the build, and separately flagged the manual steps it could not take — that last output being the honest form of a judgment task's result. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 04:55-05:34, 09:35-10:11)
- **A cheap way to find candidates: the reflex you are embarrassed by.** The CI-doctor workflow exists because of one: "how many times have you responded to a busted CI run by just running it again? All of us. Anybody who hasn't raised their hand is lying." A reflex that substitutes for diagnosis is a reliable marker of a judgment chore nobody has had time to do properly. Other shipped starters follow the same shape — an issue triager, a Repo Assist swarm finding and fixing low-hanging fruit and flagging tickets that need nudging, and hunting N+1 queries in a monolith. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 10:36-11:26)
- **The class is not limited to engineers.** Daily team and repo status is pitched at "product managers whose job it is to look at information over here and summarize those tickets over there. We can start to get everybody involved in automation. That's how you actually get industrial scale." The test transfers cleanly: summarizing a week of tickets into a status is judgment work with all its evidence already in a system. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 11:26-11:46)
- **Why this belongs to unattended automation specifically.** Gazit's bet is that this category is "going to be bigger than interactive AI, because automations that run in the background while you sleep, that's the ballgame." Judgment chores are a good fit for unattended running precisely because they are low-stakes and repetitive — but only once the output side is bounded, since an unattended judgment call that fires hundreds of times is the failure mode. See [bound what an unattended automation may emit](bound-what-an-unattended-automation-may-emit.md). ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 13:01-13:16)
- **How it relates to the enterprise ROI argument.** [Target enterprise coding agents at maintenance and incident work](target-enterprise-coding-agents-at-maintenance-and-incident-work.md) reaches an overlapping conclusion from a different direction — where the returns are, in organizations with large legacy estates. This page gives the per-task test rather than the category, and it explains *why* maintenance is where the returns sit: maintenance is dense in decisions that were always cheap for a human and always impossible for a rule.
- **The missing half: verification.** The test says nothing about how you know the judgment was right. Home Assistant's workflow closes issues, so its error mode is a wrongly closed bug report from a real user, and no accuracy figure is given for it anywhere in the talk. A judgment chore is a good automation candidate when a wrong call is cheap to notice and cheap to reverse; that qualifier is not stated in the source and should be applied before adopting the test.

Related topics:
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Target Enterprise Coding Agents at Maintenance and Incident Work](target-enterprise-coding-agents-at-maintenance-and-incident-work.md)
- [Agents Expand the Economically Viable Software Surface](agents-expand-the-economically-viable-software-surface.md)
- [Bound What an Unattended Automation May Emit, Including Emitting Nothing](bound-what-an-unattended-automation-may-emit.md)
- [The Markdown Workflow Is the Source; the YAML Is a Compiled Artifact](the-markdown-workflow-is-source-the-yaml-is-a-compiled-artifact.md)
- [Stage Proactive Coding Agents From Maintenance to System Awareness](stage-proactive-coding-agents-from-maintenance-to-system-awareness.md)
- [Automation Loops Convert Repeated Review and Triage Into Factory Improvements](automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md)

Sources:
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 02:53-13:16
