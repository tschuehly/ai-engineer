# Can LLMs generate Enterprise Quality Code?

Source: [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](https://www.youtube.com/watch?v=NuePCNMpWGc)
Uploaded: 2026-05-31
Transcript: `raw/20260531_NuePCNMpWGc/NuePCNMpWGc.en-orig.vtt`

## Summary

Prasenjit Sarkar (Sonar) argues that functional-correctness leaderboards (HumanEval, MBPP, SWE-bench pass rates of 82-84%) measure only whether generated code passes tests, and miss the engineering dimensions that decide whether code is enterprise-ready: maintainability, security, complexity, bug density, and tech debt. Sonar built an evaluation framework that ran an open-source dataset of 4,444+ distinct Java assignments through 53+ models, then analyzed the output with SonarQube Enterprise, publishing results at sonar.com/leaderboard. The headline finding is code bloat: more capable/newer models pass more tests but emit dramatically more code for the same work (GPT-4o < 250,000 lines; GPT-5.4 ~1.2 million; Claude Sonnet 4.6 627,000 with the highest security-issue rate at 300 per million lines of code), and more lines means more bugs and a larger attack surface. Sonar's prescribed response is the ACDC ("agent-centric development cycle") framework — Guide, Verify, Solve — that shifts quality enforcement left: treat training/codebase data and augment context (Guide), run SonarQube agentic analysis pre-commit in 1-5 seconds versus 1-5 minutes in CI (Verify), and use a remediation agent that creates one fix per issue and re-runs analysis + compilation, discarding any fix that regresses, before presenting it (Solve).

## Extracted Concepts

- [Measure Generated Code Quality Beyond Pass Rate](../concepts/measure-generated-code-quality-beyond-pass-rate.md) - benchmarks the same models on maintainability, security, complexity, and code bloat that functional-correctness leaderboards hide.
- [Shift Code Quality Left With a Pre-Commit Analysis and Remediation Loop](../concepts/shift-code-quality-left-with-precommit-analysis-loop.md) - the ACDC guide/verify/solve loop runs static analysis before commit and gates an auto-remediation agent on regression checks.

## Topic Links

- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)
- [Models](../topics/models.md)

## Notes

- Functional-correctness benchmarks (human eval, MBPP, SWE bench) report 80%+ pass rates but miss security, real-world reliability, architecture, maintainability, and tech debt. (02:08-02:58)
- Gemini 3.1 Pro High led pass rate at 84.17% with concise output (~307,000 LOC, cyclomatic complexity 234, 614 bugs/MLOC, 210 security issues/MLOC). (03:48-04:28, 07:21-07:38)
- Claude Sonnet 4.6 produced the highest security risk at 300 security issues per million LOC and 627,000 LOC; GPT-5.4 / GPT-5.4 Pro High produced 1.2 million LOC for the same 4,444 assignments; GPT-4o produced < 250,000. (04:44-05:21, 09:15-09:31)
- Why quality slips: training sets contain mixed-quality code, built-in security flaws, and hidden subtle logic bugs that models absorb alongside good examples; LLMs are probabilistic (same prompt → different code/different volume) and lack the company's codebase/architecture context, and are not explainable so hard to diagnose. (05:23-06:45)
- As models mature via RL, total vulnerabilities per model decrease but the bugs they still create get "finer" — harder for a human to detect. (09:54-10:32)
- ACDC = Guide / Verify / Solve, with an inner loop and an outer loop. (10:43-11:06)
- Guide stage products: Sonar Context Augmentation (push the entire codebase as context into the LLM) and Sonar Sweep (private beta — treat the training/codebase data so problematic data does not become problematic code). (11:06-11:42)
- Verify stage: SonarQube Agentic Analysis (open beta) runs over the generated code via an MCP built into Claude/Codex/Gemini CLI, analyzing pre-commit in 1-5 seconds versus a 1-5 minute CI run, surfacing issues for the agent to fix before commit. (11:42-12:40)
- Solve stage: the SonarQube Remediation Agent creates one PR per issue (and can batch tech debt from the dashboard), creates the fix, re-runs analysis and compilation, and discards any fix that introduces a regression so only passing fixes reach the developer for review. (12:40-14:05)
- Cyclomatic complexity = branch count (ifs/else/for/while loops); cognitive complexity is a Sonar-proprietary measure of how hard code is for a human to read, understand, and maintain. (08:30-09:01)
