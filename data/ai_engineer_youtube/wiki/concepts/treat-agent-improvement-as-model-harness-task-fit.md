# Treat Agent Improvement as Model-Harness-Task Fit

Summary: Agent improvement is classical machine learning with different algorithms — a fit function over data, a harness, and a model, tuned until the tasks pass — which reduces the engineering job to two things: finding good fit functions and finding good data.

Use when:
- A team treats prompt work, tool design, and model choice as three unrelated activities.
- Framing what an applied research or agent-quality function actually does.
- Explaining to an ML-background team why their instincts transfer to agent work.

Details:
- The analogy comes from the speaker's own scikit-learn-era PhD: scikit-learn "at an abstract level, it's a bunch of helpers to fit learning systems to data," and "the same principles that we use in… classical machine learning definitely still apply to this agent-first world." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 12:46-13:32)
- The named frame: **model harness task fit**. "We still have this sort of like fit function that I'm going to try to like take my data, take a harness, take a model, and I'm going to try to fit it all together to make sure that all of my tasks pass. The algorithms look slightly different, but the overall process of machine learning doesn't really look that different." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 13:32-14:07)
- The two jobs that fall out: "find good fit functions… these are like auto research. This is tons of great work that's being done in RL on different methods… And also find good data. If you put those two things together, then that is basically the applied or just overall research question that every team has to make their agents better." (The RL method names are garbled in the captions and are not attributed here.) ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 14:07-14:33)
- Auto research is the fit function running itself: "if you have some sort of score that you can make number go up, agents are pretty good at making that number go up. They might cheat a little bit and you need to like check them on some stuff." The worked example is an agent on terminal-bench reading its own traces, proposing experiments, and trying fixes. The cheating caveat is the reason a fit loop needs a held-out check rather than only a score. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 14:33-15:21)
- What the frame buys you in practice: it makes the three inputs *jointly* tunable rather than sequentially owned. The wiki's per-input pages are the components — the harness is not a fixed wrapper ([Tune coding agent harnesses per model family](tune-coding-agent-harnesses-per-model-family.md), [Match the harness to complicated vs complex problems](match-the-harness-to-complicated-vs-complex-problems.md)), the model is a selection over a measured bar ([Right-size models with prototype big, deploy small](right-size-models-with-prototype-big-deploy-small.md)), and the tasks are the eval suite that the whole assembly hill-climbs ([An Agent's Eval Suite Describes Its Behavior](an-agents-eval-suite-describes-its-behavior.md)).
- Limit of the analogy, worth stating because the talk does not: `fit()` in classical ML converges against a fixed dataset, while the harness and task set here are themselves edited by humans and by other agents during the loop, so there is no equivalent of a training/test split unless one is imposed deliberately — which is what the wiki's regression-aware and verifiable-learning pages exist to supply ([Make regression-aware optimization part of the continual-learning loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)).
- **A case where the harness term is exhausted and the model term is not.** Fitting a harness to a multi-GPU kernel task took Gemini 3 Pro from 24 to 35 of 87 problems, then stopped: "as we scaled the amount of time the performance plateaued, and additional techniques would be required to continue seeing the scaling there." The residual is diagnosed as a model property rather than a fit problem — "models do not currently understand how to reason through these trade-offs even when we provide them in context." Supplying the principles is the strongest harness-side move available, so when it fails, the fit framing correctly hands the problem back to training or task selection. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 27:07-27:56, 29:11-29:17)

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [An Agent's Eval Suite Describes Its Behavior](an-agents-eval-suite-describes-its-behavior.md)
- [Sequence Harness Engineering and Fine-Tuning by Feedback Speed](sequence-harness-engineering-and-finetuning-by-feedback-speed.md)
- [Tune coding agent harnesses per model family](tune-coding-agent-harnesses-per-model-family.md)
- [Match the harness to complicated vs complex problems](match-the-harness-to-complicated-vs-complex-problems.md)
- [Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)
- [Densify Agent Feedback Because Pass/Fail Is Not Actionable](densify-agent-feedback-because-pass-fail-is-not-actionable.md)
- [Models Solve the Parallelism Patterns the Internet Already Contains](models-solve-the-parallelism-patterns-the-internet-already-contains.md)

Sources:
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 12:46-15:21
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 27:07-27:56, 29:11-29:17
