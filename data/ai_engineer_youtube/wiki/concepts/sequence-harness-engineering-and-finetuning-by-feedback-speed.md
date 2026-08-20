# Sequence Harness Engineering and Fine-Tuning by Feedback Speed

Summary: Choose your next improvement lever by how fast it answers, not by how powerful it sounds — harness engineering returns a result in about two minutes, so exhaust its ceiling first, fine-tune only to break through that ceiling, then return to harness engineering on top of the new model.

Use when:
- A team is debating "should we fine-tune?" before the prompt and harness work has saturated.
- Planning the order of work on an agent that is close to but not at the quality bar.
- Someone treats fine-tuning as the terminal step rather than one rung in a repeating loop.

Details:
- The decision criterion is feedback latency: "if you need to do something for improving your agent, the best thing that you can do is collect feedback as quickly as possible, like either from humans labeling or just letting the agents run. So, like harness engineering gives you feedback in maybe 2 minutes." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 15:58-16:27)
- The ceiling is real and recognizable: "harness engineering is amazing. You get instant feedback and you can sort of like run on your evals, but eventually what we find is you hit a threshold of intelligence where it's like 'If I keep tweaking this prompt, I'm not going to get too much more out of it.'" ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 08:58-09:20)
- **The sandwich**: "try harness engineering, try to do fine-tuning to sort of like break through that ceiling, and then do more harness engineering again if you need to." Fine-tuning raises the ceiling; it does not end the loop. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 16:27-16:51)
- Most teams stop at the first layer, and that is treated as a good outcome rather than a failure of ambition: "we find a lot of teams are happy with harness engineering and it solves their customer use case, so we always sort of recommend it." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 16:34-16:44)
- What the fine-tuning rung actually targets is a narrow vertical, not general capability: "they don't really care about the entire variance of tasks. Like they care about what their customers care about. So, if we focus on that narrow set of tasks, then we can fine-tune base models to sort of like reach and then also go beyond frontier performance." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 09:20-09:48)
- How this composes with the wiki's other fine-tuning triggers: [Decide when to fine-tune from three business signals](decide-when-to-fine-tune-from-three-signals.md) gives the *business* conditions (API cost exceeds revenue, eval plateau, latency/throughput ceiling) and this gives the *sequencing* rule. The eval-plateau signal is the same phenomenon named from the outside; feedback speed explains why you should reach that plateau by the cheapest route available.
- The same logic applied at a smaller granularity is already in the wiki as a rule about change size: prefer the change whose feedback arrives soonest ([Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)).
- Provenance: LangChain sells fine-tuning of open models as a service, which makes the recommendation to *stop* at harness engineering an argument against the speaker's commercial interest and correspondingly more usable.

Related topics:
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Decide When to Fine-Tune From Three Business Signals](decide-when-to-fine-tune-from-three-signals.md)
- [Prefer Model-Portable Agentic Prompts Before Fine-Tuning](prefer-model-portable-agentic-prompts-before-fine-tuning.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Read the Frontier Model's Traces to Harness-Engineer Its Cheap Replacement](read-frontier-traces-to-harness-engineer-a-cheap-replacement.md)
- [Treat Agent Improvement as Model-Harness-Task Fit](treat-agent-improvement-as-model-harness-task-fit.md)
- [Invest in the Harness to Run Weaker and Local Models](invest-in-the-harness-to-run-weaker-and-local-models.md)

Sources:
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 08:58-09:48, 15:58-16:51
