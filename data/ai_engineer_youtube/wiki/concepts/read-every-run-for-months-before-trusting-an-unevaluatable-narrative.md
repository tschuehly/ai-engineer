# Read Every Run for Months Before Trusting an Unevaluatable Narrative

Summary: When the output is a recurring generated narrative with no ground-truth label, the acceptance procedure available to you is exhaustive manual reading of every run over a long enough window to see the failure classes — and that is a real, defensible method, provided you are honest that it is a burn-in, not an eval.

Use when:
- Shipping a recurring generated artifact (weekly summary, digest, brief) where correctness is judgeable but not scoreable.
- Deciding how long to keep a human in the loop on a low-frequency, high-visibility automation.
- Justifying a rollout to stakeholders who want an accuracy number you do not have.

Details:
- The procedure is stated plainly: "this architecture we tested for about 2-3 months and, you know, looking every single run to see what is going wrong. And this is the model that we had set up that is really working for us." ([Joyce](../sources/20260826_Qw_tC68KKes.md), 11:41-11:55)
- **The frequency of the artifact sets the cost of the method.** A weekly summary produces roughly eight to thirteen runs in two to three months — small enough to read exhaustively, and small enough that no statistical claim can be made from it. The same procedure is unavailable for a system answering tens of thousands of questions a week, which is why a high-traffic assistant reaches for log classification instead ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 12:18-13:50).
- What makes the reading tractable is per-call observability across the three agents in the pipeline: "with every run, we have observability into each of the LLM calls, so we can see what is passed and what is the response." Reading runs without a trace means judging the artifact; reading with one means localizing the defect. (11:32-11:41)
- **The burn-in is doing eval-set construction work, whether or not anyone writes the set down.** "Looking every single run to see what is going wrong" is how the failure taxonomy is discovered; the gap in this account is that no taxonomy, defect count, or regression suite is reported as the output of those months, so the knowledge stayed with the reader.
- Two to three months is also a trust-building window on the consuming side, not only a debugging one — the readers of the summary are the audience whose confidence the artifact needs, and a comparable internal deployment argues that "user trust is earned extremely hard and is lost overnight" for exactly this reason ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 03:26-03:52).
- **Limit and open risk.** Nothing is reported about the exit criterion. There is no statement of what "really working for us" meant numerically, no description of what monitoring replaced the manual read, and no mention of re-running the burn-in after a model or prompt change — which is the moment the accumulated confidence stops transferring.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Business Intelligence](../topics/business-intelligence.md)

Related concepts:
- [Split a Generated Narrative Into Drafter, Fact-Checker, and Tone Agents](split-generated-narrative-into-drafter-checker-and-tone-agents.md)
- [Run a Jury of Analysts and a Consensus Judge for No-Ground-Truth Questions](run-a-jury-of-analysts-and-a-consensus-judge-for-no-ground-truth-questions.md)
- [Classify the Assistant Question Log to Find Feature and Content Gaps](classify-the-assistant-question-log-to-find-feature-and-content-gaps.md)
- [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)
- [AI System Evaluation Still Depends on Human Review](ai-system-evaluation-still-depends-on-human-review.md)
- [Raise the Floor Before Maxing the Benchmark](raise-the-floor-before-maxing-the-benchmark.md)
- [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)
- [Close the Eval-to-Action Loop So Signal Survives the Dashboard](close-the-eval-to-action-loop-so-signal-survives-the-dashboard.md)

Sources:
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 11:32-12:03
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 03:26-03:52, 12:18-13:50
