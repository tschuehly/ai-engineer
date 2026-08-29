# Grade the Alignment, Not the Agents

Summary: In a multi-agent, multi-human system the thing that fails is usually the coordination, not the component. Moving the unit of evaluation from the agent to the alignment of the whole system produces a different metric set — task completion, user frustration, human-in-the-loop overstep rate, concurrency support, and token cost — that per-agent accuracy scores never surface.

Use when:
- Every agent in your system scores well and the org's delivery still has not moved.
- Choosing metrics for a platform that coordinates several role-specific agents and the humans around them.
- Deciding what to measure about a human approval gate beyond whether it exists.

Details:
- **The stated philosophy.** "The philosophy we are using… we don't grade the agents. We try to grade alignment itself." ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 10:23-10:35)
- **The frame is a 2×2**: qualitative versus quantitative, crossed with per-component versus system-level. (The talk garbles the axis labels — it names "qualitative" twice — but the examples that follow make the intended crossing clear.) ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 10:35-10:49)
- **Per-component measures are the familiar ones.** Known values against golden answers ("if that agent [is] giving you the correct output for this voltage, like known values versus golden answers"); an LLM judge comparing against a domain expert's answer; and memory recall ("You can measure how good my memory, like if the recall [is] state of art"). ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 10:49-11:11)
- **The system-level axes are the contribution.** Five, in the order given: (1) *task completion* — "if someone uses this whole thing, is he really completing the task he wants to do"; (2) *user frustration* — "Is he frustrated while using this?"; (3) *gate integrity* — "Are our agents overstepping human in the loop approval or not? Sometimes the agent goes out on that end"; (4) *concurrency* — "does our system allow you to work concurrently on multiple tasks in parallel? This is a success metric"; (5) *token tax* — "we don't want to overload you once you use this with all the lovely tokens and increase your budget." ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 11:11-11:59)
- **Three of those five are not standard eval targets and are worth adopting separately.** *Overstep rate* turns an approval gate from a design feature into a measured one — it asks how often the gate was bypassed rather than whether it was installed, and is the empirical complement to the human-side failure where a gate is honoured but rubber-stamped. *Concurrency* is a property of the coordination substrate, not of any agent: it asks whether the system lets one person hold several pieces of work open at once. *Token tax* names cost as a quality axis borne by the user rather than as a budget line, which is the framing that makes it a metric you can regress on.
- **Frustration and overstep imply instrumentation the talk does not describe.** Neither is derivable from an output trace alone: frustration needs a user signal and overstep needs the system to know what the gate covered and to detect action outside it. No collection method, and no number on any of the five axes, is reported — including for overstep, despite an overstepping agent being one of the three failures the same talk reports. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 11:11-11:59, 12:49-13:14)
- This is the *unit-of-evaluation* axis, orthogonal to the wiki's existing axes for source of eval signal and for scope within an execution tree. A trajectory eval still grades one agent's run; this grades whether the humans and agents around it stayed pointed at the same thing.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Choose Eval Scope Across Span, Multispan, Trajectory, and Session](choose-eval-scope-across-span-multispan-trajectory-and-session.md)
- [Catalog Eval Signal Sources Across Judge, Human, Golden, Deterministic, and Business](catalog-eval-signal-sources-judge-human-golden-deterministic-business.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md)
- [Alignment Is the Quadratic Term That Per-Person Tooling Does Not Touch](alignment-is-the-quadratic-term-that-per-person-tooling-does-not-touch.md)
- [Institutional Memory Has No Benchmark the Way Graph Memory Does](institutional-memory-has-no-benchmark-the-way-graph-memory-does.md)
- [Evaluate workspace isolation with positive and negative filesystem scorers](evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md)
- [Truth Drift Updates One Copy and Leaves the Rest Stale](truth-drift-updates-one-copy-and-leaves-the-rest-stale.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Scope Role Agents With a Spec Hierarchy and File Isolation](scope-role-agents-with-a-spec-hierarchy-and-file-isolation.md)

Sources:
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 10:23-11:59
