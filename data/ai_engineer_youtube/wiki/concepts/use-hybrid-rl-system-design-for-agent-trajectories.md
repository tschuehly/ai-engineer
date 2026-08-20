# Use hybrid RL system design for agent trajectories

Summary: RL infrastructure for language models should route short reasoning tasks and slow agent tasks through different systems designs. Colocated synchronous training can fit short tasks, while long agent trajectories often need decoupled rollout workers, buffers, and periodic weight updates.

Use when:
- Designing RL systems for software-engineering agents, browser agents, or tool-using models.
- Diagnosing GPU underutilization caused by long external environment waits during agent rollouts.

Details:
- SLIME uses colocated training and inference on the same GPU pool for short math or code-completion tasks so the next batch samples from the latest policy immediately after an update. (08:15-08:35)
- Real software-engineering agent tasks can involve many steps such as opening a browser, calling backend APIs, and waiting for external responses, which can drag down synchronized workers and waste GPU time. (08:35-09:03)
- For complex agent tasks, SLIME uses decoupled asynchronous rollout workers that talk to real environments, write trajectories into a buffer, and let the training side consume data at its own pace while periodically pushing new weights. (09:49-10:19)
- The practical systems benefit is that slow tasks no longer block the whole training pipeline. (10:14-10:19)
- The framework also keeps BF16 precision for training while sending lower-precision weights to rollout workers after policy updates, seeking a speed and accuracy balance. (10:26-10:56)

- **The infrastructure this page designs around is a consequence of one algorithmic choice, not of RL in general.** Group-based methods need many rollouts per task, which is what forces decoupled rollout workers, buffers, and environments that are "one-to-one copies of the real world." A method whose parallelism is one deletes that requirement rather than optimizing it, which is why [parallelism is a row on the four-property scorecard](score-post-training-algorithms-on-four-properties.md) alongside signal density. Before building the hybrid system, it is worth asking whether the training method needs group rollouts at all. ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 03:12-03:25, 04:57-05:31)

- **SLIME's "lower-precision weights to rollout workers" choice turns out to have a second payoff this page treats only as a speed/accuracy balance.** Modal's account explains why: for a fixed float format the visibility floor is roughly θ/2^(mantissa+1), so a coarser serving dtype absorbs more of each optimizer step and *fewer* served weights change per version — "in even lower precision there will be less weight changed" ([Lower Serving Precision Shrinks the Weight-Sync Patch](lower-serving-precision-shrinks-the-weight-sync-patch.md)). The same decision that trades serving accuracy for speed also shrinks the periodic weight push this page describes. ([Modal](../sources/20260810_maRzp4kImJ4.md), 13:06-13:42)
- The decoupling motivation is also worth distinguishing from a placement one. Here rollout workers are decoupled so slow agent tasks stop blocking the pipeline — a scheduling fix, with workers still inside the cluster. Modal cuts the same seam to let rollout leave the cluster entirely, and names the unit that may move: a serving island, "a coherent endpoint or maybe a local group of endpoints… serving one policy version," chosen because there is no all-reduce across islands but there is one inside them ([The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)). The two motivations are compatible and address different costs. ([Modal](../sources/20260810_maRzp4kImJ4.md), 03:37-04:18)

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Pipeline RL trades policy staleness for GPU throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)
- [Preserve rollout trajectory context for agent RFT grading](preserve-rollout-trajectory-context-for-agent-rft-grading.md)
- [Treat environments as eval, data, and training substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Score a Post-Training Algorithm on Four Properties](score-post-training-algorithms-on-four-properties.md)

Sources:
- [Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads - Yuxuan Zhang, Z.ai](../sources/20251122_m6MF1OR_9kM.md), 07:51-10:56
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 03:12-03:25, 04:57-05:31
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 03:37-04:18, 13:06-13:42
