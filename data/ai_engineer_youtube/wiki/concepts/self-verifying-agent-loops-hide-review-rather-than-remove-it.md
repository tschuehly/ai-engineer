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
- Adoption caveat: the engineers evangelizing loops work at large labs where tokens are effectively free, so treat their advice as a lighthouse of where things are heading ("skate where the puck is going") rather than a mandate to run loops in your own token-constrained environment today.

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

Sources:
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../sources/20260710_ZpK5PWX2YRM.md), 18:36-20:13
