# Run Verify-Fix-Review Loops for Agentic Refactors

Summary: Agentic refactors need a loop that separates problem discovery, agent repair, human review, and dependency-order continuation. The loop lets agents do repeatable fixes while humans approve small, tidy PRs and unblock the next wave of work.

Use when:
- Automating code-smell removal, CVE remediation, dependency updates, or large-scale migration cleanup.
- Designing an agent orchestration workflow where failures in one batch should not stop unrelated batches.

Details:
- The refactor demo uses verifier tools to identify problems, fixer agents to address them, human review and merge for the generated PRs, then repeats until the dependency-ordered work is complete. (24:56-26:57)
- Agents can continue down the dependency-ordered list while some fixers run, but should stop at a batch blocked by unfinished upstream dependencies. (25:10-25:35)
- Each fixer should return a small pull request with a useful summary, reviewer notes, and focused changes instead of one giant automated diff. (25:38-26:34)
- For CVE remediation, one agent can scan a repository, choose a language-appropriate vulnerability tool such as Trivy or `npm audit`, then spawn one agent per vulnerability to research solvability, update dependencies, fix breaking API changes, and open PRs. (35:35-36:18)
- Parallel fixers allow successful PRs to merge as they are ready while one stuck or unsolvable vulnerability does not block unrelated fixes. (36:25-36:39)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Decompose large refactors into dependency-aware agent batches](decompose-large-refactors-into-dependency-aware-agent-batches.md)
- [Run parallel issue agents in sandboxes with review and merge loops](run-parallel-issue-agents-in-sandboxes-with-review-and-merge-loops.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)

Sources:
- [Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](../sources/20260108_rcsliSIy_YU.md), 24:56-36:39
