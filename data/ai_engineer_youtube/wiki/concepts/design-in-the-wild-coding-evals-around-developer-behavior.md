# Design in-the-wild coding evals around developer behavior

Summary: Live coding-assistant evals measure both model quality and developer interaction behavior. Experiment design must control user-facing factors such as latency, presentation, and acceptance mechanics before treating preference signals as model-quality signals.

Use when:
- Running live IDE A/B tests or pairwise preference evals for code completions.
- Interpreting developer acceptance rates from production coding-assistant telemetry.

Details:
- Copilot Arena compares two IDE completions shown in the same editing context and uses keyboard acceptance behavior to pairwise compare completion assistants. (14:33-15:08)
- RepoChat evaluates repository question answering by letting users provide a GitHub URL and ask natural-language questions ranging from codebase explanation to issue-fix patch suggestions. (15:08-15:40)
- In-the-wild eval design needs to be human-centered because user behavior can dominate measurement. (15:40-16:23)
- Latency was a major factor for completion acceptance: the source reports acceptance rates dropping sharply when completion latency exceeded roughly one second, requiring latency balancing across models. (15:43-16:15)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Track user dissatisfaction alongside pairwise model preference](track-user-dissatisfaction-alongside-pairwise-model-preference.md)
- [Measure AI developer productivity with field experiments, not benchmark extrapolation alone](measure-ai-developer-productivity-with-field-experiments-not-benchmark-extrapolation-alone.md)

Sources:
- [Coding Evals: From Code Snippets to Codebases - Naman Jain, Cursor](../sources/20251215_tHN44yJoeS8.md), 14:33-16:23
