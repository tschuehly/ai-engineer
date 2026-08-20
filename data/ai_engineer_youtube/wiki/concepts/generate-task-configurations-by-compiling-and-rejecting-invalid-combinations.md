# Generate Task Configurations by Compiling and Rejecting the Invalid Ones

Summary: Scaling an agent environment to millions of task variants is not a generation problem — a coding agent can emit unlimited variation, and "a lot of software is not the same as an effective environment." The scaling primitive is a compiler that enumerates every combination of task template, verifier, mock data, base data case, and base UI state, then rejects the broken ones and keeps only verified configurations.

Use when:
- Turning a handful of hand-written eval tasks into a large varied task set.
- Someone proposes generating benchmark or RL-environment variants with a coding agent.
- Deciding what a "task" artifact should contain so it can be parameterized safely.
- Explaining why a large generated eval suite got weaker rather than stronger.

Details:
- The rejected shortcut is named explicitly: "you might think maybe it's easy to build an environment — you just generate as much software as you can with a coding agent and then you have a diverse environment. But it's a little bit trickier than that… coding agents can generate a lot of software, but a lot of software is not the same as an effective, cool environment." (07:25-07:45)
- Why generation is the easy half: the variation axes "can be manipulated by coding agents because in the end they are like forms of software" — a coding agent will happily produce new data profiles, themes, and starting screens. What it cannot do for free is establish that the resulting configuration is still a solvable, correctly-graded task. (07:11-07:24)
- The strategy in one line: "generate many configs, all the combinations of the different factors, and then have a system that rejects the broken ones, the ones that are not valid, and just keeps the valid configs." Over-generate then filter, rather than trying to generate only-valid combinations. (08:03-08:23)
- The compiler's inputs, which double as a spec for what a parameterized task should carry: a **task template** with parameters ("send a certain amount to a certain recipient"), a **verifier corresponding to that template**, and **mock data** the task needs; the compiler combines those with a **base case of data** and a **base case of UI state** to emit one valid configuration. Note the verifier is attached to the template, so it is parameterized alongside the task rather than written per-variant. (08:23-09:09)
- Combinatorics are why this pays: "even if you start from a relatively low number of base cases for each one of these variables, you end up having many many combinations… you can get to millions, and if you scale this up, you can get to easily billions." DIGIWORLD reports 387 verified scenarios expanding to 3.2 million verified configurations across 15 Android apps. (05:56-07:10)
- Where the actual difficulty sits, stated plainly: "you can build systems like this in which the main craft is good software engineering, to make sure that actually the combinations that you have are both diverse and valid." The differentiator is an engineering pipeline, not a prompt. (09:09-09:20)
- The failure this prevents is quiet. An unverified generated config that is unsolvable or mis-graded does not announce itself — it just lowers every model's score by the same amount, which looks like a harder benchmark rather than a broken one, and it corrupts model comparison only when the breakage correlates with something a model is good at.
- This is the mechanized form of the wiki's existing environment-as-software-artifact position: [environments packaged as runnable artifacts](build-rl-environments-as-software-artifacts.md) with setup, transitions, and rewards, extended with a generation-and-rejection stage so one authored artifact yields a verified combinatorial family.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Design Eval Environments to the PRISM Principles](design-eval-environments-to-the-prism-principles.md)
- [A Blind Replay Script Exposes a Deterministic Benchmark](a-blind-replay-script-exposes-a-deterministic-benchmark.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Treat Environments as Eval, Data, and Training Substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Validate eval harnesses before trusting skill scores](validate-eval-harnesses-before-trusting-skill-scores.md)
- [Keep Eval Data Constant and Task Logic Variable](keep-eval-data-constant-and-task-logic-variable.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)

Sources:
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 05:56-09:20
