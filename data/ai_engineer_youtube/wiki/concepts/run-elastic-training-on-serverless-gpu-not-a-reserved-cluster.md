# Run Elastic Training on Serverless GPU, Not a Reserved Cluster

Summary: Serverless GPU compute is usually associated with inference, but it is also a strong fit for the bursty, parallel shape of training — fan-out hyperparameter search where you spin up many on-demand containers and kill the unpromising ones, and reinforcement-learning rollouts that are "massively embarrassingly parallel" and scale to tens of thousands of sandboxes — letting a team get algorithm control and fast iteration without owning and managing a cluster.

Use when:
- Choosing where to run fine-tuning, hyperparameter search, or RL without standing up a dedicated training cluster.
- Reasoning about why RL training is a sandbox-fleet problem, not just a GPU-hours problem.
- Picking a "middle ground" between a frontier API (no algorithm control) and full in-house training (full stack responsibility).

Details:
- The old default for fine-tuning was a "huge jump" to the in-house-training end of the spectrum: get a big cluster, isolate it from production resources, and put infra engineers (or scientists) on infrastructure — taking on "massive responsibility for the entire stack." A serverless compute platform is the emerging middle ground that keeps the frontier end's fast iteration cycles while giving full algorithm control. 02:57-05:45
- Hyperparameter tuning becomes elastic: "every minute on your cluster isn't sacred anymore" — fan out to many on-demand containers, get them on demand, and as soon as a run isn't promising, kill it; it behaves "almost like a meta-evolutionary algorithm." 09:06-09:46
- RL is the strongest fit: an RL model "needs to practice a lot," and that practice (an evaluation step called a rollout) is "massively embarrassingly parallel." Modal's customers scaled to 50,000–100,000 sandboxes in a quarter just to do RL rollout (the talk's spoken range; the event description says 50,000). 09:50-10:53
- A unified API for sandboxes and GPU containers/clusters is what makes the rollout fan-out practical — the same platform spins up isolated code-execution sandboxes and GPU compute. 10:14-10:30
- Accessibility detail: with open-source libraries you no longer hand-tape gradients or implement the linear algebra, and supervised fine-tuning (and RL) fit in ~300 lines of Python — you don't need infrastructure experts to start. 07:47-08:49, 09:50-10:13
- Serving the trained model is the inference counterpart: it's what the frontier API does under the hood, doable with vLLM, SGLang, Triton Inference Server, or a custom Python inference workflow, and on serverless you auto-scale it to match incoming traffic. 10:55-11:33

- **What this page leaves unstated is the link that has to be cheap for the elastic story to hold, and a later Modal talk names it.** Rollout fan-out is only elastic if new workers can be brought to the current policy quickly; shipping a frontier-scale checkpoint (≈500 GB, "multiple minutes to hours") to each one would make an autoscaled fleet mostly stale. Jiang reframes it as a unit problem — "the problem is not whether rollout can leave the cluster; the problem is the full checkpoint is a wrong unit of synchronization" — and replaces the checkpoint with a bitwise-lossless patch of the served view, roughly 500 MB ([Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md)). ([Modal](../sources/20260810_maRzp4kImJ4.md), 05:25-06:02, 17:26-17:41)
- The later talk also extends the claim past one provider's fleet: with a pull-based bulletin board and a version-aware sidecar, rollout engines can sit in different regions and at different providers, so "scattered inference capacity became one elastic rollout fleet… inference capacity can now become RL capacity." Same company, same argument, one rung further out — the constraint being attacked is no longer cluster ownership but cluster *locality*. ([Modal](../sources/20260810_maRzp4kImJ4.md), 15:16-15:34, 18:17-18:43)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Decide When to Fine-Tune From Three Business Signals](decide-when-to-fine-tune-from-three-signals.md)
- [Match GPU Commitments To Workload Lifecycle](match-gpu-commitments-to-workload-lifecycle.md)
- [Choose Reserved Pods for Iteration, Serverless for Autoscaling Load](choose-reserved-pods-for-iteration-and-serverless-for-autoscaling-load.md)
- [Pipeline RL trades policy staleness for GPU throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Agent-Native Runtimes Provide Fast API-Controlled Sandboxes](agent-native-runtimes-provide-fast-api-controlled-sandboxes.md)
- [Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md)
- [RL Post-Training Demands Four Scarce Compute Properties at Once](rl-post-training-demands-four-scarce-compute-properties-at-once.md)

Sources:
- [What Lies Beneath the API — Benjamin Cowen, Modal](../sources/20260602_HvZXAOZ3iv8.md), 02:57-11:33
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 05:25-06:02, 15:16-15:34, 17:26-18:43
