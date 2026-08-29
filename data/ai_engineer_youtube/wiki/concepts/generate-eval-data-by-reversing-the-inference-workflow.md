# Generate Eval Data by Reversing the Inference Workflow

Summary: When you cannot keep the production data your evals need, generate it by running the task backwards — sample the label first, sample a reasoning trace that reaches it, then synthesize the input that would have produced that trace. Labels come out correct by construction, and if the trace is sampled from an explicit policy representation rather than invented by an LLM, the generated set is more diverse than production data and far more diverse than one-shot LLM generation.

Use when:
- Contracts, PHI rules, or retention policy forbid persisting the real inputs your eval sets need.
- An eval set is scored highly but you suspect it misses the rare cases that decide production accuracy.
- Ground-truth labelling by domain experts is the bottleneck on eval coverage.
- An LLM asked to "generate varied examples" keeps producing the same few cases.

Details:
- The motivating constraint is stronger than privacy hygiene: Anterior's contracts prohibit retaining, reusing, or *deriving information from* the medical records, and redaction, anonymization, and derivative copies are "a strict no-no, completely off the table," so "nothing really survives in any sort of dataset that we want to persist." The talk's framing is "what do you do when the dataset you most need is also the data you're least allowed to keep." (02:29-03:00)
- The forward task is unstructured data plus a policy → reasoning trace → outcome, and the outcome is the label. Reversing it means "sampling a random label, figuring out a reasoning trace for that label, and then trying to generate data backwards from that," which conditions generation on diverse inputs instead of hoping the generator is creative. (05:00-05:48)
- The reversal only pays off if the trace can be sampled from something structured. Anterior already models policies "explicitly as decision trees" in a symbolic representation — adopted first because it "helps us achieve a better accuracy and consistency score when executing them in LLM-based workflow" — which incidentally gives "a way to kind of deterministically sample different reasoning traces for a given outcome." That distribution is "a much more uniform and effective prior distribution than what you'd normally get from an LLM." (05:53-07:18)
- The failure mode being avoided is mode collapse, attributed to two causes: little exposure to the data source in the pre-training corpus, and pre-training/post-training objectives that "are not incentivized for creativity or diversity … they're incentivized to be helpful systems." (04:32-04:50)
- Coverage is the second argument, independent of privacy: 200 real customer cases scoring 95% "doesn't really tell you about … your performance … in those rare edge cases that are not in that data set," and with highly variant data there will always be cases outside the sampled distribution. Sampling from the policy tree tests branches production traffic has not yet exercised. (07:19-07:52)
- Because the run starts from a label, the pipeline can compare the generated record back against the original task inputs and outputs — a round-trip check that keeps the data in sync and yields "the correct labels by construction," so you "basically skip the … expensive ground truth[ing] process." This is the property that changes the economics, not just the legality. (10:26-11:00)
- Reported outcome: roughly 90% of Anterior's datasets are synthetic, used for evaluation only at the time of the talk; in a blind review clinicians distinguished synthetic from real "about 60% of the time." The operational win is that datasets are "created just in time for these customer deployments," so a workflow can be evaluated before any customer data arrives. (14:09-15:18)
- Scope claim: "you don't need a PHI problem for this" — the pattern applies whenever the needed data is "ephemeral, sensitive, or even expensive to label." (16:16-16:26)
- **Recovery as an alternative to synthesis.** Where this page generates eval items by running the workflow backwards, Wang's clone project takes them from an archive instead: hundreds of past decisions mined out of Slack and email become the eval set, on the argument that "a surprisingly large amount of everything that goes on a company is on Slack." Recovered items carry real inputs and a real chosen answer at the cost of coverage you do not control; synthesized items give coverage you design at the cost of realism. The two are complementary rather than competing. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 09:10-09:27, 13:36-14:08)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Build Synthetic Records Coarse to Fine by Emulating How They Were Produced](build-synthetic-records-coarse-to-fine-by-emulating-their-source-process.md)
- [Hand Domain Experts the Pipeline as Skills](hand-domain-experts-the-pipeline-as-skills.md)
- [Align Synthetic Retrieval Queries With Real User Specificity](align-synthetic-retrieval-queries-with-real-user-specificity.md)
- [Replace Ship-and-Rollback With Hazard-First Simulation When Errors Are Irreversible](replace-ship-and-rollback-with-hazard-first-simulation.md)
- [Production Failure Sets Drive Domain AI Iteration](production-failure-sets-drive-domain-ai-iteration.md)
- [Use Challenge Eval Sets for Future User Demands](use-challenge-eval-sets-for-future-user-demands.md)
- [Mine Chat History for Past Decisions and Turn Them Into Judgment Evals](mine-chat-history-for-past-decisions-and-turn-them-into-judgment-evals.md)

Sources:
- [Don't be data poor — Anuj Iravane, Anterior](../sources/20260819_XAsb7MIAzm8.md), 02:29-07:52, 10:26-11:00, 14:09-16:26
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 09:10-09:27, 13:36-14:08
