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

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Pipeline RL trades policy staleness for GPU throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)
- [Preserve rollout trajectory context for agent RFT grading](preserve-rollout-trajectory-context-for-agent-rft-grading.md)
- [Treat environments as eval, data, and training substrates](treat-environments-as-eval-data-and-training-substrates.md)

Sources:
- [Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads - Yuxuan Zhang, Z.ai](../sources/20251122_m6MF1OR_9kM.md), 07:51-10:56
