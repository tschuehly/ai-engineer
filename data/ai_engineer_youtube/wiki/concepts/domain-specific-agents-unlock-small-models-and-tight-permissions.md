# Domain-specific agents unlock small models and tight permissions

Summary: Because each specialist agent handles a narrow pre-picked task with minimal context (just its system prompt, its tools, and the single incoming message), composing domain-specific agents yields large token savings, makes very cheap small models viable, enforces per-agent capability limits for security, and parallelizes cleanly across cloud infrastructure.

Use when:
- Estimating whether splitting an agent into specialists will cut token cost or enable cheaper models.
- Justifying small/cheap models for production work that a big general agent currently does.
- Arguing for capability-scoped agents to satisfy IT/security review or customer-facing constraints.

Details:
- Token efficiency: StandardAgents "regularly see over 80% token efficiency for any given task," because a specialist's *total* context is just its system message, its tools, and the single incoming instruction (e.g. "get that last email from Debbie") — it never carries the surrounding conversation to make a targeted choice. ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 16:44-18:04)
- Small-model economics: for the same narrow task, a cheap model like DeepSeek V4 Flash is reported ~137× cheaper per task than Fable 5. Cheap models fail when asked to do everything, but with a narrow task and minimal context they "execute those very faithfully"; non-language models (image-generation, diffusion) can also serve as specialist agents. ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 18:05-19:29)
- Customer-facing viability: you "can't put Fable in front of a customer unless that customer has a massive lifetime value" — moving AI from internal copilots to customer-facing products needs efficacy plus efficiency, which cheap domain-specific agents provide. ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 23:54-24:15)
- Security via strict limits: rather than a big coding agent that "can do anything" and forces permission-bypassing, a domain-specific agent "can only do the things that are already explicitly approved for them to do" — a more controlled ecosystem that eases IT/security concerns without removing permission dialogs. ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 19:30-20:25)
- Scaling: each agent is its own small execution environment, so specialists parallelize easily, deploy to the cloud "without needing a giant VPC," and can run thousands of instances across regions with no geographic co-location. Agents are also portable — "squeeze up" a Gmail agent and hand it to someone else — enabling a reuse ecosystem instead of rebuilding every skill per team. ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 16:53-17:28, 20:26-20:56)

- **The security half of this page assumes a scoping mechanism, and a field report shows what happens without one.** The claim here is that a domain-specific agent "can only do the things that are already explicitly approved for them to do." AIDAChip built exactly this shape — role agents authored by subject matter experts, "digital design agent, analog design agent, and so on," one per engineer role — and still found "an analog agent that's specifically for analog design actually overstepping and doing RTL agent work. Which wasn't really great. Even we tried to enforce it, but it was a difficult problem." The specialization was real; the boundary was a description. Their fix moves it into the environment — "a spec hierarchy with agent scope and file isolation" — which is what makes this page's permission claim true rather than aspirational. ([Mohamed](../sources/20260822_0I6aoPSRzVc.md), 06:36-07:02, 12:49-13:14, 14:00-14:25)

Related topics:
- [Agents](../topics/agents.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Compose domain-specific agents instead of inflating one agent's context](compose-domain-specific-agents-instead-of-inflating-one-context.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Post-train small models for narrow capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Agentic Workloads Turn Token Price Into Unit-Economics Pressure](agentic-workloads-turn-token-price-into-unit-economics-pressure.md)
- [Scope Role Agents With a Spec Hierarchy and File Isolation](scope-role-agents-with-a-spec-hierarchy-and-file-isolation.md)

Sources:
- [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](../sources/20260629_spNAUEgq_A8.md), 16:44-20:56, 23:54-24:15
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 06:36-07:02, 12:49-13:14, 14:00-14:25
