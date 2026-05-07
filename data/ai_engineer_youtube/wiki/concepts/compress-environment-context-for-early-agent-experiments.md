# Compress Environment Context For Early Agent Experiments

Summary: When model context limits block an agent demo, shrink or decompose the environment representation before abandoning the idea. The right intermediate representation can make an otherwise impossible exploratory agent loop runnable.

Use when:
- Prototyping browser, GUI, or code-generation agents under tight context-window limits.
- Deciding whether an apparent model failure is really a context-representation failure.

Details:
- Early GPT-3 app-generation demos could not generate a whole application in one prompt, so Shameem split the request into parallel prompts for different components and joined them in the background. (03:56-04:14)
- A browser-shopping demo could not pass a raw Walmart page into the model because the page was around 24,000 tokens, far beyond the available context budget. (04:54-05:03)
- The workaround was a custom HTML parser that reduced a page to its core essence so it could fit into GPT-3's tiny context window. (05:06-05:15)
- The demo still failed by getting distracted by terms of service, but that failure was evidence about the model and environment interface rather than a reason to stop probing browser agency altogether. (05:15-05:29)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)

Sources:
- [On Curiosity -- Sharif Shameem, Lexica](../sources/20250719_0F8mnGPUycY.md), 03:56-05:29
