# Prefer thinking models for deep bug hunting, with variability caveats

Summary: Thinking models can be stronger bug hunters because they explore more codebase considerations before diving into a suspected defect. They still need verification because run-to-run findings can vary and holistic file understanding remains limited.

Use when:
- Choosing a model for defect discovery, security review, or complex codebase investigation.
- Interpreting why repeated bug-finding runs produce different issue lists.

Details:
- Bismuth's benchmark found thinking models significantly better at finding bugs in codebases than non-thinking models. (02:48-03:03)
- The talk attributes some of the advantage to broader exploration of codebase considerations before deeper investigation of a suspected bug. (05:30-05:55)
- Even thinking models showed high variability: the number of found bugs could remain similar while the specific bugs changed run to run, implying incomplete holistic file review. (05:55-06:24)
- Users should not have to run an agent many times to get a complete bug breakdown; the variability is an active limitation of current agents rather than a workflow ideal. (06:24-06:33)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Reliability thresholds determine whether coding agents save time](reliability-thresholds-determine-whether-coding-agents-save-time.md)
- [Benchmark saturation pushes capability evals toward human time horizons](benchmark-saturation-pushes-capability-evals-toward-human-time-horizons.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)

Sources:
- [How to Improve your Vibe Coding - Ian Butler](../sources/20250803_g03m-WFEu1U.md), 02:48-03:03, 05:30-06:33
