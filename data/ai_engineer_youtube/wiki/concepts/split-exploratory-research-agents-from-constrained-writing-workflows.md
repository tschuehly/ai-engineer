# Split Exploratory Research Agents From Constrained Writing Workflows

Summary: Research and writing often need different architectures. Use an exploratory agent to gather and summarize evidence, then pass a durable artifact into a constrained writing workflow with guidelines, examples, and review loops.

Use when:
- Turning open-ended research into polished technical content.
- Deciding whether two adjacent AI tasks should share one agent or communicate through artifacts.

Details:
- The workshop identifies a conflict: research needs flexibility, while writing needs constraint; the resulting architecture splits a dynamic research agent from a deterministic writing system. 25:56-26:14
- The research agent writes a `research.md` artifact with summarized findings, and the writing workflow consumes it along with guideline Markdown, profile/static files, and few-shot examples. 27:39-28:10, 01:11:21-01:13:17
- The two systems can run sequentially through a basic script rather than a heavyweight orchestrator when users normally run research first and writing second. 27:30-28:05
- For writing, a separate reviewer context can critique the draft against user guidelines, research, structure, terminology, and profiles, reducing the bias of a model reviewing its own output. 01:21:38-01:22:30
- Keeping intermediate versions helps because writing remains subjective; aggressive reviewer loops or hard score thresholds can make creative work noisy and less reliable. 01:22:38-01:23:44

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Collaborate with complex agents through high-bandwidth artifacts](collaborate-with-complex-agents-through-high-bandwidth-artifacts.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)

Sources:
- [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../sources/20260420_mYSRn6PC1mc.md), 25:56-28:10, 01:11:21-01:23:44
