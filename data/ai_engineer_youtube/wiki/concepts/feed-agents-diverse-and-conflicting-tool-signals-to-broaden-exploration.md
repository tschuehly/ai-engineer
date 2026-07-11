# Feed Agents Diverse and Conflicting Tool Signals to Broaden Exploration

Summary: Don't hand the agent only the single optimal answer — expose several tool signals that deliberately disagree (the objective best, the human-likely choice, a beginner heuristic), because the conflict gives the agent diversity to explore variations and to explain why plausible-but-wrong options fail, which is often what the human output actually needs.

Use when:
- The valuable output is an explanation or teaching artifact, not just the one correct answer — you need to cover the moves/options a human would consider, including bad ones.
- A single "best answer" oracle would make the agent terse or blind to human-relevant alternatives.
- You can compute multiple heterogeneous views of the same situation (optimal, typical, heuristic) and want the agent to reconcile them in prose.

Details:
- The counterintuitive claim: "this kind of conflicting information which we provide by the tools is actually very beneficial." Surfacing reasonable-looking-but-bad options (e.g. checks that lose) gives "quite some diversity to the agent to explore other kinds of variations" and to "describe which ones are actually bad because a human might think about them."
- "It's not always about the very very best move which we have to describe" — a pure best-move signal optimizes for correctness but strips out the human-relevant alternatives that make an explanation useful.
- Concrete signal mix: (1) engine best move / evaluation (objective truth), (2) a beginner heuristic tool — "checks, captures and threats," a well-known focus rule — that enumerates candidate forcing moves including bad ones, and (3) a rating-conditioned human-move model (the Maia engine, University of Toronto): feed a player rating and it predicts a move "that player might want to play," "not perfect" but valuable signal that a human-plausible move "deserves a description."
- The diverse signals also let you *target the audience*: the same human-move rating knob decides whether to explain a mate-in-one (trivial for strong players, valuable for beginners), so conflicting signals double as an audience-selection lever.
- This is the complement to routing a non-deterministic planner into a deterministic answer: here you *want* the agent to see and weigh disagreement rather than collapse to one path, because the deliverable is the reasoning across options, not a single committed action.

Related topics:
- [Tools](../topics/tools.md)

Related concepts:
- [Pair an LLM Narrator With a Domain Solver Via Tools](pair-an-llm-narrator-with-a-domain-solver-via-tools.md)
- [Run a Jury of Analysts and a Consensus Judge for No-Ground-Truth Questions](run-a-jury-of-analysts-and-a-consensus-judge-for-no-ground-truth-questions.md)
- [Evaluate tool definitions and outputs as context](evaluate-tool-definitions-and-outputs-as-context.md)

Sources:
- [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](../sources/20260708_BqZrTdgBaPw.md), 06:22-09:44, 14:15-15:10
