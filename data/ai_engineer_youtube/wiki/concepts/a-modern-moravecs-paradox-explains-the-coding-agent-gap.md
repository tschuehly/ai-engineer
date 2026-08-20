# A Modern Moravec's Paradox Explains the Coding-Agent Gap

Summary: Coding agents work not because coding is easy but because code is a language-native world — already symbolic, already structured, with tests standing in for rewards. Everyday digital work has none of those properties, so agents that look near-expert on the symbolic tasks once considered the crown jewel of intelligence make "brittle and silly errors" the moment they leave code.

Use when:
- Extrapolating coding-agent success to a non-code domain and estimating what will not transfer.
- Explaining to a stakeholder why an agent that writes production code cannot reliably do routine operational work.
- Deciding what infrastructure a new agent domain needs before the agent itself is worth building.

Details:
- The paradox restated for this generation: Moravec's paradox says "hard things are easy, easy things are hard." The modern version is that "we are very good at these symbolic reasoning tasks like coding and math, which were considered crown jewel of intelligence earlier. But then we still struggle with this everyday digital work because they really require quite different set of cognitive competencies to excel at them." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 04:42-05:25)
- The three properties that made code the ideal first market, stated compactly: "code is already a language-native world. Everything is already represented symbolically and recorded in a very structured way. And you get your rewards, you get your tests all in place in symbolic ways." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 03:26-03:49) Read as a transfer checklist, a new domain inherits coding-agent economics only to the extent it supplies all three: a symbolic representation, a structured record, and a cheap automatic verifier.
- What happens on the other side of that boundary: "then what happens when we leave the privileged world of codes? Well, not so well" — enterprise and personal deployments run into "quite brittle and silly errors." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 03:49-04:16)
- The talk invokes Andrew Ng's "it's not going to be the year of agents, it's going to be the decade of agents because they cannot do computer use, they don't have continual learning," and grants that coding agents may have shifted that view while insisting "the difficulties with computer use, with continual learning [are] still largely the same right now." ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 04:16-04:42)
- The market evidence offered for coding's head start is Anthropic's revenue curve — "in just under 2 years, their revenue has grown 400 times to 40 billion," with "maybe 60 billion annualized" cited as a newer number, "largely driven by coding and coding-related productivity capabilities." This is secondhand, unsourced, and illustrative; it establishes that coding is the first mass market, not a rate to reason from. ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 02:51-03:26)
- The practical consequence, consistent with the wiki's verification material: in a domain without native tests, the verification loop is something you build before the agent pays off, not something the model supplies. The wiki's high-fidelity-engine and outcome-verifier pages are the constructive form of what code gets for free.
- Provenance: a conceptual talk from the COO of a continual-learning company. Nothing here is measured; the paradox is offered as an explanation, and the three-property account of code is an argument rather than an ablation.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Digital Work Is Millions of Microworlds With Local Physics](digital-work-is-millions-of-microworlds-with-local-physics.md)
- [Separate Intelligence From Expertise When Diagnosing an Agent](separate-intelligence-from-expertise-when-diagnosing-agents.md)
- [Build High-Fidelity Engines to Create Verification Loops in Non-Code Domains](build-high-fidelity-engines-to-create-verification-loops-in-non-code-domains.md)
- [Use Verifiable Rewards for Language Model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Prefer Outcome Verifiers Over Ground-Truth Path Checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)

Sources:
- [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 02:51-05:25
