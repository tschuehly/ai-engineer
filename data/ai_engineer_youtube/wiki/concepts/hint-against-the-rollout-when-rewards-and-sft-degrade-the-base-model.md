# When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout

Summary: Teaching a coding agent an out-of-distribution output format broke two standard approaches — a format reward and SFT on correctly formatted traces both degraded overall coding performance — while a hint written against each individual rollout took correct formatting from about 15% to about 80%. The same hint applied uniformly to every rollout barely moved it, which isolates *rollout-specific* feedback as the active ingredient.

Use when:
- A narrow behavior must be installed without regressing the model's general capability.
- A format or protocol requirement is out of distribution for post-trained models.
- Choosing between reward shaping, SFT, and self-distillation for a small, well-specified behavior change.

Details:
- The task: "we needed to teach a coding agent to use very specific formatting for hyperlinks due to a certain harness nuance of one of our customers. And obviously this coding agent needed to not regress on any of the base coding agent capabilities." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 14:17-14:51)
- Why it was hard, stated distributionally rather than as difficulty: "these hyperlink formats were very very out of distribution for previously post trained models." A convention no public corpus contains is not something the model is reluctant to do — it is something it has never seen. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 14:42-14:51)
- **Both standard tools failed the same way:** "when we tried things like adding a reward for specific hyperlink formatting, or even doing SFT on traces where we knew the hyperlink was correctly formatted, we saw that there was this sort of degradation in overall coding agent performance." Note that both had access to ground truth — the correct format was known — so the failure is not about missing labels. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 14:51-15:09)
- The approach that worked, run as an online trace with an online hint: "we would do a rollout, then we would inject a hint specific to the rollout that occurred from the on policy model, and then say, 'In your prior rollout, you'd formatted hyperlinks like this. Next time, make sure to format hyperlinks in this way instead.'… the percentage of correct hyperlink formatting jumped drastically from about, I guess, 15% all the way up to around 80%." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 15:09-15:36)
- **The controlled comparison is what makes this transferable.** Applied Compute also ran the static version of the same instruction — "for every single rollout, apply the same hint, which says, 'Remember that when you do hyperlinks, you have to format it this way'" — and reports "we do climb the behavior a little bit, but far less than in this online hinting world." Same content, same task, same model; the only difference is whether the hint quotes what the model actually just did. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 15:36-15:56)
- The plausible reading of why the diff-shaped hint wins is that it names the specific error to correct rather than restating a rule the model already had in its prompt, which makes the teacher's next-token distribution differ from the student's exactly at the tokens that matter. The talk does not offer this explanation; it is inference from the two runs it does report.
- **What to take from the two failures.** Reward shaping and SFT both push the whole policy toward a narrow target, and the wiki's reward-design guidance already warns that a poorly scoped reward optimizes the thing you can measure at the expense of the thing you want ([Design Agent RFT rewards for production match and anti-hacking](design-agent-rft-rewards-for-production-match-and-anti-hacking.md)). This case adds a cleaner failure: even a correct, non-hackable format reward can cost base capability when the target is far out of distribution. Pair it with token-level masking to reduce collateral learning ([Mask Irrelevant Teacher Tokens Before Learning From Them](mask-irrelevant-teacher-tokens-before-learning-from-them.md)).
- Provenance and limits: the degradation from rewards and SFT is reported without magnitude, and 15%→80% comes from one unpublished customer run with no variance, no n, and an unidentified base model. Treat the *ordering* (online hint > offline hint > reward/SFT on this task) as the durable claim and the numbers as illustrative.

Related topics:
- [Models](../topics/models.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Place a Continual-Learning Setup on Two Axes: Trace Policyness and Hint Provenance](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)
- [Distill Without a Golden Answer by Giving the Teacher Privileged Information](distill-without-a-golden-answer-using-privileged-information.md)
- [Mask Irrelevant Teacher Tokens Before Learning From Them](mask-irrelevant-teacher-tokens-before-learning-from-them.md)
- [Design Agent RFT rewards for production match and anti-hacking](design-agent-rft-rewards-for-production-match-and-anti-hacking.md)
- [Bootstrap RL with targeted SFT before reinforcement learning](bootstrap-rl-with-targeted-sft-before-reinforcement-learning.md)
- [Prefer model-portable agentic prompts before fine-tuning](prefer-model-portable-agentic-prompts-before-fine-tuning.md)
- [Offline Hints on Offline Traces Need No Replayable Environment](offline-hints-on-offline-traces-need-no-replayable-environment.md)

Sources:
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 14:17-15:56
