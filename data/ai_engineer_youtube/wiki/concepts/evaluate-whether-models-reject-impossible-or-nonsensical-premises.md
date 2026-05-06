# Evaluate Whether Models Reject Impossible or Nonsensical Premises

Summary: Models need to be evaluated on whether they can refuse, reframe, or challenge invalid task premises, not only on whether they can complete well-formed tasks. A model that acknowledges a premise problem but then proceeds with invented analysis is still failing this capability.

Use when:
- Testing whether a model or agent should push back on impossible, contradictory, or nonsensical user requests.
- Comparing reasoning-effort settings where more deliberation might increase accommodation instead of improving judgment.

Details:
- BullshitBench tests models by asking nonsensical questions and grading responses as clear pushback, partial accommodation, or acceptance of the bad premise. (02:19-04:33)
- The talk's example asks whether deployment frequency can be attributed to indentation style versus average variable-name length; strong behavior is to say the question cannot be meaningfully measured or needs reframing. (03:27-03:53)
- Some responses start correctly by noting the premise does not make sense, then still invent proxy-variable explanations, which should be scored as accommodation rather than reliable judgment. (03:53-04:12)
- Increasing reasoning effort is not automatically a fix: the speaker says high-reasoning traces sometimes question the premise once and then spend many paragraphs trying to solve the impossible task. (06:36-08:23)
- This failure can appear in agent workflows when an agent is asked to work in the wrong project or under the wrong context and still performs some action instead of stopping to clarify. (08:23-08:44)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)

Sources:
- [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench](../sources/20260424_R7A8rX-09Zw.md), 02:19-08:44
