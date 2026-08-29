# Make the Triage Agent Ask the Reporter for the Missing Context

Summary: The standard handling for an under-specified issue is to route it away from the agent, because an agent given a vague problem will fix something regardless. Warp's repo agents take a third path: on intake, the agent researches the codebase and repo context, and when the request is still too abstract to act on it asks the reporter questions. This converts under-specification from a dispatch filter into a resolvable state, and it does so at the only moment when the person who has the missing context is still paying attention.

Use when:
- Building automatic intake for issues, bug reports, feature requests, or support tickets that agents will later act on.
- An autonomous pipeline is producing plausible-looking fixes for problems nobody stated precisely.
- Deciding whether a triage agent should classify, escalate, or interrogate.
- A backlog is full of reports that cannot be worked because the details were never captured.

Details:
- **The intake behavior, in full.** "If you file a new issue with a bug report or a feature request, an agent will kick in and start to triage the issue automatically. It'll do research across the code base and context in the repo to understand what you're trying to propose. It might ask you questions if it feels like your original query was a little abstract to get more information." Two steps in order: exhaust the context the repository already holds, then ask the human only for what is genuinely not recoverable from it. ([Abdalla](../sources/20260822_L173Z8DpaJg.md), 11:33-12:00)
- **The problem it targets, named as structural rather than incidental.** It does "the work that's historically been very hard for open source, which is somebody has a problem or a bug that they want fixed. They don't give you enough details, and it's hard to get to the clarity that you need to drive the work forward." The scarce thing is not the reporter's willingness but the maintainer's capacity to run that clarification round on every report. (12:00-12:10)
- **Why intake is the right place, rather than dispatch.** The reporter's context decays: they filed because they hit the problem, and that is the moment they can still reproduce it, name the version, and say what they expected. Asking three days later, after a triage queue, asks a colder person. The wiki records the same decay argument for [support-led coding agents](support-led-coding-agents-exploit-fresh-customer-context.md), where troubleshooting context and logs go stale while a ticket waits.
- **How this changes the wiki's existing rule rather than contradicting it.** [Gate Autonomous Fixes on Problem Specificity](gate-autonomous-fixes-on-problem-specificity.md) is right that an agent handed a vague problem will produce a random fix, and its remedy is to route under-specified problems away from the agent. That remedy treats specificity as a fixed property of the report. Warp's version treats it as a state the system can move: the same gate still applies, but a report that fails it now enters a clarification loop instead of a dead-end queue. The combination is the useful form — measure specificity, and give the failing branch somewhere to go.
- **What the downstream steps then get.** Once triage has produced a specific problem, the same agents "draft initial specifications and work for tasks, do implementation, and provide a review gate." Clarification at intake is what makes the specification worth drafting; the wiki's evidence that under-specification is the canonical degenerate case — a spec whose tests expect things "never actually requested" — comes from task curation for RL and evals ([Accept Agentic Training Tasks by Clean Failures, Not Ambiguous Specs](accept-agentic-tasks-by-clean-failures-not-ambiguous-specs.md)), but the failure is the same one in a repo. (12:10-12:25)
- **The claimed second-order effect.** "Agents providing structure and context… meant that anyone could participate in translating their intent into implementation. And oftentimes the people who have really interesting intents and goals are the ones who are using software in interesting ways. And it's not always the person that's building it." The asker-of-questions is doing enablement work: it lets someone with domain knowledge and no repo knowledge file something actionable. Abdalla scopes her own example immediately — Warp is developers building for developers, "a really unique niche" — and generalizes anyway to non-developer users, which is the least supported claim in the talk. (13:03-14:21)
- **The failure modes nobody measured.** An agent that asks questions can ask too many and become the friction it replaced; can ask the wrong ones and anchor the reporter on a misreading; and can be answered by another agent, producing a clarification round with no human context in it at all. The source reports none of these, gives no abandonment rate for issues that received questions, and does not say what happens to an issue whose reporter never answers.

Related topics:
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Gate Autonomous Fixes on Problem Specificity](gate-autonomous-fixes-on-problem-specificity.md)
- [Accept Agentic Training Tasks by Clean Failures, Not Ambiguous Specs](accept-agentic-tasks-by-clean-failures-not-ambiguous-specs.md)
- [Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)
- [Support-led Coding Agents Exploit Fresh Customer Context](support-led-coding-agents-exploit-fresh-customer-context.md)
- [AI-Generated Security Reports Need Maintainer Triage](ai-generated-security-reports-need-maintainer-triage.md)
- [Put an Agent Approval Gate in Front of Maintainer Attention](put-an-agent-approval-gate-in-front-of-maintainer-attention.md)

Sources:
- [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../sources/20260822_L173Z8DpaJg.md), 11:33-12:25, 13:03-14:21
