# Feedback turns coding-agent loops into prompt and skill improvement cycles

Summary: Coding-agent loops improve when each run produces feedback that can be folded into the next prompt, skill, or workflow rule. The loop should expose what the agent did, what failed, and what should be changed before rerunning.

Use when:
- You are turning ad hoc coding-agent usage into a reusable skill or prompt.
- You need local, fast feedback before trusting a loop on production work.

Details:
- After a loop run, inspect the generated code and process, reset if necessary, then improve the prompt or skill before the next run. 33:33-35:10
- A simple command-line tool with clear tests is a good loop target because it is easy to tell whether the agent's output works. 40:35-40:50
- AI-generated feedback can help improve AI-generated work: the speaker describes using audience-simulation personas and a second agent to critique content, surface improvements, and feed them back into the skill. 39:35-41:04
- Skills can absorb process learnings over time; the speaker asks a newsletter-writing skill to update itself with lessons from each session. 06:57-07:08

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)

Sources:
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md), 06:57-07:08, 33:33-35:10, 39:35-41:04
