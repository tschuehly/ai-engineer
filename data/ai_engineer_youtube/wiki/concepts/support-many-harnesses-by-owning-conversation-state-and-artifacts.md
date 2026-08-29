# Support Many Harnesses by Owning Conversation State and Artifacts

Summary: Letting users bring their own agent harness is not a feature you add by accepting more binaries — done that way it fragments the product, because each harness then carries its own notion of session, output, and history. The move that makes multi-harness support survivable is to pull two things below the harness line and own them at the platform: conversation state that can be stored and rehydrated, and artifacts that are structured identically no matter which harness produced them. What stays above the line, and stays different, is behavior.

Use when:
- A platform team is deciding whether to standardize on one coding-agent harness or accept several.
- Users are asking for Claude Code, Codex, and a homegrown harness on the same infrastructure and you need to know what that costs.
- Deciding which parts of an agent runtime belong to the vendor of the harness and which belong to you.
- A "bring your own agent" roadmap item needs a definition of done beyond "it launches."

Details:
- **Preference is the requirement, and it is treated as substantive rather than cosmetic.** Abdalla polls the room live — "who here has a preference for Claude Code as a harness locally? Codex? Something else entirely?" — and reads the answer as "so much diversity in the room." The general claim behind it is that a tool used daily "becomes like a part of how you think and build," so the harness sits alongside shell and language as something a developer has already chosen before meeting your platform. ([Abdalla](../sources/20260822_L173Z8DpaJg.md), 01:37-01:57, 05:07-05:28)
- **The failure mode, named as a property of the naive implementation.** "Flexibility isn't something that you just [can] be crammed into a platform because the real risk you run if you cram it in is that it becomes fragmented. Your experience with working with Claude is different from working with Codex versus a custom harness that you might have." The point is not that the harnesses differ — they do, and that is why users chose them — but that the *platform* differs when you support them by delegation. (05:28-05:52)
- **The fix, stated as a containment boundary.** "One of the key properties is making sure that the platform provides structure and guardrails around the harness so that the experience is consistent." Concretely: "harnesses can interact with all of the platform native experiences. So just being able to store conversation state and rehydrate it, being able to interact with the artifacts and outputs that are produced by agents, whether they're PRs, issues, new files that are generated. All of that should kind of be structured the same way." (05:52-06:24)
- **Why those two and not others.** Both are the things a downstream consumer indexes on. A review surface, a session-resume feature, and a cross-surface handoff all read state and artifacts, and none of them read the harness's internal loop. Owning exactly the two consumable outputs is what lets the rest stay heterogeneous — which is the same shape as the wiki's [agent/environment/session decomposition](model-a-managed-agent-as-agent-environment-session.md), with the harness demoted from the definition of the agent to a swappable executor inside it.
- **The consistency being promised is narrower than it sounds, and the wiki has the evidence for why.** Storing state uniformly does not make behavior uniform: Hylak's report is that switching to a different CLI harness leaves "80% of your evals" meaningless, because a suite encodes one harness's tools and interaction shape ([A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)). Read together, a multi-harness platform is offering a consistent *record* of work and an inconsistent *performance* of it. That is a defensible product, but it means the platform cannot make quality claims that hold across harnesses, and any eval the platform owns has to be run per harness or scoped to the artifact layer.
- **What this leaves unresolved in the source.** No account is given of the harness-specific parts that resist normalization — permission prompts, compaction behavior, tool-call formats, hooks — nor of what happens when a harness produces an artifact the platform has no schema for, nor whether rehydrated state transfers *across* harnesses (resume a Codex session in Claude Code) or only within one. The last is the interesting question, and the talk does not claim it. Nothing is measured: no comparison against a single-harness platform, no cost for the normalization layer.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Model a Managed Agent as Agent, Environment, and Session](model-a-managed-agent-as-agent-environment-session.md)
- [A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)
- [Unified Coding-Agent Harnesses Combine Models, Tools, Environments, and Safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)
- [Use stable agent harnesses as model-evolution boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md)
- [Make One Agent Session Reachable From Every Interface](make-one-agent-session-reachable-from-every-interface.md)
- [Decouple Agent Harnesses From Enterprise Data Layers](decouple-agent-harnesses-from-enterprise-data-layers.md)
- [Ship Managed and Self-Hosted Sandboxes Because Serious Teams Bring Their Own Infrastructure](ship-managed-and-self-hosted-sandboxes-because-serious-teams-bring-their-own-infrastructure.md)

Sources:
- [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../sources/20260822_L173Z8DpaJg.md), 01:37-01:57, 05:07-06:24
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 04:23-04:39
