# Reach Private MCP Servers With Outbound-Only Tunnels

Summary: A hosted agent that needs to call an MCP server inside a customer's network does not require an inbound path into that network. Invert the direction: the MCP server runs "only within their private network and only making outbound calls to the Claude agent loop." The private side dials out and holds the connection open, so there is no listener, no exposed endpoint, and no inbound firewall rule to justify.

Use when:
- A hosted or vendor-run agent must reach internal tools, databases, or services behind a corporate perimeter.
- A security review is blocking an agent integration because it requires opening a port or publishing an endpoint.
- Deciding between VPN peering, an exposed gateway, and a tunnel for agent-to-internal-tool connectivity.

Details:
- **The claim.** Customers can run MCP servers that "run only within their private network and only making outbound calls to the Claude agent loop." The agent loop never initiates a connection inward; the tunnel is established from the protected side. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 26:10-26:34)
- **Why the direction is the whole security argument.** An inbound path is a permanently reachable attack surface that must be authenticated, patched, rate-limited, and monitored on its own. An outbound-only tunnel has none of those properties because nothing is listening: an attacker who wants in has to compromise the far end first, and the private network's egress rules — which the customer already operates — are the control point. This is the same reframing that appears elsewhere in the wiki for [enforcing egress policy at the wire protocol](enforce-agent-egress-policy-below-the-http-layer.md): put the control where the connection is initiated.
- **What travels with it.** The talk pairs tunnels with self-hosted sandboxes — "the hands can run anywhere, including in your virtual private cloud," with customers who "control their sandbox control plane." Read as a pair, these are two ways of answering the same question (how does a hosted agent touch things it isn't allowed to hold): move the execution to the data, or move the connection direction. They are alternatives with different tradeoffs, not a stack. (25:47-26:34)
- **What the inversion does not change.** The tunnel controls *reachability*, not *authority*. Once established, the agent can call every tool that MCP server exposes, and the connection direction has no bearing on whether a prompt injection can make it call a destructive one. Pair it with credential handling that keeps secrets out of the model ([decrypt only at tool execution time](decrypt-agent-credentials-only-at-tool-execution-time.md)) and with a policy on what the exposed tools can do.
- **The operational cost, unmentioned in the source.** A persistent outbound tunnel is a component someone has to run: it reconnects, it has a failure mode where the agent's tools silently vanish mid-session, and it concentrates access — whatever the tunnel can reach, the hosted agent can reach. None of that is discussed.
- Provenance: an Anthropic vendor talk, delivered as one of four "lessons learned" in roughly forty seconds. There is no protocol detail, no authentication description for the tunnel itself, no availability discussion, and no threat model. Record the architectural pattern; the implementation specifics are not in the source.

Related topics:
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Enforce Agent Egress Policy at the Wire Protocol, Below HTTP](enforce-agent-egress-policy-below-the-http-layer.md)
- [Decrypt Agent Credentials Only at Tool Execution Time](decrypt-agent-credentials-only-at-tool-execution-time.md)
- [Move Agent Access Control to the Network Layer So the Sandbox Holds No Credential](move-agent-access-control-to-the-network-layer.md)
- [Decouple the Agent Loop From the Tool Execution Environment](decouple-the-agent-loop-from-the-tool-execution-environment.md)
- [Model a Managed Agent as Agent, Environment, and Session](model-a-managed-agent-as-agent-environment-session.md)

Sources:
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 25:47-26:34
