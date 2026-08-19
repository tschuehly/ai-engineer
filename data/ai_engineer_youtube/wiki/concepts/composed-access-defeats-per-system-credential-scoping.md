# Composed Access Defeats Per-System Credential Scoping

Summary: Read-only credentials and carefully scoped ACLs are the correct first answer for an agent with production access, and they stop being sufficient at a predictable point: the permissions are provisioned one system at a time, but the agent's reach is the *composition* of them, so access to system A that yields a path into system B opens a hole neither system's policy is wrong about. The MCP version fails the same way one step earlier — a well-designed tool surface is bypassed the moment the agent can spawn a subprocess.

Use when:
- Someone answers "how do we make this agent safe?" with "issue it read-only credentials" or "give it a carefully designed set of MCP tools."
- An agent has legitimate access to several production systems and you are reasoning about what it can reach transitively.
- You are deciding whether a per-system permission model can be the whole security boundary or needs a boundary underneath it.

Details:
- **The concession, then the limit.** "You might say, well, there's ACLs, there's permissions, you can issue read-only Postgres credentials… and yeah, that's true up to a point… you can do careful credential provisioning and you should." The two failures named are operational and structural: it "really requires working across many different systems, provisioning credentials in incredibly careful ways," and "the composition of access can lead to holes when you can access one system and then another system." ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 06:34-07:12)
- **The worked instance of composition.** Deno's production Postgres is inside a VPC reachable "only through an EKS endpoint." Cluster access and database access are separately reasonable grants; together they are a path from the agent's VM to `DROP TABLE users` that neither grant looks like on its own. ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 05:14-05:57)
- **The MCP version of the same failure.** "You can structure all of this as very careful MCP tools that have the proper permissions. But then you can't spawn subprocesses, right?… as soon as [the agent] spawns the psql, you're broken through the security boundary." A curated tool surface is a description of the *intended* action space, not an enforcement of it, unless something independently prevents every other path out. This sharpens the wiki's existing advice to [shrink the agent-visible MCP surface](secure-mcp-servers-by-shrinking-the-agent-visible-surface.md): shrinking helps only where the tool layer is the only exit. ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 07:12-07:40)
- **Why the scoping burden compounds rather than converges.** Each new system the agent legitimately needs adds another credential to provision correctly *and* a new set of pairs to reason about. Deno's agents hold read/write access to Postgres, Kubernetes, ClickHouse, AWS, GitHub, and Slack — six systems, and the composition surface, not the credential count, is what grows. ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 01:19-01:35)
- **What the argument does and does not license.** It is not an argument against least privilege — "you should" do the careful provisioning. It is an argument that per-system scoping cannot be the *only* layer, and that the layer underneath has to see the actions themselves rather than the grants, which is the case for [enforcing egress policy at the wire protocol](enforce-agent-egress-policy-below-the-http-layer.md). ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 06:34-07:12, 16:32-17:08)
- **The comparison Dahl uses to set the target.** The goal is not to shrink the agent's access to something safe but to "empower these agents to have kind of the same access that a human [SRE] might," with the rules doing what a human SRE's judgment would do. That is what forbids the easy resolution of simply not granting the composed access. ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 06:19-06:33)

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Enforce Agent Egress Policy at the Wire Protocol, Below HTTP](enforce-agent-egress-policy-below-the-http-layer.md)
- [Move Agent Access Control to the Network Layer So the Sandbox Holds No Credential](move-agent-access-control-to-the-network-layer.md)
- [Secure MCP Servers by Shrinking the Agent-Visible Surface](secure-mcp-servers-by-shrinking-the-agent-visible-surface.md)
- [Authorization Propagation Is the Hard Part of Enterprise Agent Workloads](authorization-propagation-is-the-hard-part-of-enterprise-agent-workloads.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)

Sources:
- [Security Firewall for Agents — Ryan Dahl, Deno](../sources/20260817_MkRYPFIMCSA.md), 01:19-01:35, 05:14-07:40, 16:32-17:08
