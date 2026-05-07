# Compose Computer-Use Agents From Reliable Atomic Actions

Summary: Computer-use agents should make small UI interactions reliable and controllable before composing them into larger workflows. Atomic action calls can be combined with structured extraction and ordinary programming constructs when the workflow needs repeatability, parallelism, or tabular post-processing.

Use when:
- Designing browser-agent SDKs, harnesses, or samples.
- Deciding whether a workflow should be one high-level autonomous prompt or a composed program around agent calls.

Details:
- Nova Act's stated approach is to make the smallest units of interaction reliable and give developers granular control over them. (11:48-11:55)
- Perszyk compares atomic actions to words: developers can string together small actions to create more complex workflows. (11:55-12:05)
- The apartment-search demo uses a first `act` call to navigate a rental site, structured extraction into JSON matching a Pydantic class, a helper function for Google Maps distance lookup, thread-pool parallel browsers, and pandas sorting. (08:41-10:01)
- The talk warns that even basic visual UI semantics are hard because icons and useful computer-use patterns cannot all be manually enumerated; agents need exploration and reinforcement learning over real interfaces. (10:11-11:01)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [Close agent loops around live action feedback](close-agent-loops-around-live-action-feedback.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)

Sources:
- [Useful General Intelligence - Danielle Perszyk, Amazon AGI](../sources/20250802_Dj0b_cEBHBI.md), 08:41-12:05
