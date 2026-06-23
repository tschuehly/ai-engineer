# Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff

Source: [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](https://www.youtube.com/watch?v=pmoDeA3RBZY)
Uploaded: 2026-06-05
Transcript: `raw/20260605_pmoDeA3RBZY/pmoDeA3RBZY.en-orig.vtt`

## Summary

Vincent Koc, a core maintainer of the open-source OpenClaw project (his day job is in evals; co-maintainer Peter Steinberger's is at OpenAI), describes the operating model behind shipping at extreme velocity — peak ~800 commits/day for the project, a personal peak of close to 3,000 commits in one day, and a "great refactor" of 2,700 commits / nearly a million lines / 82% of the core codebase touched in one night that shipped a plugin architecture by morning. The durable content is not the headline numbers but the engineering practice underneath them: organizing 15-20 parallel coding sessions into typed "swim lanes" with per-lane supervision, supervising agents by *reading their reasoning* to catch when one is "bullshitting," knowing when to nuke a session versus let it run, a continuous skill-improvement loop where the agent reads its own session logs, and a practical caveat that heavy git-worktree use at this scale can nuke your machine. The framing: 2025 was about token maxing; 2026 is about not wasting tokens — token efficiency with the agent in the loop, where the bottleneck shifts from typing code to taste and operator attention.

## Extracted Concepts

- [Run Parallel Coding Sessions as Typed Swim Lanes](../concepts/run-parallel-coding-sessions-as-typed-swim-lanes.md) - the factory operating model: 15-20 concurrent sessions split by work type, supervised differently per lane, scaled up and down.
- [Read an Agent's Reasoning to Catch It Bullshitting](../concepts/read-an-agents-reasoning-to-catch-it-bullshitting.md) - supervise by *how* an agent explains itself, not just what it does; nuke the session when it waffles.
- [Mine Agent Conversation History to Generate Missing Skills](../concepts/mine-agent-conversation-history-to-generate-missing-skills.md) - corroborates with a continuous "go read your own session logs and improve the skill" loop.
- [Isolate Parallel Coding Work With Project Worktrees](../concepts/isolate-parallel-coding-work-with-project-worktrees.md) - qualifies the pattern with a scaling caveat and the clone-the-repo-N-times alternative.
- [Human Taste Limits Fully Dark Coding Factories](../concepts/human-taste-limits-fully-dark-coding-factories.md) - corroborates that the bottleneck becomes taste and curation ("who do I say no to").

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

## Notes

- Velocity framing and external corroboration: this is "very similar to the ChatGPT era" where everyone secretly used it while denying it; organizations are now doing the same with autonomous agents at scale. Examples cited: Anthropic building a new C compiler with agents, Spotify saying they no longer write code by hand, and Steve Yegge pushing ~50 PRs/day solo as a self-described "vibe maintainer." OpenClaw at peak did ~800 commits/day across ~10-15 core maintainers who all have day jobs. (03:46-04:42)
- The "factory" frame is an industrial-revolution analogy: handlooms → centralized mills; engineers stop being the weaver's hands and become factory managers, and the bottleneck shifts from typing code to taste. (02:18-03:38)
- Swim lanes in practice: at an Nvidia hack session ("Nemo Claw"), Vincent ran ~10-15 foreground sessions and Peter ~15 (VPN'd into a Mac Studio at home); collectively, with subagents, up to 60-70 agents. (06:13-07:03)
- The "great refactor" was triggered accidentally at 2 a.m. when one maintainer moved folders (relocating MS Teams/Slack channel code); they decided to refactor the whole codebase into a plugin architecture so a provider (OpenAI, Mistral, Anthropic) could own its own provider plugin separate from everything else. Result: 2,700 commits, ~1M lines changed, 82% of the core codebase touched, plugins shipped by morning. (07:33-08:44)
- Over-fit tests as an accidental refactor safety net: "awful unit tests that AI code loves to generate" had over-fit to the old code; when everything was ripped out, those tests staying green were the signal that the rewrite was "somewhat close." Normally an over-fitting smell, here a regression anchor. (09:04-09:18)
- "In harness we trust": no elaborate process, no plan mode or spec mode — just have a conversation with the agent and work through it. The one complicated thing he adopted (and regrets) is git worktrees; the simpler path others use is cloning the repo ~10 times and pointing a session at each clone. (10:51-11:57)
- Reading reasoning tokens (the headline skill): like the Matrix "woman in red dress" scene, you build a relationship where you can "feel the reasoning tokens." A lane sounds "off" not because of *what* it's doing but *how* it explains itself — waffling, not making sense, not seeming to know what it's doing — exactly like a person who starts bullshitting. The response: nuke the session, hand that code section to another maintainer, or return days later. This intuition came from a year of high-volume "token maxing." (12:05-13:17)
- Agent development environment (ADE): skills are stored as `.skills` (analogous to dotfiles), open-sourced on GitHub. A "Go Codex" skill he's used for ~2 weeks goes through his Codex session logs, reads them, and makes improvements to the skill; he then deploys updated skills into the open core / personal environment. Tooling mentioned (auto-caption, names approximate): a skills "gem" like Geppetto (he contributes) and `vercel.skills.sh`. (13:20-14:21)
- Managing the PR/issue firehose: ~60k PRs/issues. Every new maintainer tries to "solve" it; his flavor was a semantic graph / vector embedding over the entire GitHub backlog to dedupe (one PR had ~106 edges). Convergent pressure across many duplicate issues is a prioritization signal ("if enough clankers decided it's a big problem, maybe I should address it") — not a roadmap, but a way to decide what to feed the lanes. (14:24-15:19)
- Evals for the refactor: after refactoring, they built a "fake Slack" with both synthetic and real models to run evaluation loops checking each provider and channel works. (15:21-15:36)
- "How do you manage 10+ agents?" → "How do you manage 10+ staff?" The soft skills of management transfer; it's no longer about the model or the agent, it's about the process. Closing line: 2025 was token maxing, 2026 is token efficiency / agent in the loop. (15:38-16:25)
- Caveat: most proper nouns past the first mention are auto-caption ("doc factories" = dark factories; "clan car" = clanker; "hardness" = harness; Geppetto / vercel.skills.sh approximate). The headline numbers are corroborated by the video description.
