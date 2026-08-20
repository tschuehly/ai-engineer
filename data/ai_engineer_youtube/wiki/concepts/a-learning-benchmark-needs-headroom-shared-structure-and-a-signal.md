# A Learning Benchmark Needs Headroom, Shared Structure, and a Signal

Summary: A task can only measure learning if it satisfies three things at once: headroom (it is not already solved by offline training), shared latent structure across instances (there is something for experience to transfer), and a learning signal in the environment (reward, error messages, or plain text feedback). Missing any one of them makes the resulting number uninterpretable rather than merely noisy.

Use when:
- Building an internal benchmark for a memory system, agent harness, personalization loop, or anything that accumulates state.
- A memory or learning feature shows no measurable improvement and you are deciding whether the feature or the eval is at fault.
- Vetting a published continual-learning or agent-memory result before importing its conclusion.

Details:
- **Headroom.** "You need some sort of task that actually requires online adaptation or learning from the language models. And that doesn't exist for a wide variety of the benchmarks where the models are just trained offline on that data. If the model can improve on your tasks by just training offline and not actually require any online learning, then it's not a good task for measuring continual learning." ([Evaluating Continual Learning](../sources/20260812_iqloyWCGYQQ.md), 05:51-06:32)
- Why frontier models make headroom the binding constraint: they "are pre-trained on vast distributions of the entire internet or economically valuable tasks we care about. And so if you're expecting to see improvement on new tasks, it's actually really hard to come up with what those sorts of tasks should look like." (04:48-05:08)
- **Shared latent structure.** "There needs to exist some shared latent structure between the tasks. You can kind of think of this as some sort of shared latent in the environment that your models or agents are learning over time and they're seeking to exploit these latent structures that exist in the environments to improve their performance on future tasks as a result of their prior information." (06:32-07:08)
- **A learning mechanism in the environment.** "There has to be some realistic expectation that the models are able to learn as a result of their prior experience. This could look like scalar reward. It could look like error messages. It could look like textual feedback. The point being, there needs to exist something in the environment that's giving agents signal to learn and improve on future tasks. Otherwise, it's not really a fair measure of continual learning." Note how low the bar is: an error message counts. (07:08-07:34)
- A concrete task that satisfies all three: answering natural-language questions over an unfamiliar database via SQL. Headroom, because the specific schema is not in pretraining; shared structure, because every question hits the same schemas and idiosyncrasies; signal, because query results and errors come back from the database. The reward is efficiency — a learning system needs fewer queries by the tenth instance. (10:39-12:00)
- The three criteria are also the diagnostic to run *backwards* when a learning feature measures flat. Zero measured gain is consistent with a system that does not learn, but equally with a task the base model already solves (no headroom), a task set whose instances share nothing (no structure), or an environment that never tells the system it was wrong (no signal). Only the first is a fact about your system.
- **Relationship to the general benchmark-quality checklist already in this wiki.** Snorkel's four properties — task quality, distributional diversity, headroom, robust methodology ([Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)) — share the word *headroom* but not the meaning. There, headroom means unsaturated: frontier models do not already score near the ceiling. Here it means something stricter and orthogonal: the task must not be improvable by offline training at all, so a benchmark can be unsaturated and still be useless for measuring learning. Shared latent structure has no counterpart in that checklist, because it is a property of the *sequence* rather than of any instance, and standard benchmark design deliberately removes it.
- Task validation in the source benchmark was human: "all of these task instances across domains we validate with domain experts to see is this learnable? Is this realistic? Is these the sorts of drifts you would expect and things you would expect to remember in an environment." Note the first question is precisely a check that the three criteria hold. (13:29-13:52)
- Caveats: the criteria are asserted from benchmark-design experience, not derived or ablated — no result shows what happens to measured gain when each is violated. The expert-validation protocol is not described beyond the sentence quoted.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Measure Learning as Gain Over a Memory-Wiped Rerun](measure-learning-as-gain-over-a-memory-wiped-rerun.md)
- [Chained Independent Benchmarks Cannot Measure Learning](chained-independent-benchmarks-cannot-measure-learning.md)
- [Inject Concept Drift to Test What a System Forgets](inject-concept-drift-to-test-what-a-system-forgets.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Design Eval Environments to the PRISM Principles](design-eval-environments-to-the-prism-principles.md)
- [Design Benchmarks as Forward Bets That Shape the Field](design-benchmarks-as-forward-bets-that-shape-the-field.md)
- [Treat Environments as Eval Data and Training Substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Use Verifiable Rewards for Language Model RL](use-verifiable-rewards-for-language-model-rl.md)

Sources:
- [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../sources/20260812_iqloyWCGYQQ.md), 04:48-07:34, 10:39-13:52
