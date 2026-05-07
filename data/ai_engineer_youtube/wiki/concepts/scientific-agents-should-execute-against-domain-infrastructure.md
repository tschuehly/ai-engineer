# Scientific Agents Should Execute Against Domain Infrastructure

Summary: Scientific agents become more useful when they connect literature review and hypothesis generation to executable domain tools, simulations, and compute infrastructure. The agent is then a workflow around domain models and assets, not just an LLM producing text.

Use when:
- Designing agents for research, engineering, simulation, or scientific discovery workflows.
- Deciding whether an agent should only summarize papers or also run domain-specific validation steps.

Details:
- Los Alamos' ICF demonstration asks the agent to read a paper, find tangentially related papers, generate a hypothesis, propose a fusion-capsule design, execute code, and simulate a slice through the capsule. (02:00-03:18)
- The useful "model" in this workflow includes decades of math, science, stewardship tools, and HPC assets, not just the language model itself. (02:42-03:01)
- This pattern makes validation infrastructure part of the agent design: the agent's proposal is valuable because it can be tested by thermodynamic and hydrodynamic simulation rather than left as a plausible narrative. (02:29-03:18)
- Druga adds a smaller-scale lab version of the same principle: a co-scientist should connect protocols, sensors, cameras, and open lab hardware so hypotheses can be formed from realtime empirical feedback. (07:03-10:14)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Use hardware-in-the-loop search for AI kernel generation](use-hardware-in-the-loop-search-for-ai-kernel-generation.md)
- [Treat environments as eval, data, and training substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Assemble Realtime Multimodal Context for Lab Agents](assemble-realtime-multimodal-context-for-lab-agents.md)
- [Use Open Lab Hardware as the Co-Scientist Action Surface](use-open-lab-hardware-as-the-co-scientist-action-surface.md)

Sources:
- [Government Agents: AI Agents Meet Tough Regulations - Mark Myshatyn, Los Alamos National Lab](../sources/20251206_TnSGx36Ly0Q.md), 02:00-03:18
- [Real-time Experiments with an AI Co-Scientist - Stefania Druga, fmr. Google Deepmind](../sources/20250728_wNH3q9pqn0U.md), 07:03-10:14
