# Automating Harness Design Requires Co-Optimizing the Model

Summary: Searching over agent harnesses with the model held fixed is argued to be the wrong factorization — an automated harness designer "will only work… if you also co-optimize it with a model," which turns harness design from a fast prompt-engineering loop into a long-horizon co-training problem.

Use when:
- Considering an automated optimizer over prompts, tools, scaffolds, memory policies, or agent topology.
- Deciding whether harness work and model work belong to one team and one loop or two.
- Estimating how long an automated harness-improvement program takes to pay off.
- Reconciling fast harness iteration with slow model iteration in a roadmap.

Details:
- The claim, offered as a generalization of the same team's data result: "I mentioned that this only work[ed] because we co-optimized data and model… it will only work to do… an AutoScientist for harnesses if you also co-optimize it with a model. And so, it's… actually a long horizon problem, and that's super fascinating to think about where you're optimizing the choices for each and co-training." ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 17:19-17:38)
- The pattern being generalized is that whatever the search leaves fixed becomes the term that caps the return: data left to the agent's discretion capped the training search ([co-optimize data with the model](co-optimize-data-with-the-model-or-the-search-does-not-pay.md)), and a fixed model would cap a harness search the same way. The best harness for model A is a local optimum that says little about the harness you would build if the model could also move.
- This puts a cost on the wiki's most reliably useful advice. Harness engineering is normally attractive *because* it is cheap and fast against a frozen model — [invest in the harness to run weaker and local models](invest-in-the-harness-to-run-weaker-and-local-models.md), [read frontier traces to harness-engineer a cheap replacement](read-frontier-traces-to-harness-engineer-a-cheap-replacement.md), and [treat agent improvement as model–harness–task fit](treat-agent-improvement-as-model-harness-task-fit.md) all assume you tune the harness around a model you did not train. The claim here is narrower than it first looks: it is about *automating* harness design as a search, not about doing harness work by hand. Hand-tuning against a fixed model stays valid; a searcher that expects the harness alone to keep yielding is the thing predicted to stall.
- The practical read for a team: if you build a harness optimizer, decide up front whether you also control training. If you do not, expect the optimizer to converge and then flatten, and treat the flat part as the signal to change models rather than to keep searching. If you do, the loop is long-horizon — each harness generation's value is only visible after the model is re-trained against it — and should be budgeted like a training program, not a prompt sweep.
- The question this answers is not the one that was asked. The attendee's question (audio unrecoverable, restated by the speaker) was about balancing parametric against non-parametric storage; she names it as "one of the core questions" for automating and speeding up learning and then does not answer it, pivoting to harness co-optimization. The parametric/non-parametric balance is left open here, as it is on [Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md). ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 17:08-17:19)
- **A second founder reached the same position in Q&A at the same event, independently and with the same hedge.** Asked about harnesses, Malde: "one of the most underexplored and most exciting questions is not only just harness improvement — and I think there's some literature out there now starting to explore that — but the really exciting part is how does the model and the harness interplay with each other as you're both updating them… it's completely unexplored territory." Two companies whose products are model-side improvement both name joint model/harness updating as the open frontier and both say it is unbuilt, which raises the confidence that the factorization argument is real and lowers the confidence that anyone has a method. ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 22:11-22:36)
- Provenance: a forward-looking assertion in Q&A about a system the speaker's company has not built, extrapolated from an unpublished result about data. No harness search is described, attempted, or measured anywhere in the talk. Treat it as a well-motivated prediction about factorization, and note that the wiki holds one controlled counter-instance of harness-only measurement paying off at component level — [run harness ablations on local models to own every step](run-harness-ablations-on-local-models-to-own-every-step.md), where the model was deliberately held fixed and the ablation still separated good policies from bad. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 17:19-17:38)

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Co-Optimize Data With the Model or the Search Does Not Pay](co-optimize-data-with-the-model-or-the-search-does-not-pay.md)
- [Treat Agent Improvement as Model–Harness–Task Fit](treat-agent-improvement-as-model-harness-task-fit.md)
- [Invest in the Harness to Run Weaker and Local Models](invest-in-the-harness-to-run-weaker-and-local-models.md)
- [Read the Frontier Model's Traces to Harness-Engineer Its Cheap Replacement](read-frontier-traces-to-harness-engineer-a-cheap-replacement.md)
- [Run Harness Ablations on Local Models to Own Every Step](run-harness-ablations-on-local-models-to-own-every-step.md)
- [Automate the Agent-Building Loop With an Agentic AI Engineer](automate-the-agent-building-loop-with-an-agentic-ai-engineer.md)
- [Automated Training Search Beats Staff by Not Carrying Architecture Priors](automated-training-search-beats-staff-by-not-carrying-architecture-priors.md)
- [Today's Continual Learning Is Batch Updates and a Model Re-Upload](todays-continual-learning-is-batch-updates-and-a-model-reupload.md)

Sources:
- [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../sources/20260812_XEd_SRVHBgU.md), 17:08-17:38
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 22:11-22:36
