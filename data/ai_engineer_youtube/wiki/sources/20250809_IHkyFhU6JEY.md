# Designing AI-Intensive Applications - swyx

Source: [Designing AI-Intensive Applications - swyx](https://www.youtube.com/watch?v=IHkyFhU6JEY)
Uploaded: 2025-08-09
Transcript: `raw/20250809_IHkyFhU6JEY/IHkyFhU6JEY.en-orig.vtt`

## Summary

swyx frames AI engineering as a young discipline still searching for durable "standard models" like MVC, CRUD, ETL, and MapReduce. The talk argues that agent versus workflow terminology is less useful than measuring how much valuable AI output an application can produce per unit of human input, and proposes the SPADE pattern for AI-intensive applications that synchronize sources, plan, analyze in parallel, deliver artifacts, and evaluate results.

## Extracted Concepts

- [Standard models guide AI engineering practice](../concepts/standard-models-guide-ai-engineering-practice.md) - this source argues that AI engineering needs reusable mental models beyond RAG.
- [Measure AI intensity by human input to valuable output](../concepts/measure-ai-intensity-by-human-input-to-valuable-output.md) - this source reframes agent/workflow debates around output produced per human input.
- [SPADE structures AI-intensive workflows](../concepts/spade-structures-ai-intensive-workflows.md) - this source proposes a sync, plan, analyze, deliver, evaluate loop for applications that make many AI calls.

## Topic Links

- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

## Notes

- The talk treats AI engineering as a forming discipline where the important task is finding standard models that can guide many applications, analogous to common engineering patterns such as ETL, MVC, CRUD, and MapReduce. (04:55-05:58)
- Candidate AI engineering standard models include an LM OS updated for multimodality, tools, and MCP, an LLM-shaped SDLC, and received wisdom around building effective agents. (06:00-08:04)
- The speaker cautions that RAG is useful but not a full answer to AI application design, especially as long context and fine-tuning compete with retrieval-heavy designs. (05:37-05:58)
- The talk argues that the workflow-versus-agent label is less important than the ratio between human input and valuable AI output, ranging from autocomplete and chat to reasoning models, deep research, and ambient agents with no immediate human prompt. (08:49-10:35)
- AI News is presented as a workflow, not necessarily an agent: it repeatedly scrapes sources, plans, recursively summarizes, formats, and evaluates. (10:37-10:57)
- Generalizing that workflow yields SPADE: synchronize inputs, plan, process/analyze in parallel, reduce and deliver a user artifact, then evaluate. (11:05-11:35)
- The SPADE loop can produce knowledge graphs, structured outputs, or code artifacts rather than only text responses. (11:36-12:00)
