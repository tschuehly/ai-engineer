# Target Enterprise Coding Agents at Maintenance and Incident Work

Summary: In mature engineering organizations, agent ROI may be stronger when agents attack maintenance, migration, patching, and incident-response work than when they only generate new code from requirements.

Use when:
- Choosing first scaled enterprise coding-agent use cases.
- Comparing greenfield code generation against maintenance, migration, and operational troubleshooting agents.

Details:
- Bloomberg reframed AI for coding from narrow code generation toward broader software engineering work, including maintenance and migration tasks developers often prefer not to do. (06:18-06:45)
- Uplift agents scan the codebase for places a patch applies, create pull requests with the fix, and explain why the patch was made, improving on earlier regex-based refactoring tools. (06:48-07:38)
- Uplift work still needs deterministic verification; without tests, linters, or other checks, generated patches can be difficult to trust and apply. (07:40-08:05)
- Incident-response agents can inspect code, telemetry, feature flags, traces, metrics, logs, topologies, alarms, triggers, and SLOs quickly, while reducing human anchoring on a first hypothesis. (08:37-10:37)
- **A second source generalizes the ROI argument past incidents to routine operations, with a specific denominator.** Resolve AI's premise is that "70% of the time from an engineer is actually not focused just on writing code. It's actually spent on actually running the code that is actually shipped into production," covering maintenance, scaling, on-call, hot fixes, runbook updates, escalations, and other teams' questions — so "really coding was never the the big bottleneck." The argument extends this page's from-maintenance-not-greenfield reasoning to work that is not a defect at all. Note the figure is attributed only as "this was a survey study done," with no publisher, sample, or year. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 01:47-02:25)
- **And it names the compounding effect that makes the targeting choice more urgent over time.** More code shipping faster, including "from even non-developers that maybe don't actually know the code," means "AI is creating a lot more issues in production… it's not clear we have the right sort of structures in place to deal with the amount of kind of changes that are coming through." On this reading, coding-agent adoption enlarges the operational half it was meant to offset. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 01:15-01:35, 02:37-02:49)
- **A per-task test that explains why this category is the one that pays.** Gazit's filter is not "maintenance" but "judgment, not rules": until now "the only automations that we had were heuristics like make sure there's a semicolon at the end of every line," and what is newly automatable is anything needing "some amount of basic judgment and intelligence." Maintenance work is where the returns sit because it is dense in exactly those decisions — cheap for a human, impossible for a rule. His example is Home Assistant's first agentic workflow, which "looks at every submitted issue, walks the Python stack trace to figure out if the bug is in first-party code or third-party code, closes the issue if it's not their issue. That's something that was not possible before AI, not possible with heuristics, but is possible now." See [automate the chores that needed judgment, not the ones that needed rules](automate-the-chores-that-needed-judgment-not-rules.md) for the test itself and its missing verification half. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 02:53-03:41, 12:36-13:00)

- **Maintenance as a subscription with a scheduler, and incidents as the source of new skills.** Uber operationalizes this page's targeting advice into a mechanism: services "enroll" into shared maintenance skills such as feature-flag cleanup, and the recurring runs are configured on "a managed loop that you go to" because "we don't want thousands of loops being set up across the company without any bounds" ([Huda](../sources/20260821_17-YSUHo6Lk.md), 15:54-16:34). The incident half of this page's claim is closed the other way round from the usual: rather than agents responding to incidents, "at a kind of monthly cadence, we're looking to see what skills can we now learn from in our incident reviews and turn those into new maintenance skills that we can apply to all of our services" — an incident review normally produces one team's action item, and this converts it into a fleet-wide recurring check (16:58-17:10). See [Run Maintenance Skills From One Managed Loop Surface](run-maintenance-skills-from-one-managed-loop-surface.md).

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Decompose large refactors into dependency-aware agent batches](decompose-large-refactors-into-dependency-aware-agent-batches.md)
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md)
- [Watch the Change Paths That Bypass Your Deployment Pipeline](watch-the-change-paths-that-bypass-your-deployment-pipeline.md)
- [Automate the Chores That Needed Judgment, Not the Ones That Needed Rules](automate-the-chores-that-needed-judgment-not-rules.md)
- [Run Maintenance Skills From One Managed Loop Surface](run-maintenance-skills-from-one-managed-loop-surface.md)

Sources:
- [What We Learned Deploying AI within Bloomberg's Engineering Organization - Lei Zhang, Bloomberg](../sources/20251216_Q81AzlA-VE8.md), 06:18-10:37
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 01:15-02:49
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 02:53-03:41, 12:36-13:00
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 15:54-17:10
