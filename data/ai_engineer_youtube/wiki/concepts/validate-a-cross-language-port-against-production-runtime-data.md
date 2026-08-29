# Validate a Cross-Language Port Against Production Runtime Data

Summary: A model-driven port of a large codebase to another language is now tractable as an unattended churn loop, but the source code alone is a weak oracle for whether the port is correct. Capture what the system actually does in production — the types and values really flowing through it — and use that as the check, alongside segmented traffic tests. The remaining hard problem is not translation but finding an incremental cutover boundary.

Use when:
- Scoping a language migration, runtime swap, or cross-compilation that an agent would execute.
- Deciding what a port's verification loop should compare against.
- Judging whether a "port the whole thing" ask is unreasonable in the useful sense or in the reckless sense.

Details:
- The unattended loop, run over a weekend on "a couple hundred thousands of lines" of Python moved to TypeScript: "I basically created this dynamic workflow setup and over the weekend had it port the whole thing, verify it, double-check it, then read both code... basically churn and churn and churn and then came back Monday to a completed workflow that was a ported version of that thing." The loop's distinguishing step is reading *both* codebases, which makes the original the reference rather than a starting point. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 04:31-05:14)
- The motive is worth copying: the port was not for code quality but for a downstream capability — "Claude Code had figured out a better deployment story with Bun." Ports justified by tooling or deployment have a concrete acceptance test; ports justified by taste do not. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 04:31-04:38)
- The production-data oracle, drawn from Instagram's Python 3 migration and its MonkeyType tool: "we captured runtime type... the types that were actually getting used in production and then map those back to the types in the code base." Generalized to model-driven work: "if you're doing conversion or cross compiling using LLMs, you can also lean on production data a lot more or run sort of like segmented tests." Runtime capture supplies the behavior the static source underdetermines, which is exactly where a plausible-looking port silently diverges. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 05:33-06:19)
- The residual hard part is scoping, not generation: "the hardest part is always finding the boundary around where you can start doing it incrementally without trying to boil the whole ocean and swap it overnight." A model that can produce the whole port in one pass does not tell you where to cut the system so the port can ship in pieces. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 06:20-06:28)
- The tractability claim is time-indexed and stated as such: "if I put on my 2010s engineering hat or even my early 2020s, that's a dumb idea. Who would ever port... a couple hundred thousands of lines of code. But I was like, I think this is doable now." Treat the size threshold as moving, not fixed. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 04:38-04:52)
- Limits: one self-reported weekend with no verification result, no test outcome, no deployment confirmation, and no description of the "dynamic workflow setup" beyond port/verify/double-check/churn. The interviewer raises the harder case — porting a *product* rather than a compiler or runtime, which has "lots of tests" — and the answer is the MonkeyType precedent rather than a completed product port. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 05:16-05:33)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use Playbooks for Repetitive Codebase Migrations](use-playbooks-for-repetitive-codebase-migrations.md)
- [Run Verify-Fix-Review Loops for Agentic Refactors](run-verify-fix-review-loops-for-agentic-refactors.md)
- [Manual migration seeds teach agents the hidden constraints](manual-migration-seeds-teach-agents-the-hidden-constraints.md)
- [Audit a Refactor Against Having Waited for Better Models](audit-a-refactor-against-having-waited-for-better-models.md)
- [Pre-Measure Everything and Build Runtime Knobs Before You Need Them](pre-measure-everything-and-build-runtime-knobs-before-you-need-them.md)

Sources:
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 04:17-06:31
