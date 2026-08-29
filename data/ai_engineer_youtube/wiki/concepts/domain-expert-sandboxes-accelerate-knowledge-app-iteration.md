# Domain-expert Sandboxes Accelerate Knowledge-app Iteration

Summary: Enterprise knowledge-app platforms should let domain experts iterate on extraction templates, prompts, model strategies, validation rules, and run comparisons directly, because much of the useful document logic lives in operational expertise rather than engineering code.

Use when:
- Building document extraction, Q&A, or workflow apps for teams with specialized business rules.
- Prompt and extraction logic changes faster than a central engineering team can safely encode by hand.

Details:
- BlackRock found that complex financial documents make prompt engineering a domain-expert activity: a prompt can grow from a few sentences into several paragraphs that describe an instrument and its extraction rules. (04:03-04:35)
- The sandbox gives operators a place to build extraction templates, run extractions over document sets, compare outputs, and adjust model or LLM strategies before the workflow becomes a production app. (07:52-09:08)
- Useful extraction-template metadata goes beyond field names and prompts: operators may need data types, extracted-versus-derived source, required flags, interfield dependencies, validations, and multiple QC checks. (09:10-11:04)
- Domain experts still need education on LLM strategy selection because simple in-context extraction may work for small vanilla documents, while long documents or instrument-specific logic may require different retrieval, prompting, or model-provider strategies. (04:42-05:52)
- **What happens when one configurable sandbox will not stretch far enough.** BlackRock's experts iterate inside a surface the platform built and parameterized. DoorDash found their use cases too unlike for that — image annotation, menu grading, and manual testing did not share a screen — but similar enough underneath to share endpoints: "the underlying patterns were similar. So if we are API first we can actually enable our partners to simply vibe code these UIs for annotation." The choice between a parameterized sandbox and generated per-use-case apps turns on where the variation sits relative to the data model. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 08:39-10:01)

Related topics:
- [Workflows](../topics/workflows.md)
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Agentic Document Extraction Decomposes Complex Fields](agentic-document-extraction-decomposes-complex-fields.md)
- [Build Internal AI Engineering Platforms When Off-the-Shelf Tools Lack Enterprise Context](build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md)
- [Stage Complex AI Applications Into Inspectable Deterministic and Agentic Steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)

Sources:
- [How BlackRock Builds Custom Knowledge Apps at Scale — Vaibhav Page & Infant Vasanth, BlackRock](../sources/20250823_08mH36_NVos.md), 04:03-11:04
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 08:39-10:01
