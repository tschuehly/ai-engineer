# A Teacher Can Install a Tool Call by Moving the Reasoning Path, Never the Call Tokens

Summary: In a distillation run conditioned on an old trace that never performed the target action, the teacher has no target tokens to imitate — so it shifts the *reasoning* toward the action instead, and the action follows. The behavior can be installed from a corpus that does not contain a single example of it.

Use when:
- A desired agent behavior appears nowhere in your trace corpus, so imitation looks impossible.
- Explaining why a reasoning model's tool-call rate moved without any tool-call supervision.
- Deciding whether reasoning tokens or output tokens are the right place to intervene.

Details:
- The setup: a Qwen thinking model on SWE-bench "was essentially taking like up to 80 turns to submit its answer. What we wanted to do was encourage it to call a tool to submit its task before turn 40" — without "letting it do its normal sort of full reasoning chain." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 10:40-11:21)
- The hint is a budget fact the model does not track: "you are near your 40-turn limit. There's only about three turns left… You often keep exploring and forget to wrap up investigating. So, finalize and verify your fix and then call this tool before you run out of time." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 12:04-12:22)
- The result: "the task complete call rate increases dramatically from about 22% to 60%," while the test pass rate "is relatively constant. In fact, it goes up a little bit." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 12:22-12:48)
- **The mechanism, which the speaker singles out as the surprise.** The run was fully offline, on "a trace that was created ahead of time that never basically never called this task complete tool." So the student was nudged "towards calling this task complete tool call without ever specifically changing the tokens for the tool call. Because again, the rollout is conditioned on the production trace… it never had the reasoning path to think to call the tool call. And so, the teacher doesn't force the tool call. It just starts to force the reasoning path towards the tool call without ever actually changing the tool call." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 12:48-13:38)
- **Why this is worth generalizing.** The usual assumption behind behavior cloning is that the corpus must contain the behavior. Here the corpus contains only the *precursor* — deliberation about wrapping up — and the action is reachable from it. For a reasoning model, the chain of thought is a lever on the action space that does not require action-level supervision, which widens what an existing trace dump can teach.
- **Where it stops.** This works because the target action is one the policy already knows how to emit and merely fails to choose. Nothing here suggests a reasoning-path nudge can install an action the model cannot produce — the whole SWE-bench exercise was framed as a proof "to ourselves that we could get it to sort of wrap up its reasoning quickly." A genuinely out-of-distribution *output format*, in the same talk, needed the on-policy corner instead ([When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)).
- The complement in the prompting literature: the wiki's [leading words](steer-agents-with-leading-words-that-surface-in-reasoning-traces.md) page describes the same lever without training — put a dense phrase in the prompt, watch the model re-emphasize it in its reasoning, and see the behavior change. Denton's version moves that effect into the weights, and offers the same verification signal: watch the reasoning trace, not just the action rate.
- **Measurement caveat built into the result.** The headline number is a *tool-call rate*, not a capability gain; it was reported alongside a flat base-task metric precisely because a behavior change of this kind can be bought with capability. See the three-metric design on [Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md).
- Provenance: one unpublished internal run, no seeds, variance, or task counts, from a vendor demonstrating its own method. The 22%→60% figure should be read as an existence proof for the mechanism, not as a calibrated effect size.

Related topics:
- [Models](../topics/models.md)
- [Coding Agents](../topics/coding-agents.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Distill Without a Golden Answer by Giving the Teacher Privileged Information](distill-without-a-golden-answer-using-privileged-information.md)
- [Offline Hints on Offline Traces Need No Replayable Environment](offline-hints-on-offline-traces-need-no-replayable-environment.md)
- [Buy On-Policyness With a Single Rollout Step on an Offline Trace](buy-on-policyness-with-a-single-rollout-step.md)
- [Steer agents with leading words that surface in reasoning traces](steer-agents-with-leading-words-that-surface-in-reasoning-traces.md)
- [Interleave reasoning and tool calls for long-horizon agents](interleave-reasoning-and-tool-calls-for-long-horizon-agents.md)
- [Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)

Sources:
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 10:40-13:38
