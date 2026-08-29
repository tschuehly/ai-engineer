# Run Maintenance Skills From One Managed Loop Surface

Summary: Recurring agent work at Uber is set up through a single managed surface rather than by teams creating their own schedules, on the explicit reasoning that "we don't want thousands of loops being set up across the company without any bounds." Central scheduling then buys two things a team cron job cannot: runs are placed when shared CI capacity is available, and the volume of diffs arriving in front of engineers is controlled. Whether each diff lands becomes label data for improving the skill that produced it.

Use when:
- Teams are independently scheduling recurring agent jobs and nobody can say how many exist.
- Background agent work is arriving faster than reviewers can absorb it.
- Recurring maintenance agents compete with human-triggered builds for the same CI pool.
- Looking for a training signal from agent work that already happens.

Details:
- **Enrollment, not authoring.** "We can actually enroll our feature or service into maintenance skills" — the unit is a service subscribing to a shared skill, so one improvement to feature-flag cleanup reaches everything enrolled. The worked example is the A/B modal from earlier in the talk: "now that the B variant is no longer needed, we can have that scheduled on a loop." ([Huda](../sources/20260821_17-YSUHo6Lk.md), 15:54-16:22)
- **The governance rule, stated plainly.** "This is actually a managed loop that you go to. We don't want thousands of loops being set up across the company without any bounds. You have a managed surface that you go to to set up the loop." The failure being avoided is not that any one loop is dangerous; it is that an unbounded population of them has no owner, no inventory, and no aggregate cost. (16:22-16:34)
- **Scheduling is a capacity decision and a human-attention decision at once.** "So it runs on Sunday when we know we have better CI capacity available. We also don't want to overwhelm engineers that Monday morning with a bunch of extra diffs. We want to control how many diffs they're seeing on Monday as well." Two different scarce resources — build queue and reviewer attention — are both managed by the same scheduling lever, and neither is visible from inside a single team's cron entry. See [Treat CI and Experiment Capacity as the Scarce Resource Agent Throughput Consumes](treat-ci-and-experiment-capacity-as-the-scarce-resource-agent-throughput-consumes.md). (16:34-16:46)
- **Land-rate as free labels.** "When that skill runs and makes those diffs, those diffs will get comments and either get landed or not landed. That's all good label data that we can use to improve the skill itself." A merge decision is a judgment a human was already going to make, recorded per skill rather than per PR — which is what turns it into a signal about the skill instead of noise about one change. (16:46-16:58)
- **New skills are harvested from incidents on a fixed cadence.** "At a kind of monthly cadence, we're looking to see what skills can we now learn from in our incident reviews and turn those into new maintenance skills that we can apply to all of our services." The direction is worth noting: an incident review normally produces an action item for one team, and this converts it into a fleet-wide recurring check. (16:58-17:10)
- **The two loops compose into a system.** Incidents supply new skills, enrollment fans them across services, scheduling meters their output, and land-rate feeds back to the skill. That is a closed improvement loop whose every input is a byproduct of work already happening — no separate annotation effort appears anywhere in it.
- **Caveat.** No numbers on any of it: how many services are enrolled, how many maintenance skills exist, what the land rate is, or whether any skill has measurably improved from the label data. The monthly incident-mining cadence is described as an intention ("we're looking to see"), not a running process.

Related topics:
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Target Enterprise Coding Agents at Maintenance and Incident Work](target-enterprise-coding-agents-at-maintenance-and-incident-work.md)
- [Stage Proactive Coding Agents From Maintenance to System Awareness](stage-proactive-coding-agents-from-maintenance-to-system-awareness.md)
- [Run a Skills Marketplace With Lint Gates, Persona Auto-Install, and Trace Feedback](run-a-skills-marketplace-with-lint-gates-persona-auto-install-and-trace-feedback.md)
- [Treat CI and Experiment Capacity as the Scarce Resource Agent Throughput Consumes](treat-ci-and-experiment-capacity-as-the-scarce-resource-agent-throughput-consumes.md)
- [Observability to PR Agents Turn Incidents Into Reviewable Fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)
- [Automation Loops Convert Repeated Review and Triage Into Factory Improvements](automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md)
- [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Feedback Turns Coding Agent Loops Into Prompt and Skill Improvement Cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 15:54-17:10
