# Mine Stuck-Then-Solved Sessions for Injectable Fixes

Summary: Instrument production sessions for "stuck → solved" transitions, capture the fix that worked, cluster similar cases into a generalized knowledge entry, eval-verify it, then inject it just-in-time into future runs — while A/B-testing each entry's real value and pruning it aggressively as models and features change.

Use when:
- Building a self-improving context layer for an AI product with many users hitting recurring friction.
- Turning high-friction sessions that eventually succeeded into reusable upstream fixes instead of letting the next user re-discover the same problem.

Details:
- Detect the signal, don't guess it: an LLM judge flags "stuck" from a user asking for the same thing more than once, complaining about an implementation, failing explicitly, or abandoning a session; the high-value sample is the transition where a stuck session becomes unstuck *and not because the user gave up*, because that yields both a real problem and the solution that resolved it, 05:22-08:50.
- Generalize, don't overfit: cluster similar issues and extract the reusable information rather than keying an entry to one exact prompt — the failure mode is "a million Stack Overflow pages" that each only match a specific prompt, 08:50-09:17.
- Verify before trusting: an external reviewer — usually an agent, a human only when uncertain — generates and runs a quick eval to confirm the proposed fix resolves the example set, producing a continually-updated bank of problem/solution entries, 09:17-09:46.
- Inject just-in-time with a cheap model: a lightweight model watches the working agent and injects the matching entry only when it detects a known issue with a known answer, so frontier intelligence isn't spent re-reading large context, 09:46-09:57, 17:50-18:04.
- Measure value with blank-injection holdouts: for a small sample where it *would* inject, inject a blank instead; comparing project success where the entry was injected vs. where it could have been but wasn't gives a high-signal A/B that ranks each entry up (show more) or down (show less), 09:57-10:27.
- Prune aggressively: the knowledge set goes stale "incredibly quickly" — every new model release or feature change — so rebalance and discard entries to stay at the frontier of what's solvable, because deprecated entries cause context rot and hamper the agent, 10:27-11:02.
- The payoff metric is completion, not engagement: stuck/"fixing it" messages drop and project deploy/finish rates rise, signalling users never got stuck badly enough to abandon; the same problem bank also doubles as an internal model-ranking eval set, 11:05-12:00.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Demand-driven context pulls knowledge from failed work](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Inject tool context just-in-time during agent sequencing](inject-tool-context-just-in-time-during-agent-sequencing.md)
- [Apply online scoring to production traces with cost-aware sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)
- [Mine agent conversation history to generate missing skills](mine-agent-conversation-history-to-generate-missing-skills.md)
- [Give agents a vent tool to report platform friction](give-agents-a-vent-tool-to-report-platform-friction.md)

Sources:
- [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../sources/20260602_KA5kPbdkK2E.md), 05:22-12:00
