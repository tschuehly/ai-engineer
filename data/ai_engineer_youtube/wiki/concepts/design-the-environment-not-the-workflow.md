# Design the Environment, Not the Workflow

Summary: A workflow tells an agent *how* to work — steps, prompts, tools, instructions. An environment tells it *where* to work, and supplies incentives, infrastructure, guardrails, and resources instead of a procedure. Zou's argument is that the first caps what the agent can produce and the second does not, and that the cap tightens as models improve, because every step you specify is a decision you took away from something that might have decided better.

Use when:
- Deciding whether the next unit of engineering effort goes into the agent's prompt and step sequence or into the surface it acts on.
- An agent harness has accumulated procedure and you are asking which parts are still earning their place.
- Framing a project where the desired output is open-ended (a discovery, an optimization, a design) rather than a known task executed reliably.
- Choosing what to hand a *fleet* of agents rather than one — an environment scales to arbitrarily many participants, a workflow has to be re-authored per agent.

Details:
- The distinction, in the source's own terms: the prevailing paradigm "involves designing workflows that sort of tells the agents what to do… or how the agent should work. And it's typically done through a series of steps or prompts, tools, and instructions," against which "the environment should really specify not how the agent should work, but really where the agent should work… and the environment then should provide a set of incentives and infrastructure for the agents and guardrails and resources so that agent can then flexibly work within that environment." (00:39-01:19)
- **The claim is conditional on the capability trend, and says so.** "As agents become more and more powerful… if we try to design workflows that often can limit the capabilities and creativity of the agents. Whereas if we properly design the environment, this can enables a lot more creativity and capabilities and intelligence for the agents to naturally emerge." That conditional is what makes it usable rather than a slogan: the argument gets *stronger* over time and is weakest exactly where the model is the binding constraint. On a task where the model cannot do the work, removing the workflow removes the only thing making it succeed. (01:20-01:40)
- The closing framing is a three-stage progression rather than a binary: build individual models and tools → build agents, harnesses, and workflows around them → build environments, "a set of infrastructure and incentives that motivates the agents [to] solve more and more challenging [problems]," which "can actually unlock much more creativity and collective intelligence from the agents that's limited by the existing workflows." (15:39-16:31)
- **What replaces the procedure is not nothing.** The four named substitutes are incentives, infrastructure, guardrails, and resources, and in the worked case each has a concrete referent: the incentive is a live leaderboard scored by a deterministic verifier, the infrastructure is a forum plus downloadable submissions, the guardrail is the admission gate, and the resource is the curated problem set. Building an environment is not less engineering than building a workflow; it is engineering aimed at a different layer. See [Open Agent Arenas Reach Solutions No Single Agent Reaches](open-agent-arenas-reach-solutions-no-single-agent-reaches.md).
- **The strongest evidence in the source is a retarget, not a score.** Pointing the same arena at GPU kernel optimization changed only the backend verifier and produced kernels reported at over 2x, in production at Together AI. An environment that survives a domain swap with its social and scoring mechanics intact is evidence that the design generalizes in a way a tuned workflow does not. See [Swap the Verifier to Retarget an Agent Arena](swap-the-verifier-to-retarget-an-agent-arena.md). (08:57-10:54)
- **The wiki holds this position from the harness side too, which is worth reading as convergence rather than repetition.** Anthropic's Applied AI team argues that "harnesses have become the limiting factor to what models can achieve" because "harnesses encode assumptions about what Claude cannot do on its own" — the same mechanism (a specification of procedure is a dated belief about capability), stated as a reason to keep revising the harness. Zou's version is more radical: not revise the procedure, delete it and specify the arena instead. See [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md) and [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md).
- **Do not read this as an argument against scaffolding in general.** The wiki carries a large body of evidence that constraint buys reliability: [choosing autonomy level by task uncertainty and control needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md), [building harnesses incrementally up a capability ladder](build-agent-harnesses-incrementally-up-a-capability-ladder.md), and [constraining agent effects rather than expression](constrain-agent-effects-not-expression-with-a-typed-sdk.md). The reconciliation the source implies without stating: environments beat workflows where the *outcome* is checkable and the *path* is unknown, which is precisely the condition its two examples satisfy — a packing that a verifier can confirm, a kernel that a compiler and a stopwatch can confirm. Where the outcome is not mechanically checkable, deleting the procedure deletes your only control.
- Provenance: this is a design thesis argued by two demonstrations from the group that built them, not a controlled comparison. No workflow-based baseline was run against either arena, so "workflows limit the agents" is supported by the ceiling never being tested rather than by two numbers.

- **The same primacy claim reached from control rather than from capability, which is worth noting because the two agree on the mechanism and disagree on the motive.** Mohamed's closing lesson is that "if you have your agents which are intelligent, what matters is the substrate layer that they are living in. Like the world they [are] living in is more important than the agents itself. Like what they can do, what they cannot do, what you allow and what you don't allow." Zou designs the environment so a capable agent is not constrained; Mohamed designs it so a capable agent *is* — after discovering that instructions did not constrain it. Both conclude the environment dominates the agent, which is a stronger position than either talk alone: the environment is where you put the affordances you want the agent to find and the boundaries you need it to not cross, because both are the only things a sufficiently capable model cannot argue with. ([Mohamed](../sources/20260822_0I6aoPSRzVc.md), 14:47-15:11)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Open Agent Arenas Reach Solutions No Single Agent Reaches](open-agent-arenas-reach-solutions-no-single-agent-reaches.md)
- [Swap the Verifier to Retarget an Agent Arena](swap-the-verifier-to-retarget-an-agent-arena.md)
- [Curate Tasks by Live Human Demand and a Deterministic Verifier](curate-tasks-by-live-human-demand-and-a-deterministic-verifier.md)
- [Build RL Environments as Software Artifacts](build-rl-environments-as-software-artifacts.md)
- [Treat Environments as Eval, Data, and Training Substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)
- [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)
- [Choose autonomy level by task uncertainty and control needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md)
- [Build Agent Harnesses Incrementally Up a Capability Ladder](build-agent-harnesses-incrementally-up-a-capability-ladder.md)
- [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)
- [Give Parallel Agents Complementary Optimization Personas](give-parallel-agents-complementary-optimization-personas.md)
- [Gate an Environment to Agents Only](gate-an-environment-to-agents-only.md)
- [Block the Capability at the Substrate, Because Denying a Tool Only Denies a Name](block-the-capability-at-the-substrate-because-denying-a-tool-only-denies-a-name.md)

Sources:
- [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 00:39-01:40, 08:57-10:54, 15:39-16:31
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 14:47-15:11
