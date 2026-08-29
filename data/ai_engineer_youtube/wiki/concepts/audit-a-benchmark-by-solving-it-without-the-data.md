# Audit a Benchmark by Solving It Without the Data

Summary: Run your benchmark with the thing it claims to be testing use of removed — the dataset, the codebase, the documents, the tool — and score what the agent still gets right. That residual is the benchmark's floor, and on three widely used data-science benchmarks it was 20-50%: up to half the tasks were answerable by reasoning from the prompt alone, without ever touching the data.

Use when:
- Adopting an existing benchmark and wanting one cheap check before trusting its scores.
- Building a benchmark whose whole premise is that the agent must work with a supplied artifact — a dataset, a repository, a corpus, a database, an API.
- A score looks credible and you need evidence that the agent is doing the work rather than pattern-matching the task description.
- Diagnosing why benchmark improvements are not showing up in production behavior.

Details:
- The finding, in the source's terms: existing widely-used data-science benchmarks "are actually very vulnerable to shortcuts," shown as a red bar next to each benchmark's green performance bar measuring "what fraction of the benchmark the agents can actually solve without actually using the data sets themselves… just by reasoning or by doing other shortcuts without actually working with the underlying data sets." Across the three shown, "sometimes up to 20 to 50% of the tasks can be solved without actually looking at any of the underlying data." (11:58-13:01)
- **The method is an input ablation, and that is what makes it general.** It needs no new tasks, no new grader, and no ground truth beyond what the benchmark already has. Name the input the benchmark exists to test the use of, withhold it, re-run, and read the residual. A repository-level coding benchmark answerable without the repository, a RAG benchmark answerable without the corpus, and a tool-use benchmark answerable without the tool all fail the same way for the same reason: the task statement leaks the answer.
- **Interpret the residual as a floor, not as an error rate.** Some tasks in any well-designed set will be answerable from general knowledge and that is not automatically a defect; what the number tells you is how much of a reported score is not evidence of the capability being claimed. A model scoring 60% on a benchmark with a 40% no-data floor has demonstrated far less than the headline implies, and two models 5 points apart may be indistinguishable on the part that matters.
- **This is a third, distinct benchmark exploit, and it defeats the fixes for the other two.** [Sealing the environment](seal-eval-environments-against-answer-leaking-agents.md) blocks an agent reaching *outside* the task at runtime to read a leaked solution — irrelevant here, because nothing is fetched. [Varying the initial state](a-blind-replay-script-exposes-a-deterministic-benchmark.md) defeats a script that replays a recorded action sequence — irrelevant here, because the shortcut is not an action sequence but an inference from the prompt. This exploit lives in the *task statement*: the question is over-specified relative to its data. The fix is also different in kind — you cannot seal it or randomize it, you have to rewrite the tasks so the answer depends on the artifact.
- **DSGym's own tasks were curated to survive this audit**, along two tracks: for scientific analysis, going "through recently published papers and then carefully curated data and then also tasks from those papers," with "human scientists and experts to review each of those tasks"; for predictive modeling, recent still-open Kaggle competitions "where also you have high quality data sets and also high quality evaluations." The summary claim is "we have carefully verified that there are no shortcuts in these tasks." (13:03-13:47, 15:20-15:28)
- Headroom on the rebuilt set: frontier models "often are only still achieve less than 50% accuracy performance on the DSGym tasks… these are definitely not saturated benchmarks." (14:06-14:25)
- **What the source does not supply, and you will have to decide yourself.** How the no-data condition was actually run is unreported — whether the agent was told the data was missing, what it saw in its place, how a "solved" task was scored when no data existed to compute against, which three benchmarks were tested, and with which models. The 20-50% figure is read off a bar chart by the group building the replacement benchmark. That makes it weak as a citation about those specific benchmarks and strong as a method you can run against your own, where you control all of those choices.
- Related but distinct from the wiki's [construct-validity](build-coding-benchmarks-around-construct-validity.md) material: construct validity asks whether the task measures the intended capability, this asks whether the task's *inputs* are load-bearing. A perfectly valid construct can still be answerable without its data if the prompt says too much.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [A Blind Replay Script Exposes a Deterministic Benchmark](a-blind-replay-script-exposes-a-deterministic-benchmark.md)
- [Seal Eval Environments Against Agents That Read the Leaked Answer](seal-eval-environments-against-answer-leaking-agents.md)
- [Build coding benchmarks around construct validity](build-coding-benchmarks-around-construct-validity.md)
- [Curate Tasks by Live Human Demand and a Deterministic Verifier](curate-tasks-by-live-human-demand-and-a-deterministic-verifier.md)
- [Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)
- [Benchmark your tool by running agents with and without it](benchmark-your-tool-by-running-agents-with-and-without-it.md)
- [Design Eval Environments to the PRISM Principles](design-eval-environments-to-the-prism-principles.md)
- [Treat Environments as Eval, Data, and Training Substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Distill Reasoning Traces Into Small Models](distill-reasoning-traces-into-small-models.md)

Sources:
- [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 11:58-15:28
