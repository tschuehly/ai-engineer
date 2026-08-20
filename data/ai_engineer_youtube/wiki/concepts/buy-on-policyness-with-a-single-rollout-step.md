# Buy On-Policyness With a Single Rollout Step on an Offline Trace

Summary: Between "learn from stored traces" and "train the model that is serving traffic" sits a cheap middle rung: replay an old trace up to a chosen point, let the current policy produce exactly one step, and write the hint against that step. It needs no environment interaction, and Applied Compute reports it beat the fully offline setup on the same task.

Use when:
- The offline corner is working but you cannot yet stand up a replayable environment.
- A distillation run is learning slowly because every trace is from a policy several versions old.
- Someone frames on-policy training as all-or-nothing infrastructure.

Details:
- The construction: "off policy traces with some on policy step and hints that are constructed against that one on policy step… the trace that led to the point where I inject a hint was fully off policy. It was some production trace that came from a few days ago. And we are using our on policy model to just roll out one step **without actually having to interact with the environment**. And we construct the hint based on what that on policy model did in that one step." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 06:28-07:15)
- The reason no environment is needed is structural: a single next step is a forward pass over the stored prefix. Nothing has to be executed, no tool has to respond, no state has to be reconstructed — which is exactly the requirement that makes replayable environments expensive.
- Reported effect on the SWE-bench task: "we obviously see that the student model sort of learns to wrap up its reasoning, and eventually the teacher starts encouraging it to actually call this tool token… by having something that's a little bit more on policy that we're able to increase sort of the SWE-bench pass rate more than in the fully offline world." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 13:38-14:17)
- **This claim is the weakest-supported in its talk and should be labeled as such.** It is delivered against a chart with no numbers, no seeds, and no statement of how many steps were sampled or where in the trace they were placed. It is a design idea worth trying with a cheap A/B, not a result to plan around.
- What the single step buys, conceptually: it converts the hint from a statement about traces in general into a statement about *this policy's current mistake*, which is the same asymmetry that made online hints outperform static ones on a different task ([When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)). The step count is the price you pay for that specificity, and one is the minimum.
- It also pairs naturally with per-step hinting: if a judge is already choosing where in the rollout the hint belongs, that chosen point is where the single on-policy step should be taken ([Let a Judge Place the Hint and Distill Only the Steps Near It](let-a-judge-place-the-hint-and-distill-only-nearby-steps.md)).
- **The staleness framing this refines.** The wiki's [pipeline RL](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md) page — from the same company eight months earlier — treats policy staleness as a cost to be tolerated for throughput, measured in policy versions behind. Here staleness is a *dial you can partially buy back* on trace data that is days old, by regenerating just the step that matters. The two pages are about different loops (RL sampling versus distillation on logs) but share the underlying quantity.
- Read the grid honestly: this rung is the clearest evidence for Denton's own caveat that the boxes "sometimes don't make sense as boxes, but more as spectrums" — one on-policy step is a coordinate partway along the trace axis, not a corner. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 05:11-05:33)

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Place a Continual-Learning Setup on Two Axes: Trace Policyness and Hint Provenance](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)
- [Offline Hints on Offline Traces Need No Replayable Environment](offline-hints-on-offline-traces-need-no-replayable-environment.md)
- [Let a Judge Place the Hint and Distill Only the Steps Near It](let-a-judge-place-the-hint-and-distill-only-nearby-steps.md)
- [Pipeline RL Trades Policy Staleness for GPU Throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)
- [A Teacher Can Install a Tool Call by Moving the Reasoning Path, Never the Call Tokens](move-the-reasoning-path-not-the-target-tokens.md)
- [Turn Recorded Agent Traces Into Free Replay Test Cases](turn-recorded-agent-traces-into-free-replay-test-cases.md)

Sources:
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 05:11-05:33, 06:28-07:15, 13:38-14:17
