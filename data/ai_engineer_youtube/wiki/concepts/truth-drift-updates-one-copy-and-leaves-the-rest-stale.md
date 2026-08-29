# Truth Drift Updates One Copy and Leaves the Rest Stale

Summary: An agent asked to change a value changes it where it was looking and stops. Every other place that value appears keeps the old number, and nothing errors — the system is now internally inconsistent and still passes every check that only reads one copy. The answer is a single source of truth plus automatic conflict detection that is rule-based rather than another model call.

Use when:
- A value, threshold, constant, or requirement appears in more than one artifact and agents can edit any of them.
- Diagnosing why a system that looked correct in the changed file behaves as if the change never happened.
- Choosing between an LLM check and a deterministic rule for detecting internal contradictions.

Details:
- **The failure as reported.** "An agent modifying something in the system not necessarily means it modifies it everywhere it should be modified. And that makes it harder. Like we have the cases specifically where one agent was modifying a parameter, it updated it in one place, five other places were forgotten." ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 13:14-13:36)
- Why it is worse than an ordinary miss: the edit *succeeded*. There is no failed tool call, no exception, and no diff that looks wrong. The agent's local view is consistent, so neither self-verification nor a reviewer reading the diff will see it. The inconsistency is only visible to something holding all the copies at once.
- **The fix has two halves and both are load-bearing.** "We have a single source of truth with automatic conflict detection that is not LLM based but actually rule based that can detect that this agent did this issue… and actually resonate in the whole system immediately." The single source of truth reduces the number of copies; the detector catches the copies that remain. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 14:25-14:47)
- **Rule-based, deliberately.** Contradiction detection is exactly the case where a deterministic check beats a judge: the comparison is an equality between known references, it must run on every write rather than on a sample, and a judge that misses one contradiction reintroduces the failure it was hired to catch. This is the wiki's cheapest-sufficient-signal rule applied to an internal-consistency check rather than an output quality check.
- **Propagation is the third element.** In the same system, an approved change to the intent graph "echoes in the whole system," so a value change reaches every stakeholder holding the old one. Detection tells you a contradiction exists; propagation is what prevents the next one. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 09:52-10:15)
- **The coverage question the source leaves open.** Who writes the rules, where the cross-reference map comes from, and what fraction of duplicated values it covers are all unstated — which matters most for this failure specifically, because the five stale copies were the ones nobody had enumerated. A rule-based detector only finds contradictions between references someone thought to declare. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 14:25-14:47)
- No rate is given for how often drift occurred, and the fix is described as a principle they now work under rather than as a measured before-and-after.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Keep a Living Intent Graph That Agents Read but Cannot Write](keep-a-living-intent-graph-that-agents-read-but-cannot-write.md)
- [Prune skills with single source of truth, sediment removal, and no-op deletion tests](prune-skills-with-single-source-of-truth-sediment-and-no-op-deletion-tests.md)
- [Catalog Eval Signal Sources Across Judge, Human, Golden, Deterministic, and Business](catalog-eval-signal-sources-judge-human-golden-deterministic-business.md)
- [Make Memory Notice Conflicts and Seek the Evidence That Settles Them](make-memory-notice-conflicts-and-seek-the-evidence-that-settles-them.md)
- [Scope Role Agents With a Spec Hierarchy and File Isolation](scope-role-agents-with-a-spec-hierarchy-and-file-isolation.md)
- [Grade the Alignment, Not the Agents](grade-the-alignment-not-the-agents.md)

Sources:
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 13:14-13:36, 14:25-14:47, 09:52-10:15
