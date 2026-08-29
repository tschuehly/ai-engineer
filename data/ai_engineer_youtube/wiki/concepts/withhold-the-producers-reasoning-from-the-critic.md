# Withhold the Producer's Reasoning From the Critic

Summary: A critic agent should receive the claim and the evidence, and not the chain of thought that produced them. Agents that read each other's reasoning converge — the group talks itself into one idea — so the reasoning trace is the specific part of the producer's context that has to be redacted for the critic's verdict to be independent.

Use when:
- Wiring a critic, verifier, or judge agent that runs after a producer agent in the same system.
- Deciding what to put in a reviewing subagent's context, given that you control all of it.
- A multi-agent panel keeps agreeing, and you want to know which shared input is causing it.

Details:
- The construction is explicit: for the critic, "just give it what it needs to solve that critic problem… we're passing it the claim and the evidence. So, this is your claim is sort of how we're going to solve the problem. Here's the evidence, but we're not giving it the thought processes that went in to creating this claim." ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 13:44-14:25)
- **The justification is convergence, not cost.** "When you get a bunch of agents together collaborating and talking to each other, there's a tendency to have group think. And all the agents seem to kind of devolve into one idea." The analogy given is social: "you're at a party, and everybody wants pizza except you, but then people talk you into… you don't want to spoil the party, so you'll go along. And it seems that agents kind of work in the same way." ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 14:26-14:57)
- The generalization is per-agent slicing: "you're going to give each agent only a slice… Every agent gets its own slice." Every agent sees the portion of state its job requires, and no more — a context rule derived from independence rather than from token budget, though it saves tokens too. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 14:58-15:12)
- **This is a fourth axis of reviewer independence, and the cheapest one to apply.** The wiki already records three: a separate context ([Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)), a separate prompt or provider ([Separate generation and verification prompts or models](separate-generation-and-verification-prompts-or-models.md)), and a separate method class ([Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md)). Those vary *who or what* reviews. This varies *what the reviewer is shown*, and it applies even when the reviewer is the same model behind the same prompt, because it removes the artifact that carries the producer's framing.
- The practical consequence is that a naive "pass the whole transcript to the reviewer" implementation is actively harmful on this reading, not merely wasteful — and transcript-passing is exactly what several reviewer designs in this wiki do, including Codex's [auto review subagent](escalate-risky-actions-to-a-read-only-review-subagent.md), which "receives the transcript as well as… the tool calls that are actually happening." That is a real tension rather than a contradiction: an authorization reviewer needs the transcript because *what the user asked for* is the thing it is judging, while a correctness critic is judging an artifact and the transcript only tells it what conclusion to reach. The distinguishing question is whether the trace is the evidence or the persuasion.
- **What is not established.** No experiment, ablation, or agreement-rate figure is offered for the groupthink claim; it is asserted from analogy in a talk about exam preparation, and the identical framing appears in the exam's own multi-agent scenario as a question about "how much information should they know." The cost of the redaction is also unpriced: a critic denied the reasoning cannot flag a claim that is right for the wrong reason, and cannot tell a well-supported inference from a lucky guess. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 05:08-05:21)
- **A weaker independence mechanism that is worth naming as distinct: re-derivation from the source.** In Cloudflare's three-agent summary pipeline the checker "checks the veracity of the data" against a draft whose reads went out through MCP servers, rather than against a fixed context handed to both agents. That buys independence of *evidence* — the checker can look again — but the account says nothing about whether the drafter's reasoning is excluded from the checker's prompt, which is the redaction this page argues for. Per-call observability makes the omission auditable after the fact but does not enforce it. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 11:11-11:41)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Separate generation and verification prompts or models](separate-generation-and-verification-prompts-or-models.md)
- [Run a jury of analysts and a consensus judge for no-ground-truth questions](run-a-jury-of-analysts-and-a-consensus-judge-for-no-ground-truth-questions.md)
- [Make Intent and Evidence the Review Surface](make-intent-and-evidence-the-review-surface.md)
- [Escalate Risky Actions to a Read-Only Review Subagent](escalate-risky-actions-to-a-read-only-review-subagent.md)
- [Bound Context Twice: Fork the Subtask, Then Compact on a Token Threshold](bound-context-twice-fork-the-subtask-then-compact-on-a-token-threshold.md)
- [Split a Generated Narrative Into Drafter, Fact-Checker, and Tone Agents](split-generated-narrative-into-drafter-checker-and-tone-agents.md)

Sources:
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 05:08-05:21, 13:44-15:12
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 11:11-11:41
