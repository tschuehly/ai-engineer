# Agents

## Overview

Agent workflows depend on both model capability and the context substrate around the model. On-device agents can keep core inference local while invoking selected tools, APIs, and structured outputs; enterprise agents also need institutional knowledge that is accurate enough to move real work through delivery systems. Small models can sit in front of the main agent as retrieval, extraction, classification, or reranking tools that reduce context rot. For coding work, simple loops can give agents enough structure to process one ticket at a time while avoiding the coordination failure modes of large multi-agent plans.

## Key Concepts

- [On-device agents can combine local reasoning with tool and API calls](../concepts/on-device-agents-can-combine-local-reasoning-with-tool-and-api-calls.md) - local inference can still support function calling, JSON output, and selected API-backed skills.
- [Enterprise agent failures often expose missing institutional knowledge](../concepts/enterprise-agent-failures-expose-missing-institutional-knowledge.md) - task failures can reveal missing enterprise knowledge rather than insufficient model capability.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - narrow models can filter, classify, retrieve, or extract context before the main agent reasons.
- [Ralph loops process one ticket at a time with fresh context](../concepts/ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md) - coding agents can be constrained to one work item, one validation cycle, and a clean handoff.
- [Use independent validation contexts to reduce agent confirmation bias](../concepts/use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md) - separate review contexts can catch failures the producing agent rationalizes away.

## Open Questions

- Which classes of tool calls are reliable enough for small on-device models without cloud fallback?
- How should agents distinguish missing institutional knowledge from ambiguous task instructions?
- When is a small-model preprocessing step worth its latency and operational complexity compared with giving the main agent more raw context?
- How much autonomy should coding agents receive before independent validation and permission boundaries become mandatory?

## Sources

- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md)
