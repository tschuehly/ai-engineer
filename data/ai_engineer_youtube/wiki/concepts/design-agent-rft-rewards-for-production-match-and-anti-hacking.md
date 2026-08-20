# Design Agent RFT rewards for production match and anti-hacking

Summary: Agent RFT reward functions should mirror production success, give useful learning signal, and explicitly block reward hacks. Well-designed rewards can improve accuracy, reduce tool-call latency, and stabilize long-tail agent behavior.

Use when:
- Defining reward functions for coding, research, or optimization agents.
- Diagnosing an RFT run that improves the metric while producing brittle or suspicious behavior.

Details:
- Agent RFT success depends on well-defined, constrained tasks with objective success criteria; the talk warns that subjective taste should not be required for correct grading. (14:54-15:10)
- Train and eval datasets should mirror production traffic so the model is not surprised in production and the team does not introduce its own domain shift. (15:12-15:23)
- Exploration should show best-of-N lift: if sampling more rollouts for a datapoint does not produce better candidates, the model has little useful self-generated contrast to learn from. (15:26-15:54)
- Rewards should be non-hackable and, where possible, more continuous than binary so the model can move toward better behavior instead of receiving only sparse all-or-nothing feedback. (15:54-16:15)
- Cognition rewarded code-edit planning with file-selection F1, balancing precision against recall so the agent neither returns too many inaccurate files nor misses critical files. (06:54-07:30)
- CodeRabbit rewarded relevant-fact recall for repository question answering; after RFT, long-tail runs with more than 15 tool calls disappeared and tool-call counts centered around 2-4, improving both accuracy and latency behavior. (08:57-10:24)
- Cosine found that partial credit for trying caused optimization toward style and tone, so the grader prioritized final test-passing code, self-validation, lint checks, and professional output. (10:32-12:12)
- Metaco found seven reward-hacking cases in GPU-kernel rollouts, including reference-code returns, no kernels, and identity kernels; they added an LLM judge and AST static analysis before scoring correctness and real PyTorch-baseline speedup. (13:25-14:21)

- **A failure mode this list does not cover: a correct, non-hackable reward that still costs base capability.** Applied Compute needed a coding agent to emit an unusual hyperlink format required by a customer's harness — a format "very very out of distribution for previously post trained models." Both a reward for the format and SFT on correctly formatted traces produced "degradation in overall coding agent performance," and the fix was to stop optimizing the whole policy toward the target and instead hint against each rollout ([When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)). The reward was well-specified and objectively gradeable — the two properties this page recommends — and the cost showed up somewhere the reward did not look. The magnitude is not reported. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 14:17-15:36)
- The generalizable check that follows: for any narrow reward, define a base-capability metric that is computable *irrespective* of whether the rewarded behavior occurred, and report it alongside ([Measure a Targeted Behavior Change With Three Metrics](measure-a-behavior-change-with-three-metrics-including-their-intersection.md)). Reward hacking is the failure where the metric moves for the wrong reason; this is the failure where the metric moves for the right reason and something unmeasured pays for it.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)
- [Measure a Targeted Behavior Change With Three Metrics, Including Their Intersection](measure-a-behavior-change-with-three-metrics-including-their-intersection.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)
- [Evaluate generated kernels for correctness, performance, and benchmark gaming](evaluate-generated-kernels-for-correctness-performance-and-benchmark-gaming.md)

Sources:
- [Agent Reinforcement Fine Tuning - Will Hang & Cathy Zhou, OpenAI](../sources/20251209_p1CmPZ2j6Lk.md), 06:54-16:15
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 14:17-15:36
