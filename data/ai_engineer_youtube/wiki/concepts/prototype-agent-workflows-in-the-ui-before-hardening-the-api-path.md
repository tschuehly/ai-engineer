# Prototype Agent Workflows in the UI Before Hardening the API Path

Summary: For agent products that expose both a web UI and an API, start by proving the workflow in the UI, then encode the stable request, context, permissions, and delivery path in the API integration. This avoids hardening an API path before the agent task shape is understood.

Use when:
- Turning a repeated manual prompt or web-app workflow into an API-backed automation.
- Deciding what context, files, connectors, task state, and callbacks an integration really needs.

Details:
- In Q&A, Ivan recommends first trying repeated work in the web app because the UI already has integrations and webhooks set up; if Manus completes the task reliably there, then move to API testing (73:22-73:43).
- The API-hardening step is to test requests, identify required context, and get the request shape nailed down consistently before treating the workflow as an integration contract (73:43-73:56).
- The conference-site demo also shows the UI path as an iterative design and implementation loop: ask for scraping, search, mobile support, calendar/star actions, try providers, and refine until the output works (74:44-75:20).
- This pattern should not be read as proof that every UI success is safe to automate; the same source notes browser permission design is still required before user-local browser actions can be exposed through the API (78:43-79:21).

Related topics:
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use hosted model playgrounds to prototype before owning infrastructure](use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md)
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)

Sources:
- [Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)](../sources/20251230_xz0-brt56L8.md), 73:22-79:21
