# Map RL Assumptions to Deployment Realities for Computer-Use Agents

Summary: The assumptions that make reinforcement learning work in a game-like environment — observable state, cheap actions, clear reward, resettable failure, passive environment, autonomy as the goal — are each false on a real UI, and every one of them has a specific adaptation. Use the six-row mapping as a readiness checklist before deploying an RL-trained agent against real software.

Use when:
- Moving an agent that scores well in a sandbox or benchmark into real user-facing work.
- Diagnosing why a computer-use agent that passes evals produces dangerous trajectories in production.
- Deciding what a training environment still has to model before it is a fair proxy for deployment.

Details:
- Mishra's framing line for the whole gap: "RL worked when the world was a game, and IRL starts when the game fights back." ([From RL to IRL](../sources/20260814_Cc0_nyxROBA.md), 06:20-06:26)
- The mapping, as presented (14:02-15:02):

| Traditional-RL assumption | Reality | Adaptation |
| --- | --- | --- |
| State is observable | UI is partial and messy | Perception primitives |
| Actions are cheap | Actions can be irreversible | Risk-aware execution |
| Reward is clear | Success is often ambiguous | Audit and verification |
| Failure resets | Failure is often persistent | Recovery policies |
| Environment is passive | Content can be really adversarial | Trust boundaries |
| Autonomy is always good | Handoff can be optimal in some cases | Calibrated confidence |

- Each row is grounded in the failure catalogue the talk walks through first (06:37-08:17):
  - **Partial observability** — the DOM misses content baked into images (the sponsored ad text was in the image, so the DOM did not have it) and the screenshot misses whatever needs scrolling, so "the model is being fed all these sources of information and doesn't really know what to expect from each and what to pay attention to." Adaptation: [screen-perception primitives](train-screen-perception-primitives-beyond-coding-ability.md).
  - **Irreversibility** — "once you submit a form, once you delete a file, once you lock an account, it's often irreversible for the time being."
  - **Non-determinism** — a click may work, may load slowly, may hit flaky internet, or the machine may restart for an upgrade.
  - **Ephemeral authority** — sessions and credentials expire mid-trajectory, "very, very common."
  - **Ambiguous success** — "done often doesn't mean successful": an agent that filed the expense report *and* sent a resignation letter to the CEO is done, but not correct. This is why audit trails, not just terminal verifiers, are listed as the adaptation.
  - **Adversarial content** — "everything we see around us is designed to grab our attention," and the model acting on the user's behalf has to navigate that too.
- The two rows most often skipped are the last two. A benchmark environment is passive by construction, so trust boundaries never get exercised; and benchmark scoring rewards completion, so an agent is never rewarded for correctly refusing and escalating. Both were visible as concrete failures in the same lab's early browser-training trajectories: an account locked by password guessing after the agent decided "I will resolve this without handoff," and personal details typed into a third-party site after a click on an ad styled like the submit button. (04:14-06:15)
- Non-determinism has no row of its own in the summary table even though it is in the spoken failure list; it is folded into the recovery-policies row, since a slow load, a flaky network, and a restarted machine are all failures the agent has to survive rather than reset out of.

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Train Computer-Use Agents in a Flight Simulator, Not on Exams](train-computer-use-agents-in-a-flight-simulator-not-on-exams.md)
- [Make Recovery a Native Model Action, Not an Infra Reset](make-recovery-a-native-model-action-not-an-infra-reset.md)
- [Teach Calibrated Confidence So an Agent Knows When to Hand Off](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)
- [Keep the Harness Thick Early and Thin It as the Model Improves](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md)
- [Measure Agent Robustness per Variation Axis, Not Just Average Success](measure-agent-robustness-per-variation-axis-not-just-average-success.md)
- [The Open Web Is Adversarial to Agent Access](the-open-web-is-adversarial-to-agent-access.md)
- [An Audit Trail Is a Chain of Evidence, Not a Developer Log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md)

Sources:
- [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../sources/20260814_Cc0_nyxROBA.md), 04:14-08:17, 14:02-15:02
