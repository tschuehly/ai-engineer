# Constrain Sensitive File Access With Purpose-Built Tools

Summary: Agent safety for sensitive files should be enforced with narrow tools, not broad read access plus prompt instructions. A purpose-built tool can expose the specific operation needed while keeping secrets out of model context and logs.

Use when:
- An agent needs to modify `.env` or other secret-bearing configuration files.
- A workflow requires file edits but should not upload file contents to a model provider or trace log.

Details:
- PostHog found that early wizard versions read `.env` files and risked sending sensitive contents into cloud inference or logs. 12:08-12:58
- The replacement was a narrow tool that could check whether a key exists and write a new value to a key, without sending `.env` contents through inference. 13:00-13:42
- The broader lesson is to decide which tools and read types are allowed, and to lock down access around sensitive file classes rather than assuming successful task completion means the method was acceptable. 13:00-13:57

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)
- [Hackable agent runtimes need tight safety boundaries](hackable-agent-runtimes-need-tight-safety-boundaries.md)

Sources:
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md), 12:08-13:57
