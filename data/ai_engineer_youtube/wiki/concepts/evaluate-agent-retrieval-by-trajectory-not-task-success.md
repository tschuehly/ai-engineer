# Evaluate Agent Retrieval by Trajectory, Not Task Success

Summary: A pass/fail task score hides whether an agent found the right context efficiently. Scoring the trajectory — file/line/symbol precision and recall against human-labeled "golden" targets the agent should have read — measures retrieval quality directly and reveals waste and tool-behavior differences that a solved/not-solved verdict cannot.

Use when:
- Comparing retrieval tools or harness changes (grep, windowed reads, semantic search) where two configurations can both solve a task but explore very differently.
- Diagnosing context waste: a coding agent that "works" may still read mostly irrelevant files, burning tokens and context budget.
- Building a benchmark for how an agent *finds* context rather than only whether it reaches the answer.

Details:
- ContextBench (Cursor's internal context benchmark; a public ContextBench paper exists) is built on the thesis that "it's also important how you get there, not just the end goal — the process really matters." It is a human-labeled dataset of the golden files, lines, and symbols an agent should have looked at to complete each task well. (05:10-05:53)
- Two metrics, each at file / line / symbol granularity. Precision = of everything the agent read, how much was golden (read 10 files, 8 needed → 80%). Recall = of the golden targets, how many the agent found (10 needed, found 3 → 30%). The two can move in opposite directions. (06:26-06:55, 07:33-07:49)
- The benchmark compared three conditions across 50 tasks: raw Claude Code, Claude Code capped at 50-line windowed reads, and windowed reads + a semantic-search tool. The 50-line read cap is a deliberate measurement choice: full long-file reads are "noisy really fast" and make the conditions indistinguishable, so capping reads sharpens the signal. (05:53-06:24)
- What it surfaced: file precision rose 65% → 87% as windowed grep and then semantic search were added — Claude Code "wastes 1 in every 3 file reads," windowed grep cuts that to 1-in-5, semantic search to 1-in-8. The low baseline reflects that Claude Code is "really exploratory" and "loves to read everything." (06:26-07:30)
- The precision/recall split exposed a behavior a task score would miss: raw Claude Code actually *wins* file recall (it explores every file it can) but its line recall drops sharply, because it read many files without golden context lines — it "explored a lot" but "explored the wrong things a lot." High exploration is not the same as good retrieval. (07:33-08:25)
- Trajectory scoring also let the analysis break results down by where each tool won, turning an aggregate that looked flat ("semantic search didn't help") into the real finding that different task types need different tools (see related concept). (08:25-08:54)

- **The specific defect trajectory scoring catches that outcome scoring cannot.** An agent that finds one correct document and stops produces a plausible answer from real evidence — no error, no empty result, nothing for an outcome metric to fail. Against a golden set of targets the agent *should* have read, the same run scores high precision and low recall, which is the signature of early termination rather than bad ranking. That distinction changes the fix: a stopping failure is not repaired by a better embedding model. See [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md). ([Werry](../sources/20260827_qdAkxLoYNI8.md), 04:37-05:12)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Choose Lexical, Vector, and Reranking Retrieval by Query Shape](choose-lexical-vector-and-reranking-retrieval-by-query-shape.md)
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)
- [Choose Eval Scope Across Span, Multispan, Trajectory, and Session](choose-eval-scope-across-span-multispan-trajectory-and-session.md)
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)
- [Native Tool Integration Beats a Bolted-On Tool the Model Can't Time](native-tool-integration-beats-a-bolted-on-tool.md)
- [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md)

Sources:
- [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](../sources/20260603_zKk7sDMGDEQ.md), 05:10-08:54
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 04:37-05:12
