# Staff Agent Operations With a Team of Agents

Summary: Because operating an agent product is itself an agent problem (it needs reasoning to separate a real bug from noise and a symptom from a root cause), staff the operations with a "meta harness" — a team of specialized operating agents that watch, diagnose, test, and draft fixes at a volume no human team could match — while humans stay only at the merge/approval boundaries.

Use when:
- A single person can no longer read every production trace, so you need agents doing the watching and drafting.
- Designing an operations pipeline for a live agent product (monitor → diagnose → PR → review → merge).
- Deciding where humans should remain in a high-volume, agent-generated fix flow.

Details:
- "The operating agent itself is an agent problem": handing raw logs to an agent is not easy because it must reason about real-bug-vs-noise and symptom-vs-root-cause, not just filter text. (05:48-06:50)
- Log-monitoring agent (fastest loop): runs every ~15 min–1 hr over a rolling window of logs/trajectories with code-base access, checks whether users got stuck, and opens a PR or fires a Slack alert for critical issues — PR-ready in ~half an hour. (06:50-07:42, 09:07-09:47)
- The drafted PR carries a short description, metadata, mermaid/ASCII diagrams, and sometimes HTML artifacts for an at-a-glance view; a static-analysis pass gives quick critical-vs-heads-up feedback. (09:47-10:31)
- Separate fresh-context review agent: because agents are "eager to send the PR" and biased toward their own fix, a distinct agent with fresh context criticizes and scores each PR from a different angle against one question — root cause or just the symptom? — runs focused tests, and requests changes or closes it, "not biased of the problem itself." (06:50-07:42, 10:31-10:53, 11:52-12:22)
- Volume argument for keeping humans thin: the PR agent + review agent "send 10 times more PRs than the three of us every day," so you need a clean system so the human is not the bottleneck. The stance on human-in-the-loop: "close the loop first" (make yourself the bottleneck), then you can remove yourself easily. (10:53-11:52)
- A computer-use agent adds the user's perspective that logs/code miss — it logs in and simulates the customer to catch UI failures; a product-specific skill that knows the site's DOM is much faster than a generic Codex-driven browser (but token-heavy). (16:12-17:43)
- Meta-harness principle: give every operating agent all the context a human would need — trajectories, metrics, database, UI — so its output "depends on the real problem"; e.g. the computer-use agent, on finding a problem, should analyze trajectories and check the database. "It's not the model alone; you need to build the harness around it that watches itself, understands, improves." (17:43-19:00)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Operate Agent Products as the Missing Post-Launch Layer](operate-agent-products-as-the-missing-post-launch-layer.md)
- [Score Every Production Conversation to Judge Agent Health](score-every-production-conversation-to-judge-agent-health.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Use Reviewer and Approver Roles To Make Agent Workflows Reliable](use-reviewer-and-approver-roles-to-make-agent-workflows-reliable.md)
- [Observability-to-PR agents turn incidents into reviewable fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)

Sources:
- [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](../sources/20260705_kZsf_Sfm7RU.md), 05:48-12:22, 16:12-19:00
