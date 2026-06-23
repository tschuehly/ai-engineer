# Declare Every External Domain Your MCP App Touches

Summary: An MCP-app view runs inside a nested host iframe whose content-security-policy is rewritten from the app's declared metadata, so any external domain the view calls that is not declared in the app's CSP directives will be blocked, breaking the app in production or getting it rejected from the store.

Use when:
- Shipping a ChatGPT-app / MCP-app view that fetches data, scripts, images, or other frames from external domains.
- Debugging an MCP app that works in a dev preview but fails or is rejected once submitted to the host's app store.

Details:
- Because the view is rendered inside the double-iframe sandbox, the host rewrites the app's CSP from the metadata the developer declares; undeclared domains are not rewritten correctly and the call is blocked. (14:00-14:49)
- Declare every domain the app depends on in the MCP app metadata. The most important directives are `connect-src` (external API calls the view makes) and `script-src`; image, frame, and base directives also exist but matter less for typical apps. (14:00-14:49)
- Failure mode: OpenAI's developer mode removed all CSP up to now, so a view that calls undeclared domains works fine in dev and only breaks when it reaches production with the real CSP enforced — a dev/prod parity trap. (14:49-15:50)
- The speaker reports many ChatGPT app-store submission rejections and production failures caused specifically by missing CSP domains, making domain declaration a routine submission blocker rather than an edge case. (19:00-19:15)
- Tooling can close the gap before submission: Alpic's open-source Skybridge ships a CSP inspector that lists the domains declared in metadata versus the domains the view actually calls at runtime and flags any missing ones live as the component re-renders, so a developer adds the domain and re-checks before shipping. (15:50-19:00)
- Skybridge more broadly is a superset over the official Apps SDK adding end-to-end type safety between the MCP server and the app widgets/views plus polyfills for host-specific (ChatGPT) APIs not in the common spec. (15:50-16:23)

Related topics:
- [Tools](../topics/tools.md)
- [Security](../topics/security.md)

Related concepts:
- [Render Third-Party Generative UI Through a Double Iframe](render-third-party-generative-ui-through-a-double-iframe.md)
- [MCP Applications Ship UI and Tools Together](mcp-applications-ship-ui-and-tools-together.md)
- [Harden Third-Party MCP Tools Against Silent Failure and Endpoint Risk](harden-third-party-mcp-tools-against-silent-failure-and-endpoint-risk.md)

Sources:
- [Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic](../sources/20260615_c-2eEv2ou7Y.md), 14:00-19:15
