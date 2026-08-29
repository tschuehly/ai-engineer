# Use Evals As Durable AI System Specifications

Summary: Evals are part of the stable AI system specification: they state what the application should care about even as models, prompts, inference strategies, and optimizers change.

Use when:
- Turning implicit prompt tinkering criteria into explicit optimization and regression targets.
- Evaluating whether a model swap or optimizer run preserved the behavior the application actually needs.

Details:
- Khattab says prompt iteration often hides the real criteria by tweaking text to appease a model; evals externalize those criteria by saying what the system actually cares about. 15:09-15:26
- Evals should not replace task instructions: learning from data is harder than following instructions, so a system needs both localized natural-language definitions and evals that measure whether the whole system works. 15:29-15:39
- The eval should evaluate the full application-specific system, not a generic model default, because the goal is to make the assembled task, control flow, tools, and model choices work together. 16:48-17:12
- Once evals name the target behavior, optimizers can change lower-level artifacts such as prompts, modules, or reinforcement-learning policies without making the product requirement itself disappear into model-specific prompt text. 17:05-17:22, 18:52-19:04
- **The descriptive counterpart: whether or not you write them as a spec, they already act as one.** LangChain's version is that "you can basically define agent behavior by showing the evals that you ran on it," because the agent "literally like hill climbs those evals, and you alter the behavior of the agent to make the evals pass." Read alongside this page, that turns a recommendation into an observation with a sharp corollary — behavior absent from the suite is behavior nothing optimized for ([An Agent's Eval Suite Describes Its Behavior](an-agents-eval-suite-describes-its-behavior.md)). ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 11:43-12:15)

- **Two artifacts share the word "specification" and guarantee different things.** Evals are durable against changes of model, prompt, and optimizer, and are evaluated statistically. A formal specification is durable against changes of implementation and is checked mechanically: "you write what correct means, which is the specification, and a formal verification tool proves that your code satisfies it. If the proof passes, it holds for every possible input." The division of labour they imply also differs — "humans own the specification and machines own the code and proof" concentrates all human judgment in one document, where the eval framing spreads it across thresholds, datasets, and judges. Use both terms deliberately, since a reader who hears "spec" hears a universal claim. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 00:57-01:08, 02:04-02:10)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Optimize LLM programs with metrics and teacher feedback](optimize-llm-programs-with-metrics-and-teacher-feedback.md)
- [Build AI app benchmarks before optimization](build-ai-app-benchmarks-before-optimization.md)
- [Avoid premature low-level AI system coupling](avoid-premature-low-level-ai-system-coupling.md)
- [An Agent's Eval Suite Describes Its Behavior](an-agents-eval-suite-describes-its-behavior.md)
- [Validate the Specification, Because the Proof Cannot](validate-the-specification-because-the-proof-cannot.md)

Sources:
- [On Engineering AI Systems that Endure The Bitter Lesson - Omar Khattab, DSPy & Databricks](../sources/20250806_qdmxApz3EJI.md), 15:09-15:39, 16:48-19:04
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 11:43-12:15
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 00:57-01:08, 02:04-02:10
