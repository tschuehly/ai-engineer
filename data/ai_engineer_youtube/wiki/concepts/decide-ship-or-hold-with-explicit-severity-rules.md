# Decide Ship-or-Hold With Explicit Severity Rules

Summary: When one open issue sits between an AI feature and its launch date, each stakeholder sees a different risk and proposes a different fix. Five rules — worst case sets severity, severity is independent of capacity, defaults are asymmetric by bug class, calibrate to revealed rather than stated risk tolerance, and humans are the scarce resource — turn that dispute into a decision procedure instead of a negotiation.

Use when:
- A launch-blocker argument is being resolved by seniority, deadline pressure, or whoever is loudest.
- You need a severity definition for AI failures that does not collapse into "how often does it happen."
- Deciding whether a known issue ships, holds, or ships with an accepted risk — and what a fast follow actually commits you to.

Details:
- **The setup.** Five days before launch, one issue is left on the board. Clinical sees member safety risk and wants to hold. Legal sees regulatory exposure. Compliance sees audit risk. Product sees adoption risk — a feature that ships broken "won't land." Engineering sees velocity risk — it can't be fixed without slipping the date. "Five rational people, five different risks, and five very different fixes." Nobody is wrong; the framework's job is to say which risk sets the answer. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 12:55-13:54)
- **Rule 1 — worst case always wins.** "Severity is set by the worst plausible outcome, not the average… A bug that lightly annoys 100% of users is way less severe than one that could cause serious harm in 0.1% of cases." The operational form is a substitution in triage: "don't ask, how often does this happen. Ask, what's the worst version of this? That sets the severity." This is the rule that frequency-weighted metrics — error rates, pass rates, average judge scores — structurally cannot express. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 14:12-14:54)
- **Rule 2 — severity is not capacity.** "This one keeps politics out of it." Severity "comes from the harm that it causes. Not who owns it, not whether your team has the capacity to fix it, not how hard the fix is." Once severity is set, exactly three moves are legal: "fix, delay the launch, or accept the risk with explicit sign-off." The prohibition is the substance: "you never quietly downgrade a bug just because you can't get to it." Accepting risk stays available — it just has to be someone's signature rather than a silent reclassification. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 14:54-15:37)
- **Rule 3 — asymmetric default, flipped by bug class.** "When you don't know what to do, always pick the safer mistake," but "safer" points in opposite directions for the two classes. For safety bugs "the math is one-sided. Shipping a real safety bug is much worse than delaying for a false alarm" — so when unsure, hold and fix. For polish bugs "the math runs the other way. Delaying a launch costs more than shipping a small flaw" — so when unsure, ship. "The framework doesn't decide for you. It just tells you which way to lean." ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 15:37-16:28)
- **Rule 4 — calibrate to revealed, not stated, risk tolerance.** "Your launch bar is what your org already accepts in production, not what it says it will accept." If a behavior "has been live in your existing product for weeks, months, without escalation, without member complaints, without leadership concern, you cannot call it a launch blocker just for a new thing." "Your stated risk tolerance might be no bugs in production, but your revealed risk tolerance is what's actually shipping today. Calibrate to the revealed one. That's the floor." This is the rule that stops a new AI feature from being held to a standard the existing product has never met — and it cuts both ways, since it also makes the existing product's real bar auditable. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 16:28-17:12)
- **Rule 5 — humans are the constraint.** "Judges scale, pattern interpretation doesn't." Judges score traces automatically and "dashboards refresh every few hours. None of that is hard anymore. But what's hard is having enough people to read the signal and act on it." So the design question for any monitoring plan is not how many judges you can run but how much human interpretation the launch will consume. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 17:14-17:41)
- **Fast follows are committed debt.** "If you didn't ship it at launch, it's not a wish list item. It's already committed." This is what makes rule 2's third option ("accept the risk with explicit sign-off") honest rather than a euphemism for dropping the issue. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 17:43-17:52)
- **The rules have a precondition.** They "all assume one thing, that your underlying signal is true" — so judge verification comes before any of them are applied to a production score. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 17:55-18:13)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Check Whether the Judge Is Right Before Changing the Agent](check-the-judge-before-changing-the-agent.md)
- [Sort Failures by Whether the User Can Retry](sort-failures-by-whether-the-user-can-retry.md)
- [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md)
- [Earn Release Confidence From Repeated Runs and Post-Launch Sampling](earn-release-confidence-from-repeated-runs-and-post-launch-sampling.md)
- [Plan AI Reliability Risk Inside Product Work](plan-ai-reliability-risk-inside-product-work.md)

Sources:
- [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](../sources/20260819_YXEqC05WEI0.md), 12:55-18:13, 20:42-21:00
