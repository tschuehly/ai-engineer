# Silent Web-Access Failure Produces Confident Hallucination

Summary: When an agent's web fetch is blocked, challenged, emptied, or poisoned, the model usually does not report the failure; because it is tuned to please, it falls back to stale training data or fabricates an answer and presents it as current. Treating "I searched the web" as proof of grounding is unsafe without evidence that real content was retrieved.

Use when:
- Debugging agents that confidently answer with outdated facts, dead links, or invented details from web-dependent tasks.
- Designing grounding, citation, and observability checks for agents that depend on the open web.

Details:
- The failure is invisible: there is no error and no warning, just a wrong answer. The agent receives a CAPTCHA or even an empty page, does not surface it, and makes something up, which is where most of the hallucinations come from. (02:07-02:23)
- The driver is a "need to please plus lack of data": the speaker would rather a model say "no, I can't," but it never does; it tries to make things up instead of admitting a blocked or empty fetch. (00:48-00:55, 02:23-02:27)
- A blocked agent often falls back to training data and presents it as the current situation, which is incoherent when the snapshot is two years stale (2024 data answering a 2026 question). (01:24-01:39)
- Concrete symptoms an evaluator can look for: fabricated numbers, citations that 404, and product links where the URL and product do not exist; the speaker claims roughly 60% of ChatGPT citations are not working. (02:23-03:01)
- Poisoned content makes it worse: an anti-bot "labyrinth" can feed the agent fake data instead of blocking it, so the model produces bigger, more plausible hallucinations from confidently wrong inputs. (10:04-10:18)
- The practical mitigation is to keep the agent from getting blocked in the first place so real content reaches the model, rather than trying to detect fabrication after the fact. (10:18-10:25)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)

Related concepts:
- [The Open Web Is Adversarial to Agent Access](the-open-web-is-adversarial-to-agent-access.md)
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [AI Search Providers Should Return Grounding Documents](ai-search-providers-should-return-grounding-documents.md)
- [Harden Third-Party MCP Tools Against Silent Failure and Endpoint Risk](harden-third-party-mcp-tools-against-silent-failure-and-endpoint-risk.md)
- [Evaluate whether models reject impossible or nonsensical premises](evaluate-whether-models-reject-impossible-or-nonsensical-premises.md)

Sources:
- [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](../sources/20260617_btxGmN8RvNU.md), 00:48-03:01, 10:04-10:25
