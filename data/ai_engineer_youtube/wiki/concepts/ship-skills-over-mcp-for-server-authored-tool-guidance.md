# Ship Skills Over MCP for Server-Authored Tool Guidance

Summary: Skills over MCP let server authors package updatable usage guidance with large MCP tool surfaces. This keeps workflow knowledge close to the integration without depending on each client having a separate plugin or registry mechanism.

Use when:
- A large MCP server needs to explain how its tools should be used without dumping all guidance into every prompt.
- Server authors need to update agent-facing instructions as the service or recommended workflow changes.

Details:
- The talk describes skills over MCP as an extension mechanism for shipping the "main knowledge" of how a large MCP server should be used alongside the server's tools. (16:33-16:50)
- Server-authored skills can be updated continuously by the MCP server author instead of relying on client-specific plugin mechanisms or external registries. (16:50-16:57)
- A rough version is possible today by giving the model a load-skills tool, but the talk says protocol-level semantics are intended to standardize the pattern. (17:00-17:15)
- This pattern reinforces that skills and MCP are complementary: MCP provides the connection, while skills provide the operational guidance for using that connection well. (05:28-07:12, 16:33-17:15)
- **The cruder predecessor of the same idea, from a server that had no guidance channel at all.** Before clients implemented server instructions — the field was "in the spec, but no clients implemented it" — Figma's answer was to append usage instructions to every tool result, and later to expose resources describing how to use the server. Both are server-authored guidance in the sense this page argues for; the difference is that a skill is fetched once and read as a unit, while instructions welded to each tool result are re-sent on every call and never seen by an agent that has not already chosen the tool. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 09:28-10:14)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use Skills for Workflow Guidance and MCP for Integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Package Reusable Context as Skills, Libraries, and Registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Agent Skills Package Progressive-Disclosure Context for Repeatable Workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Tools Are the Only Primitive Every Client Implements](tools-are-the-only-primitive-every-client-implements.md)

Sources:
- [The Future of MCP - David Soria Parra, Anthropic](../sources/20260419_v3Fr2JR47KA.md), 05:28-07:12, 16:33-17:15
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 09:28-10:14
