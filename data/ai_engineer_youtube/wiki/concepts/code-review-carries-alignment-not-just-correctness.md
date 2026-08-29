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

- Matt Dailey (Ref) agrees the alignment function must survive and puts it somewhere else entirely: upstream of implementation, in a shared decision document, so that "the code review is easier because the hardest part of any code review is… what actually matters here." On his account the later review does not need to carry alignment because alignment already happened. The open question the pairing raises is what remains of Jain's second list — mentorship, onboarding, knowledge sharing — when the alignment moment moves to a document that only the people already in the conversation write. ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 16:03-16:54)
- **A team that kept review fully human for the alignment half, while automating the accuracy half.** Through a six-month rebuild, WiseDocs ran "all human PR reviews during that refactor" alongside skills used as local checks — "we did some local checks where we ran skills to say, 'Hey, review this code. Make sure that it's good.'" The reason given is exactly this page's second job, and it is stated as the primary one: "PRs were really good way for us to build context for that repo as we only had a few developers working on it, and we wanted to make sure people understood what had gone into the refactor." The split is instructive — tooling took semantic accuracy, humans kept the PR as the mechanism that spread understanding of a codebase nobody had worked in yet — and he expects the automated half to keep growing: "they're continuing to get more autonomous as time goes on." ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 16:36-17:00)

- **The cleanest available split between the two jobs, from the correctness side.** Pant's capacity argument is why the semantic half gets substituted at all — "human code review doesn't scale to match agent speed" — and a machine-checked proof is the strongest possible substitute for it, since "none of these can say for all inputs the code is correct" and a verifier can. It is also the starkest illustration of what substitution costs: a kernel accepting 32,000 lines of proof transfers no knowledge, no mentorship, and no architectural context to anyone. Correctness fully automated leaves the alignment job exactly where it was, and with less incidental reading to carry it. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 00:33-00:42, 05:47-05:56)

- **Surfacing what a specific senior engineer already said is the alignment half, delivered by machine.** Unblocked's review agent boosts mined comments by author seniority and expertise, and the demonstration is a recognition moment: the senior engineer's response to a bot comment was "that's something I would say," because it was. That transfers a team's accumulated judgment to whoever is reviewing now, which is the mentorship function this page says cannot be substituted by better bug-finding. What it does not transfer is the two-way part — the junior engineer who would have asked a follow-up question gets an answer without the conversation. ([Werry](../sources/20260827_qdAkxLoYNI8.md), 12:44-13:40)

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
- [Separate the Decision Layer From the Implementation Layer](separate-the-decision-layer-from-the-implementation-layer.md)
- [Audit a Refactor Against Having Waited for Better Models](audit-a-refactor-against-having-waited-for-better-models.md)
- [Ship a Proof a Small Kernel Can Recheck, Not a Claim You Must Trust](ship-a-proof-a-small-kernel-can-recheck.md)
- [Weight Mined Review Guidance by the Author's Expertise](weight-mined-review-guidance-by-the-authors-expertise.md)

Sources:
- [How to Kill the Code Review — Ankit Jain, Aviator](../sources/20260817_YgEv7IQzGdM.md), 00:40-04:21, 09:33-10:10, 13:48-14:04
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 16:03-16:54
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 16:36-17:00
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 00:33-00:42, 05:47-05:56
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 12:44-13:40
