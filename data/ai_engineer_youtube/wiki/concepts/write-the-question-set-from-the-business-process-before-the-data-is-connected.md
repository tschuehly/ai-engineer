# Write the Question Set From the Business Process Before the Data Is Connected

Summary: Derive the evaluation set from the work the users actually do, not from what the current system can reach. Questions the agent cannot answer yet are the point: they measure the gap between the product and the job, and they are the only thing that keeps a data roadmap honest.

Use when:
- Starting or inheriting an assistant that already has data sources connected but no eval set.
- The engineering team objects that a proposed test question is out of scope because the data is not wired up.
- Deciding which data source to connect next and wanting the ranking to come from demand rather than from availability.
- Establishing a baseline number that a launch decision can be argued against.

Details:
- The method, and its order of operations: "before I even tried the agent, I opened a spreadsheet, I took the sales process, I wrote down 150 questions." The source of the questions is the documented business process, not the system's capabilities or a brainstorm. ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 04:08-04:28)
- **The objection is the signal.** "And then our engineering team was like, 'What are you doing? We don't have that data in the agent.' I was like, 'It doesn't matter. These are the questions your sellers are going to ask.'" An eval set restricted to connected data measures the system against itself; one written from the process measures it against the job, and the unanswerable questions become the data backlog. (04:28-04:36)
- The baseline it produced was low and useful: "we run our test, 50% accuracy, you know, like everyone's depressed." That number is what made the quality-over-coverage decision arguable rather than a preference ([Choose Quality Over Coverage](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)). (04:36-04:42)
- The state it was written against matters for how cheap this is: the team already had dashboard data sources connected, a knowledge assistant, and "three lines of agent instructions." The eval set was a spreadsheet written by one person from an existing process document — no labeling budget, no annotation tool, no traces required, and available before any usage exists. (04:08-04:22)
- **This is the pre-launch counterpart to trace mining, and it solves the cold start that trace mining has.** Promoting clustered production failures into a golden dataset ([Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md)) needs traffic; a process-derived question set needs only the process. Once traffic exists, the same team reads demand off the log instead ([Classify the Assistant Question Log to Find Feature and Content Gaps](classify-the-assistant-question-log-to-find-feature-and-content-gaps.md)), and the two are the same instrument at different stages.
- Limits: what "accuracy" means over 150 free-form business questions is never defined in the source — no rubric, grader, or partial-credit scheme is described, and no later score against the same set is reported, so the set's value as a tracked regression suite is asserted rather than shown. ([Provenance and Limits](../sources/20260826_DrTdD-ttjCY.md))
- **A sibling pre-build method that captures the process by observation rather than by enumeration.** Where Izmit writes 150 questions off the sales process before the data is connected, Liu watches the reps run it: "before you build, shadow your best human… I saw how many tabs and tools they were navigating between, and that was chaos, but it was also the spec." The two produce different artifacts from the same commitment — the eval set comes from what people ask, the workflow spec from what they do — and both refuse to let the current system's reach define the requirement. ([Liu](../sources/20260826_L4I7WgiEquo.md), 19:26-20:01)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Business Intelligence](../topics/business-intelligence.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)
- [Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md)
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Use Challenge Eval Sets For Future User Demands](use-challenge-eval-sets-for-future-user-demands.md)
- [Evaluate BI agents with real metadata and expert feedback](evaluate-bi-agents-with-real-metadata-and-expert-feedback.md)
- [Mine Chat History for Past Decisions and Turn Them Into Judgment Evals](mine-chat-history-for-past-decisions-and-turn-them-into-judgment-evals.md)
- [Shadow Your Best Human Before Encoding the Workflow](shadow-your-best-human-before-encoding-the-workflow.md)

Sources:
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 04:08-04:42
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 19:26-20:01
