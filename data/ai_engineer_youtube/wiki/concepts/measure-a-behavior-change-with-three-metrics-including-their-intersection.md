# Measure a Targeted Behavior Change With Three Metrics, Including Their Intersection

Summary: When you train an agent to do one specific new thing, report three numbers — the rate of the new behavior, the base-task success rate measured independently of it, and the intersection of the two. The first alone can be bought with capability; the second alone hides the change; the intersection is the only one that says the behavior was added rather than traded for.

Use when:
- Installing a narrow behavior (a tool call, a format, a stopping rule) into a model that must not regress.
- Reviewing a post-training result that reports only the metric that moved.
- Designing the eval for a continual-learning update before running it.

Details:
- The three metrics, as defined for a SWE-bench task where the goal was to make a model call a submit tool before turn 40. **Task complete rate:** "the percentage of the time that the agent calls this tool to finish a submission." **Test pass rate:** "how we measure the regression in performance on sort of the base task… the percentage of the time that the environment passes all tests accompanying the SWE-bench task **irrespective of whether the agent… submitted the task via this tool call**." **SWE-bench pass rate:** "how we basically combine these two metrics. It's the intersection of those two behaviors." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 11:20-12:04)
- The goal is stated as a joint condition rather than a single objective: "we want to raise the SWE-bench pass rate performance while not degrading the test pass rate." Two numbers must move in specified directions; neither is optional. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 11:56-12:04)
- **The design detail that does the work is the word "irrespective."** The base-task metric is deliberately measured *without* conditioning on the new behavior, so it cannot absorb the change. If the base metric were only computed on submitted runs, installing the submit behavior would move it for reasons that have nothing to do with capability, and the regression check would be circular.
- The reported result reads correctly under this scheme: task complete rate "from about 22% to 60%," test pass rate "relatively constant. In fact, it goes up a little bit." The behavior rate nearly tripled and the independent capability metric did not pay for it ([A Teacher Can Install a Tool Call by Moving the Reasoning Path](move-the-reasoning-path-not-the-target-tokens.md)). ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 12:22-12:48)
- **The generalizable form.** For any targeted change, name (a) the behavior indicator, (b) a task-success measure defined so it is computable whether or not the behavior occurred, and (c) their conjunction. The pattern applies well beyond tool calls — output formats, refusal rates, stopping rules, latency-shaped behaviors. On the same talk's formatting task, only the behavior rate is reported (15%→80%) with the base-capability requirement stated qualitatively, which is a visible gap in an otherwise disciplined measurement story ([When Rewards and SFT Both Degrade the Base Model](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)).
- **Relationship to regression-aware optimization.** RELAI's page argues that "don't break the past" belongs *inside* the optimizer rather than in a post-hoc check ([Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)). This is the measurement layer under that argument: you cannot constrain what you have not defined independently, and the intersection metric is what makes "helped and broke nothing" a single readable number ([Verifiable Continual Learning](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)).
- Provenance: a vendor's own unpublished run, with no seeds, sample counts, or variance reported for any of the three metrics. The *scheme* is the durable contribution here; the numbers are an existence proof.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)
- [Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [A Teacher Can Install a Tool Call by Moving the Reasoning Path, Never the Call Tokens](move-the-reasoning-path-not-the-target-tokens.md)
- [When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)
- [Split LLM judges into narrow binary metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Measure AI ROI with primary output and guardrails](measure-ai-roi-with-primary-output-and-guardrails.md)

Sources:
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 11:20-12:48, 15:09-15:36
