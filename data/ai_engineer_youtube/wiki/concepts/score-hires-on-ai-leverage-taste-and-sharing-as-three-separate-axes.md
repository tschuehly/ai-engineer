# Score Hires on AI Leverage, Taste, and Sharing as Three Separate Axes

Summary: New AI job titles carry intent, not validation, because nobody has enough tenure in the role to be judged mature in it. A usable substitute is a three-part interview — an exercise where the candidate is told to use AI as hard as they can, a walkthrough where they explain why the result is good, and a read on whether they share their work — with the three scored separately rather than collapsed into a seniority level.

Use when:
- Writing a job posting or an interview loop for an AI-heavy engineering role and the titles are not helping.
- Deciding whether to ban AI in a take-home exercise or require it.
- A candidate is strong on one dimension and weak on another and the loop wants a single number.
- Explaining to a hiring committee why "senior" is the wrong output of this process.

Details:
- **Titles are a discovery channel, not a signal.** "We have all the titles, the new job titles: AI product engineer, forward deployed engineer, agentic engineer, AI engineer. It doesn't mean anything. You cannot judge the maturity of this because nobody's really that mature. But it's a signal when you put a job posting out there that people with the new intention will be looking there. But it's not a validation of the skills as such." ([Debois](../sources/20260822_zCJtYuqwm7E.md), 15:09-15:53) The distinction is worth keeping: title as advertising works, title as evidence does not, and the second is what interview loops usually assume.
- **Stage one — require AI, do not police it.** "First step is we give them an exercise and we want them to really go nuts on the AI to solve this. If they have help from AI, that's all good. That shows you how much they can leverage the AI to do this." (15:53-16:32) This directly answers the take-home-cheating problem he mentions a moment earlier (candidates being fed answers during interviews, 15:53-16:20): if the tool is mandatory, its use stops being a detection problem and becomes the measurement.
- **Stage two — the walkthrough is where taste is measured.** "After they pass this, you do a walk-through and you actually say, 'Please explain me what happened. Why is this a good idea?' That's where you are testing the taste and the engineering skills on why they're doing this. First part AI, then engineering." (16:20-16:42) The ordering is the mechanism. The artifact is produced with maximum assistance, and then the candidate has to defend decisions inside it, which is exactly the situation an engineer is in when reviewing agent output in the job.
- **Stage three — collaboration, because the leverage is shared.** "This third thing is: how do you collaborate? Are you willing to share? Are you open or are you a solo player? That's another signal that you tap into… making it shareable, making it reusable, making it engineering grade within our organization." (16:42-17:01) This is not a culture-fit add-on; it follows from the talk's central metric, that a fix which stays on one person's machine is not a multiplier — see [Measure Enablement by Human Touches and Share of Fixes Reused](measure-enablement-by-human-touches-and-share-of-fixes-reused.md).
- **Who this is not looking for.** "Not people who studied ML or AI, not people who are experts per se at the coding. There's a blend on this." (16:59-17:12) A useful negative: the profile is neither the ML researcher nor the strongest programmer, which fits the wiki's [AI Engineering Practice Is Heterogeneous and Fast Moving](ai-engineering-practice-is-heterogeneous-and-fast-moving.md) picture of the discipline: there is no settled body of knowledge to test for, so the loop tests behaviour instead.
- **Do not collapse the three into a level.** "You might not find a person who has all three, which is okay, but at least you know, hey, they're very savvy on this piece, but then for the other piece, they need mentoring and they need tutoring. But don't put all the three pieces into one, saying they're junior or they're senior. They have different skills on there." (17:12-17:32) The output of the loop is a three-part profile with a named development plan, not a band. That has a practical consequence most loops resist: a hire can be strong on AI leverage and weak on taste, which is a different onboarding from the reverse and is invisible once both are averaged into "mid-level."
- **Relation to the wiki's existing hiring page.** [Hire for AI Fluency and Agent Orchestration Ability](hire-for-ai-fluency-and-agent-orchestration-ability.md) says to probe whether candidates can guide and supervise agents. This page supplies a concrete loop for doing that, and adds the axis that page omits — whether the candidate's improvements leave their own workflow.
- **Caveats.**
  - The whole sequence is second-hand: "what I hear from most companies is." No company is named, no outcome is reported, and there is no evidence that candidates selected this way perform better.
  - The exercise measures AI leverage under exam conditions with an unfamiliar codebase, which is not the setting where harness and context work happens.
  - "Are you willing to share?" is asked, not observed. Self-reported collaborativeness is among the least reliable interview signals, and the talk offers no behavioural substitute — unlike the wiki's [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md), where the equivalent test is whether someone actually edits the shared setup.

Related topics:
- [Workflows](../topics/workflows.md)

Related concepts:
- [Hire for AI Fluency and Agent Orchestration Ability](hire-for-ai-fluency-and-agent-orchestration-ability.md)
- [Measure Enablement by Human Touches and Share of Fixes Reused](measure-enablement-by-human-touches-and-share-of-fixes-reused.md)
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Practice-Driven AI Tool Fluency Beats Theory-Only Adoption](practice-driven-ai-tool-fluency-beats-theory-only-adoption.md)
- [AI Engineering Practice Is Heterogeneous and Fast Moving](ai-engineering-practice-is-heterogeneous-and-fast-moving.md)
- [Hire Humans for Context, Verification, and Accountability](hire-humans-for-context-verification-and-accountability.md)
- [Building the Harness Is the Engineering Path That Prompting Took Away](building-the-harness-is-the-engineering-path-that-prompting-took-away.md)

Sources:
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 15:09-17:32
