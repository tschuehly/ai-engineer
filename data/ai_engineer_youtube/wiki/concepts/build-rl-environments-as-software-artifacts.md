# Build RL Environments as Software Artifacts

Summary: Reinforcement-learning environments for language models should be packaged as runnable software artifacts, not only as static datasets. The environment owns setup, state transitions, parsing, rewards, rollouts, and evaluation or training hooks.

Use when:
- Turning an interactive task into an evaluation or post-training setup.
- Deciding whether a static dataset is enough or a stateful environment is needed.

Details:
- Fiorucci frames RL environments as gyms where LLM agents can use tools, run code, solve multi-step tasks, and learn from interaction and feedback. (00:45-01:02)
- Verifiers packages environments as installable Python packages and provides base classes for single-turn, multi-turn, and tool-using environments, plus parsers, reward functions, model-serving abstraction, parallel trajectories, and trainer integrations. (10:19-11:46)
- Brown frames the same environment artifact as a harness plus tasks and rewards that can serve evals, synthetic data, SFT, distillation, direct RL, and deployed user-task streams. 05:42-06:24
- Environment registries extend the software-artifact pattern: each shared environment can be a Python project with dependencies, versions, async tools, a data set, and reward rubrics. 11:19-12:05
- In the simple reverse-text environment, `load_environment` prepares the dataset, a parser extracts the model answer, a reward function compares it to ground truth, and a weighted rubric defines the score used for evaluation or training. (11:52-14:20)
- For tic-tac-toe, the environment behaves like a game engine: it stores board state, parses the model's move, checks validity, applies opponent moves, checks win or draw state, and emits the next prompt until the trajectory ends. (19:00-20:52)
- CWM adds a large-scale code-agent training example: samplers execute terminal actions in an environment, trajectories are scored, trainers compute gradients, checkpoints are pushed to samplers, and queued models plus queued trajectories keep asynchronous RL throughput high. 08:43-10:31
- The talk notes that mid-trajectory checkpoint updates can make a trajectory somewhat off-policy, but the system accepts that risk to remove bottlenecks and process more interaction data. 10:34-11:31
- Cline's coding-agent environment recipe starts from a real repository snapshot and user prompt, reconstructs the real solved state, documents dependencies, removes Git from the Dockerized environment to reduce reward hacking, and records traces for repeatable scoring. 05:07-10:01
- Snorkel's FinQA environment shows the same artifact pattern for a financial-analysis tool task: it is fully self-contained with no external dependencies (no remote data center the trainer cannot reach), provides a fixed set of tools (`get_table_names`, `get_table_info`, query), and packages two benchmarks inside one environment — FinQA (290 samples) and the harder multi-table FinQA-reasoning (79 samples). It is published on Prime Intellect's infrastructure, saved into the OpenEnv repo on GitHub, and hosted in Hugging Face spaces (PyTorch and Hugging Face co-host), and a ~21-hour GRPO run inside it cost under $500. (12:10-13:30)

- DIGIWORLD adds a generation stage to the same artifact pattern for computer use: a compiler takes a parameterized task template, its verifier, and mock data, combines them with a base data case and a base UI state, enumerates every combination, and rejects the invalid ones — turning 387 authored scenarios into 3.2 million verified configurations across 15 sandboxed Android apps. The warning attached is that emitting the software is the easy half: "coding agents can generate a lot of software, but a lot of software is not the same as an effective, cool environment," and "the main craft is good software engineering" in the verification pipeline. See [compiling configurations and rejecting the invalid ones](generate-task-configurations-by-compiling-and-rejecting-invalid-combinations.md). ([Computer Use at the Edge of the Statistical Precipice](../sources/20260814_CTLa_p6iOiY.md), 05:31-09:20)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Post-train small models for narrow capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Train code models on execution traces, not only syntax](train-code-models-on-execution-traces-not-only-syntax.md)
- [Treat environments as eval, data, and training substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Environment registries make AI research more accessible](environment-registries-make-ai-research-more-accessible.md)
- [Fix Tool Discipline Before Reaching for a Bigger Model](fix-tool-discipline-before-reaching-for-a-bigger-model.md)
- [Generate Task Configurations by Compiling and Rejecting the Invalid Ones](generate-task-configurations-by-compiling-and-rejecting-invalid-combinations.md)
- [Design Eval Environments to the PRISM Principles](design-eval-environments-to-the-prism-principles.md)

Sources:
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md), 00:45-20:52
- [Code World Model: Building World Models for Computation - Jacob Kahn, FAIR Meta](../sources/20251217_sYgE4ppDFOQ.md), 08:43-11:31
- [Hard Won Lessons from Building Effective AI Coding Agents - Nik Pash, Cline](../sources/20251212_I8fs4omN1no.md), 05:07-10:01
- [RL Environments at Scale - Will Brown, Prime Intellect](../sources/20251209__IzZWeuTx7I.md), 05:42-12:05
- [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](../sources/20260610_TNwJ1LMiENk.md), 12:10-13:30
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 05:31-09:20
