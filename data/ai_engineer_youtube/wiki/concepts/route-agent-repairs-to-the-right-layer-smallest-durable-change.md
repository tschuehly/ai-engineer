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

- **A second team reaches the same three-way split independently, and adds a reason each layer resists a generic fix.** LangChain says agent state has to be updated "across all three axes": training data ("observational data from agents taking actions"), the harness, and memory. Two additions are useful here. On the harness: "the Codex harness and the Claude Code harness and like our harness and everyone's harness, like they look a certain way because like models are trained in them and they look a certain way because of the tasks that they do in the real world," so a harness edit is entangled with the model's training distribution rather than being a free parameter, and "evolving those over time is going to be super important." On memory: "we are not append-only logs of information," and over year-to-lifetime horizons "we cannot just append everything to a really big file and then search over it" — the update mechanism proposed is sleep-time compute, "read all of the traces over the entire agent life cycle and then do things to update agent state." Two convergent accounts of the same partition make the routing frame more credible than either alone. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 17:22-18:49)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Ambient agents need self-maintenance and memory hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)

Sources:
- [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../sources/20260705_2IxD9OB3XuQ.md), 06:25-11:01, 12:34-13:26, 21:35-21:52
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 17:22-18:49
