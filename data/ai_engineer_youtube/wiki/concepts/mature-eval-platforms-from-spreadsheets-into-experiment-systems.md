# Mature Eval Platforms From Spreadsheets Into Experiment Systems

Summary: Eval platforms should grow from simple documented runs into systems that let teams compare agent configurations, collect scores, and include domain experts in the evaluation loop.

Use when:
- Moving beyond a spreadsheet of prompt outputs and handwritten scores.
- Designing evaluation tools for both engineers and non-technical subject matter experts.

Details:
- A for-loop over inputs plus a spreadsheet of outputs is a useful start because it acknowledges the eval problem and has almost no barrier to entry, 08:48-09:24.
- Spreadsheet-based evals quickly become documentation rather than experimentation: direct experiment comparison, analytics across runs, and scaled human scoring are hard to manage, 09:24-10:15.
- Evals are a team sport; domain experts and user-proximate non-technical collaborators need accessible ways to contribute, but they are unlikely to work effectively inside raw spreadsheets, 10:15-10:37.
- A mature eval surface should provide a sandbox where users can tweak controlled agent parameters, such as system instructions, compare configurations, and inspect scores for both functional and technical behavior, 12:25-13:53.
- **A team that ran the spreadsheet stage exactly once and treated it as a decision, not a phase.** Figma graded design-to-code output by hand on a mix of quantitative criteria (did it use variables, the expected theming, the right spacing) and qualitative ones (does it look good, "did it make good decisions with incomplete information"), and stopped immediately: "we spent like two hours grading an eval into an Excel spreadsheet. And we said, we're never we're never doing that again. It was awful. Don't do eval by hand if you can help it." They built a web app for the grading process, then automated it behind LLM judges — "an eval that sort of runs like hundreds of times a week. Engineers can kick this off and sort of grade against prompt changes… So, we kind of remove the human from the loop where we don't need it." The useful reading is that the manual pass earns its keep by proving the criteria are gradeable at all; two hours was enough to establish that. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 05:40-06:58)

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Evaluate agent skills with task scenarios and comparative conditions](evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md)
- [Pick the Serialization the Models Have Seen Most, Not the One Native to Your System](pick-the-serialization-the-models-have-seen-most.md)

Sources:
- [Why building eval platforms is hard - Phil Hetzel, Braintrust](../sources/20260428__fQ7Z_Wfouk.md), 08:48-13:53
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 05:40-06:58
