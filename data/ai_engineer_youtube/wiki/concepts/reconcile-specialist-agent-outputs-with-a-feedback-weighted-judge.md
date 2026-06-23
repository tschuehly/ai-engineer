# Reconcile Specialist Agent Outputs With a Feedback-Weighted Judge

Summary: One agent handed many tasks gets overwhelmed and silently drops some, so split the work across specialist agents and add a judge node that recombines their heterogeneous outputs into one coherent result. Make the judge useful by weighting suggestions against organizational signals — PR history, uploaded guidelines, and a running tally of which suggestions developers accept or reject.

Use when:
- A single broad agent loses track of part of its task (e.g. given four tasks it does well on two and drops the others).
- Several specialist agents each return their own findings and you need them combined and ranked, not concatenated.
- Designing a code-review or analysis pipeline whose suggestions should reflect a team's conventions and past decisions.

Details:
- Single-agent overload failure: as context grows, teams try one agent for everything (testing, review, security); the agent gets overwhelmed and loses the original task — given four tasks it focuses on two while the others "get lost in the middle." The remedy is a mixture of small expert agents, each strong at one task. (12:25-14:05)
- Judge agent: when each specialist returns its own result, a judge agent combines them and checks they cohere — the vacation example is a hotel in Greece and a flight Amsterdam→Portugal that only make sense once a judge reconciles them — and refines by relevance ("out of the 10 things, how many actually make sense for you"). This reconciles *heterogeneous* specialist outputs, distinct from picking the best of several *parallel attempts* at the same task. (14:05-15:56)
- Qodo's live architecture: a context collector gathers from PRs, the context engine, and tools, then bifurcates the context to specialist agents (security flaws, code differences, Jira issues) rather than reviewing directly; a judge node recombines and weighs the results against PR history. (14:44-15:56)
- Plumbing: LangChain at the bottom for inter-agent communication — it collects responses and stuffs them into the next agent's prompt, and a dedicated agent collects results and writes a refined prompt for the next agent. (16:32-17:08)
- Feedback-weighted calibration, three signals: (1) PR history — index all PRs, find similar past changes and how reviewers/developers commented, and feed that context twice, to the sub-agents and to the judge; (2) uploaded guidelines — architects and compliance staff upload architecture/compliance guidelines through a web portal that an agent validates code against, mapping old senior-engineer/security/auditor roles onto agents; (3) accept/reject weighting — every accepted suggestion gains weight for the next run and every rejection loses weight ("it's all about indexing and managing weights"). (17:32-25:00)
- Rules vs bugs caveat: because "it happened in history doesn't mean it's good" (e.g. hard-coded API keys appearing in past PRs), a "rule" is highlighted regardless of accept history, while a "bug" is weighted by whether reviewers repeatedly agree but don't implement. (25:44-26:08)
- Scoped-context tradeoff: each specialist sees only its slice and runs autonomously without the full picture, which works for simple checks (linting, tests) but raises holistic-architecture concerns where "everything is a balance"; the judge plus multi-angle weighting is the reconciliation mechanism, not a guarantee.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Role-specialized agent systems beat one giant coding agent](role-specialized-agent-systems-beat-one-giant-coding-agent.md)
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)
- [Split Discovery and Validation Across Reasoning and Deterministic Models](split-discovery-and-validation-across-reasoning-and-deterministic-models.md)
- [Context quality determines AI code review trust](context-quality-determines-ai-code-review-trust.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Curate Context Strategically Because Models Drop the Middle](curate-context-strategically-because-models-drop-the-middle.md)

Sources:
- [Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo](../sources/20260608_EcqMYoIV57A.md), 12:25-26:08
