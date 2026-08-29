# Mine Chat History for Past Decisions and Turn Them Into Judgment Evals

Summary: Nobody keeps a decision log, but chat and email hold hundreds of decisions already made with their context attached — which makes the archive a ready-made eval set for calibrating an agent's judgment against a specific person's or team's, on the axis where no benchmark exists.

Use when:
- Building an agent expected to decide or recommend the way a particular person or team would.
- You want evals for judgment quality and have no labelled data, no rubric, and no time to write one.
- Someone objects that decisions were never recorded anywhere, so calibration is impossible.

Details:
- The construction is stated as an eval build, not a prompt build: "I made a decision-making framework where I analyzed hundreds of decisions I've made in the past… I actually created evals from those decisions and calibrated this agent system to behave like myself." ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 09:10-09:27)
- The objection and its answer are the reusable part. Asked "what artifacts are those? Usually people don't save like their decisions. Is it Slack? Is it email?", the answer is both, with the general claim behind it: "a surprisingly large amount of everything that goes on a company is on Slack… if you just read like a ton of Slack history, like you can definitely find hundreds of decisions that you made in the past." (13:36-14:08)
- The archive supplies the two things a judgment eval needs and a rubric does not: the *situation as it actually arrived* (partial information, in someone else's words) and the *decision as actually made*, rather than the decision a person says they would make when asked in the abstract.
- This is the judgment half of a person-clone; the style half is a separate measurement over a different corpus, and the two fail differently — a draft can sound exactly right and decide wrong. See [Derive an Agent Persona From a Measured Corpus, Not a Described Tone](derive-an-agent-persona-from-a-measured-corpus-not-a-described-tone.md). (08:52-09:27)
- Because an eval suite is also the behavioral specification an agent is tuned toward, a decision-mined suite inherits the biases of the recovered decisions — including the selection effect that decisions worth typing into Slack are the contested ones. See [An Agent's Eval Suite Describes Its Behavior](an-agents-eval-suite-describes-its-behavior.md).
- **Limits.** This is the strongest methodological claim in the talk and the least verified: no pass rate, no baseline, no held-out split, no description of how a decision was scored, and no evidence about whether the resulting drafts were accepted or rewritten by their recipients. Mining a company's chat history for one person's decisions also reads every conversation those decisions sat in, which is not discussed. (09:10-09:27, 13:36-14:08)
- **The pre-traffic alternative when there is no history worth mining.** Where this method recovers an eval set from what already happened, Izmit derives one from what is supposed to happen: 150 questions taken straight from the documented sales process, written before the agent was tried and deliberately including questions the system could not yet answer. Chat history gives you real distribution and real judgment calls; a process document gives you coverage of the job and nothing about how it is actually done. They fail in opposite directions, and a new deployment usually only has the second one. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 04:08-04:42)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Go To Market](../topics/go-to-market.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Derive an Agent Persona From a Measured Corpus, Not a Described Tone](derive-an-agent-persona-from-a-measured-corpus-not-a-described-tone.md)
- [An Agent's Eval Suite Describes Its Behavior](an-agents-eval-suite-describes-its-behavior.md)
- [Use Golden Data Sets and Mixed Scoring Functions for AI Application Confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Generate Eval Data by Reversing the Inference Workflow](generate-eval-data-by-reversing-the-inference-workflow.md)
- [Scope a Person-Cloned Agent by Caller, With Drafts as the Shared Capability](scope-a-person-cloned-agent-by-caller-with-drafts-as-the-shared-capability.md)
- [Write the Question Set From the Business Process Before the Data Is Connected](write-the-question-set-from-the-business-process-before-the-data-is-connected.md)

Sources:
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 09:10-09:27, 13:36-14:08
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 04:08-04:42
