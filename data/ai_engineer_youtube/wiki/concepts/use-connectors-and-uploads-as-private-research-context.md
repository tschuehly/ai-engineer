# Use Connectors and Uploads as Private Research Context

Summary: Internal research agents can combine private connectors with uploaded files so they reason over both durable company knowledge and task-specific evidence. The agent output is more useful when policy, documents, receipts, screenshots, and other files are explicitly available as source context.

Use when:
- Building a company research or operations agent that must answer from private tools such as Notion, Microsoft 365, or custom MCP-style systems.
- Designing workflows where users upload evidence and expect the agent to compare it against internal policy or knowledge.

Details:
- The workshop says Manus can query sources such as Notion and custom MCP-style integrations, and that API users can provide keys, custom code, files, and toolkits for the agent to use (12:48-13:03, 72:22-72:41).
- The connector demo uses a Notion company-policy source and an uploaded receipt; Manus uses OCR to extract receipt details and then compares those details against policy context from Notion (69:08-70:24).
- The source frames this as useful for internal deep research APIs because the agent can repeatedly reference private sources the organization already maintains rather than requiring every answer to be self-contained in the prompt (69:43-69:59).
- Uploaded task files are ephemeral evidence unless the workflow explicitly writes results back; in the demo, the agent can update the right Notion page after identifying the relevant receipt and dates (70:44-71:24).
- Mendelevitch's enterprise deep research examples extend private research context to existing enterprise systems such as Jira, Notion, Google Drive, and SharePoint for on-demand onboarding guides and other document-heavy workflows. (04:17-04:47)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Surface existing company information before redesigning processes](surface-existing-company-information-before-redesigning-processes.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Enterprise deep research runs multi-step synthesis over private corpora](enterprise-deep-research-runs-multi-step-synthesis-over-private-corpora.md)

Sources:
- [Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)](../sources/20251230_xz0-brt56L8.md), 12:48-13:03, 69:08-72:41
- [Enterprise Deep Research: The Next Killer App for Enterprise AI — Ofer Mendelevitch, Vectara](../sources/20251124_fh9LgKXBGnQ.md), 04:17-04:47
