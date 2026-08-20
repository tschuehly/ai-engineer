# Compile Natural-Language Analytics Into Reusable Deterministic Widgets

Summary: An LLM can answer a one-off business question directly, but the durable artifact is a "widget" the model writes once as declarative code that calls the data sources itself; every subsequent run is deterministic, cheap, and LLM-free, turning an ad hoc query into a shareable self-serve tool.

Use when:
- Building an internal natural-language analytics or BI tool where the same questions recur and answers must stay trustworthy.
- Deciding whether the LLM should stay in the loop on every query or compile a stable tool once.

Details:
- WorkOS's Studio lets anyone ask a business question against Snowflake, Linear, and Notion and either get an answer or promote it into a widget: sandboxed code bundling the UI, the APIs, and the query into one fully usable tool. (06:15-06:34)
- Once the widget is created it is reliable and live: hitting refresh reruns the underlying query for new time slices, and the LLM is no longer involved until the user asks to change the widget (add a column, fix a visual bug). (06:46-07:01, 16:18-16:39)
- The widget is ordinary JavaScript that makes the underlying API/tool calls directly, so user inputs (e.g. an email to search) are passed as normal function arguments rather than re-parsed by the LLM, removing a class of nondeterminism. (16:08-16:58)
- Widgets can combine data from multiple tools into one interface, and because they are code they can be shared internally so a support team self-serves in Slack instead of a platform or data team building and maintaining dashboards. (07:07-09:51, 15:48-16:02)
- Economically, declarative widgets pay the LLM cost only at generation time, not on every run, so caching is largely unnecessary; the team still pays for generation because Opus's quality is worth more than the cost saved by a weaker model. (18:10-18:43)
- This is the opposite trade from prompt-coded behavior: instead of leaving probabilistic logic in the prompt, the agent emits deterministic code once and freezes it, accepting that any change requires re-invoking the model.
- **The same compile-once shape in CI automation, with the canonical artifact deliberately inverted.** GitHub's agentic workflows have a person describe a standing job in English and compile it into a GitHub Actions workflow that the runner executes — an LLM produces the artifact once, deterministic machinery runs it thereafter. The difference worth noting is which side is treated as source. Here the deterministic widget becomes the thing you keep, inspect, and edit; there the generated YAML is a build output nobody looks at and the English stays canonical: "the markdown is the source code. The YAML is like a compiled artifact… If you don't like the way that the automation works, just edit the English." Both bets are defensible and they trade differently: an editable deterministic artifact is reviewable and drifts from its description, while an always-recompiled one stays honest to its description and is never reviewed. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 05:38-06:58, 10:20-10:35)

Related topics:
- [Business Intelligence](../topics/business-intelligence.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Validate Generated SQL by Execution Before Trusting It](validate-generated-sql-by-execution-before-trusting-it.md)
- [Inject Tool Context Just-in-Time During Agent Sequencing](inject-tool-context-just-in-time-during-agent-sequencing.md)
- [Start GenBI with certified assets before autonomous SQL](start-genbi-with-certified-assets-before-autonomous-sql.md)
- [Prompt-coded product behavior reduces code but weakens hard guarantees](prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md)
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)
- [The Markdown Workflow Is the Source; the YAML Is a Compiled Artifact](the-markdown-workflow-is-source-the-yaml-is-a-compiled-artifact.md)

Sources:
- [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](../sources/20260611_iUWwcG-C8OU.md), 06:15-09:51, 15:48-18:43
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 05:38-06:58, 10:20-10:35
