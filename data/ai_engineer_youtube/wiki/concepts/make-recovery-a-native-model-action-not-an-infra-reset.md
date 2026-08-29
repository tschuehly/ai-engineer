# Make Recovery a Native Model Action, Not an Infra Reset

Summary: Standard RL training resets the environment when infrastructure errors occur, which trains an agent that has never recovered from anything. Pass the error to the model instead and require it to recover with ordinary actions — refresh, backtrack, compare, wait, abandon, escalate — because in deployment there is no reset.

Use when:
- Designing the error path of an agent training environment or rollout harness.
- An agent handles the happy path well but stalls, loops, or gives up when a page fails to load or a session expires.
- Deciding whether a runtime failure should be swallowed by infrastructure or surfaced into the agent's context.

Details:
- The practice being replaced is named directly: "often during traditional RL, what we do is when there's an infra error, we just reset the state or ask the model to just restart, but that's not an option in real life." ([From RL to IRL](../sources/20260814_Cc0_nyxROBA.md), 09:22-09:34)
- The replacement: "whenever we have an infra error, we pass it to the model and we expect the model to recover from it using native tool use, native actions like, you know, refresh, backtrack, compare, wait, abandon, escalate to the user." (09:34-09:48)
- The six recovery actions are worth reading as a vocabulary the environment must actually support: `compare` implies the agent can re-observe and diff state, `wait` implies a non-punitive way to spend a step, `abandon` implies partial credit is possible, and `escalate` implies a handoff channel exists ([calibrated confidence](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)). An environment that only offers click and type cannot train any of them.
- Why it matters in deployment terms: in the reality table, the assumption "failure resets" is replaced by "failure is often persistent," with recovery policies as the adaptation — a locked account, a submitted form, and a deleted file do not go away because the episode ended. ([Map RL Assumptions to Deployment Realities](map-rl-assumptions-to-deployment-realities-for-computer-use-agents.md), 14:37-14:45)
- The failure this prevents is visible in the lab's early trajectory: signed out mid-task, the agent chose to guess the password twice — "I will resolve this without handoff" — and locked the account. The corrected trajectory after training replaces exactly that step with a recovery action: "I see a sign-in screen. Credentials expired. So the task data should not go here. Next, I'll hand off to the user." (04:47-05:38, 15:34-15:49)
- **This is the training-side counterpart of tool-error design.** Chrome DevTools' argument is that a tool's error messages should be actionable enough for the agent to self-heal; Mishra's is that the model should be *trained* on unrecoverable-looking errors so it has a recovery policy at all. Neither substitutes for the other: an actionable message helps a model that knows what to do with it, and a trained recovery policy still needs the error to reach the context window. See [Turn Tool Errors Into Agent Self-Healing Recovery](turn-tool-errors-into-agent-self-healing-recovery.md).

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Train Computer-Use Agents in a Flight Simulator, Not on Exams](train-computer-use-agents-in-a-flight-simulator-not-on-exams.md)
- [Turn Tool Errors Into Agent Self-Healing Recovery](turn-tool-errors-into-agent-self-healing-recovery.md)
- [Map RL Assumptions to Deployment Realities for Computer-Use Agents](map-rl-assumptions-to-deployment-realities-for-computer-use-agents.md)
- [Teach Calibrated Confidence So an Agent Knows When to Hand Off](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)
- [Close agent loops around live action feedback](close-agent-loops-around-live-action-feedback.md)
- [Fail Loudly and Bill Only for Successful Results](fail-loudly-and-bill-only-for-successful-results.md)

Sources:
- [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../sources/20260814_Cc0_nyxROBA.md), 04:47-05:38, 09:22-09:48, 14:37-14:45, 15:34-15:49
