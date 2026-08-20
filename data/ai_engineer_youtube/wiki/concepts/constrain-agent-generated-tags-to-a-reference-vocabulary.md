# Constrain Agent-Generated Tags to a Reference Vocabulary

Summary: An agent that labels documents will invent a new label almost every run unless you hand it the existing vocabulary as a file and instruct it to be reluctant to extend it — the failure is not bad labels but a vocabulary that grows monotonically until nothing groups.

Use when:
- Having an agent tag, categorize, or file notes, tickets, meeting records, or assets on a repeating schedule.
- Debugging a knowledge base where filtering by tag returns almost nothing because near-duplicate tags proliferated.
- Designing any batch pass where the agent both reads and writes the taxonomy it uses.

Details:
- The mechanism is a file, not a prompt paragraph: "I actually put all of my tags into this little reference folder over here. That way the agent isn't inventing new tags every time it goes through and tries to add more detail. This gives it a concrete list of things to look through." ([LLM Knowledge Bases](../sources/20260812_I3bpdgFJCUY.md), 06:58-07:13)
- The behavioral instruction is explicit and is aimed at a known model tendency: "I actually instruct the agent to be reluctant to add new tags because Claude loves to get creative. Uh so just telling it please don't do that." Reuse is stated as the default; invention is the exception. (07:13-07:21)
- The escape hatch keeps the vocabulary alive rather than frozen: "if you really find a pattern, go ahead and add something to this list. You can go ahead and do that." The agent may append to the reference file, which means the next run inherits the extension — the vocabulary evolves through a controlled write path instead of drifting through unrecorded per-run invention. (07:21-07:27)
- Why this matters more for agents than for humans: a person tagging notes carries the existing vocabulary in their head and matches against it implicitly. A stateless per-note agent run has no such memory, so absent an explicit vocabulary file every run is a fresh act of naming. Materializing the tag list is what gives the pass memory of its own past decisions — the same move as [stamping processing state into the artifact](stamp-processing-state-in-the-artifact-to-make-agent-passes-resumable.md), applied to the label space instead of to progress.
- The retrieval stake is stated in the talk's own framing of why tags exist at all: "tagging things based on categories so that you can find them or so agents can find them." A vocabulary that splits into synonyms defeats both readers. (02:13-02:19)
- Generalizes past tags. The same shape — hand the agent the closed set, make extension deliberate — is what [schema-first classification](schema-first-classification-turns-llms-into-enterprise-categorization-tools.md) does for enterprise categorization, and the inverse case is instructive: when you *want* the label space discovered rather than fixed, an unsupervised tagger is the right tool, not a constrained one. See [Use sparse autoencoder features as an unsupervised data tagger](use-sparse-autoencoder-features-as-an-unsupervised-data-tagger.md).
- Caveat: the talk reports no measurement of drift with or without the reference file, no count of how often the agent takes the escape hatch, and no review step over vocabulary additions. In a shared or long-running setting, an agent-appendable tag list needs someone to prune it — the source does not address that.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Stamp Processing State in the Artifact to Make Agent Passes Resumable](stamp-processing-state-in-the-artifact-to-make-agent-passes-resumable.md)
- [Materialize Backlinks at Ingest With Key-Term Search](materialize-backlinks-at-ingest-with-key-term-search.md)
- [Schema-first classification turns LLMs into enterprise categorization tools](schema-first-classification-turns-llms-into-enterprise-categorization-tools.md)
- [Use sparse autoencoder features as an unsupervised data tagger](use-sparse-autoencoder-features-as-an-unsupervised-data-tagger.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)

Sources:
- [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../sources/20260812_I3bpdgFJCUY.md), 02:13-02:19, 06:58-07:27
