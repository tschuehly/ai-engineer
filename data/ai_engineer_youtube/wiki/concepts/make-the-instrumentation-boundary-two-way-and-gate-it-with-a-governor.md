# Make the Instrumentation Boundary Two-Way and Gate It With a Governor

Summary: The annotation you wrap a method in to report its token cost is already sitting at the only place a control plane could reach into a running agent, so make it a two-way channel rather than a telemetry export — and then bound it with a developer-owned allowlist of permitted actions, because an out-of-band service that can mutate your agent arbitrarily is a worse problem than the spend it was added to fix.

Use when:
- Adding cost, token, or trace instrumentation to an existing agent and deciding how invasive it should be.
- A policy engine needs to change a running agent's behaviour, not just observe it or stop it.
- Reviewing an SDK that asks you to annotate methods and also claims to control them.
- Deciding what an external control plane is allowed to do to code you own.

Details:
- **The annotation does two jobs.** "You take any method. It doesn't matter what framework you're using… If you have a method you can annotate it with `boundary`. What this annotation is going to do is… First it's going to track the input and the output and it's going to float that up to the control layer and record it there as a ledger entry… The second thing the boundary annotation does is it acts as a channel through which the control plane can push actions down to the agent. This is where the entire intelligence lies. So we do not have a single directional highway." ([Chawla & Koul](../sources/20260822_GJX19pNhmSw.md), 12:01-12:52)
- **The reason it must be two-way.** An out-of-band observability plane can report and it can be a precondition for refusing service, but it cannot change how a run behaves. Steering requires a downlink into the process, and the instrumentation point is the natural one because it already brackets the call being governed. This is the mechanism gap behind [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md), and it is why a gateway — which sits on the wire, not in the call stack — can only halt.
- **The governor is the bound that makes it acceptable.** "The governor knows what actions are allowed on your agent by you as a developer and it receives those actions from the control plane and knows how to apply it in a non-destructive way." It is instantiated with your configs, which "declare what sort of actions are allowed for those agents… so that your control plane cannot just willingly do any random things on your agents." Two properties are worth separating: the allowlist is authored by the code owner, and it is enforced *in* the process, not by the plane proposing the action. (13:22-13:34, 15:39-15:56)
- **This inverts the usual control-plane direction, and both directions are needed.** The wiki's control-plane page has the model propose and the platform decide. Here the platform proposes and the *code owner's* declared policy decides — because the platform is now an external service reaching into an application it did not write. A system that does both has two allowlists pointing in opposite directions, and neither substitutes for the other. See [Build an Agentic Control Plane So the Model Proposes and the Platform Decides](build-an-agentic-control-plane.md).
- **The blast radius the governor is defending against, made concrete.** A steer action can mutate a tool result (cap a retrieval at five chunks) or inject into system instructions. Both are the kind of change that would be a code review if a human made it and is invisible if a policy engine makes it, and the RAG example is exactly a case where the "correct" cap depends on the workload. An unbounded downlink is a remote code-behaviour-modification primitive; the allowlist is what turns it into a configuration surface. (12:52-13:22, 18:28-18:39)
- **Deployment details that come with the decision.** The annotation floats method inputs and outputs to the plane, which is why the control plane is placed "in your own tenant. So you do not need to worry about any data leaks." A `wrap_complete` helper covers the case where providers "provide objects rather than methods for their LLMs" — the same boundary applied to an object. Both are consequences of choosing an in-process boundary over a network chokepoint. (13:35-13:50, 15:19-15:38)
- **Caveat.** No failure mode of the downlink is discussed anywhere in the talk: what happens if the control plane is unreachable mid-run, whether actions are idempotent or ordered, and what a "non-destructive" application actually guarantees are all unstated. The wiki's standing question for any in-path dependency applies — a channel in the call path needs its own fail-open or fail-closed decision. See [Treat Guardrails as a Failable Dependency With Its Own Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md).

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Make the LLM Gateway the Agent Observability Chokepoint](make-the-llm-gateway-the-agent-observability-chokepoint.md)
- [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md)
- [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md)
- [Build an Agentic Control Plane So the Model Proposes and the Platform Decides](build-an-agentic-control-plane.md)
- [Treat Guardrails as a Failable Dependency With Its Own Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md)
- [Ship Enforcement Policies in Preview Mode Before Enabling Them](ship-enforcement-policies-in-preview-mode-before-enabling-them.md)
- [Emit Attribution Dimensions So Budgets Can Target Any Cohort](emit-attribution-dimensions-so-budgets-can-target-any-cohort.md)
- [Version-Control and Unit-Test the Agent Permission Policy](version-control-and-unit-test-the-agent-permission-policy.md)

Sources:
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 12:01-13:50, 15:19-15:56, 18:28-18:39
