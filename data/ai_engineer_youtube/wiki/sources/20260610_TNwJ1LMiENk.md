# Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel

Source: [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](https://www.youtube.com/watch?v=TNwJ1LMiENk)
Uploaded: 2026-06-10
Transcript: `raw/20260610_TNwJ1LMiENk/TNwJ1LMiENk.en-orig.vtt`

## Summary

Kobie Crawford (developer advocate at Snorkel, the "Frontier AI Data Lab") presents a research result done with the RLLM / Agentic project lab at UC Berkeley: a 4-billion-parameter model RL-finetuned on a financial-analysis tool-use task outperformed Qwen 3 235B on the same task. The durable lesson is that for this class of task the bottleneck is tool *discipline* (discover available tables, inspect the schema before querying, self-correct on tool errors), not reasoning depth — the 235B "reasoning" model queried a non-existent table twice and then hallucinated, while the small finetuned model called `get_table_names`, then `get_table_info`, ran a query, hit a missing-column error, and self-corrected to the right answer. Training was cheap (GRPO, ~21-hour job, under $500/run) inside a self-contained FinQA environment Snorkel built and published. Two counterintuitive findings: single-table-only training gave the largest uplift (beating multi-table-mixed and curriculum learning) and generalized to the harder multi-table FinQA-reasoning benchmark (13.9% → 26.6%); and the way to find *which* behavior to fix was to break evals into rubrics of sub-question checks before generating any training data, even though the RL reward itself collapses to a single value.

## Extracted Concepts

- [Fix Tool Discipline Before Reaching for a Bigger Model](../concepts/fix-tool-discipline-before-reaching-for-a-bigger-model.md) - a 4B RL-tuned model beat Qwen 3 235B on FinQA tool use because tool discipline, not reasoning, was the failing behavior.
- [Train on the Simplest Task Variant That Transfers](../concepts/train-on-the-simplest-task-variant-that-transfers.md) - single-table-only training beat multi-table and curriculum regimes and still doubled performance on the harder multi-table benchmark.
- [Decompose Evals Into Rubrics to Target the Failing Behavior](../concepts/decompose-evals-into-rubrics-to-target-the-failing-behavior.md) - rubrics of sub-question checks diagnose which behavior to fix and which data to generate, while RL still consumes a single reward value.
- [Build RL environments as software artifacts](../concepts/build-rl-environments-as-software-artifacts.md) - Snorkel's self-contained FinQA environment packages two benchmarks and is published on Prime Intellect, OpenEnv, and Hugging Face spaces.
- [Environment registries make AI research more accessible](../concepts/environment-registries-make-ai-research-more-accessible.md) - OpenEnv (co-hosted by PyTorch and Hugging Face) is a second registry alongside Prime Intellect for sharing runnable environments.

## Topic Links

- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

## Notes

- Goal stated as making a 4B model outperform a 235B model on a tool-use task for financial analysis; partnership with the RLLM "Agentic" lab at UC Berkeley. (02:47-03:05)
- Enterprise framing for smaller models: cost, speed, security, on-prem deployment without data export — especially for financial and healthcare data. RL is positioned as a behavior-changing lever, not a knowledge-changing one. (04:30-06:02)
- "Terence Tao effect" (the RLLM team's framing): a financial analyst does not need a mathematician brilliant at everything; over-large models are "a sledgehammer to crack a walnut" for narrow tool tasks. (06:20-07:00)
- Failure trace of Qwen 3 235B ("235 billion" reasoning model): asked for YouTube YoY ad-revenue growth 2023→2024, it queried a non-existent table without inspecting the environment, queried again with nothing back, then hallucinated an answer. (07:08-08:00)
- Data generation is expert-in-the-loop (PhD-level and industry domain experts) plus a verification step that confirms tasks are answerable and have verifiable ground-truth answers before RL. (09:30-10:40)
- RL setup: GRPO, 4B base model, RLLM framework (UC Berkeley), Snorkel's FinQA environment; ~21-hour job at under $500 per run. ("Even if Karpathy doesn't like it.") (10:56-12:10)
- FinQA environment is fully self-contained with no external dependencies (compared to Harbor / OpenEnv); published on Prime Intellect's infrastructure, saved into the OpenEnv repo on GitHub, and hosted in Hugging Face spaces (PyTorch + Hugging Face co-host). (12:10-13:05)
- Two packaged benchmarks: FinQA (290 samples) and the harder FinQA-reasoning (79 samples, multi-table queries). (13:16-13:30)
- Result: pass@1 roughly doubled vs the 235B model. Success trace of the 4B model: `get_table_names` to discover tables, `get_table_info` to inspect schema, run query, hit a missing `revenue` column error, self-correct to the actual column, return the correct answer. The two key learned behaviors were tool discovery and error self-correction. (13:56-16:10)
- Single-table-only training gave the greatest uplift over multi-table-mixed and curriculum (single→multi) regimes; the uplift transferred to the harder multi-table FinQA-reasoning set, 13.9% → 26.6%. The fixed core failure mode (tool discipline) generalized. (16:35-18:30)
- Rubric method: Snorkel's research team breaks the rightness/wrongness of a response into a list of sub-questions; the per-check feedback locates which behavior is the actual problem and decides which datasets/data to generate, before writing any training data. GRPO itself still uses a single reward value. (18:37-19:40)
- Blog post links to a partner post from the UC Berkeley Agentic team with additional detail. (20:00-20:20)
