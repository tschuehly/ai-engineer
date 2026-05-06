# Use prompt mutation loops to hill-climb product behavior

Summary: Prompt mutation loops can improve complex LLM product behavior without weight updates by repeatedly evaluating prompt variants, selecting strong ones, reflecting on failures, and generating new candidates.

Use when:
- Improving an LLM product when reinforcement learning or fine-tuning is too expensive or slow.
- Turning prompt iteration from ad hoc manual edits into a scored experiment loop.

Details:
- The Browser Company describes prompt mutation as a sample-efficient way to improve complex LLM systems without reinforcement learning or other fine-tuning techniques. (06:50-07:07)
- The loop seeds the system with prompts, executes them across tasks, scores them, uses Pareto-style selection to keep better prompts, then uses an LLM to reflect on what worked and generate new prompt variants. (07:09-07:32)
- The useful mechanics are reflective prompt mutation, selection that explores more than one prompting path, and improving text rather than model weights. (07:28-07:42)
- In the broader product loop, teams first dogfood many ideas, then collect and refine evals to clarify product requirements before hill climbing through code, prompting, and automated techniques. (08:02-08:49)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use explanatory feedback to optimize prompts](use-explanatory-feedback-to-optimize-prompts.md)
- [Structure prompt-learning experiments with train/test splits and loop budgets](structure-prompt-learning-experiments-with-train-test-splits-and-loop-budgets.md)
- [Evaluator quality is a dependency of prompt optimization](evaluator-quality-is-a-dependency-of-prompt-optimization.md)

Sources:
- [From Arc to Dia: Lessons learned building AI Browsers - Samir Mody, The Browser Company of New York](../sources/20251219_o4scJaQgnFA.md), 06:50-08:49
