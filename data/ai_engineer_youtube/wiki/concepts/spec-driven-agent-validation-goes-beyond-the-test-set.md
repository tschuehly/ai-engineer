# Spec-Driven Agent Validation Goes Beyond the Test Set

Summary: An agent spec is not just a dataset of good inputs and outputs; it should also capture explicit rules, domain ontologies, rights and roles, and robustness envelopes, written independently of the implementation so it survives a model or framework swap and can drive both security testing and iterative improvement.

Use when:
- Deciding what "good" and "harm" mean for a deployed agent beyond a golden eval set.
- Building integration/penetration tests for a customer-facing or task-performing agent that must hold across model or framework changes.
- Turning implicit business rules and domain knowledge into testable specifications.

Details:
- A test set (ground-truth input/output examples graded by accuracy/F1) is only one component of an agent spec; the rest is otherwise "guesswork." (05:03-05:27)
- Add explicit rules customers actually have — e.g. never give a discount over 10%, no refunds after 30 days — and recognize that proving a rule is *never* violated is hard, which is why it belongs in the spec rather than only in the prompt. (05:27-05:51)
- Add domain ontologies/dictionaries: the relevant universe (an airline chatbot only flies to certain destinations), internal company terminology, and valid substitutions (gross profit vs gross sales are different in business even though an LLM may conflate them). The testing system must be told these so it generates fair variants. (05:55-06:59)
- Add rights and roles: the agent may behave differently logged in vs out, or with different permissions. (07:01-07:07)
- Add robustness requirements — the agent analogue of vision robustness (can I detect the runway at sunset, in fog, with camera shake?): how many typos or rephrasings before the agent fails, and how stable results are under input change. Go beyond the test set to task- and role-specific benchmarks. (07:08-07:52)
- These look like integration tests; make implicit elements explicit. The A2A agent card describes what an agent does but is still not enough to evaluate it — you also need the valid range of change. (08:00-08:48, 10:21-10:38)
- The spec feeds two activities: security testing (knowing the domains the agent engages and where it has power to act tells you where it is most vulnerable) and robustness testing (vary inputs to measure its valid range). (08:48-09:39)
- Keep the spec implementation-independent so the same integration/unit/penetration tests survive swapping e.g. LangSmith for Vertex agents; version it like an OpenAPI spec in a GitHub repo and pull it into whatever tool runs it. The improvement loop is a "backyard RL" jury-rigged around the agent (not the model): run it automatically, get results, iterate to fill robustness gaps. (11:14-12:31)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Security](../topics/security.md)

Related concepts:
- [A Bigger Model Is Not Automatically a Safer or Better Agent](a-bigger-model-is-not-automatically-a-safer-or-better-agent.md)
- [Verify Spec Adherence With Executable, Readable BDD Scenarios](verify-spec-adherence-with-executable-readable-bdd-scenarios.md)
- [Choose Eval Scope Across Span, Multispan, Trajectory, and Session](choose-eval-scope-across-span-multispan-trajectory-and-session.md)
- [Spec-driven development turns prompts into requirements, design, and tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)
- [LLM attack surfaces span prompts, context, retrieval, tools, and actions](llm-attack-surfaces-span-prompts-context-retrieval-tools-and-actions.md)

Sources:
- [Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence](../sources/20260531_UQKg0td-Bf4.md), 05:03-12:31
