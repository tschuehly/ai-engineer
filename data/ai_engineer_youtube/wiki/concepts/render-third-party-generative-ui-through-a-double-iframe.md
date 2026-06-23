# Render Third-Party Generative UI Through a Double Iframe

Summary: Embedding untrusted third-party app UI inside a chat host (ChatGPT, Claude) requires an outer iframe that loads one host-controlled loader script from a per-app subdomain, which injects the real app HTML into an inner `srcdoc` frame; every simpler single-iframe option fails an origin/CSP elimination chain.

Use when:
- Building or reasoning about MCP-app / ChatGPT-app UI ("views") that the host must render without exposing its own origin, storage, or cookies.
- Designing any platform that must run third-party HTML/JS inside its own trusted web app (marketplaces, embedded widgets, plugin surfaces).

Details:
- MCP-app UI is delivered as "views": small HTML/JS/CSS snippets rendered as the result of a tool call, advertised ahead of time on the `tools/list` call so the host can cache or fetch the resource and inject tool results into the rendered frame. (02:02-03:31)
- The host cannot just drop the view into one iframe. The elimination chain: an iframe `srcdoc` shares the parent origin and therefore ChatGPT's content-security-policy, so app scripts are blocked by ChatGPT's per-request script-nonce rule on `script-src`. (06:22-07:42)
- Relaxing the CSP to allow arbitrary scripts means the same-origin app code can read ChatGPT's origin-indexed `localStorage`/cookies and exfiltrate them — unacceptable for the host. (07:42-08:22)
- Adding the `sandbox` attribute moves the frame to an opaque (null) origin so it cannot reach the parent DOM, but that also breaks every origin-indexed capability the app needs: `localStorage`, IndexedDB, and cookies all stop working. (08:22-09:12)
- Adding `allow-same-origin` to restore storage hands the frame the parent origin again — the classic sandbox escape, back to reading parent DOM, storage, and cookies. (09:12-09:36)
- Pointing an iframe `src` at each app's own server would force the host to add every new app's domain to `frame-src` forever, which does not scale; a single host-owned proxy domain (e.g. `openaiusercontent.com`, routing by subdomain prefix) avoids the CSP churn but makes the host serve untrusted third-party code on its own domain and demands heavy dynamic-serving infrastructure non-frontier hosts may not have. (09:36-12:07)
- The surviving design is the double iframe: the outer frame loads one identical lightweight loader script (same for every app) from a dedicated domain different from the host; that script initiates an inner `srcdoc` iframe holding the real app HTML. The loader is served on per-app subdomains so each app gets a distinct origin and their `localStorage`/cookies cannot collide (app ABC123 cannot read app ABC456's storage); infra stays cheap because the same script content is served on every subdomain. (12:07-13:16)
- The app's own CSP is delivered through a meta tag inside the first iframe per the MCP spec, letting the view restrict its own script execution and frame rendering. (13:16-13:39)
- This is not a new invention — Facebook first shipped the same nested-frame approach for its app marketplace, which faced the identical problem of running third-party UI inside its own trusted app context. (13:42-14:00)

Related topics:
- [Tools](../topics/tools.md)
- [Security](../topics/security.md)

Related concepts:
- [Declare Every External Domain Your MCP App Touches](declare-every-external-domain-your-mcp-app-touches.md)
- [MCP Applications Ship UI and Tools Together](mcp-applications-ship-ui-and-tools-together.md)
- [Merchant-Owned Generative Surfaces Travel Into Chat Interfaces](merchant-owned-generative-surfaces-travel-into-chat-interfaces.md)

Sources:
- [Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic](../sources/20260615_c-2eEv2ou7Y.md), 02:02-14:00
