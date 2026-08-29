# Use Golden Data Sets and Mixed Scoring Functions for AI Application Confidence

Summary: AI application releases need curated test cases and scoring functions that combine deterministic assertions with LLM-as-judge checks for nuanced behavior.

Use when:
- Replacing anecdotal manual testing with a repeatable pre-production confidence gate.
- Choosing between deterministic checks and judge-model scoring for an AI workflow.

Details:
- The workshop recommends creating a golden data set of edge cases for a support application so teams can show business stakeholders concrete release evidence instead of relying on vibe-based demos, 58:17-58:48.
- Deterministic scoring functions are analogous to unit tests: cheap, easy to run, and useful where the expected condition can be encoded without another model, 58:51-59:13.
- LLM-as-judge scoring is reserved for nuanced criteria that deterministic checks cannot capture, such as brand style or customer satisfaction, 59:15-59:46.
- Golden data sets should include failure modes and edge cases that are likely to matter in production, and later production failures can be added as regression cases, 01:35:30-01:35:43.
- Witan Labs corroborates the "deterministic where possible, LLM-judge as fallback" split for agent output: they started with LLM-as-judge only ("sometimes it's the only option you really have"), but its annoyance is a confound — "you can't really tell when a score changes, is it because the agent changed something or the evaluator changed what it outputs" — so a judge-only setup can't separate agent regressions from judge drift. ([Witan Labs](../sources/20260708_HEFSExa0xl0.md), 13:29-14:23, 18:38-18:47)
- Their deterministic replacement is a golden artifact used as a black box: take a golden spreadsheet with known inputs and outputs, put the same inputs into the model-produced spreadsheet, and check the outputs match — "sometimes more trustworthy than just using an LLM to grade that work." Getting evaluation right was what actually told them whether alternative representations (CSV, SQL) were any good. ([Witan Labs](../sources/20260708_HEFSExa0xl0.md), 14:23-15:05, 13:29-13:53)
- **When the eval needs a *pair* of artifacts, the public corpus usually has only one of them.** Grading design-to-code output requires a design file and the codebase it should produce, and Figma found that "there's a lot of open source code out there but there's not a lot of uh open-source code that also has fig files attached," so "we had to either create our own or sort of find different ways to make automated systems" — a set of toy repos authored or commissioned for the purpose. Any system that spans two artifact types inherits this: dataset construction, not scoring design, is the first cost, and a self-authored corpus carries whatever assumptions its authors held about typical inputs. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 06:13-06:45)
- **The golden set's second job is calibrating the judge, not only gating the release.** In DoorDash's loop the annotated golden dataset is the optimization target: "you obviously have some LLM as a judge metric that you're tracking; you want to now start improving that with these golden data sets," running baseline scores across traces and then an optimizer against the labeled set. The set is therefore consumed twice — once as a pass/fail gate, once as the ground truth that decides whether the judge is any good — and both uses degrade together if the annotations are thin. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 10:29-11:24)

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Pick the Serialization the Models Have Seen Most, Not the One Native to Your System](pick-the-serialization-the-models-have-seen-most.md)
- [Show the Prompt Diff So a Non-Engineer Can Promote an Optimized Judge](show-the-prompt-diff-so-a-non-engineer-can-promote-an-optimized-judge.md)

Sources:
- [Shipping complex AI applications - Braintrust & Trainline](../sources/20260501_ZdheJTfLu-s.md), 58:17-59:46, 01:35:30-01:35:43
- [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../sources/20260708_HEFSExa0xl0.md), 13:29-15:05, 18:38-18:47
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 06:13-06:45
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 10:29-11:24
