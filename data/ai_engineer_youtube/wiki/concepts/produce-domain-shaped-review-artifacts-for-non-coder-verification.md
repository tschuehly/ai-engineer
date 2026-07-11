# Produce Domain-Shaped Review Artifacts for Non-Coder Verification

Summary: When a coding agent's users are domain experts rather than engineers, its raw code is not a reviewable surface. Because you own the final deterministic execution step, have it emit a structured, domain-shaped review artifact — aggregate outcomes, impact, and drill-down — so a non-technical expert can verify *what the agent did* without ever reading the underlying code. The code becomes just the means to an end.

Use when:
- The people who must sign off on agent work are domain experts (analysts, scientists, ops) who don't read code, and manual code review "is not in their wheelhouse."
- The agent is frequently "right for the wrong reasons," so checking the output requires understanding the reasoning, which code review would otherwise force.
- You already own a deterministic execution/commit step and want to turn its validated outputs into a verification surface for both users and downstream automated checks.

Details:
- The problem: after a coding agent finishes, its work is hard to review — users "are not software engineers," and when the agent is "right for the wrong reasons" (frequent in judgment-heavy domains) "it's really hard to check its work without going and reading that code directly." ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 05:50-06:35)
- The fix: the owned deterministic execution, once it has validated output artifacts, "create[s] a well-structured review artifact that makes it easy to review what the agent did without having to actually ever go read the underlying code that produced it." ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 11:20-11:32)
- Concrete shape of the artifact: an emissions report where a graph-edit function ("impact analysis") ran on 50 graphs, two functions produced 749 edit actions and reduced overall emissions by 45.6%; the reviewer can drill from that summary into each edit (one large chunk, one small change) and down to the per-graph node level — all without reading the low-level code. ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 11:32-12:16)
- Because the deterministic system "produces artifacts in an expected form," you can build verification against them — catching both good outcomes and errors and surfacing them clearly "to both the user and the AI," so even a wrong-or-unexpected answer is easy to follow and loop back on. ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 12:17-13:34)
- The principle: "use that deterministic final outcome to produce outputs that are easy to validate even for non-coders. The code is kind of just the means to an end." ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 16:16-16:36)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Constrain Agent Effects, Not Expression, With a Typed SDK](constrain-agent-effects-not-expression-with-a-typed-sdk.md)
- [Verify the Process, Not Just the Answer, in Judgment-Heavy Domains](verify-the-process-not-just-the-answer-in-judgment-heavy-domains.md)
- [Dynamic Artifacts Make Agent Work Reviewable and Reusable](dynamic-artifacts-make-agent-work-reviewable-and-reusable.md)
- [Domain expert review tools convert judgment into deployable knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md)
- [Non-technical collaborators can steer agents with natural work artifacts](non-technical-collaborators-can-steer-agents-with-natural-work-artifacts.md)

Sources:
- [Respect The Process - Andrew Dumit, Watershed Technology Inc.](../sources/20260707_CLttOU7n6sI.md), 05:50-06:35, 11:20-13:34, 16:16-16:36
