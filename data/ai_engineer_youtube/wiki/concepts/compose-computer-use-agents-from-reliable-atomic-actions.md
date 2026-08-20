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

- Measured support for the underlying worry, from the evaluation side: when DIGIWORLD varies a task's starting screen or the app's visual theme — changes that leave the goal untouched — "in the worst case, frontier models are pretty bad actually at being robust to these variations," against the natural expectation that "the model should pretty much have the same performance." That fragility is the argument for making small interactions reliable and controllable rather than trusting a high average task-success number. See [measuring robustness per variation axis](measure-agent-robustness-per-variation-axis-not-just-average-success.md). ([Computer Use at the Edge of the Statistical Precipice](../sources/20260814_CTLa_p6iOiY.md), 09:59-10:55)

- **The same lab's later position on where the reliability comes from.** Mishra (Amazon AGI Lab) states as "one of our biggest bets" that "coding abilities are not sufficient to do well on computer use" — the model needs grounding, semantic understanding, change detection, and multi-source observation baked in, not only a well-designed action API. Read together with Perszyk's atomic-action framing, the two describe one program: make the units reliable at the interface, and train the perception that decides *which* unit to fire (the ad button versus the real submit button). See [Train Screen-Perception Primitives Beyond Coding Ability](train-screen-perception-primitives-beyond-coding-ability.md). ([From RL to IRL](../sources/20260814_Cc0_nyxROBA.md), 11:04-12:20)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [Close agent loops around live action feedback](close-agent-loops-around-live-action-feedback.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Measure Agent Robustness per Variation Axis, Not Just Average Success](measure-agent-robustness-per-variation-axis-not-just-average-success.md)
- [Train Screen-Perception Primitives Beyond Coding Ability](train-screen-perception-primitives-beyond-coding-ability.md)

Sources:
- [Useful General Intelligence - Danielle Perszyk, Amazon AGI](../sources/20250802_Dj0b_cEBHBI.md), 08:41-12:05
- [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../sources/20260814_Cc0_nyxROBA.md), 11:04-12:20
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 09:59-10:55
