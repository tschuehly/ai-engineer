# Code Review Carries Alignment, Not Just Correctness

Summary: Code review does two jobs that are usually treated as one. *Semantic accuracy* — bugs, conventions, security — can be substituted with better tooling. *Alignment* — knowledge sharing, mentorship, architectural feedback, onboarding, collaboration — has no tooling substitute, and a plan that automates review without preserving it deletes the half nobody was measuring.

Use when:
- Designing a workflow that lets agent-written changes merge without line-by-line human reading.
- Evaluating an AI code-review product or trust model that frames review purely as defect detection.
- Explaining why review time did not simply become free when agents started reviewing agents.

Details:
- Jain wrote a five-layer trust model for merging without line-by-line review a few months before this talk, and opens by naming what it got wrong: it was built around correctness, and "code review is also about alignment… a big part of code reviews is knowledge sharing, mentorship, architectural feedback, onboarding, being able to collaborate." (00:40-03:49)
- The rule that follows: "for semantic accuracy, we can build better tooling, but alignment must survive." Tooling substitution is granted for one half and refused for the other. (04:14-04:21)
- Why it matters now rather than in principle: the correctness half is already being automated to the point of vacuity. An AI writes the code, two or three AI reviewers argue with it in a web UI, the human skims and merges — "when AI reviews and nobody reads, we have configured the wrong thing." The review artifact still exists; the alignment it used to carry does not. (02:19-02:58)
- Alignment is concentrated in specific moments rather than spread over the diff: the decisions made when the agent stops to ask a question, what was tried and rejected, and how data models and services should interact. Jain's argument for their value is that "this is how you teach your junior engineers on how to improve over time. These are the decisions which make a software engineer valuable today." (09:33-10:10, 13:48-14:04)
- Formal code review is a recent and replaceable practice, which is what makes the distinction usable: it is "maybe 15 to 20 years" old — Google launched Mondrian internally in 2006 and "made formal code review as a thing," and early Windows versions were built without reviews. The mechanism can be replaced; the function it acquired cannot be dropped silently. (03:00-03:19)
- Scope caveat the speaker volunteers: this argument is for teams. "If you're doing… [vibe] coding, you're working as a solo project, this is not a talk for you," and it assumes you are not running "completely dark factories, orchestrators, where nobody looks at the code." (03:51-04:11)
- This sharpens a caution the wiki already carries from the other direction. Litt's argument is that humans should stay in the loop to *participate*, because understanding compounds across loops; Jain's is the organizational version of the same claim — the review ritual is where that participation currently happens, so automating it without relocating the alignment work is how a team acquires cognitive debt at scale.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Make Intent and Evidence the Review Surface](make-intent-and-evidence-the-review-surface.md)
- [Understand Agent Work to Participate, Not Just to Verify](understand-agent-work-to-participate-not-just-to-verify.md)
- [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Make Code Review the Bottleneck Skill for AI-Generated Code](make-code-review-the-bottleneck-skill-for-ai-generated-code.md)
- [Human ownership keeps agent pull requests from bypassing review](human-ownership-keeps-agent-pull-requests-from-bypassing-review.md)

Sources:
- [How to Kill the Code Review — Ankit Jain, Aviator](../sources/20260817_YgEv7IQzGdM.md), 00:40-04:21, 09:33-10:10, 13:48-14:04
