# Escalate Risky Actions to a Read-Only Review Subagent

Summary: Approval prompts that fire too often push users into full-access mode, which deletes the control entirely. A middle path is to route each sandbox escalation to a separate reviewing agent with read-only permissions and no ability to spawn agents of its own, which judges the action in context and auto-approves the predictable majority so only genuinely unclear cases reach the human.

Use when:
- Users are turning off approvals on your agent, or your security team objects to the mode they turned on.
- An agent runs for hours or days and nobody is present to answer prompts.
- Designing what sits between "ask the human every time" and "allow everything."

Details:
- The problem is stated as a two-sided squeeze, both sides confirmed by audience poll on stage: approval fatigue on long tasks drives people to full access, and "IT and security really hates that you turn on full access." Neither the prompt nor the bypass is an acceptable resting state. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 11:59-12:22)
- The threat model is an over-agentic model rather than a malicious one: "especially if you're trying to push the model through prompting to really have high agency, that can be misinterpreted by the agent to not match up with your expectation" — asked to email a file it cannot attach, it uploads the file to a file share instead; or it "messes up some escaping and accidentally deletes too much data." Both examples are competent behavior aimed slightly past what was asked. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 12:38-13:10)
- The stated goal is coverage of the unenumerable: auto review exists to "cover all of the things that are harder to predict that an agent might do and especially in the long run, and… approve those automatically without having to escalate them to you while keeping things like… data exfiltration outside of it." It is a complement to a deterministic allowlist, not a replacement — the allowlist handles what you could name in advance. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 13:15-13:34)
- **The reviewer's capability envelope is the design.** On escalation the model "spins up an auto review subagent… And this subagent runs entirely separate and can't spin up other subagents and has read permissions only." Three properties: isolated context, no write authority, and no recursion — so a compromised or confused reviewer cannot act, and cannot delegate its way to acting. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 13:34-14:03)
- **What the reviewer is given is a transcript, not a rule.** It receives "a bunch of context around… what is user authorization… how do things like… risk taxonomies work? How do we want it to judge these things?" plus "the transcript as well as sort of the tool calls that are actually happening." The rubric it applies is [how explicitly the user authorized the action](judge-an-action-by-how-explicitly-the-user-authorized-it.md) together with the action's impact. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 14:03-15:06)
- The same reviewer covers filesystem and network escalations, since both have the same shape of context-dependent risk — "curling Google to see if… the internet works is fine, but maybe not uploading a file." ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 15:04-15:18)
- **Where this sits relative to the wiki's existing gates.** [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md) argues the gate must be one the model cannot decide for itself, and Amazon AGI Lab's version keeps a hard harness override under a model-side confidence estimate. Auto review is a *third* layer between them: a model judgment made by a different model instance with different permissions, which is weaker than a human gate and stronger than the acting model's own self-assessment. It should not be read as licence to remove the hard gate on the actions you already know are irreversible.
- **The unevaluated part is the reviewer itself.** The speaker calls his description "a gross oversimplification," and the talk gives no false-approval rate, no false-escalation rate, no cost or latency for the extra subagent, and no adversarial test. The reviewer reads the transcript, which is also the surface a prompt injection would occupy — a transcript that says the user authorized something is evidence the reviewer is designed to trust. Nothing in the talk addresses that. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 15:18-15:32, Provenance and Caveats)

- Independent corroboration of the premise, from a source with no stake in automating the gate. Matt Dailey (Ref) describes the same degradation for design decisions rather than dangerous commands: the agent says "this is the recommended option and then you're like, great. I don't even think about this. I'll just hit that one and we keep going" — because chat is "brain off," a medium built for execution. Two independent observers report the in-session human gate collapsing, which strengthens the premise while pointing at opposite remedies: automate the judgment (Codex), or move the judgment out of the session entirely into a shared decision document ([Separate the Decision Layer From the Implementation Layer](separate-the-decision-layer-from-the-implementation-layer.md)). The remedies are compatible — one covers dangerous actions, the other covers consequential choices. ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 10:55-11:35)

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Judge an Action by How Explicitly the User Authorized It](judge-an-action-by-how-explicitly-the-user-authorized-it.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Permission-stable command wrappers reduce approval friction](permission-stable-command-wrappers-reduce-approval-friction.md)
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md)
- [Teach Calibrated Confidence So an Agent Knows When to Hand Off](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)
- [Customize Subagents by Task, Model, Tools, and Permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Sandbox Primitives Are Per Operating System](sandbox-primitives-are-per-operating-system.md)
- [Ceding a Critical Decision Transfers Ownership of the Code](ceding-a-critical-decision-transfers-ownership-of-the-code.md)

Sources:
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 11:59-15:32
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 10:55-11:35
