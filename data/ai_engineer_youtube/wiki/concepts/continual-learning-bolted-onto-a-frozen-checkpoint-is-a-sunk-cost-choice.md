# Continual Learning Bolted Onto a Frozen Checkpoint Is a Sunk-Cost Choice

Summary: Almost all continual-learning work starts from a frozen checkpoint and asks how to make it learn after the fact — but those models were never designed to learn after training, and the hypothesis worth taking seriously is that this is a sunk-cost fallacy rather than a constraint. The alternative shape is one phase of training for continual learning, after which everything is deployment.

Use when:
- Deciding how much to invest in memory and context machinery around a frozen model versus waiting for a differently-trained one.
- Reading a claim that some post-hoc method "solves" continual learning.
- Framing a research or roadmap bet about where the constraint on learning systems actually sits.

Details:
- The deployment shape being challenged: training data goes "in a box in some offline training process," then "we extract a frozen checkpoint," and "the weights don't really change after that in today's paradigm." ([Evaluating Continual Learning](../sources/20260812_iqloyWCGYQQ.md), 02:14-02:32)
- The diagnosis: "A lot of the work in continual learning today is how do we take these models that are already trained and… that frozen checkpoint. How do we figure out methods for continual learning that work after the fact? But these models were never designed to be continual learners to begin with. And one of my hypotheses here at least is that we're operating in a bit of a sunk cost fallacy that because we've trained models the way we are today, we need continual learning methods that work on top of that." (17:31-18:00)
- The alternative shape, stated as a thought experiment: "In the purest sense, continual learning might just be one set, one phase of training for continual learning and everything after that is deployment. You're just… the model is interacting in the environment. It's updating its weights. There's only one phase of learning." (18:04-18:20)
- The supporting observation that the stack is not fixed: it "used to look something simple like… pre-training, then we did supervised fine-tuning, and then we do RLHF," and now "might look something more like… mid-training, you have RL for different teacher models and you finish everything off with multi-teacher on-policy distillation." The stack already changed once under pressure; treating its current shape as a boundary condition is a choice. (17:07-17:31)
- What the speaker would bet on, offered explicitly as opinion: "I'm personally quite excited about the parametric methods for continual learning that look at alternative architectures, data, and algorithms jointly to optimize what continual learning should look like." Note *jointly* — the claim is that architecture, data, and algorithm have to move together, not that weight updates are better than notes. (16:48-17:07)
- **This is the same "co-optimize or it does not pay" shape argued from a different direction elsewhere in this wiki.** Sara Hooker reports that an automated training search "did not get the returns… until you control for data quality" ([Co-Optimize Data With the Model or the Search Does Not Pay](co-optimize-data-with-the-model-or-the-search-does-not-pay.md)), and that pointing the same search at agent *harnesses* only works if the model moves with it, because search against frozen weights converges ([Automating Harness Design Requires Co-Optimizing the Model](automating-harness-design-requires-co-optimizing-the-model.md)). Asawa's version says the same about the learning mechanism: optimizing memory machinery against fixed weights has a ceiling set by weights that were never trained to be updated.
- **The tension with the wiki's own strongest practical result, which should be held rather than resolved.** The same talk measures plain in-context learning beating elaborate context management ([Plain In-Context Learning Topped a Continual-Learning Benchmark](plain-in-context-learning-topped-a-continual-learning-benchmark.md)). Read together, the two say: the machinery you can build around a frozen checkpoint is not currently beating the null option, and the speaker's explanation is that the checkpoint is the constraint. That is a coherent position, but it is a hypothesis about *why* the harnesses underperform, not a demonstration — no parametric system in this benchmark is shown beating vanilla in-context learning either.
- What this does not license today: an engineer shipping against current APIs has only the post-hoc options, and this page is an argument about where the research constraint sits, not permission to skip building memory. The practical reading is to keep the machinery thin and the switching cost low, because it is scaffolding around a limitation rather than the durable layer.
- **There is a second freeze downstream of this one, and a vendor selling weight updates admits it.** Even for teams that do change the weights, the deployed loop is "pseudo continual learning… batch updates offline and then re-uploading the model," with merging thousands of concurrent production rollouts into one update named as unsolved ([Today's Continual Learning Is Batch Updates and a Model Re-Upload](todays-continual-learning-is-batch-updates-and-a-model-reupload.md)). So the inherited shape Asawa objects to holds at two levels: training terminates in a frozen checkpoint, and deployment freezes again between batches. Neither freeze is a design decision anyone defends; both are what the available infrastructure produces.
- Caveats: presented as a personal hypothesis by a PhD student, with no experiment, no proposed architecture, and no evidence that a differently-trained model would do better. The talk's own benchmark evaluated mostly context-management systems, with parametric approaches listed as roadmap. The corroborating point above comes from a founder describing his own field, not from a survey.

Related topics:
- [Models](../topics/models.md)
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Plain In-Context Learning Topped a Continual-Learning Benchmark](plain-in-context-learning-topped-a-continual-learning-benchmark.md)
- [Co-Optimize Data With the Model or the Search Does Not Pay](co-optimize-data-with-the-model-or-the-search-does-not-pay.md)
- [Automating Harness Design Requires Co-Optimizing the Model](automating-harness-design-requires-co-optimizing-the-model.md)
- [Define Continual Learning as Adaptive Compression of Experience](define-continual-learning-as-adaptive-compression-of-experience.md)
- [Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)
- [Pretraining Size Is No Longer the Most Lucrative Scaling Axis](pretraining-size-is-no-longer-the-most-lucrative-scaling-axis.md)
- [Place a Continual-Learning Setup on Two Axes: Trace Policyness and Hint Provenance](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)
- [Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md)
- [Today's Continual Learning Is Batch Updates and a Model Re-Upload](todays-continual-learning-is-batch-updates-and-a-model-reupload.md)

Sources:
- [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../sources/20260812_iqloyWCGYQQ.md), 02:14-02:32, 16:48-18:20
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 21:24-21:57
