# Wrap Generic Tool Descriptions With Use-Case Guidance

Summary: A tool wrapper can preserve an upstream tool's implementation while replacing its description with task-specific operational guidance. This lets the agent use the same callable function with better local instructions.

Use when:
- A public MCP tool is functionally useful but its description is too generic for the agent's task.
- An agent needs to prefer one tool sequence over another without changing the upstream server.

Details:
- Tool descriptions tell agents when and how to use callable integration code, so shallow descriptions such as "press a key" or "resize the browser window" leave too much task judgment to the model. 02:29-02:45, 11:20-12:22
- The demo wrapper kept the original Playwright function behavior and only created a new tool object with an enhanced description. 18:39-21:39
- Rewritten descriptions can encode local operating rules, such as using the accessibility snapshot before hover or click and preferring it over a visual screenshot for page understanding. 19:35-20:37
- Longer descriptions are not always a problem; they can add context when the added guidance improves tool selection more than the extra prompt cost hurts it. 39:57-40:17
- **The upstream vendor's side of the same repair, and the ledger that decides how long a description may be.** This page's wrapper is what a consumer does when they cannot change the server. Jarmak describes the vendor doing it at the source: read benchmark traces, find where the model's training priors fought the schema, and fix the description so the guess never happens. The cost side is stated by the buyer rather than guessed — organizations evaluate a tool on "how many tokens is the agent dealing with to work with your tool? And how fast is it?" — which gives the "longer descriptions are not always a problem" judgment above a measurable form: added description tokens are worth it when they remove more burned turns than they cost. See [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 06:33-07:38)

Related topics:
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Use Tool Names and Descriptions as Operational Prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Adapt Third-Party MCP Servers to the Agent Workflow](adapt-third-party-mcp-servers-to-the-agent-workflow.md)
- [Agent Skills Should Point to Current Docs Instead of Embedding Every API Detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md)
- [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md)

Sources:
- [Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz](../sources/20260408_U00AOI1eJUE.md), 02:29-22:24
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 06:33-07:38
