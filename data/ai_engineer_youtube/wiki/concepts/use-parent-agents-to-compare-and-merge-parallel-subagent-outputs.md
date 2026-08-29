# Use parent agents to compare and merge parallel subagent outputs

Summary: A parent agent can coordinate multiple subagents working in isolated workspaces, then compare their outputs and help the user merge the strongest pieces. This turns parallel coding from separate attempts into a reviewable selection and synthesis workflow.

Use when:
- Running the same coding task across several models or implementation strategies.
- Designing a review interface for parallel subagent work.

Details:
- Cursor's "best event" workflow gives the same task to multiple models in parallel, each running in its own worktree, so users can compare implementations rather than committing to one model upfront. 02:22-02:58, 09:08-09:40
- The prompt asks a parent agent to create one subagent per model, have each subagent create and work inside its own worktree, wait for all subagents, then summarize, grade, and critique the implementations in a table-like form. 06:18-07:12
- The parent agent has enough context after the subagents finish to explain what each model did, identify duplicated or unique implementation choices, and accept follow-up instructions to stitch together preferred pieces from different outputs. 09:40-09:58, 11:45-12:13
- This pattern improves over choosing a single subagent result, but it relies on the same isolation discipline as any worktree workflow and needs review before applying changes back to the primary checkout. 08:10-08:21, 12:33-13:18

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Give Parallel Agents Complementary Optimization Personas](give-parallel-agents-complementary-optimization-personas.md)
- [Open Agent Arenas Reach Solutions No Single Agent Reaches](open-agent-arenas-reach-solutions-no-single-agent-reaches.md)

Sources:
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md), 02:22-12:13
