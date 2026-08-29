# Curate Context Strategically Because Models Drop the Middle

Summary: Current LLMs attend to the start and end of a prompt and quietly drop the middle (a "U curve"), so dumping a whole codebase or every source makes results worse, not better. The fix is to select context with a deliberate strategy, chosen by developer-input cost and how it scales, rather than asking the model to be smart enough to find what matters in a giant prompt.

Use when:
- Deciding whether to paste a whole codebase or all sources into an agent versus building a selection layer.
- Choosing among a context engine, summarization, knowledge graph, iterative retrieval, or self-correction for supplying agent context.
- A larger context window did not improve agent reliability and you suspect mid-prompt context is being ignored.

Details:
- The U-curve failure mode: the model takes the initial inputs and the last inputs but the in-between context is "basically removed"; mid-prompt additions such as "I have Jira, I have MCPs, can you look into that" get purged so the model can make sense of the task by itself. Qodo observes this when benchmarking which provided context actually shows up in the result, and stresses that growing the window did not fix it. (02:57-04:31)
- Context engine (a "bouncer"): builds a search pattern and ranking logic so it can tell the agent "this is more important." Good for a large messy codebase; indexing is moderate effort, but **scaling is the hard part** — at 600-700 repositories the mapping and indexing slow down and become unpredictable unless the team is dedicated to building a context engine. (05:00-06:01)
- Hierarchical summarization: a summary per file and folder so the agent reads summaries to decide relevance before reading code. Cost is high upfront LLM processing plus re-mapping on every file create or change. (06:09-06:43)
- Knowledge graph: complex to build (very high initial developer time, graph DB hosting) but "works wonders" when there are logical dependencies — file A impacts B impacts C — or dependencies spanning multiple repos. (06:44-07:13)
- Iterative retrieval: instead of a summary it builds an index, "a library card you give your agents" (here is the topic; if it's relevant, look deeper into the code). Has cost impact but needs low developer energy and input, and is the speaker's default for teams building agents for themselves rather than as a product. (07:14-07:53)
- Self-correction: a critic node checks whether output is still relevant to the initial goal and triggers a retry when context is lost. Adds latency from re-running the agent but needs little initial developer input. (07:57-08:30)
- Decision shape: pick the strategy by developer-input cost versus scaling and whether you are a product company — knowledge graphs and context engines pay off only when dependencies or corpus messiness justify the build, while iterative retrieval and self-correction win when you want low setup cost.

- **A second, non-attentional reason to curate — and it is the one that holds when the window is not full.** The U-curve argument says the model attends poorly to a long prompt's middle. Werry adds a task-level version that does not depend on attention mechanics at all: irrelevant-but-real organizational context makes the agent "get distracted… if you give them things that cause them to look this way in that way," spending tokens and turns chasing threads that belong to another task. Both arguments point at selection, but they predict different failures — dropped facts versus pursued digressions — and a fix that solves one need not solve the other. ([Werry](../sources/20260827_qdAkxLoYNI8.md), 05:52-06:20)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Agentic retrieval lets models plan search steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Reconcile Specialist Agent Outputs With a Feedback-Weighted Judge](reconcile-specialist-agent-outputs-with-a-feedback-weighted-judge.md)

Sources:
- [Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo](../sources/20260608_EcqMYoIV57A.md), 02:57-08:30
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 05:52-06:20
