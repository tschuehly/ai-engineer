# Manual migration seeds teach agents the hidden constraints

Summary: For tangled refactors, one hand-done migration can expose invariants, dependency seams, and failure modes that code search or broad context stuffing will miss. The resulting pull request can become a concrete seed example for later agent research and planning.

Use when:
- A large migration crosses business logic, authorization, data models, or other deeply coupled concerns.
- Agent analysis stalls, preserves legacy patterns, or cannot distinguish desired behavior from accidental structure.

Details:
- In Nations' Netflix authorization example, legacy permission checks, role assumptions, and auth calls were woven through business logic and hundreds of files, so direct agent refactoring stalled or recreated old logic with the new system. (08:29-09:39)
- When accidental complexity is deeply tangled, even broad code context may not reveal a clean path because the model cannot reliably see where business logic ends and infrastructure logic begins. (09:21-09:39)
- The team had to perform an initial migration manually, reading dependencies and observing what broke, to uncover hidden constraints, invariants, and affected services. (14:29-15:09)
- Feeding that manual migration PR into the research process gave the agent an example of a clean migration, but each subsequent entity still required interrogation, extra context, validation, and edge-case discovery. (15:09-15:46)
- The broader lesson is that research-plan-implement workflows need earned human understanding when the system is too tangled for prompts, models, or specs alone to safely solve. (15:52-16:09)
- **The constraint that a seed example cannot supply, named as the residual hard part.** After describing an unattended weekend port of a few hundred thousand lines, Krieger locates the difficulty somewhere the model does not help: "the hardest part is always finding the boundary around where you can start doing it incrementally without trying to boil the whole ocean and like swap it overnight." A hand-done migration exposes invariants and seams within a slice; it does not tell you where to cut the system so the migration can ship in slices at all. The complementary substitute he offers for the invariants themselves is captured production behavior rather than a hand-written example. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 05:33-06:28)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use research-plan-implement loops for coding agents](use-research-plan-implement-loops-for-coding-agents.md)
- [Agent-legible codebases reduce generated-code entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [Decompose large refactors into dependency-aware agent batches](decompose-large-refactors-into-dependency-aware-agent-batches.md)
- [Validate a Cross-Language Port Against Production Runtime Data](validate-a-cross-language-port-against-production-runtime-data.md)

Sources:
- [The Infinite Software Crisis - Jake Nations, Netflix](../sources/20251220_eIoohUmYpGI.md), 08:29-09:39, 14:29-16:09
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 05:33-06:28
