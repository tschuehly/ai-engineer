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

Sources:
- [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](../sources/20260531_NuePCNMpWGc.md), 02:08-10:32
