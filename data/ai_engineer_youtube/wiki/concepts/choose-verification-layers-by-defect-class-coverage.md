# Choose Verification Layers by Defect-Class Coverage

Summary: Verification layers should be picked by which defect classes each one can reach, not by how many tools you have running. Syntax, data-flow, architectural, and control-flow problems are found by different techniques, so a computational analyzer and a reasoning-based reviewer are complements rather than alternatives — "you're never going to be able to find every single problem that can occur in software by just using one or two methods."

Use when:
- Deciding whether adding an AI code reviewer lets you drop static analysis, or vice versa.
- Justifying a second verification layer to someone who sees it as duplicated spend.
- Designing a quality gate and needing a coverage argument rather than a tool list.
- Auditing an existing pipeline for defect classes that no layer currently reaches.

Details:
- **The claim.** "It also needs to be multi-layered. You need to have… multiple techniques being used, multiple approaches being used to review the code that is being generated… because you're never going to be able to find every single problem that can occur in software by just using one or two methods. You need to use computational review, you also need to use LLM driven review, and everything else in between." ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 10:13-10:35)
- **The defect classes named** are the useful part, because they are what a coverage audit checks against: "syntax issues, data flow issues, architectural issues, control flow issues." A grep-and-style layer reaches the first; interprocedural analysis reaches the second and fourth; whether the change fits the intended architecture is where a reasoning layer earns its place. (13:40-13:49)
- **Why one technique cannot span them** is grounded in a separate argument in the same talk: "software is not provable in the same way that code is." A function written correctly "is going to run the same way every single time," but requirements and externalities change what correct means, accumulated code interacts "in unpredictable ways," and "users can do all kinds of things you didn't expect." Techniques that are sound about a function are silent about a system, which is why the layer count is a coverage question rather than a redundancy question. (07:43-08:41)
- **The worked instantiation** is the PR gate, where both layers run over the same diff with different outputs: "a superhuman review that is LLM driven by Gitar and there's a computational review that is run by SonarQube that actually assigns grades for all three of those things [quality, security, maintainability] and won't allow the PR to go past into production unless it gets a passing grade across that criteria." Note the division of labor — the reasoning layer produces findings, the computational layer produces the pass/fail that blocks, which is the layer whose verdict is reproducible. (18:25-18:47)
- **Verification must also cut across concern types, not just defect types**: the talk requires it to "cut across quality issues, security issues, and compliance issues," and its shift-left security argument is timing-driven — "CVEs are announced and then immediately exploited… by bad actors almost often the same day," so a security layer that only runs at release is running after the exploitation window opened. (11:12-11:20, 12:49-13:13)
- **Relation to the wiki's existing layering pages.** [Use Hierarchical Verification Before Trusting Weak Agent Feedback](use-hierarchical-verification-before-trusting-weak-agent-feedback.md) orders layers by *strength of signal*; this page orders them by *class of defect reached*, and the two questions are independent — a strong signal about the wrong class is still a gap. [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md) answers who may verify; this one answers how many layers and chosen by what.
- **Caveat: the coverage argument is a taxonomy, not a measurement.** No data appears in the talk on what each layer catches that the other misses, no marginal return is estimated for the third method, and the defect-class list is the vendor's own analyzer's feature set. It is a useful checklist for finding holes; it is not evidence that these four classes are exhaustive. The talk's closing recommendation — "standardize on a single independent multi-layered verification platform" — also sits in mild tension with its own diversity argument, since one supplier providing every layer is method diversity without supplier diversity. (21:48-22:03)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md)
- [Use Hierarchical Verification Before Trusting Weak Agent Feedback](use-hierarchical-verification-before-trusting-weak-agent-feedback.md)
- [Fix Defects Inside the Agent Loop Before They Become Foundation](fix-defects-inside-the-agent-loop-before-they-become-foundation.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [AI Code Quality Needs Full-SDLC Workflows](ai-code-quality-needs-full-sdlc-workflows.md)
- [Make Validation Fast, Local, Deterministic, and Actionable](make-validation-fast-local-deterministic-and-actionable.md)

Sources:
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 07:43-08:41, 10:13-10:35, 11:12-11:20, 12:49-13:49, 18:25-18:47, 21:48-22:03
