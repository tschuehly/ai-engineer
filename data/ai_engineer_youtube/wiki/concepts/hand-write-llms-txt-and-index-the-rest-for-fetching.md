# Hand-Write llms.txt and Index the Rest for Fetching

Summary: `llms.txt` works better hand-written than generated — one team's testing found roughly 40 good lines beat 1,000 lines of noise — and its companion full-form file should be built as an index of links with a one-line statement of what each page is for, because agents fetch rather than browse.

Use when:
- Adding `llms.txt` to a documentation or marketing site and reaching for the generator.
- A site has hundreds of pages and an agent picks the wrong one or reads too many.
- Deciding what the "full" variant of an agent-facing site map should actually contain.

Details:
- **The problem being solved is navigation, not exposure.** "If your docs have hundreds of pages, how can it navigate them to find the right questions?" The file exists to reduce the number of pages an agent has to consider, so anything that grows it works against its purpose. ([Burns](../sources/20260826_V_5bn4q-vAI.md), 05:52-06:14)
- **Write it by hand.** "It's much better not to just generate this. It is much better to write your `llms.txt` from hand… write it as you are trying to get the answers across to the LLMs. For about 40 good lines beats 1,000 lines of noise from our testing." The authoring stance is the transferable part: you are writing to answer the questions a reader arrives with, not enumerating what the site contains — which is exactly what a generator over your file tree cannot do. (06:14-06:39)
- **The behavioral claim underneath the companion file.** "Agents don't know how to browse. They know how to fetch." An agent will not wander a site accumulating orientation the way a human does; it retrieves specific URLs. So the second file is "a sitemap, where it takes the actual page and the links and a short description of what each page is for the LLMs to reference" — link plus purpose, so a single read is enough to choose the next fetch. (06:39-07:07)
- **Note the naming divergence, because it matters when you implement.** The wiki's earlier source describes `llms-full.txt` as a variant that "can bring a site's content into a single file for agent consumption" — the whole corpus concatenated ([Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md), Leplus/Lasorsa 38:23-38:36). Burns describes the full form as a link index with per-page descriptions. These are opposite artifacts: one maximizes what is in context, the other minimizes it. The fetch-not-browse argument favors the index; the concatenated form is a fallback for agents that will only take one document. Decide which one you are publishing and say so in the file.
- **Why a hand-written short file resists the usual objection.** The obvious complaint is that hand-authored files rot. The counter this source implies is that these 40 lines are orientation — what the product is, which page answers which question — which changes far more slowly than the API surface it points at. The volatile material stays in the pages; see [Agent skills should point to current docs instead of embedding every API detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md) for the same split applied to skills.
- **A caveat this page inherits.** A published authoritative file is inert against an assistant answering from weights rather than retrieving; it only pays off when the agent is actually using tools and real-time information. See [Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md).
- **For sites without Markdown at all, still write it.** Asked about ordinary websites whose CMS cannot emit Markdown, the advice is to hand-author the files anyway: "you can always get creative with creating these files on the go." (15:44-16:08)
- **Limit.** "40 good lines beats 1,000 lines of noise" names no metric, no task set, no model, and no comparison protocol. Read it as an authoring heuristic that one team settled on, not a measured threshold.

Related topics:
- [Tools](../topics/tools.md)
- [Retrieval](../topics/retrieval.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Serve Markdown Through Three Redundant Paths](serve-markdown-through-three-redundant-paths.md)
- [Generate Agent-Facing Docs Artifacts From One Markdown Source](generate-agent-facing-docs-artifacts-from-one-markdown-source.md)
- [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md)
- [Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md)
- [Agent skills should point to current docs instead of embedding every API detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md)
- [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)

Sources:
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 05:52-07:07, 15:44-16:08
