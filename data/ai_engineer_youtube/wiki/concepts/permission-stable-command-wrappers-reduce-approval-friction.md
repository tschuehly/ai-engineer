# Permission-stable command wrappers reduce approval friction

Summary: Agent harnesses that require per-command approval can reduce repeated prompts by keeping the executed command text stable and moving variable inputs into files. This improves ergonomics, but it makes the wrapper a security-sensitive boundary because the approved command can still execute different agent tasks based on file contents.

Use when:
- A shell-invoked agent helper receives different task text on each run.
- Approval systems key decisions on command shape or arguments.
- A wrapper needs to support repeated subagent calls without asking the user to approve every query.

Details:
- The Codex CLI demo writes the subagent name and user query to files, then runs the same wrapper command each time. 09:08-09:22
- Passing the agent name and query as command arguments would make the command look different on every invocation, causing repeated approval prompts. 09:22-10:03
- The wrapper also has to account for sandbox constraints: a child Codex process may need workspace write access for output files, access to copied Codex home credentials, and disabled rollout logging when parent sandboxing blocks writes outside the workspace. 03:26-04:51, 10:10-10:42
- The security tradeoff should be assessed explicitly: in a proprietary codebase, the child agent has private data access, can change state, and can communicate externally to the model API, so convenience does not remove risk. 05:00-06:15
- **Why the friction this page routes around is worth engineering against: it degrades the gate itself.** OpenAI's Codex team observed that repeated prompts do not just annoy — "we saw people would just start clicking yes," and "people started to just use full access mode more" ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 11:59-12:22). That reframes a wrapper trick as a safety measure rather than an ergonomics one, since every avoidable prompt spends attention that the unavoidable ones need. It also marks the limit of the technique: a stable command string reduces prompt *count* without changing what the approval covers, which is exactly the gap [Human approval can hide tool-description and parameter risk](human-approval-can-hide-tool-description-and-parameter-risk.md) describes — the user approves the same wrapper while the file behind it says something new each time.
- **The one context where the prompt is not friction but a hang.** Coyle lists "always have interactive modes in a pipeline" as the named anti-pattern for running a coding agent in CI, since interactive mode means the agent "will stop and ask you, 'You want to do this? You want to do that? Can I have permission for that?'" with nobody there to answer, and "there are ways to set it up so that it'll just run straight through." That is worth separating from this page's problem: a wrapper reduces prompt count in an attended session, while a pipeline needs the prompt path gone entirely — which means the approval decision has to be made in advance, in configuration, rather than deferred to a person who is not present. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 18:09-18:34)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md)
- [Shell-wrapped subagents can retrofit harness capabilities](shell-wrapped-subagents-can-retrofit-harness-capabilities.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)
- [Human approval can hide tool-description and parameter risk](human-approval-can-hide-tool-description-and-parameter-risk.md)
- [Escalate Risky Actions to a Read-Only Review Subagent](escalate-risky-actions-to-a-read-only-review-subagent.md)
- [Read a Certification Blueprint as a Map of Production Anti-Patterns](read-a-certification-blueprint-as-a-map-of-production-anti-patterns.md)

Sources:
- [Hacking Subagents Into Codex CLI - Brian John, Betterup](../sources/20251124_5eJqXtevlXg.md), 03:26-06:15, 09:08-10:42
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 11:59-12:22
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 18:09-18:34
