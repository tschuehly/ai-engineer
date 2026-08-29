# Keep a Protocol Boundary So the Browser Backend Stays Swappable

Summary: When an agent drives a browser through a standard protocol surface rather than a library it embeds, the browser itself becomes a replaceable component. A local automation browser that keeps drawing CAPTCHAs can be swapped for a hardened remote one behind the same interface, with no change to the agent, the prompts, or the tool definitions.

Use when:
- Choosing between embedding a browser automation library in the agent process and driving one through an MCP server or equivalent protocol surface.
- A browser agent works on friendly pages and fails on defended ones, and the fix is infrastructural rather than logical.
- Evaluating a managed browser vendor, where drop-in compatibility with an existing protocol surface is the migration cost.

Details:
- **The swap.** Both the failing implementation and the rebuilt one use "Playwright MCP with a browser and a large language model"; the checkout stage's logic is identical. The only difference is what sits behind the protocol: "I just connected Oxylabs' headless browser — since it supports Playwright MCP it's just a drop in replacement." ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 11:54-12:58)
- **What the swap bought.** "Proper stealth done at the browser source code level, a residential proxy attached to it out of the box, and… a geolocation capability." Stealth *at the source level* is the load-bearing phrase: it is a property of the browser build, which is precisely the kind of thing you cannot add to an embedded library from the agent side, and precisely the kind of thing a boundary lets you buy. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 12:58-13:20)
- **The general principle.** The protocol boundary partitions the problem into what the agent decides and what the environment provides. Everything on the agent's side — tool names, prompts, the action vocabulary, the recorded flow — survives a change of provider, and everything on the environment's side (fingerprint, IP reputation, exit location, render fidelity) becomes a procurement decision rather than a code change. That partition is what makes vendor comparison meaningful at all; without it, "try a different browser provider" is a rewrite.
- **Why this stage in particular.** Checkout is the one stage the same source refuses to move off a browser, because "we need to process inputs and the content is highly dynamic," and it is also where the counterparty is most adversarial. So the stage with the least architectural freedom is the one that most needs a swappable backend — the boundary is worth most exactly where the primitive cannot be replaced. See [Assign a Web-Access Primitive Per Pipeline Stage](assign-a-web-access-primitive-per-pipeline-stage.md). ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 11:54-12:37)
- **What the boundary does not give you.** Interface compatibility is not behavioural equivalence: a different browser build with a different fingerprint, proxy pool, and exit location will render and be treated differently, which is the whole point of swapping it and also why a swap invalidates anything calibrated against the old environment — recorded selectors, timing assumptions, and the run-to-run determinism argued for in [Hold the Browser Environment Constant Across Runs](hold-the-browser-environment-constant-across-runs.md). "Drop-in" describes the wiring, not the results.
- **Caveat.** The evidence is one sentence in a vendor talk, asserting that its product implements Playwright MCP. Nothing is measured before or after the swap, and no compatibility limits are named.

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Assign a Web-Access Primitive Per Pipeline Stage](assign-a-web-access-primitive-per-pipeline-stage.md)
- [Hold the Browser Environment Constant Across Runs](hold-the-browser-environment-constant-across-runs.md)
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [Adapt Third-Party MCP Servers to the Agent Workflow](adapt-third-party-mcp-servers-to-the-agent-workflow.md)
- [Keep Geolocation Consistent Across Pipeline Stages](keep-geolocation-consistent-across-pipeline-stages.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)

Sources:
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 11:54-13:20
