# Run a Submission-and-Review Alias for Shared Skills

Summary: A shared skill library for non-engineers needs an intake point with named reviewers — a central alias where skills are submitted, curated by the business team and the operations team together, and reviewed before they land — because the visible failure of an ungoverned library is not bad skills but too many of them.

Use when:
- Opening a skill or prompt library to a large non-engineering population.
- Deciding what governance a skill catalog needs beyond search, versioning, and permissions.
- Responding to a proliferation of near-duplicate internal skills after an initial burst of enthusiasm.

Details:
- The mechanism is specific and low-tech: "we have a central alias where skills are presented to the central team, curated by the go-to-market team, as well as by operations team, and they're reviewed, so we can make sure that we're not having a proliferation of skills, and we have an expert-level knowledge skill at every level." ([Joyce](../sources/20260826_Qw_tC68KKes.md), 13:36-14:02)
- **Two reviewer constituencies, not one.** The business team validates that the encoded procedure is what an expert would actually do; the operations team validates that it queries the data correctly. A single reviewer from either side can approve a skill that is fluent and wrong in the other dimension.
- The stated goal is coverage without duplication — "an expert-level knowledge skill at every level" — which makes the review a placement decision as much as a quality one: does this belong as a new skill, or as an edit to one that exists?
- **Curation is named as the foundation of the whole system, ahead of the model or the workspace:** "skill curation is the basis for all of this agentic workforce. If you're able to embed the knowledge of the business into the skill files... you're really able to give them the ability to use the agentic systems in a more predictable and deterministic way so that they can execute evenly across the board." Predictability is claimed as a property of the curated context, not of the model. (15:34-16:09)
- **The urgency is framed as a phase the organization is currently in:** "we're sort of reached the Cambrian stage of using agentic systems, which means there's an explosion of excitement and skills and finding out ways to solve anything with AI," with the intended response explicitly not prohibition — "not really limit, but just figure out a really strategic approach for allowing each team to use the agentic system so that the source of truth in all the systems are aligning." (18:19-18:49)
- Source-of-truth alignment is the concrete risk being managed. Independently authored skills that each define a metric or a filter slightly differently produce divergent answers from one warehouse, which is the spreadsheet problem the platform existed to remove.
- This is the intake half of skill governance; the maintenance half is pruning stale and no-op material from the skills that survive ([Prune skills with single source of truth, sediment removal, and no-op deletion tests](prune-skills-with-single-source-of-truth-sediment-and-no-op-deletion-tests.md)), and the amplification risk is that any loop which authors skills automatically inherits whichever regime is in place ([Auto-Evolving Skills Multiply Whatever Governance You Already Have](auto-evolving-skills-multiply-whatever-governance-you-already-have.md)).
- **Limit.** No throughput, rejection rate, review latency, or skill count is reported, and human review at an alias is the first thing to become a bottleneck if submissions scale — a risk the talk names as a coming problem rather than a solved one.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Prune skills with single source of truth, sediment removal, and no-op deletion tests](prune-skills-with-single-source-of-truth-sediment-and-no-op-deletion-tests.md)
- [Auto-Evolving Skills Multiply Whatever Governance You Already Have](auto-evolving-skills-multiply-whatever-governance-you-already-have.md)
- [Package Reusable Context as Skills, Libraries, and Registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Skill Composability Is Decided Before Authoring, Not in the Registry](skill-composability-is-decided-before-authoring-not-in-the-registry.md)
- [Put the Business Question Set Inside the Skill File, Not Just the Schema](put-the-business-question-set-inside-the-skill-file-not-just-the-schema.md)
- [Hand Domain Experts the Pipeline as Skills](hand-domain-experts-the-pipeline-as-skills.md)
- [Domain Expert Review Tools Convert Judgment Into Deployable Knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)

Sources:
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 13:01-14:02, 15:34-16:09, 18:19-18:49
