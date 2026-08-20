# Decrypt Agent Credentials Only at Tool Execution Time

Summary: Hold agent credentials in a vault and decrypt them "only when needed at tool execution runtime," so "the model never sees your security tokens." The property is not achieved by prompting or by redaction — it is a consequence of architecture: a secret can be kept out of the context window only if the thing that uses it runs somewhere the context window is not.

Use when:
- An agent needs to call authenticated APIs and someone proposes putting the token in the system prompt or in a tool result.
- Reviewing whether "the agent can't leak the key" is a property of the design or a hope about the model.
- Deciding what has to be true architecturally before a secrets policy is enforceable.

Details:
- **The claim.** Credentials live in vaults, "decrypted only when needed at tool execution runtime… the model never sees your security tokens." The model emits a tool call naming what it wants done; the execution layer resolves the credential, uses it, and returns only the result. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 22:25-22:47)
- **The precondition that makes it possible.** This only works if tool execution is not in the model's process — which is exactly what [decoupling the agent loop from the tool execution environment](decouple-the-agent-loop-from-the-tool-execution-environment.md) provides. In a coupled harness the secret has to be reachable from wherever the loop runs, and "the model never sees it" degrades into "we try not to put it in the prompt." Filing the two together is the point: the security property is downstream of an architecture decision usually made for latency and reliability reasons.
- **What it defends against and what it does not.** It removes an entire class of exposure — prompt-visible secrets leaking via output, logging, trace capture, summarization into memory, or a context window shared with untrusted content. It does not stop a model from *misusing* a credential it cannot see: the agent can still call the tool, and the tool will still authenticate. Confidentiality of the token and authority over its use are different problems, and only the first is addressed here.
- **How it relates to the scope-exchange pattern.** [Vaulting and exchanging tokens for scoped upstream access](vault-and-exchange-tokens-for-scoped-upstream-agent-access.md) attacks the second problem: narrow what the credential can do. The two compose — never-in-context bounds who can read the secret, scope exchange bounds what the secret can do — and neither substitutes for the other.
- **The unstated surface.** The talk gives no threat model for the execution layer itself. A malicious or compromised tool, an untrusted skill uploaded into the environment, or a tool that echoes its own auth header into its return value all reach the credential at exactly the moment it is decrypted. "The model never sees it" is a statement about one component, not about the system.
- Provenance: an Anthropic vendor talk describing its managed-agent product; this is one of four "lessons learned" delivered in about twenty seconds. The mechanism is stated, not demonstrated — no audit, no attack analysis, no discussion of vault compromise, key rotation, or what is logged at decryption time.

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Vault and Exchange Tokens for Scoped Upstream Agent Access](vault-and-exchange-tokens-for-scoped-upstream-agent-access.md)
- [Decouple the Agent Loop From the Tool Execution Environment](decouple-the-agent-loop-from-the-tool-execution-environment.md)
- [Reach Private MCP Servers With Outbound-Only Tunnels](reach-private-mcp-servers-with-outbound-only-tunnels.md)
- [Separate Agent Harnesses From Generated-Code Execution](separate-agent-harnesses-from-generated-code-execution.md)
- [Move Agent Access Control to the Network Layer So the Sandbox Holds No Credential](move-agent-access-control-to-the-network-layer.md)

Sources:
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 22:25-22:47
