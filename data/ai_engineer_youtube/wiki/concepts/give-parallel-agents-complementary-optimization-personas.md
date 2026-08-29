# Give Parallel Agents Complementary Optimization Personas

Summary: When several agents attack the same optimization problem, giving each a different persona — a role and a prior about where the win is — turns redundant sampling into coverage. On GPU kernels, Together AI ran one agent biased toward profiling, one toward memory consumption, and one toward precision and tensor computations, competing and collaborating on the same leaderboard.

Use when:
- Parallel attempts on the same problem keep converging on the same approach and more samples stop helping.
- Designing a fan-out where the goal is search breadth rather than throughput on independent items.
- You have a small set of named optimization axes an expert would work through, and want them worked in parallel rather than in sequence.
- Deciding what to vary across parallel agents: the prompt, the model, the temperature, or the *prior*.

Details:
- The mechanism, in the source's terms: "we also found it to be quite useful to have different agents with different personas… these different personas actually corresponds to different roles and priors that agents can actually have. So, for example, we have one agent that looks at… more of the profiling, another agent that tends to look at more of the memory consumptions, a third agent that looks at the precisions, the tensor computations. And these agents… across different personas, they can collaborate and compete on the arena to speed up the kernels." (09:43-10:12)
- **"Persona" here means an optimization prior, not a voice.** The wiki's other persona material is about tone, prosody, and brand fit ([derive an agent persona from a measured corpus](derive-an-agent-persona-from-a-measured-corpus-not-a-described-tone.md), [prompt voice agents for persona, prosody, and brand fit](prompt-voice-agents-for-persona-prosody-and-brand-fit.md)). This is a different use of the same word: the persona biases *where the agent looks for the win*, and its output is measured by a stopwatch rather than judged by a human.
- **Why the axes are a good decomposition, and how to find yours.** Profiling, memory, and numerical precision are three of the standing decision axes an expert kernel engineer works through, and they are largely independent — a memory-layout win and a precision win compose. The transferable rule is to derive personas from the axes your domain's experts already enumerate, so the priors are genuinely non-overlapping. Simran Arora's talk from the same event names an analogous decision set for multi-GPU kernels — transfer mechanism, overlap schedule, collective ordering, data partitioning — which is the shape a persona split would take there.
- **The personas need a shared surface to be worth more than an ensemble.** They "collaborate and compete on the arena," which means each persona's best result is visible and downloadable by the others; a memory-focused agent can pick up a precision-focused agent's submission and apply its own axis to it. Without that, differentiated priors give you N independent attempts to pick a max from; with it, they give a chain of composed improvements. See [Open Agent Arenas Reach Solutions No Single Agent Reaches](open-agent-arenas-reach-solutions-no-single-agent-reaches.md).
- **The evidence is a "found it useful," not a measurement.** No comparison against identical agents at matched compute is reported, so the contribution of persona diversity cannot be separated from the arena mechanics or the underlying models. The reported outcome — "sometimes over two-fold speed ups in some of these production kernels," in production at Together AI — belongs to the whole system. Treat this as a technique worth trying with a cheap A/B (same fleet, differentiated versus uniform prompts, same budget), not as a validated multiplier. (10:14-10:54)
- Related failure mode to watch for: a persona is a bias, and a biased agent can be biased *wrong*. If the actual win on a kernel is in collective ordering and no persona covers it, the fleet will systematically miss it while looking busy. Audit persona coverage against the domain's decision set rather than choosing personas for variety.

Related topics:
- [Agents](../topics/agents.md)
- [Inference](../topics/inference.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Swap the Verifier to Retarget an Agent Arena](swap-the-verifier-to-retarget-an-agent-arena.md)
- [Open Agent Arenas Reach Solutions No Single Agent Reaches](open-agent-arenas-reach-solutions-no-single-agent-reaches.md)
- [Design the Environment, Not the Workflow](design-the-environment-not-the-workflow.md)
- [Scale Test-Time Search Through Parallel Verifier-Checked Branches](scale-test-time-search-through-parallel-verifier-checked-branches.md)
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)
- [Use Hardware-In-The-Loop Search For AI Kernel Generation](use-hardware-in-the-loop-search-for-ai-kernel-generation.md)
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Derive an Agent Persona From a Measured Corpus, Not a Described Tone](derive-an-agent-persona-from-a-measured-corpus-not-a-described-tone.md)

Sources:
- [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 09:43-10:54
