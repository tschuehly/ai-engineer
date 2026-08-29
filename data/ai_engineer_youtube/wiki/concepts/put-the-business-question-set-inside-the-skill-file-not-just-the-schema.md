# Put the Business Question Set Inside the Skill File, Not Just the Schema

Summary: A skill file that only carries table and column semantics leaves the model to invent how the business asks its questions; adding the actual recurring questions — discovered by testing, not by interview — is what converts it from documentation into a reliable answering surface for people who cannot write SQL.

Use when:
- Authoring the context layer for an internal data agent or analytics assistant.
- Deciding what belongs in a skill file beyond the schema and metric definitions.
- Removing the human SQL bottleneck between a business team and its own data.

Details:
- The files are scoped by role and carry semantics rather than syntax: "we have built role-specific skill files, which have the context of the business information tying it to the data. This is for both technical and non-technical users." ([Joyce](../sources/20260826_Qw_tC68KKes.md), 06:47-07:05)
- **The question set is the additive part, and it was found empirically:** "through testing, we've included the types of questions that the business would ask of the data. In this case, looking at closed date changes and opportunities, as well as changes in the amount of the opportunities, so that we can answer essentially 80% or more of the questions, where the other 20% might be more complex strategic questions." (07:27-07:53)
- **The residual is characterized, not just sized.** The uncovered 20% is described as strategic rather than as hard SQL, which is a claim about where the file's leverage runs out: recurring operational questions are enumerable, one-off analytical ones are not, and the file should not try to be a substitute for an analyst.
- What is removed is a person in a queue, not a query: "I've seen users who do not know any SQL, and essentially their request in the past we bottleneck to someone who knows data and can write SQL for complex queries, be able to just ask questions of the data and get answers." (08:02-08:15)
- **The same file has a second consumer that justifies its cost.** "In our team we've used these same skill files to build multiple applications. Uh when usually that is done in IT and bottlenecked in those areas, we're able to use the semantic information about the business knowledge, as well as the columns table to build these applications rather quickly." A business-semantics artifact written for chat answers turns out to be the spec a coding agent needs to generate internal apps. (08:29-08:50)
- The pattern differs from writing an eval set from the business process ([Write the Question Set From the Business Process Before the Data Is Connected](write-the-question-set-from-the-business-process-before-the-data-is-connected.md)) in where the questions land: there they are the test, here they are shipped inside the context the agent reads. Both start from the questions people actually ask, and the two uses compose — the same list can grade the system and prime it.
- Curation is what keeps the files trustworthy at organization scale, through a central review alias rather than per-team authoring; see [Run a Submission-and-Review Alias for Shared Skills](run-a-submission-and-review-alias-for-shared-skills.md). (13:36-14:02)
- **Limit.** "Through testing" is the only description of how the questions were discovered — no sample, log analysis, or interview protocol is named — and the 80% coverage claim has no measurement behind it. Nothing is said about how the question set is refreshed as the sales process changes.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Business Intelligence](../topics/business-intelligence.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Write the Question Set From the Business Process Before the Data Is Connected](write-the-question-set-from-the-business-process-before-the-data-is-connected.md)
- [Preflight Agents Through a Business-Definitions Librarian](preflight-agents-through-a-business-definitions-librarian.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)
- [General Agents Need Skills for Domain Expertise](general-agents-need-skills-for-domain-expertise.md)
- [Run a Submission-and-Review Alias for Shared Skills](run-a-submission-and-review-alias-for-shared-skills.md)
- [Separate the Context Gap From the Expert Gap](separate-the-context-gap-from-the-expert-gap.md)
- [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)
- [Classify the Assistant Question Log to Find Feature and Content Gaps](classify-the-assistant-question-log-to-find-feature-and-content-gaps.md)

Sources:
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 04:56-05:49, 06:47-08:55, 13:36-14:02
