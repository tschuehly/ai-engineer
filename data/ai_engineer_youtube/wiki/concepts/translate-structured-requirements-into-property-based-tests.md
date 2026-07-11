# Translate structured requirements into property-based tests

Summary: Structured natural-language requirements can become testable invariants when acceptance criteria are translated into property-based tests. This gives agentic coding workflows a falsification path: find an input that breaks the claimed property, or gain bounded confidence that the implementation satisfies the spec.

Use when:
- Turning acceptance criteria into executable validation for agent-generated code.
- Deciding how to make natural-language requirements more than a planning artifact.

Details:
- Kiro's EARS requirements can be translated into system properties, which the speaker describes as invariants that the system should deliver. (03:59-04:13)
- Property-based testing is framed as trying to produce a single test case that falsifies an invariant; if no counterexample is found, confidence increases but still depends on how well the tests were written. (04:16-04:56)
- The workflow goal is a throughline from structured requirements to finished code, where matching code properties to initial requirements increases confidence that the expected software shipped. (05:11-05:31)
- Task definitions can include explicit unit-test cases because agents may claim completion even when tests are failing or have become inconvenient to fix. (18:08-18:47)
- The talk names Hypothesis, fast-check, and Clojure's spec library as examples of property-based testing ecosystems. (04:16-04:29)
- Independently corroborated: a second Kiro talk shows property-based tests generated against the requirements and design documents, run in the TypeScript/Node world with fast-check "dozens if not hundreds of times with different values" — e.g. for any movie dataset, the extracted genre list must contain exactly a sorted set of unique genres. (IddXPepIAS4 12:13-12:34, 15:44-17:27)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use research-plan-implement loops for coding agents](use-research-plan-implement-loops-for-coding-agents.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Use deep modules to make agent work testable](use-deep-modules-to-make-agent-work-testable.md)

Sources:
- [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro](../sources/20260109_HY_JyxAZsiE.md), 03:59-05:31
- [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](../sources/20260628_IddXPepIAS4.md), 12:13-12:34, 15:44-17:27

