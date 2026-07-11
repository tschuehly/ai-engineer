# Route Agent Repairs to the Right Layer With the Smallest Durable Change

Summary: One agent failure usually has several possible causes and repairs spread across the model, harness, and memory layers; a good learning engine diagnoses the root cause and applies the *smallest durable change at the right layer* rather than defaulting to one repair type.

Use when:
- Deciding whether to fix an agent failure by fine-tuning, editing the harness, or writing to memory.
- Building a self-improvement or continual-learning system that must choose *where* to change the agent.
- Weighing the cost and verifiability of a proposed fix.

Details:
- Agent continual learning is not necessarily model fine-tuning — many useful updates happen in the harness and memory layers. (21:35-21:52)
- The three layers and their update methods: **model** (SFT to imitate correct trajectories, RL post-training like DPO/GRPO/RLVR to reinforce reward/preference winners, LoRA to limit changeable parameters — expensive, and needs benchmarks/evaluators unless logs are lifted into replayable environments); **harness/context** (prompts, skills, tools, code, workflow — via trace-to-harness coding-agent edits, or prompt-search like GEPA that mutates/scores/keeps winners); **memory** (write facts / distill successful trajectories into reusable skills — Letta, Mem0 — cheapest and fastest, works directly on log+feedback but usually unverified). (06:25-11:01)
- The holisticness principle: a single failure — e.g. an agent cites a stale policy and skips the required escalation — could stem from stale memory, an unoptimized prompt, a tool that doesn't normalize the policy, a missing workflow escalation gate, or a weak reasoning model. Route the fix to the layer(s) that explain the failure with the smallest durable change. (12:34-13:26)
- Cost/verifiability tradeoff across layers: memory writes are cheap but usually unverified; prompt/harness changes are medium cost; model-weight changes are expensive. Trace-to-harness edits are flexible but "vibe-based" and untestable (risking hidden regressions); prompt-search is testable but needs a benchmark and explicit evaluators. Efficiency should also govern which layer you touch. (09:09-10:04, 14:38-15:13)
- The routing depends on first making the failure testable — see the replayable-learning-environment step — so the chosen layer's change can be scored before/after and regression-checked. (04:14-06:15)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)

Sources:
- [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../sources/20260705_2IxD9OB3XuQ.md), 06:25-11:01, 12:34-13:26, 21:35-21:52
