# Measure Generated Code Quality Beyond Pass Rate

Summary: Functional-correctness leaderboards (HumanEval, MBPP, SWE-bench pass rates) measure only whether generated code passes tests and hide the engineering dimensions that decide enterprise readiness — maintainability, security, complexity, bug density, and code bloat. Benchmarking the same models on those axes with static analysis reveals that more capable models often pass more tests while emitting far more code, and more lines means more bugs and a larger attack surface.

Use when:
- Choosing a code-generation model for production rather than for a benchmark score.
- Arguing that an 80%+ pass rate is necessary but not sufficient evidence of enterprise-ready code.
- Designing an evaluation that scores generated code on quality, not just functional correctness.

Details:
- Sonar ran an open-source dataset of 4,444+ distinct Java assignments through 53+ models and analyzed the output with SonarQube Enterprise (published at sonar.com/leaderboard), measuring pass rate, lines of code, cyclomatic and cognitive complexity, bugs per million LOC, and security issues per million LOC. (02:58-03:40, 06:45-07:16)
- Code bloat scales with model capability: GPT-4o produced < 250,000 LOC for the assignment set, GPT-5.4 / GPT-5.4 Pro High produced ~1.2 million, and Claude Sonnet 4.6 produced 627,000 with the highest security-issue rate at 300 per million LOC — so the highest pass rate does not imply the most concise or safest code. (04:44-05:21, 09:15-09:39)
- The pass-rate leader can still be concise: Gemini 3.1 Pro High led at 84.17% with ~307,000 LOC, cyclomatic complexity 234, 614 bugs/MLOC, and 210 security issues/MLOC. (03:48-04:28, 07:21-07:38)
- Root causes are structural: training data carries mixed-quality and insecure code plus hidden subtle logic bugs that models absorb alongside good examples; LLMs are probabilistic (same prompt yields different code and different volume), lack the company's codebase and architecture context, and are not explainable, so defects are hard to diagnose. (05:23-06:45)
- Maturing models are not a free pass: as RL fixes known issue classes, total vulnerabilities per model fall but the remaining bugs get "finer" and harder for a human reviewer to detect. (09:54-10:32)
- **The board is maintained per release, and its per-dimension spread is now stated as a routing input.** A later Sonar talk describes scoring "each of the major new models that come out… on 4,000 or so coding tasks" against "correctness, complexity, the rate at which they're solving the tasks we assign them, and then our classic things maintainability, reliability, and security," and reads the Claude tier pair off it: Sonnet 4.6 ahead on correctness and task-solving, Opus 4.6 the better pick where maintainability, security, or lower complexity is what the task needs. That turns this page's finding from a caution about benchmarks into a selection key — see [Route Between Model Tiers by Quality Dimension, Not Only Cost](route-between-model-tiers-by-quality-dimension-not-only-cost.md). No numbers accompany the tier comparison; it is spoken over a slide. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 04:51-05:57)
- **The vendor's own conclusion from the board is a floor, not a ranking**: "None of these models are ever going to be perfect. You're always going to have some kind of need for verification in the loop." Read with the maturing-models bullet above, the two together say the quality gap narrows and changes shape rather than closing, which is the premise the same talk builds its verification argument on — see [Verification Debt Outlives the Productivity Spike](verification-debt-outlives-the-productivity-spike.md). (06:12-06:27)
- Cyclomatic complexity counts branches (ifs/else/for/while); cognitive complexity is a proprietary measure of how hard the code is for a human to read, understand, and maintain — both rise with the more verbose models. (08:30-09:48)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)
- [Models](../topics/models.md)

Related concepts:
- [AI Code Quality Needs Full-SDLC Workflows](ai-code-quality-needs-full-sdlc-workflows.md)
- [Agentic coding economics shift attention from writing cost to assurance cost](agentic-coding-economics-shift-attention-from-writing-cost-to-assurance-cost.md)
- [Do not trust a single leaderboard for model selection](do-not-trust-a-single-leaderboard-for-model-selection.md)
- [Shift Code Quality Left With a Pre-Commit Analysis and Remediation Loop](shift-code-quality-left-with-precommit-analysis-loop.md)
- [Route Between Model Tiers by Quality Dimension, Not Only Cost](route-between-model-tiers-by-quality-dimension-not-only-cost.md)
- [Verification Debt Outlives the Productivity Spike](verification-debt-outlives-the-productivity-spike.md)

Sources:
- [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](../sources/20260531_NuePCNMpWGc.md), 02:08-10:32
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 04:51-06:27
