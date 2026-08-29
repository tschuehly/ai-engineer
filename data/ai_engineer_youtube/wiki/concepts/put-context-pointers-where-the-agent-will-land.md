# Put Context Pointers Where the Agent Will Land

Summary: Treat the codebase itself as the mechanism that injects context at the moment it is needed: put the pointer to a runbook or design doc in the comments of the code an agent will grep into, so that arriving anywhere in the repo hands the agent its own next hop.

Use when:
- Deciding where documentation should live so an agent finds it without being told.
- Structuring a repo so the first prompt does not have to enumerate what matters.
- Reviewing why an agent keeps reimplementing behavior that is already documented somewhere.

Details:
- The framing, which Khandelwal calls smart prompt injection: "You want to treat your entire code base as one way to that so that you're able to like smartly prompt inject the model with just the right context at just the right time. Without you needing to do it… I've set it off on this task. It has like a map of how to find the things it needs at the time it needs it." ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 07:25-07:48)
- The worked instance: "If it's looking at some code and that code has, let's say some documentation, the documentation needs to live in the comments. So, if it ever grabbed into that code, it reads the comment, goes to that file, finds all the information about it." Restated in the Q&A for runbooks specifically: "make sure the runbook is reflected in the comments so that… if somehow the agent figures its way into like [grepping] into the code base and find that file, it knows I need to go look at this for like all the description of how this is relevant." (07:48-08:01, 15:09-15:27)
- The design rule underneath is about *placement*, not about volume: the pointer has to sit where retrieval actually terminates. An agent's entry point into a repo is wherever its search matched, which is a source file — not a docs directory, not a wiki, and not the repo context file it read on turn one. A doc that is only reachable if the agent already knows to look for it is not reachable.
- This is the counterpart to a thin repo index. The index handles "where do I start"; comment-level pointers handle "I have landed somewhere unexpected and need to know what governs this code." Together they let the always-loaded layer stay small without stranding the deferred material. See [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md).
- It also gives a specific answer to the codebase-legibility question the wiki records more abstractly. [Agent-Legible Codebases Reduce Generated-Code Entropy](agent-legible-codebases-reduce-generated-code-entropy.md) argues that structure should make the intended path visible and that agents fall back to trial-and-error when required information is missing from the codebase; this names one cheap, mechanical way to make it present — a comment whose only job is to be a link.
- Consequence for review: pointer comments are load-bearing context, so moving or renaming the file they reference silently breaks the retrieval path with no test failure. This is a maintenance cost the talk does not price, and it is the obvious thing to lint for (do referenced paths exist?).
- Caveat: the whole mechanism is described in two sentences with no example file, no convention for the comment's format, and no measurement of whether agents followed the pointers. It rests on the agent choosing to read and act on a comment it happened to load, which is probabilistic; nothing here is enforcement.

- **The other place an agent reliably lands is the answer it just received.** This page puts pointers in the code an agent will grep into; a context service can put them in its own responses. In Werry's demo the returned plan carries the PRs, Slack threads, Notion pages, and architecture documents it drew on, "and then Claude knows exactly where to jump to next if it needs to elaborate on that context." Same mechanism — a pointer waiting at a location the agent is guaranteed to visit — applied to the response channel rather than the repository. The two compose: repository breadcrumbs cover cold starts, response citations cover continuations. ([Werry](../sources/20260827_qdAkxLoYNI8.md), 10:35-11:13)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md)
- [Measure First-Prompt Context Burn to Test Progressive Disclosure](measure-first-prompt-context-burn-to-test-progressive-disclosure.md)
- [Agent-Legible Codebases Reduce Generated-Code Entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [Model-Shaped Codebase Architecture for Coding Agents](model-shaped-codebase-architecture-for-coding-agents.md)
- [Use Repository Instructions To Ground Coding Agents](use-repository-instructions-to-ground-coding-agents.md)
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Attach Sources as Both a Correction Surface and a Continuation Pointer](attach-sources-as-a-correction-surface-and-a-continuation-pointer.md)

Sources:
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 07:25-08:01, 15:09-15:27
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 10:35-11:13
