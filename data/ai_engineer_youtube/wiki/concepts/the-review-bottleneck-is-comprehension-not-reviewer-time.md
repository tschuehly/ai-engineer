# The Review Bottleneck Is Comprehension, Not Reviewer Time

Summary: When agent output outruns review, the instinct is to schedule more review hours — but the binding constraint is whether a human can hold the change in their head at all, and no amount of carved-out time fixes a 2,000-line diff that "looks like code to me." The remedy is to change the artifact, not the calendar: ship an explanation of intent and tradeoffs alongside the diff, and let machine verification carry the correctness half.

Use when:
- A team is trying to fix review lag by adding reviewers, review time, or review SLAs.
- Deciding what an agent-written change should present to a human beyond the diff.
- Arguing about whether "we just need to review faster" is a real plan.

Details:
- The distinction, stated by someone running it at scale: still bottlenecked on review "especially for things that are touching some architecture pieces," but "it's actually more subtle than just being bottlenecked on review, cuz that's — okay, we can carve out time differently. It's like bottlenecked on human ability to even fully conceptualize what we're doing." Time is reallocatable; comprehension is not. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 10:11-10:30)
- The failure it produces is not a missed bug but a null review. "You would send somebody a PR, and then they'd be like, I don't know, man. This is like 2,000 lines of code. It looks like code to me." A reviewer who cannot form a model of the change approves it or stalls; neither is review. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 10:36-10:44)
- The remedy is an artifact that travels with the change: "here's the explanation. Here's the intention of the change. Here's the trade-offs that were made" — Anthropic shipped Claude Code artifacts partly for this. The split of labour is explicit: "the code is ultimately verifiable using some things, but actually discussing intent and trade-offs, and then measuring in production." ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 10:30-11:08)
- What an honest senior reviewer actually does once the diff exceeds comprehension: "I wish I could say I reviewed every line of code. I definitely do not. I actually talk to Claude about the code and say, these are the questions that I would have. Can you go investigate it?" — described as "Claude-powered code review, but still human-driven," reserved for important changes. The human contributes the *questions*, which is the part that requires the model of the system. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 11:08-11:20)
- The relief valve is routing, not more review: cosmetic visual changes get fix-forward rather than pre-merge scrutiny, which conserves comprehension for the architecture-touching changes that consume it. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 11:21-11:29)
- Consequence for tool builders: a review tool that only makes diffs faster to read is optimizing the wrong resource. The thing to compress is the size of the mental model the reviewer must build, which is why intent, tradeoffs, and a production measurement plan are the load-bearing artifacts.
- Limits: an unmeasured claim from one interview. No review-time data, no defect-escape rate, and no evidence that intent artifacts produce better catches than diffs — including the obvious risk that an agent-authored explanation of an agent-authored change is persuasive rather than accurate.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Make Intent and Evidence the Review Surface](make-intent-and-evidence-the-review-surface.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Route each change to the proof it needs](route-each-change-to-the-proof-it-needs.md)
- [Have Agents Write Literate Explainer Docs for Their Changes](have-agents-write-literate-explainer-docs-for-their-changes.md)
- [Make Code Review the Bottleneck Skill for AI-Generated Code](make-code-review-the-bottleneck-skill-for-ai-generated-code.md)

Sources:
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 10:11-11:29
