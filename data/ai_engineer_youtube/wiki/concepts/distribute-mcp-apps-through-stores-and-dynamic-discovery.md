# Distribute MCP Apps Through Stores and Dynamic Discovery

Summary: The client stores (ChatGPT apps, Claude connectors, Cursor directory) turned MCP servers and Apps into a one-click, self-serve distribution channel, and dynamic discovery — where the client searches the MCP registry for the right connector when a task has no matching tool — makes store presence a high-intent organic acquisition channel, not just a directory listing.

Use when:
- Deciding how to distribute an MCP server or App to end users instead of sharing a raw JSON config.
- Treating agent-client presence as a go-to-market channel and weighing the effort to be the connector a model selects.
- Preparing an MCP server for store submission and vetting.

Details:
- The stores opened quietly at the end of 2025 (Character AI and Claude) and are now accepting more apps after an initial design-partner-gated phase; the speaker frames the store opening as a bigger shift than the UI capability itself. (03:44-05:31, 05:34-06:00)
- Three main surfaces support self-serve submission: ChatGPT (chatgpt.com/apps), Claude (connectors directory), and Cursor (directory). Both plain MCP servers and MCP Apps are eligible — a UI is not required. (21:41-23:00)
- Submission flow: link your remote MCP server; the store scans tools for correct annotations and arguments, and checks that declared authentication works; you provide test cases and prompts; the app is tested partially manually / partially automatically and accepted or rejected. ChatGPT currently accepts faster than Claude. (23:00-24:06)
- The install-time payoff: once accepted, users install in one click from a store URL you can send directly to customers — "no more sharing that ugly JSON file" with your MCP configuration. (24:06-24:59)
- **Dynamic discovery** is the real acquisition unlock: Claude is currently the only client doing it — when assigned a task with no specific tool, it searches the MCP registry for the right connector to complete the task. With 1B+ active users expressing intent in chat, being the connector the model selects is "a huge wave of high-intent individuals" who find your product dynamically and organically; ChatGPT is expected to add this soon. (24:59-26:07)
- Positioning thesis: Paul Graham's "AI apps are the new browsers" — if AI apps (Claude Code, Codex, Claude Cowork) are the new browsers, then ChatGPTs are the new websites and, like a website, can return a UI via MCP Apps; the speaker treats "does this product have an MCP server" as a basic buying decision. (26:07-28:28)
- Tooling can front-run the vetting: Manufact (manifact.com) runs the checks the stores will run pre-submission and generates required artifacts (screenshots, test cases) from a connected MCP server. (24:06-24:59)
- **Registry presence stated as a go-to-market instruction, with the second half attached.** "You want to make sure your product is where the agents are… You're going to market. So, go go to agent market… make sure you're in the marketplace in the MCP registries, everywhere that you would expect an agent to be able to easily find you." Jarmak pairs it immediately with adoptability, because the two fail independently: being listed does nothing if the path from discovery to "embedding it in their workflow" runs through demos and sales email. See [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 12:12-12:53)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Tools](../topics/tools.md)

Related concepts:
- [MCP Applications Ship UI and Tools Together](mcp-applications-ship-ui-and-tools-together.md)
- [Use MCP App Primitives for Bidirectional Model–UI State](use-mcp-app-primitives-for-bidirectional-model-ui-state.md)
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)
- [Agent Experience Prioritizes APIs, CLIs, and MCP Over Dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md)

Sources:
- [MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc](../sources/20260705_sAOBXCDiDOs.md), 03:44-28:28
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 12:12-12:53
