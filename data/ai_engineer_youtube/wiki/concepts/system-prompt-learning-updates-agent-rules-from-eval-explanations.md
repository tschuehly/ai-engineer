# System Prompt Learning Updates Agent Rules From Eval Explanations

Summary: System-prompt learning treats agent rule files as mutable context that can be improved from benchmark traces, tests, and judge explanations. Instead of fine-tuning model weights, the loop writes learned instructions into agent-visible rules such as `CLAUDE.md` or Cline rules.

Use when:
- Improving a coding agent whose failures repeat across benchmark tasks or production traces.
- Deciding whether to update model weights, hand-edit rules, or automate prompt-rule learning from eval feedback.

Details:
- The talk frames coding-agent system prompts as important non-static context: successful agents repeatedly iterate on system prompts and repo rules, 00:34-01:17.
- The concrete loop runs the coding agent on software engineering tasks, executes unit tests, asks an LLM judge for pass/fail plus explanations, and sends the original prompt, current rules, inputs, judge result, and explanation to a meta-prompt that generates new rules, 04:24-08:28.
- This is explicitly a prompt/context update path rather than fine-tuning: the benchmark checks whether new system-prompt rules improve outcomes without changing model weights, 05:01-05:24.
- In the described 150-example SWE-bench Lite run, learned rules improved resolved GitHub issue rates by about 5 percentage points for Claude Code and 15 percentage points for Cline, 08:31-08:59.
- The differentiator is not merely using English feedback; the eval prompt must produce explanations detailed enough to become useful rules, 09:07-10:20.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use explanatory feedback to optimize prompts](use-explanatory-feedback-to-optimize-prompts.md)
- [Evaluator quality is a dependency of prompt optimization](evaluator-quality-is-a-dependency-of-prompt-optimization.md)
- [Structure prompt-learning experiments with train/test splits and loop budgets](structure-prompt-learning-experiments-with-train-test-splits-and-loop-budgets.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)

Sources:
- [The Unreasonable Effectiveness of Prompt Learning - Aparna Dhinakaran, Arize](../sources/20251223_pP_dSNz_EdQ.md), 00:34-10:20
