# Verification Debt Outlives the Productivity Spike

Summary: In a Carnegie Mellon study of GitHub projects sorted by whether an AI tool wrote the code, the productivity gain was temporary — about three months — while the static-analysis warnings and added complexity persisted. The two effects have different half-lives, so a measurement taken during the spike describes a state the project will not stay in, and the leftover gap between the quality a model gives you and the quality the application needs is what has to be paid down.

Use when:
- Someone reports an AI-coding productivity gain measured in the first weeks or months of adoption and treats it as the steady state.
- Deciding how much verification infrastructure a project needs, and wanting an argument that is not "AI code is bad."
- Explaining why a team that felt fast in month two feels slow in month six with the same tooling.
- Sizing how much of the quality gap you can tolerate for a given application.

Details:
- **The result, as reported.** Researchers "looked at projects that were posted on GitHub" and used "the metadata to… sort them into projects where… there were just traditional tools that were being used and projects where an AI tool was used to write the code. In this case, it was Cursor, although it could have been any AI tool." They found "a temporary spike in productivity… but it lasted about 3 months and then it went back down." ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 01:45-02:16)
- **The asymmetry is the finding.** Alongside the transient gain there was "a persistent increase in static analysis warnings and code complexity" that "went beyond the 3-month mark and persisted well into the future." The proposed causal link — that the residue is what erases the gain, because "it's these types of issues that end up actually slowing developers down even more" — is explicitly the speaker's inference, flagged in his own words as "the reason for that, we think." (02:16-02:40)
- **Verification debt is the name for the gap, and criticality sets how much of it you can carry.** For "a short-lived project that's not going to last very long," or an internal app with a few users, "the gap between the quality that you're getting from the AI tool and the quality you need from the application is quite small… and you can live with that gap." At the other end — many users, "a larger code base with many lines of code and many changes happening across that code base all the time," and users who "could be adversaries that are actively trying to break your software" — "the quality level you need is quite a bit higher than the quality level you're getting by default." (02:46-03:53)
- **Two independent causes of the gap, worth keeping separate.** Models "will still make mistakes… they are still somewhat error-prone" — a capability gap that better models shrink. And separately they are "missing context… They don't know what's happening with your business. They don't know what happened in the meeting you had with somebody else 2 weeks ago that's going to influence the code you're writing today" — an information gap that better models do not shrink, because the information was never in the prompt. Only the first is on a curve you can wait out. (03:55-04:46)
- **What this adds to the wiki's existing quality-axis evidence.** [Measure Generated Code Quality Beyond Pass Rate](measure-generated-code-quality-beyond-pass-rate.md) shows the same vendor's static analysis finding rising complexity and bug density in *generated output measured at generation time*; this page adds the longitudinal half — that the same signals accumulate in a real repository over months and outlive the speedup that produced them. Read with [Agentic coding economics shift attention from writing cost to assurance cost](agentic-coding-economics-shift-attention-from-writing-cost-to-assurance-cost.md): assurance cost is not merely large, it arrives later than the benefit, which is exactly the shape that makes it easy to under-budget.
- **Caveats, and they are substantial.** The study is cited with no link, cohort size, control for project type, or definition of "productivity"; the measurement instrument was SonarQube, cited by a Sonar speaker as evidence for adopting Sonar; and the three-month figure is quoted as "about 3 months" with no confidence interval. Treat the *shape* — transient gain, persistent residue — as the reusable claim and the numbers as unverified. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 02:16-02:34)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Measure Generated Code Quality Beyond Pass Rate](measure-generated-code-quality-beyond-pass-rate.md)
- [Agentic coding economics shift attention from writing cost to assurance cost](agentic-coding-economics-shift-attention-from-writing-cost-to-assurance-cost.md)
- [Match the Quality Method to Your User Count](match-the-quality-method-to-your-user-count.md)
- [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Treat slop as a quality failure, not an AI provenance label](treat-slop-as-a-quality-failure-not-an-ai-provenance-label.md)

Sources:
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 01:45-04:46
