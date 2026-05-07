# Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands

Source: [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=o_hhkJtlbSs)
Uploaded: 2025-07-25
Transcript: `raw/20250725_o_hhkJtlbSs/o_hhkJtlbSs.en-orig.vtt`

## Summary

Robert Brennan frames coding agents as tool-using development loops that are strong at inner-loop implementation but still need human judgment for product goals, architecture, review, and ownership. The talk extracts practical OpenHands patterns: give agents editor, terminal, browser, and sandbox surfaces; start with small verifiable chores; scope credentials tightly; discard bad generated work early; and keep human accountability on agent-created pull requests.

## Extracted Concepts

- [Start Coding Agents With Small Verifiable Chores](../concepts/start-coding-agents-with-small-verifiable-chores.md) - supports choosing low-risk, single-commit, testable work before expanding agent autonomy.
- [Human Ownership Keeps Agent Pull Requests From Bypassing Review](../concepts/human-ownership-keeps-agent-pull-requests-from-bypassing-review.md) - shows why agent-created PRs need an accountable human owner and ordinary review routing.
- [Unified Coding-Agent Harnesses Combine Models, Tools, Environments, and Safety](../concepts/unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md) - adds OpenHands evidence for editor, terminal, browser, and sandbox surfaces.
- [Give Code-Executing Agents Isolated Computers](../concepts/give-code-executing-agents-isolated-computers.md) - adds Docker-container isolation and least-privilege credential guidance.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Security](../topics/security.md)
- [Workflows](../topics/workflows.md)

## Notes

- Brennan says coding agents are best understood as loops between an LLM and the external world, repeatedly asking what action gets one step closer to the goal, then feeding file, command, or webpage output back into the model. (03:50-04:30)
- The agent harness is more than chat: OpenHands-style agents need code-editing, terminal, and browser tools; efficient editors use find-and-replace or diff-based edits rather than full-file rewrites. (02:11-06:40)
- Browser context should avoid dumping raw HTML when possible; the talk reports better results from accessibility trees, Markdown conversions, scrolling, or screenshots with labeled nodes. (05:52-06:38)
- Sandboxing is required because agents can run autonomously for minutes; OpenHands runs agents in Docker containers by default, and third-party API tokens should be tightly scoped by least privilege. (06:44-07:23)
- Good starter tasks are small single-commit chores with a clear definition of done, such as passing tests, resolved merge conflicts, lint errors, database migrations, failing tests, and test coverage expansion. (07:31-08:12, 14:48-15:45)
- Prompting should include desired frameworks, test-driven-development strategy, and relevant files or function names so the agent spends less time exploring and fewer tokens guessing. (08:39-09:21)
- Bad or far-off generated work should often be discarded and restarted from a better prompt rather than endlessly salvaged, because generated code is cheap and stale conversational context can anchor the next attempt. (09:24-10:31)
- Production code still needs human review; automatically merging agent output can grow duplicate code and technical debt quickly, and teams should run or validate agent code locally or in ephemeral environments. (10:34-11:15)
- Early OpenHands PRs owned by the bot caused accountability failures: the triggering human could approve their own agent's PR, and agent PRs could languish because no person clearly owned failing tests or follow-up. (11:32-12:09)
