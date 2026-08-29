# Generate Agent-Facing Docs Artifacts From One Markdown Source

Summary: There is no single file or trick that makes a site agent-readable — it is a growing set of small surfaces (`llms.txt`, per-page Markdown, sitemaps, RSS, `robots.txt`, in-page tools, bundled package docs). Maintaining them by hand does not survive contact with a docs site, so treat them as build outputs generated from one Markdown source and regenerated on every publish.

Use when:
- The agent-readability checklist has grown past what one person will keep in sync.
- Deciding whether to hand-maintain `llms.txt` and Markdown twins or generate them.
- Rolling the same treatment across several sites or a docs site plus a marketing site.

Details:
- **The framing that motivates a pipeline.** "There is no one tool that fixes everything. I like to think about these problems like Batman's utility belt. Loads of really small things targeted in different areas to get it done." The list named spans eras deliberately — "`llms.txt` to sitemaps to RSS feeds to `robots.txt`… so many micro optimizations that you can do from old methods of running the internet to new methods." ([Burns](../sources/20260826_V_5bn4q-vAI.md), 02:39-03:03, 04:20-04:38)
- **The shape.** After building enough docs sites, the accumulated optimizations were "abstracted" into what the speaker calls, with some self-deprecation, "a very non-sexy title, but a framework-neutral docs pipeline": "take your `.mdx` files, you run [it] generate, and it will spit out everything for optimized agent experience for your websites." (04:38-05:45)
- **Why generation is the right call here, even though `llms.txt` should be hand-written.** These are different artifacts. The orientation file is authored prose about what the product is and which page answers which question, and generating it produces noise ([Hand-Write llms.txt and Index the Rest for Fetching](hand-write-llms-txt-and-index-the-rest-for-fetching.md)). The Markdown twins, route handlers, header links, sitemap, and bundled package docs are mechanical projections of content that already exists. The rule that reconciles them: generate the projections, hand-write the judgments.
- **Framework-neutral is the load-bearing adjective.** The output set includes framework-specific pieces — a redirect in a Next.js config, for instance — so a pipeline that only works in one framework leaves the marketing site, the blog, and the docs site each solving it separately. The same pipeline running on the vendor's marketing site is what produces "every part of our marketing website also has a markdown file." (12:11-12:48)
- **The maintenance argument the talk makes implicitly.** The closing caution is that "the market, agents, LLMs, everything is forever changing. There is no such thing as perfection." A checklist that changes every few weeks is an argument for putting it behind a regenerable step: when a new convention appears, one pipeline change republishes it across every page, rather than a migration across hundreds of files. See [Score Agent-Readiness Against a Moving Baseline](score-agent-readiness-against-a-moving-baseline.md). (13:33-14:10)
- **Same discipline the wiki records elsewhere.** [The Markdown Workflow Is Source, the YAML Is a Compiled Artifact](the-markdown-workflow-is-source-the-yaml-is-a-compiled-artifact.md) makes the same move in a different domain: keep the human-editable representation authoritative and treat every machine-facing format as derived, so the two cannot drift.
- **Limit.** The pipeline is the speaker's own open-source project, described but not demonstrated, and the claim that other developer companies run it and see "similar results" comes with none of their numbers. Nothing here establishes that generation outperforms hand-maintenance; it establishes that one team stopped hand-maintaining.

Related topics:
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Hand-Write llms.txt and Index the Rest for Fetching](hand-write-llms-txt-and-index-the-rest-for-fetching.md)
- [Serve Markdown Through Three Redundant Paths](serve-markdown-through-three-redundant-paths.md)
- [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)
- [Score Agent-Readiness Against a Moving Baseline](score-agent-readiness-against-a-moving-baseline.md)
- [The Markdown Workflow Is Source, the YAML Is a Compiled Artifact](the-markdown-workflow-is-source-the-yaml-is-a-compiled-artifact.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)

Sources:
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 02:39-03:03, 04:20-05:45, 12:11-12:48, 13:33-14:10
