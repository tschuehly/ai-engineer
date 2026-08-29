# Let Users Author the Output Format as a Skill

Summary: For a generated artifact someone reads every day, let each user write their own format and content preferences as plain text and have the agent compose them with the platform-owned skills at run time. The claim is not that this improves quality — it is that it is what makes people use the thing at all.

Use when:
- A well-built internal generation feature is technically correct and going unused.
- Deciding whether an internal agent's output format is a platform decision or a user decision.
- Designing the composition boundary between system-owned skills and user-supplied instructions.

Details:
- **The mechanism and the reason are given together, and the reason is adoption.** "We've gone and built a skill library to allow people to customize their agents. Getting back to the meeting brief example, different people have different formats that they care about. They have different information that they care about, and allowing them to represent that in text, giving that to the agent to pull it together, has been very valuable for getting adoption." ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 12:11-12:32)
- **Two skill tiers compose at run time.** The nightly background agent draws on "meeting prep skills that we own at the system level, as well as custom instructions that users are providing themselves." The platform owns what a brief must contain and how to gather it; the user owns what theirs looks like. (12:47-13:00)
- **Why this is a real lever rather than a preference setting.** A pre-meeting brief is consumed under time pressure between back-to-back meetings; a format that does not match how a particular account manager scans will be skipped regardless of how good its content is. Adoption failures of this kind look identical to accuracy failures on a usage dashboard ([Separate the Did-Not-Try Problem From the Did-Not-Return Problem](separate-the-did-not-try-problem-from-the-did-not-return-problem.md)).
- **It sits directly opposite the governance stance in the same cluster.** Cloudflare routes skills through "a central alias where skills are presented to the central team, curated by the go-to-market team, as well as by operations team, and they're reviewed, so we can make sure that we're not having a proliferation of skills" ([Run a Submission-and-Review Alias for Shared Skills](run-a-submission-and-review-alias-for-shared-skills.md)). Both are defensible, and the difference is scope, not philosophy: a *shared* skill that others will execute is a shared liability and deserves review; a *personal* formatting instruction affects only its author's own artifact and reviewing it would cost more than it saves. Curate what is shared; let people own what only they read.
- **The self-serve tier still has to be authored somewhere.** Format instructions do not carry domain judgment — they say what to show, not how to decide. The expertise half of the same library remains a platform responsibility ([Separate the Context Gap From the Expert Gap](separate-the-context-gap-from-the-expert-gap.md)).
- **Limit.** "Very valuable for getting adoption" is the entire evidence: no adoption rate, no before/after, no count of users who wrote a skill, and no example of a user-authored instruction. Nor is any control described for a user instruction that suppresses information the platform considers mandatory — the composition rule between the two tiers, when they conflict, is unstated. (12:11-13:00)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Run a Submission-and-Review Alias for Shared Skills](run-a-submission-and-review-alias-for-shared-skills.md)
- [Fan Out a Scheduled Per-Entity Agent Instead of Waiting for a Trigger](fan-out-a-scheduled-per-entity-agent-instead-of-waiting-for-a-trigger.md)
- [Separate the Context Gap From the Expert Gap](separate-the-context-gap-from-the-expert-gap.md)
- [Separate the Did-Not-Try Problem From the Did-Not-Return Problem](separate-the-did-not-try-problem-from-the-did-not-return-problem.md)
- [Package Reusable Context as Skills, Libraries, and Registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Agent Skills Package Progressive-Disclosure Context for Repeatable Workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Invest in One High-Value Skill to Convert Agent Skeptics](invest-in-one-high-value-skill-to-convert-agent-skeptics.md)
- [Read Employee-Built Automations as the Productionization Backlog](read-employee-built-automations-as-the-productionization-backlog.md)
- [Solve One Team, Then Mirror the Build Sideways](solve-one-team-then-mirror-the-build-sideways.md)

Sources:
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 12:11-13:00
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 13:36-14:02
