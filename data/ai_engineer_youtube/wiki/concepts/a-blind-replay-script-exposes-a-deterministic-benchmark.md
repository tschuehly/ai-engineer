# A Blind Replay Script Exposes a Deterministic Benchmark

Summary: If a benchmark's tasks always start from the same state, you can record one successful trajectory per task from a frontier model, compile the raw action sequences into a script under a megabyte, and replay them blindly without ever reading the screen — and that script matches or beats the model it was copied from. Building the replay agent is a cheap, constructive audit of whether your benchmark measures capability or memorized determinism.

Use when:
- Vetting an agent benchmark (computer use, browser, GUI, or any environment with a fixed starting state) before trusting its scores.
- A benchmark score looks strong and you need evidence that the agent is perceiving and deciding rather than executing a fixed path.
- Deciding whether to invest in environment variation, and needing a number that shows the current environment is exploitable.
- Reviewing a leaderboard claim about computer-use agents.

Details:
- Construction, in full: run a frontier model on the benchmark; for every task keep one successful trace — "a recorded tape" of taps, typing, and scrolling; repeat across all tasks; "compile this into a replay agent that just, when the task arrives, replays that sequence of actions blindly." For a benchmark with hundreds of tasks the artifact is "a script that is less than a megabyte." (00:36-01:32)
- Result on standard deterministic benchmarks (OSWorld is named in the video description; a mobile benchmark is named in the same sentence but garbled in the captions): "the success rate of this agent compared to the frontier model from which the agent was extracted is actually the same or even better." A script that never looks at the screen ties or wins. (01:34-01:50)
- The rhetorical force comes from admissibility, not from cheating: "this is a completely valid type of agent that you can evaluate on the benchmark." No benchmark rule excludes it, which is why the score is the benchmark's problem rather than the submitter's. (01:29-01:34)
- The cause is stated narrowly — "if the benchmark is static, is deterministic, then it is somehow gameable by this sort of strategy" — so this is a property of the *environment*, not of the model, the harness, or the grader. (02:05-02:19)
- Distinguish this from answer leakage. In [sealed eval environments](seal-eval-environments-against-answer-leaking-agents.md) the agent reaches outside the task boundary at runtime to read a solution that happens to be present; here nothing leaks and the agent reads nothing at all. Sealing network access, stripping future git history, and blocking `curl` do not touch this exploit, because the exploit is that the correct action sequence is a constant of the task.
- The passing bar after a fix is not zero. On a benchmark rebuilt with variation, "the replay agent doesn't get a lot of performance. It gets a little bit of performance that is probably what you want. Sometimes some tasks maybe are repeatable by nature, but on average you shouldn't expect a replay agent to have good performance." Treat replay score as a *residual* to keep small, not an error to drive out. (09:21-09:57)
- The reason to run the audit yourself rather than assume: D'Oro's counter to the common shrug ("this benchmark can be gamed but everybody's still using it") is that the cost lands on your own decisions before it lands on the field — "if you are deluding yourself on thinking that a score is confidently telling that your model is good, actually you are going to pay for those mistakes." (15:57-16:46)
- **A sibling audit with the same spirit and a different target, worth running alongside this one.** The replay script attacks a benchmark whose *action sequence* is a constant. Zou's ablation attacks a benchmark whose *answer is inferable from the task statement*: withhold the dataset the benchmark exists to test the use of, re-run, and read the residual — 20-50% across three popular data-science benchmarks. Neither audit finds the other's defect, and the fixes do not overlap: varying the initial state does nothing about an over-specified prompt, and rewriting the prompt does nothing about a recorded tape. Both share the property that makes them worth doing — they are constructive, cheap, and produce a number rather than a suspicion. See [Audit a Benchmark by Solving It Without the Data](audit-a-benchmark-by-solving-it-without-the-data.md). ([Einstein Arena — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 11:58-13:01)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [pass@k on a Deterministic Environment Measures Replay, Not Capability](passk-on-a-deterministic-environment-measures-replay.md)
- [Design Eval Environments to the PRISM Principles](design-eval-environments-to-the-prism-principles.md)
- [Measure Agent Robustness per Variation Axis, Not Just Average Success](measure-agent-robustness-per-variation-axis-not-just-average-success.md)
- [Seal Eval Environments Against Agents That Read the Leaked Answer](seal-eval-environments-against-answer-leaking-agents.md)
- [Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Inspect Rollouts Before Trusting RL Environment Scores](inspect-rollouts-before-trusting-rl-environment-scores.md)
- [Audit a Benchmark by Solving It Without the Data](audit-a-benchmark-by-solving-it-without-the-data.md)

Sources:
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 00:36-02:19, 09:21-09:57, 15:57-16:46
- [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 11:58-13:01
