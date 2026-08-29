# Being in the Loop Is the Ceiling on Agent Parallelism

Summary: Conversational back-and-forth with a coding agent caps the achievable multiplier no matter how good the model is, because a human waiting 30 seconds for each turn is serialized and cannot occupy more than one loop. The exit is not a better prompt but a different payload: send the task *and* the criteria the agent can check itself against, so it returns only at a quality bar.

Use when:
- Explaining why a team with excellent tooling is stuck near 1x while another with the same tools is not.
- Deciding what to add to a prompt before deciding whether to run more agents in parallel.
- Diagnosing a workflow where parallel agents were tried and abandoned as too hard to manage.

Details:
- **The arithmetic.** "If you are vibe coding, if you are having a back-and-forth conversation with your agent all day long, of course you're not going to see four to five x productivity improvements because you are in the loop the entire time. You're probably sitting there for 30 seconds to a minute waiting for it to generate code and come back to you with the code to review." ([Liguori](../sources/20260828_pqlWNihgdjI.md), 11:21-11:44)
- **Why the cap is structural rather than a matter of discipline.** "If you're sitting there waiting for it, then you can't go off and do other stuff. It's really difficult to run agents in parallel. It's very difficult to clone yourself into multiple agents." One human's attention is the scarce serialized resource; a workflow that consumes it continuously has a ceiling of one, and every further improvement in model speed just shortens the wait rather than releasing the human. (11:44-11:58)
- **The substitution.** Babysitting sends *what to do*; feeding sends "what it needs to do **and how it can self-validate**." The return condition is the point: the agent should "only come back to you when it meets a certain quality bar, when it actually runs and compiles and passes tests, when it's testable, when it actually has high coverage." (11:58-12:24)
- **Make the criteria recur.** Having discovered what the validation criteria are for a class of task, promote them out of the prompt: "the next level is put all of this content into your steering file so it does it every time without you having to prompt it." Otherwise the human is re-typing the acceptance conditions every run, which is a smaller version of the same serialization. (12:24-12:31)
- **The two habits this depends on, and the order they come in.** Self-validation only buys unattended time if the checks are fast and local — Liguori's fifth habit exists to supply that ("mock services that run entirely locally with deterministic responses because it lets the agent do everything locally"), and its stated purpose is exactly this page's: fast feedback "is what lets it go off for hours at a time and self-correct." (13:53-15:19) Attempting the feeding habit on a codebase whose test loop requires cloud services will fail for reasons that look like model failure.
- **Distinguish this from the trust argument.** A [deterministic completion gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md) exists because an agent's "task completed" is not credible; it is enforcement, sitting outside the agent. This page is about throughput, and the criteria sit *inside* the prompt so the agent can iterate against them before it ever returns. The two compose — self-validation criteria in the steering file, an external gate on the result — and neither substitutes for the other.
- **The cost this moves rather than removes.** Freeing yourself from the inner loop hands you several outer loops at once, and Liguori reports the bill: "the cognitive load increases as you run these multiple agents in parallel. You're constantly shifting between terminal tabs," alongside engineers "staying up late late at night trying to get that perfect prompt that's going to make their agent run for hours overnight." Escaping serialization is what makes attention, not waiting, the binding constraint. (16:08-16:17, 15:43-16:08)
- Provenance: an internal-practice talk from AWS with the frontier-developer target state defined behaviourally — "run for up to hours at a time without their intervention," "multiple agents in parallel churning through a backlog of tasks" (02:00-02:20) — but with no measurement of intervention rate, parallel-agent count, or the marginal gain of the feeding habit specifically. The 4.5x median is reported for teams that changed several habits at once.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Read a Broken Agent Setup From Babysitting, Context Burn, and Slop](read-a-broken-agent-setup-from-babysitting-context-burn-and-slop.md)
- [Treat Human Attention as the Bottleneck for Agentic Work](treat-human-attention-as-the-agentic-bottleneck.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [Manage an Agent Manager Instead of Polling Parallel Agents](manage-an-agent-manager-instead-of-polling-parallel-agents.md)
- [Make Validation Fast, Local, Deterministic, and Actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Budget the Productivity Dip That Precedes the Agent Speedup](budget-the-productivity-dip-that-precedes-the-agent-speedup.md)

Sources:
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 02:00-02:20, 11:09-12:31, 13:53-15:19, 15:43-16:17
