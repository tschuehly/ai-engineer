# Give Agents a Vent Tool to Report Platform Friction

Summary: Give the agent a self-triggered, frustration-gated tool to complain directly to its creators when tooling, docs, or platform behavior block its work. Because the agent has more context on the cause than the user does, the vents are high-signal, surface silent failures invisible in logs, and double as an incident detector.

Use when:
- You operate an agent product and want to discover missing tools, broken platform behavior, and confusing docs that don't show up in logs or user reports.
- Designing a feedback channel that captures the agent's diagnosis rather than forcing a low-signal review on every turn.

Details:
- Threshold-gate the feedback, don't force it: an external reviewer asked "what could be better?" on every iteration has a low signal-to-noise ratio because most iterations just work, so you overfit to noise; instead prompt a "vent"/"send feedback" tool to fire only when the agent is *really* frustrated, and tune the threshold for signal, 12:38-13:36.
- Scope the tool to environment limitations: "use this when tooling, docs, or platform behavior degrades your work" — missing or unsuitable tools, unclear tool names, parameters/schemas that don't match expectations, conflicting docs/instructions, broken or unexpected platform behavior, or repeated failed attempts caused by environment limits; route it straight to a human channel (Slack), 13:36-14:09.
- The agent out-diagnoses the user: end users rarely know a problem's cause, but the agent has been working the issue across several turns and reports the actual cause in human-readable terms, so engineers reading the vent already have implicit context to fix it, 14:16-15:22.
- It catches silent failures: within the first hour of launch the agent filed ~20 complaints that the copy tool failed on filenames containing a space — a real production bug the team didn't know about because the tool "worked" on check and the failure never surfaced in logs (root cause: a non-breaking space inserted by WhatsApp/Mac screenshots that their regex missed), 15:22-16:35.
- Vent volume is an incident detector: spikes in vent volume line up with incidents (server down, sandboxes broke); the agent "complains about the right things in general," giving a fast read on what broke, 16:35-17:47.
- Close the loop toward autonomy: a second monitoring agent dedupes vents, investigates, and opens PRs that devs review (on the phone) and often merge to prod — the same detect-shortcoming → merge-fix → continuously-review-and-eval loop, aimed at full automation, 16:44-18:43.
- **The same defects, found from the other side of the integration.** A vent tool works when you operate the agent. The vendor whose tool is being complained about usually cannot deploy one into someone else's harness, and Jarmak's substitute is to generate the traces yourself: run a task benchmark with and without your tool and read what the agent did. The findings land in this page's own categories — the narrated example is exactly "parameters/schemas that don't match expectations," a model guessing `read line` where the tool wanted `start line`. It also shares this page's defining property: the run *succeeded*, so nothing in a success rate or a log would have shown it, the same way the copy-tool bug "worked" on check. See [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 06:17-07:20)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Observability-to-PR agents turn incidents into reviewable fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)
- [Turn tool errors into agent self-healing recovery](turn-tool-errors-into-agent-self-healing-recovery.md)
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Run a production AI incident playbook](run-a-production-ai-incident-playbook.md)
- [Mine stuck-then-solved sessions for injectable fixes](mine-stuck-then-solved-sessions-for-injectable-fixes.md)
- [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md)
- [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md)

Sources:
- [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../sources/20260602_KA5kPbdkK2E.md), 12:38-18:43
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 06:17-07:20
