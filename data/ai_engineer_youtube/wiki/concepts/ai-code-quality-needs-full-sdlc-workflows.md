# AI Code Quality Needs Full-SDLC Workflows

Summary: AI-generated code quality should be managed across the software-development lifecycle, not only at the moment code is generated. Planning, development, review, testing, deployment, ownership, verification, guardrails, and standards each expose different quality failures.

Use when:
- Evaluating whether an AI coding rollout measures quality beyond generation speed.
- Designing quality workflows for agentic coding in mature or high-consequence systems.

Details:
- Code generation can be useful for greenfield prototypes, but heavy-duty software still has to satisfy integrity, governance, review standards, testing, reliability, security, and operational constraints. (09:12-09:51)
- Quality issues can be mapped by SDLC stage, including planning, development, code review, testing, and deployment. (09:54-10:31)
- A second useful split is code-level versus process-level quality: security and efficiency are code-level concerns, while learning, ownership, verification, guardrails, and standards are process responsibilities. (10:34-11:24)
- If an outage comes from AI-generated code, the team still needs to learn from and own the code rather than assigning responsibility to the model. (11:00-11:16)
- Confident vibe coding extends the same full-SDLC idea earlier in the workflow: generation alone may be enough for simple greenfield demos, but enterprise work needs review, testing, maintainability, bug fixing, refactoring, and standards woven into agentic workflows. (05:17-08:08)

- Sonar states the agentic-era version of the same span as a two-loop requirement rather than a stage list: "the verification needs to run in both the inner agentic loop and also in the outer loop for CICD," and it must "cut across quality issues, security issues, and compliance issues." The addition worth carrying is that the inner loop is a *new* stage this page's SDLC map does not have — it sits inside development, runs many times per change, and is the only place a defect can be caught before later agent loops build on it. The four adoption drivers the same talk attributes to customers are also process-level in this page's sense: quality, security, compliance/auditability, and developer productivity. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 11:12-11:20, 13:18-13:32, 18:25-19:04)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Measure AI ROI with primary output and guardrails](measure-ai-roi-with-primary-output-and-guardrails.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Treat agent readiness as verification infrastructure](treat-agent-readiness-as-verification-infrastructure.md)
- [Fix Defects Inside the Agent Loop Before They Become Foundation](fix-defects-inside-the-agent-loop-before-they-become-foundation.md)
- [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md)

Sources:
- [The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo](../sources/20251211_rgjF5o2Qjsc.md), 09:12-11:24
- [Vibe Coding with Confidence - Itamar Friedman, Qodo](../sources/20250806_n991Yxo1aOI.md), 05:17-08:08
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 11:12-11:20, 13:18-13:32, 18:25-19:04
