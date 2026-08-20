# Grade With a Parallel Rubric Agent and Retry Until It Passes

Summary: "Outcomes" moves rubric grading out of the offline eval suite and into the running loop: you define a rubric and explicit failure cases, and the platform "starts a separate grader agent that runs alongside your agent loop," which on failure means the agent "will keep trying until it reaches that success criteria that you have defined." It converts an eval into a runtime controller — with the two bounds that turns it from a demo into a production mechanism left unspecified.

Use when:
- A task has a checkable success criterion that is cheaper to state than to guarantee by prompting.
- Deciding whether quality enforcement belongs in CI, in the loop, or in a human review step.
- Reviewing a proposal to add automatic retry to an agent and needing the list of things that must be bounded first.

Details:
- **The mechanism as described.** The developer supplies a rubric and failure cases; a *separate* grader agent runs concurrently with the primary loop; failing the rubric restarts or continues the work rather than returning it. The separation matters — the grader is not the same context asked to check itself, which is the difference between this and a self-critique prompt. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 29:08-30:03)
- **What is genuinely different about it.** An offline rubric eval tells you a *population* of runs is worse than you wanted, after the fact. A rubric in the loop changes the outcome of *this* run. That is a real shift in what a rubric is for, and it is the reason to file this under evaluation rather than under agent design: the rubric artifact is the same, the consumer is not.
- **The two bounds the source does not state, and you must.** *Termination*: "keep trying until it reaches that success criteria" has no stated iteration cap, no cost ceiling, and no described behavior for a criterion the agent cannot meet — a rubric that is unsatisfiable (or subtly mis-specified) becomes an unbounded spend rather than a failure. *Rubric correctness*: the retry loop optimizes the agent against the grader, so a wrong rubric is now enforced rather than merely mismeasured, and the well-documented failure mode of optimizing against a judge — see [detecting reward hacking in evals](detect-reward-hacking-in-code-optimization-evals.md) — applies directly to a loop whose exit condition *is* the judge.
- **Where the grader's cost lands.** Running a grader alongside every agent turn is a second model in the request path, and a retry loop multiplies the primary agent's cost by however many attempts it takes. The talk gives no figure for either, so treat the mechanism as buying reliability with tokens at an unstated exchange rate.
- **A reasonable adoption shape given the above.** Use it where the criterion is cheap to check and objectively decidable (format conformance, a test suite passing, a required field present) rather than where it is a matter of judgment, cap the retries explicitly, and keep the offline eval suite — the in-loop grader tells you nothing about how often the *first* attempt succeeds, which is still the number that says whether the agent is improving.
- Provenance: an Anthropic vendor talk, where outcomes appears on a frontier/coming-soon list. It is announced, not evaluated: no measurement of how often retries succeed, no cost accounting, no iteration cap, no treatment of rubric error, and no comparison against offline rubric evaluation. The hazards named above are this wiki's reading, not the source's.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)
- [A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)
- [Keep the Session Log Separate From the Context Window](keep-the-session-log-separate-from-the-context-window.md)
- [Model a Managed Agent as Agent, Environment, and Session](model-a-managed-agent-as-agent-environment-session.md)

Sources:
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 27:17-27:34, 29:08-30:03
