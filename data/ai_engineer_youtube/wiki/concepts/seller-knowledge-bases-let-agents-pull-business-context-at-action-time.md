# Seller Knowledge Bases Let Agents Pull Business Context at Action Time

Summary: A domain agent can replace brittle manual context forms with a seller- or customer-specific knowledge base that retrieves the right business context only when generating an action. This is useful when the agent needs many product, market, and proof-point details but each output should use only the subset relevant to the current target.

Use when:
- Designing agents that must speak for a company, seller, team, or product line using uploaded business materials.
- Reducing onboarding friction from manually entered product offers, value props, case studies, and pain points.
- Deciding whether to retrieve context at action time instead of stuffing all possible offers into the prompt.

Details:
- Alice needs seller context such as products, services, case studies, pain points, value props, and ICP, plus lead context such as role, responsibilities, attempted solutions, pain points, and company. The talk focuses on the seller-knowledge side. (02:24-03:06)
- The manual library flow required users to enter detailed offer descriptions before campaigns could run, which created onboarding friction and made email quality sensitive to whether users selected too few or too many offers. (03:09-04:47)
- The knowledge-base approach lets users upload seller source material and lets the agent pull the most relevant pieces at email-generation time. (04:49-05:09)
- This pattern is closer to onboarding a human SDR: give the worker source material once, then let them apply relevant context per message rather than asking the operator to preselect every offer for every campaign. (05:35-06:11, 20:21-20:36)

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Surface existing company information before redesigning processes](surface-existing-company-information-before-redesigning-processes.md)
- [Use connectors and uploads as private research context](use-connectors-and-uploads-as-private-research-context.md)

Sources:
- [Building Alice's Brain: an AI Sales Rep that Learns Like a Human - Sherwood & Satwik, 11x](../sources/20250729_KWmkMV0FNwQ.md), 02:24-06:11
