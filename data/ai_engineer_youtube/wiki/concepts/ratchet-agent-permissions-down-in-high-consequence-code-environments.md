# Ratchet agent permissions down in high-consequence code environments

Summary: Coding agents operating in defense, government, or other high-consequence systems should receive narrowly scoped data and action permissions instead of broad repository or data-source access.

Use when:
- Designing agent access for classified, regulated, safety-critical, or mission-critical codebases.
- Reviewing whether a coding-agent demo or deployment has hard permission boundaries beyond a generic "be careful" instruction.

Details:
- Poolside's demo is framed around Ada code used in critical infrastructure, satellites, government, and defense contexts, where the speakers say broad agent access is inappropriate. (01:27-03:22)
- They explicitly warn that an agent cannot be allowed to "run around and do stuff" or be handed data sources with unrestricted authority; access has to be ratcheted down to match organizational comfort and permission requirements. (03:37-04:01)
- The live demo still uses useful agent affordances, including a VS Code interface, live diff view, generated test commands, manual execution, and visible build output, showing that constrained access can coexist with productive coding assistance. (01:55-05:09)
- For AI engineering, this means treating permissions, live diffs, command review, and verification surfaces as part of the coding-agent architecture for high-impact environments.

- **Chip design is another instance of the environment class, and it supplies the mechanism this page states as a preference.** The consequence structure is the same shape as defense and satellites — "in chips, you can't [patch]… it's fixed on silicon, it has been printed," at a respin cost given as "on average… about $50 million" — but the actionable addition is *where* the ratchet has to be installed. Telling an agent not to touch spec files failed through bash, then `sed`, then `cat`; the ratchet only held once it moved to "block from system level, not tool by tool." In a high-consequence environment, a permission expressed as an instruction is not a ratchet, because nothing prevents it from being loosened by the agent's own next idea. ([Mohamed](../sources/20260822_0I6aoPSRzVc.md), 03:30-04:08, 13:36-15:11)


- **The counter-position, from an operator who tried the ratchet and put it back.** Anthropic's CI team reaches the opposite conclusion for a verb the agent needs daily: after an agent's cleanup deleted about 200 workloads, "the standard fix for an incident like that is basically that you narrow the token scope… you just take the deletes away effectively… Maybe it works for about a week, maybe two, but then you eventually end up in a situation where the agent is genuinely trying to delete something… and you will just be there sitting and pressing enter by hand all over again." The reconciling variable is how *routine* the withheld verb is. In Ada codebases and in silicon, the catastrophic verbs are rare and can be structurally excluded at no cost to the agent's ordinary work; in CI, deleting workloads is the ordinary work, so removing it converts an autonomous agent into a proposal generator. Where the verb is routine, this source argues the dial should be [a budget rather than a scope](replace-the-token-boolean-with-a-budget-on-four-dimensions.md) — how much, how fast, what is undoable, and who notices. ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 04:23-05:45)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Block the Capability at the Substrate, Because Denying a Tool Only Denies a Name](block-the-capability-at-the-substrate-because-denying-a-tool-only-denies-a-name.md)
- [Replace the Token's Boolean With a Budget on Four Dimensions](replace-the-token-boolean-with-a-budget-on-four-dimensions.md)

Sources:
- [AGI: The Path Forward - Jason Warner & Eiso Kant, Poolside](../sources/20251227_OGCG_QkCcZo.md), 01:27-05:09
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 03:30-04:08, 13:36-15:11
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 04:23-05:45
