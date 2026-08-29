# Make Memory Notice Conflicts and Seek the Evidence That Settles Them

Summary: A memory system that only writes and reads is missing the behavior that would keep it true. The complaint worth acting on is not that a profile contained a wrong fact, but that nothing noticed the fact contradicted itself and nothing went looking for the already-reachable evidence that would resolve it — a product omission, not a model limitation.

Use when:
- A personalization layer keeps serving a stale or self-contradictory claim and nobody can say which component owns fixing it.
- Deciding whether a memory pipeline needs a step between extraction and serving.
- Arguing for a gap-filling or clarification behavior against the objection that models cannot do this yet.

Details:
- The failing artifact: a profile entry about his 2025 travel listing Thailand and Turkey with **overlapping dates**, synthesized from conversations where he was deciding between the two. He went to Thailand and has never been to Turkey (05:56-06:29, 16:03-16:20).
- Two things the system did not do. It did not notice that the entry is internally impossible — "ChatGPT today doesn't realize that there is a conflict." And it did not act on the gap — "It's not curious about trying to fill in gaps in the information it knows about me" (16:50-17:11).
- The evidence was in reach: flight and hotel bookings in an inbox the product is already connected to but does not reason over or synthesize into the profile (16:31-16:50). Conflict detection without an evidence-seeking step would have flagged the contradiction and stopped; the pair is what closes it.
- The attribution he insists on: "it's not a technology problem. It's a product problem. There is no fundamental reason from an LLM level that these things can't be solved. It's just that products today are not designed to help us with this" (17:11-17:34).
- Why the standard extraction pipeline misses this by construction: extraction turns deliberation into assertion, synthesis merges assertions without an entailment check, and serving prepends the result. No stage owns the question "can both of these be true?"
- Design cues that follow: check new claims against existing ones at write time rather than at read time; treat a detected conflict as a task with a resolution source attached, not as a note; and prefer a source that records outcomes (bookings, calendar entries) over a source that records intent (conversations) when the two disagree.
- Related but distinct from surfacing conflicts between *retrieved documents*: the contradiction here lives inside the memory store's own synthesized output, so a system that only reconciles external sources will never see it.

- **A conflict class where the detector should not be a model, and the reason is structural.** AIDAChip's failure is an agent that "updated it in one place, five other places were forgotten," answered with "a single source of truth with automatic conflict detection that is not LLM based but actually rule based." The distinction against this page's harder case is what the conflict is *about*: two sincere accounts of a fact need judgment to reconcile, but two copies of a declared value that no longer match need only an equality check that runs on every write. Deciding which kind of conflict a system faces determines whether the detector can be deterministic — and the deterministic case should not be handed to a judge, because a judge that misses one contradiction reintroduces the failure it was hired to catch. ([Mohamed](../sources/20260822_0I6aoPSRzVc.md), 13:14-13:36, 14:25-14:47)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Surface Unresolved Context Conflicts to Agents and Users](surface-unresolved-context-conflicts-to-agents-and-users.md)
- [Memory Quality Is Capped by the Context It Can Reach](memory-quality-is-capped-by-the-context-it-can-reach.md)
- [Replace User-Managed Memory Lists With a Background-Synthesized Profile](replace-user-managed-memory-lists-with-a-background-profile.md)
- [Make the Memory Profile Visible and Editable](make-the-memory-profile-visible-and-editable.md)
- [Ambient Agents Need Self-Maintenance and Memory Hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)
- [Truth Drift Updates One Copy and Leaves the Rest Stale](truth-drift-updates-one-copy-and-leaves-the-rest-stale.md)

Sources:
- [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../sources/20260812_5ZGyKWjQDr0.md), 05:56-06:29, 16:03-17:34
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 13:14-13:36, 14:25-14:47
