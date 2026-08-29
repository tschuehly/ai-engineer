# Self-verifying agent loops hide review rather than remove it

Summary: Autonomous agent "loops" (scheduled agents that discover a task, plan, execute, and grade their own work) are becoming a 2026 primitive, but an agent that verifies itself has not removed human review — it has hidden it. Loops move where judgment belongs and raise the stakes on placing it correctly; they do not eliminate the need for an independent check.

Use when:
- Designing scheduled or background agent loops that pick up tickets and fix them autonomously.
- Evaluating a workflow where the same agent both produces and grades its output.
- Deciding where to keep a human or an independent verifier as agent autonomy increases.

Details:
- Loops are the emerging next primitive: Peter Steinberger (creator of Open Claude, then OpenAI) and Boris Cherny (Claude Code) both began talking about loops within ~2 days of each other. (18:36)
- Mechanically, a loop is "basically a fancy cron job that runs on a schedule": it discovers a task, writes a plan and the prompt for that task, executes, and — most importantly — verifies itself against the goal and retries if it fails, with less human intervention. (19:21)
- The core caveat: "an agent that loops grades its own work against the goal… but if the builder grades itself, you didn't remove the review, you hid it." Self-grading is the same failure as "coming up with an exam, taking it, and scoring yourself." This is why the review routing table keeps the writer separate from the verifier. (19:45)
- Concrete downside (Addy Osmani, Google): if you rely entirely on automated loops to fix your code — e.g. a bug appears in Jira and the loop picks it up and starts fixing — product quality would suffer, likely ending in "a downward spiral, digging yourself into a deeper hole." (20:07)
- The corrective framing: "loops don't remove judgment, they raise the stakes on where you put it." Rising capability shifts the review layer outward (from inspecting outputs, to inspecting task direction, to inspecting the loops themselves) without removing the requirement for proof. (20:13, 17:42-17:57)
- Ankit Jain (Aviator) gives the pattern a concrete instance and a fix. Building the verification artifact from the diff reproduces the self-grading failure — "if your code is built by the same agent which is actually building a test plan, it's not going to build a test plan which will actually catch issues" (he attributes the point to Dex Horthy's talk the previous day) — so the plan must instead be derived from the human's coding-session decisions, which contain what was wanted rather than what was done. The generalizable rule: independence of the verifier comes from independence of its *input*, not only from running it as a separate agent or model. (YgEv7IQzGdM 13:22-13:47)
- Adoption caveat: the engineers evangelizing loops work at large labs where tokens are effectively free, so treat their advice as a lighthouse of where things are heading ("skate where the puck is going") rather than a mandate to run loops in your own token-constrained environment today.
- **One structural constraint keeps a self-verifying loop honest about its exit condition.** If the agent writes the check after the code, the loop's success criterion is a description of what the loop produced — the review is not merely hidden, it is manufactured. Fixing the criterion first ("you set a goal, then you tell the agent to strive toward that goal") at least guarantees the exit condition predates the output. It does not restore the review this page says was relocated; it only prevents the loop from writing its own passing grade. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 06:12-06:42)

- **What a wrong verifier costs once no human sits between it and the fixer.** Uber wires the agent loop into the same review service as its pull requests, and reports the failure that follows: "with the inner loop, our accuracy needs actually need to go up, or else we can result in… cavitation of an agent where it fixes something, goes back, gets another code review, and has to kind of like fix backwards because the quality of the comment was low." The hidden review this page describes is not merely unaudited, it is obeyed — the agent has no mechanism for disbelieving its reviewer, so an inaccurate verifier converts directly into rework rather than into a comment somebody skips. Reported as an operating observation with no incidence rate attached. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 12:14-12:36)

Related topics:
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Separate generation and verification prompts or models](separate-generation-and-verification-prompts-or-models.md)
- [Route each change to the proof it needs](route-each-change-to-the-proof-it-needs.md)
- [Use hierarchical verification before trusting weak agent feedback](use-hierarchical-verification-before-trusting-weak-agent-feedback.md)
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)
- [Capture the Coding Session as the Intent Record](capture-the-coding-session-as-the-intent-record.md)
- [Write the Test First So the Agent Cannot Fit It to the Code](write-the-test-first-so-the-agent-cannot-fit-it-to-the-code.md)
- [Review Comments Have Two Audiences With Inverted Error Costs](review-comments-have-two-audiences-with-inverted-error-costs.md)

Sources:
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../sources/20260710_ZpK5PWX2YRM.md), 18:36-20:13
- [How to Kill the Code Review — Ankit Jain, Aviator](../sources/20260817_YgEv7IQzGdM.md), 13:22-13:47
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 06:12-06:42
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 12:14-12:36
