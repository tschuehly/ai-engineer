# Prefer Simple Debuggable Eval Scores

Summary: Eval scores should be as simple and inspectable as the domain allows. Deterministic pass/fail checks make failures easier to debug and share, while human review is acceptable when code cannot capture the right signal.

Use when:
- Choosing between deterministic checks, LLM judges, and human review for application evals.
- Designing CI reports that must help reviewers understand regressions.

Details:
- For simple domains, a scorer can check whether the output contains the correct answer; for subjective domains such as writing, scoring varies and may need a more nuanced signal, 10:40-11:03.
- The talk recommends leaning toward deterministic pass/fail scoring because debugging produces many inputs and logs, and teams need quick failure diagnosis, 11:03-11:29.
- Overengineered scores can be hard to share across teams because nobody understands how results are computed, 11:17-11:29.
- A practical scorer starts by asking what evidence in the data would show failure, then writing code to look for that evidence; if code cannot capture it, human review is still a valid way to collect the correct signal, 11:32-12:08.
- Eval-only prompt additions, such as asking for an answer inside tags, can make string matching easier even if those tags are not part of the production user experience, 12:09-12:34.
- CI eval reports should show whether a PR changes failures to passes or introduces regressions across the product court, 12:36-13:07.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Write custom scorers as product specifications](write-custom-scorers-as-product-specifications.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)

Sources:
- [Evals Are Not Unit Tests - Ido Pesok, Vercel v0](../sources/20250806_L8OoYeDI_ls.md), 10:40-13:07
