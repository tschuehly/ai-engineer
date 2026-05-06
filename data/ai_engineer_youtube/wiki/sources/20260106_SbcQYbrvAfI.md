# Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize

Source: [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](https://www.youtube.com/watch?v=SbcQYbrvAfI)
Uploaded: 2026-01-06
Transcript: `raw/20260106_SbcQYbrvAfI/SbcQYbrvAfI.en-orig.vtt`

## Summary

Arize presents prompt learning as a feedback-driven optimization loop for agent prompts: collect traces or datasets, attach human labels and free-text explanations or evaluator feedback, split data for optimization and testing, run iterative prompt candidates, and validate that the evaluators themselves are high quality enough to guide the loop.

## Extracted Concepts

- [Use explanatory feedback to optimize prompts](../concepts/use-explanatory-feedback-to-optimize-prompts.md) - this source argues that why an output failed is more valuable than a bare correct/incorrect label.
- [Structure prompt-learning experiments with train/test splits and loop budgets](../concepts/structure-prompt-learning-experiments-with-train-test-splits-and-loop-budgets.md) - this source describes the configurable data and iteration controls needed for repeatable prompt optimization.
- [Evaluator quality is a dependency of prompt optimization](../concepts/evaluator-quality-is-a-dependency-of-prompt-optimization.md) - this source warns that prompt learning only works when the eval signal is reliable and detailed.

## Topic Links

- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

## Notes

- Agent failures are framed as often coming from weak environment, instructions, planning, missing tools, missing tool guidance, and insufficient context rather than only weak model capability, 02:22-03:46.
- Prompt learning combines LLM evals, human labels, subject-matter-expert explanations, and prompt rewriting so the optimizer sees not only whether an output failed but why it failed, 06:32-08:27.
- Subject-matter experts should explain failures such as missed instructions, context noncompliance, or missing information instead of only labeling rows correct or incorrect, 07:34-08:05.
- The workshop configures sample counts, train/test split, number of evaluation prompts or rules, and number of optimization loops so teams can trade fast iteration against representative validation, 28:24-30:39.
- Evaluators can be LLM-as-judge or code-based checks; the example uses a comprehensive binary output evaluator plus a granular rule checker, both producing feedback for prompt improvement, 37:12-38:19.
