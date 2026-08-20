# Multi-Repo Cost Has Moved From Navigation to Verification

Summary: The usual argument for consolidating repositories is that a coding agent cannot see across them. That premise has expired — put the repos under a common parent directory and current models navigate them fine. What still breaks across repository boundaries is the execution half: end-to-end testing, verification, deployment, and the time to clone and provision a sandbox before any of it can run. Consolidate for the agent's feedback loop, not for its reading.

Use when:
- Justifying (or declining) a monorepo consolidation on coding-agent grounds.
- Diagnosing why agents work well in a multi-repo estate until they need to prove a change works.
- Budgeting the environment setup cost of running many agent tasks in parallel over several repositories.

Details:
- **The reversal, stated in answer to exactly this question.** Asked whether the multi-repo-to-monorepo move was the point, Linkov separates the two halves: "models are much better at navigating multiple repos. So, if you put it into a higher-level folder, right, they could navigate the file directory. But, for doing that end-to-end testing and verification and deployment, it's still much harder to do with multiple repos." A shared parent directory is enough to solve reading; nothing about it solves running. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 15:15-15:36)
- **The provisioning cost is named separately and it scales with agent count.** "If you're building a sandbox environment to run sort of a full AI factory, it also takes more time to clone repos and get everything set up." This is a per-task cost, not a one-time one: every isolated agent environment pays the clone-and-provision bill again, so it compounds precisely in the regime where teams run many agents at once. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 15:36-15:44)
- **This qualifies the wiki's existing repo-architecture evidence rather than contradicting the data.** Jellyfish measured that highly distributed repository layouts showed essentially no positive correlation with PR-throughput gains, and proposed *context* as the mechanism — tools working best in one repository at a time, with cross-repo relationships undocumented ([Active Repos Per Engineer Exposes Context Architecture Drag](active-repos-per-engineer-exposes-context-architecture-drag.md)). Linkov reports the same drag persisting while naming a different mechanism a model generation later. Both can be true — the observed drag may have shifted from the reading side to the running side — but the two mechanisms imply different remedies. If the problem is context, the fix is documentation, indexes, and cross-repo retrieval; if the problem is verification, none of that helps and only a working end-to-end environment does. Neither source tests the other's mechanism.
- **The practical test.** Ask what an agent has to do to know it succeeded. If the answer is "read code in three repos," a parent directory is sufficient. If it is "run the pipeline, hit the service, deploy the change," you are paying the multi-repo tax and consolidation buys something a retrieval improvement cannot.
- **Why this is the strongest available argument for consolidation in an agent-heavy team.** The wiki's existing case for monorepos and agent-legible layouts rests largely on comprehension and entropy control. This adds an independent, mechanical reason that survives further model improvement: better navigation makes the reading argument weaker every release, while the cost of standing up a coherent test-and-deploy environment across N repositories does not fall as models improve.
- **Caveats.** This is one practitioner's answer in a three-minute Q&A, with no measurement of clone or provisioning time, no comparison of end-to-end test setup before and after consolidation, and no statement of how many repositories the claim was tested at. "Models are much better at navigating multiple repos" is an unquantified before-and-after impression, not a retrieval benchmark. The talk also does not describe the monorepo's own test suite or CI, so "verification is easier now" is asserted structurally rather than shown.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Active Repos Per Engineer Exposes Context Architecture Drag](active-repos-per-engineer-exposes-context-architecture-drag.md)
- [Give Code-Executing Agents Isolated Computers](give-code-executing-agents-isolated-computers.md)
- [Run Agentic Coding Evals as an Infrastructure-Reliability Problem](run-agentic-coding-evals-as-an-infrastructure-problem.md)
- [Agent-Legible Codebases Reduce Generated-Code Entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [Audit a Refactor Against Having Waited for Better Models](audit-a-refactor-against-having-waited-for-better-models.md)

Sources:
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 15:15-15:44
