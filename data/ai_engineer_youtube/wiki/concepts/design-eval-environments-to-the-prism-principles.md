# Design Eval Environments to the PRISM Principles

Summary: PRISM is a five-property checklist for an agent environment that cannot be gamed by memorized determinism — privileged verification, realism, integrity-checked configurations, sandboxed execution, and multifactorial variation. Most existing benchmarks satisfy some of them; the one that is both rare and load-bearing is varying the initial state across runs.

Use when:
- Building an agent benchmark or RL environment and needing an acceptance checklist before you trust its scores.
- Auditing an existing environment to find which property it is missing.
- Deciding what to vary between runs of the same task.
- Justifying why "we sandbox and we have a verifier" is not enough.

Details:
- The five properties, with the acronym expansion taken from the video description (the audio names PRISM but does not spell it out):
  - **P**rivileged verification — the environment must support verifiers, which means giving the grader privileged information about internal state rather than judging from the same screen the agent saw. (05:04-05:10)
  - **R**ealism — "if it's a reproduction of a real system, you want that reproduction to be faithful so that the score that you get out is a good one." (05:14-05:24)
  - **I**ntegrity-checked configurations — "a system for checking and verifying that everything is working as intended for *every* combination," which is the cost that variation imposes. (04:42-04:58)
  - **S**andboxed execution — the ordinary isolation requirement. (05:02-05:05)
  - **M**ultifactorial variation — generate stochasticity across data, appearance/theme, and the initial state. (04:21-04:41)
- Multifactorial variation is derived rather than assumed: it is the direct answer to "what would stop [a blind replay script](a-blind-replay-script-exposes-a-deterministic-benchmark.md) from hacking my benchmark," which is why it heads the list of things to add to an existing environment. (04:10-04:25)
- Integrity checking is not optional hygiene but the paired cost of variation — every combination you generate is a new opportunity for the task to be broken or unsolvable, and an unverified config silently becomes an unsolvable task that depresses every model's score equally. See [compiling configs and rejecting the invalid ones](generate-task-configurations-by-compiling-and-rejecting-invalid-combinations.md).
- Field coverage: "if you look at existing benchmarks, some of them do some things in a good way, some others do other things in a good way, but there is no unified benchmark that sort of matches all of these boxes." DIGIWORLD is presented as the attempt to satisfy all five at once — 15 sandboxed Android apps, 387 verified scenarios, 3.2 million verified configurations. (05:38-06:22)
- The single highest-value addition for a team that already sandboxes and verifies: "some things like *varying initial state across runs* — they are pretty rare across existing benchmarks, but they are very important, and so I would suggest you try to incorporate these into your evals." Starting every run of a task from the login screen is exactly what makes the recorded action sequence a constant. (15:16-15:30)
- Relation to the wiki's other benchmark checklist: Snorkel's four properties ([task quality, diversity, headroom, methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)) are about whether the *task set* is a sound measuring stick; PRISM is about whether the *environment each task runs in* can be short-circuited. They are complementary and neither implies the other — a benchmark can have expert-validated, diverse, unsaturated tasks and still be beaten by a one-megabyte script.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [A Blind Replay Script Exposes a Deterministic Benchmark](a-blind-replay-script-exposes-a-deterministic-benchmark.md)
- [Generate Task Configurations by Compiling and Rejecting the Invalid Ones](generate-task-configurations-by-compiling-and-rejecting-invalid-combinations.md)
- [Measure Agent Robustness per Variation Axis, Not Just Average Success](measure-agent-robustness-per-variation-axis-not-just-average-success.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Push Agent Benchmarks on Environment Complexity, Autonomy Horizon, and Output Complexity](push-agent-benchmarks-on-environment-autonomy-and-output-complexity.md)
- [Control environment noise for group-based RL](control-environment-noise-for-group-based-rl.md)
- [Seal Eval Environments Against Agents That Read the Leaked Answer](seal-eval-environments-against-answer-leaking-agents.md)

Sources:
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 03:47-06:22, 15:16-15:30
