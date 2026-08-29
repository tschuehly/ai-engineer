# Ship Bundled Docs and an AGENTS.md Inside the Published Package

Summary: For a library, the documentation site is largely a human surface. Coding agents work from the repository, `node_modules`, and compiled source, patched by stale training data — so the highest-leverage place to put Markdown documentation is inside the published package, next to an `AGENTS.md` that tells the agent the docs are there.

Use when:
- You ship an installable module (npm, cargo, PyPI, Maven) and are investing in a documentation site for agent readability.
- A coding agent hallucinates your API despite correct, current, published docs.
- Deciding where fresh documentation should live so an agent gets it without a network fetch.

Details:
- **The premise, stated as the talk's most important point.** "The uncomfortable truth is that coding agents are actually never visiting the website if you have a library. They're actually visiting the node modules. They read the repo and they read the node modules. They have previous stale training data and they're trying to work it out on what it can do from the compiled source." ([Burns](../sources/20260826_V_5bn4q-vAI.md), 10:04-10:46)
- **The intervention.** Bundle the Markdown documents into the published artifact and add an `AGENTS.md` beside them that "basically says, if you've got a problem, if you've got a question, all the documents are here. Grab them." The point is a pointer at the location the agent already reads, not a new place for it to look. (10:46-11:16)
- **The measured effect, and what it is measuring.** "Almost 50% token saving on instead of trying to search the web, find the right tools, pulling the markdown files from your code base," observed "between many different models." The baseline is the whole web-research detour — decide to search, pick a tool, fetch, read HTML — so the saving is mostly the elimination of a retrieval subplot rather than a compression of the docs themselves. (11:16-11:45)
- **No skill required, but a skill sharpens it.** The behavior works with nothing installed on the consumer's side, because the files are simply present where the agent is already looking; "if you want as well, you can add skills to it to say, look at the node modules and go from that." That property is what distinguishes it from every other agent-experience surface on this wiki: it is the only one whose adoption cost on the consumer's side is zero. (11:45-11:53)
- **Write the pointer as a verification instruction, not a reading suggestion.** The suggested `AGENTS.md` line is "when working with [the] Next.js library, read the bundles and verify that they match and go from there" — the agent is told to reconcile what it believes against what shipped, which targets the specific failure (a prior belief from training data) rather than generically encouraging reading. (11:53-12:10)
- **Why this is the right layer for a fast-moving library.** "If you have a library that's forever changing, then having the node modules built in is a very effective solution." Version-pinning does the work that a docs URL cannot: the docs the agent reads are the docs for the exact version installed, so the usual freshness question — are these docs current? — is answered by the lockfile instead of by a publishing cadence. (11:36-11:45)
- **Relationship to the wiki's other freshness answers.** [Fresh Markdown Context Mitigates Model Rot in Codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md) has the agent select current Markdown at runtime, and [Agent skills should point to current docs](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md) links out to them. Both assume the agent will fetch. This page removes the fetch, which also removes the failure modes that come with it — no web tool, no network, an air-gapped or sandboxed run, or a model that simply does not bother.
- **Cost side, unaddressed by the source.** Bundled Markdown adds weight to every install of the package for every consumer, agent or not, and the talk gives no size figure or opt-out mechanism. For a widely-installed dependency this is a real externality: the token saving accrues to agent users, the download and disk cost to everyone. Treat "ship the docs" as having a size budget the same way the entry file for a skill does — see [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md).
- **Limit.** One vendor, its own library, one self-reported number with no model list, task set, or baseline definition, and no statement of whether the ~50% is per session or per task. The direction is well-motivated by the mechanism; the magnitude is a single observation.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Fresh Markdown Context Mitigates Model Rot in Codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md)
- [Agent skills should point to current docs instead of embedding every API detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md)
- [Generate Agent-Facing Docs Artifacts From One Markdown Source](generate-agent-facing-docs-artifacts-from-one-markdown-source.md)
- [Serve Markdown Through Three Redundant Paths](serve-markdown-through-three-redundant-paths.md)
- [Repository skills and AGENTS.md encode repeatable web-agent workflows](repository-skills-and-agents-md-encode-repeatable-web-agent-workflows.md)
- [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md)
- [Publish Per-Site Skills So Agents Do Not Rediscover a Website](publish-per-site-skills-so-agents-do-not-rediscover-a-website.md)
- [Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md)
- [Agent Experience Means Autonomous Access, Understanding, and Operation](agent-experience-means-autonomous-access-understanding-and-operation.md)
- [Hand-Write llms.txt and Index the Rest for Fetching](hand-write-llms-txt-and-index-the-rest-for-fetching.md)
- [Attribute LLM-Sourced Inbound With a How-Did-You-Hear Field](attribute-llm-sourced-inbound-with-a-how-did-you-hear-field.md)
- [The Install Handoff Is Now a Prompt](the-install-handoff-is-now-a-prompt.md)

Sources:
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 10:04-12:10
