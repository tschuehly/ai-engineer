# Parallel Agent Prototypes Turn Design Choices Into Measurements

Summary: When knowledge infrastructure makes agent work cheap enough, teams can prototype divergent product or architecture options in parallel, test them with real metrics, and converge on decisions from evidence instead of debating guesses.

Use when:
- Deciding whether to run multiple prototype paths before committing to an architecture or product direction.
- Explaining how coding-agent parallelism can improve decision quality, not only throughput.

Details:
- The source frames the economic shift as moving from serial design-build-test decisions toward rapid prototype, iterate, test, and convergence loops. 16:24-17:06
- Augment's examples include a VS Code fork prototype, agent feature prototypes, and user-loved features that began as agent-assisted experiments. 17:07-17:30
- Parallel approaches should be measured with real data so teams can decide which designs, prototypes, or architectures deserve production investment. 17:30-18:25
- The claim is not that AI makes software less disciplined; used effectively, it can make software creation more scientific by validating hypotheses earlier. 18:25-18:44

- A countervailing force this page does not price: Matt Dailey (Ref) calls it **prototype gravity** — "we build something and we're so excited to just ship that thing and we're going down like one path of the idea maze." A built prototype is shippable, and shippable things get shipped, so parallel prototyping only produces a decision if the losing branches are genuinely disposable. His alternative for the early, non-empirical questions is to explore in writing instead, where nothing acquires gravity. The practical reconciliation is to split by question type — prototype when the open question is empirical, plan when the open question is what matters — and to state a prototype's disposability before building it. ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 15:12-15:48)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel Coding Agents Support Multitasking and Variation Search](parallel-coding-agents-support-multitasking-and-variation-search.md)
- [Treat Product Evals as Probabilistic Specifications](treat-product-evals-as-probabilistic-specifications.md)
- [Measure AI ROI with primary output and guardrails](measure-ai-roi-with-primary-output-and-guardrails.md)
- [Unimplemented Plans Signal a Working Decision Layer](unimplemented-plans-signal-a-working-decision-layer.md)

Sources:
- [Mentoring the Machine - Eric Hou, Augment Code](../sources/20250724_Zniw5c9_jx8.md), 16:24-18:44
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 15:12-15:48
