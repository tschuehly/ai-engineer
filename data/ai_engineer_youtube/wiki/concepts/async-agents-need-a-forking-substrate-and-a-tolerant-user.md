# Async Agents Need a Forking Substrate and a User Who Tolerates Out-of-Order Completion

Summary: Background agents work for code because of two accidents that do not travel: git plus sandboxes give the work a fork-and-merge substrate, and engineers already accept that job seven finishes before job three. Port an async agent to a domain missing either property and it fails on the substrate or on the human, not on the model.

Use when:
- Planning to move an agent from synchronous chat to background execution in a non-engineering domain.
- A background agent works in demos but its output is never picked up, and you are trying to decide whether the problem is quality or reception.
- Estimating how much of a parallel-coding-agent pattern transfers to operations, finance, design, or field work.
- Sizing what a "co-worker" product actually requires before its most-cited rung exists.

Details:
- The two properties, separated. Shenoy's autonomy ladder runs copilot → synchronous agent → asynchronous agent → long-running agent → AI coworker, and he calls the async rung for code "largely solved": "you take the exact same coding agent, you wrap it in a sandbox, and you just let it go run. It can build, it can test, and once it's done with its work, it can provide the code in the form of a PR." ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 05:23-08:16)
- **Substrate**: "we've figured out what the async and forking mechanism for code is. You just spin up a bunch of sandboxes and do work. What does that look like for the rest of the world?" A repository can be cheaply copied, diverged, tested in isolation, and merged back with review. Scoping a building from a blueprint, closing books with missing receipts, and coordinating vendors for a roof repair have no equivalent primitive — there is no branch of a roof. (09:08-09:24)
- **Reception**: "One thing that's really unique about engineers is folks are incredibly good at already parallelizing their work. It's very commonplace to launch 10 jobs and be comfortable with the fact that job seven might finish before job three." The counterexample is deliberately mundane: "people clean out their inbox one email by one email, not 10 emails at once." Out-of-order completion is a learned professional tolerance, not a universal one. (08:16-08:35, 09:44-09:54)
- The consequence is that the async form factor is not one design to be ported. "This varies dramatically from industry to industry. Just because you have one way of launching an async agent for code, doesn't mean that same way is going to work for architecture or property management." Moving up the ladder is framed as two problems solved together — product and user enablement — rather than a product problem alone. (09:54-10:13)
- The synchronous rung, by contrast, does transfer: the services equivalent already exists as "a co-working agent… an agent that has deep context about your enterprise. It interacts potentially with MCPs, custom tools, custom integrations, and you can chat with it synchronously." So the discontinuity is specifically at async, which is where the throughput gain is. (08:35-08:53)
- A sidestep worth naming even though the source offers no mechanism for it: rather than wait for models to become competent at services knowledge work, "what if we just use that code knowledge and represent knowledge work as code?" — on the argument that "the models are trained on code, they want to write code, they're incredibly good at writing code." If it worked it would supply the missing substrate for free, since a codified task inherits diffs, branches, tests, and review. Posed as a question with no example and no result. (09:24-09:44)
- What this predicts about every parallel-agent pattern in this wiki. Worktree isolation, VM-backed queues, swim lanes, agent managers, and parent agents that merge subagent output all assume both properties silently. Read as a portability checklist, the substrate question is "what plays the role of the branch and the PR here?" and the reception question is "who is downstream of this, and do they already work out of order?" A negative answer to either predicts failure that no model upgrade fixes.
- Limits. The async-services rung is explicitly unsolved by the speaker's own account — he presents it as the frontier he works on, not as something built — and none of this is measured. The reception claim rests on two contrasting observations (ten jobs, one inbox) rather than on any study of how professionals accept parallel work. ([Provenance and Limits](../sources/20260828_B0fjR3yaZFU.md))

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Cloud Agents Turn Coding Work Into Asynchronous VM-Backed Queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)
- [Manage an Agent Manager Instead of Polling Parallel Agents](manage-an-agent-manager-instead-of-polling-parallel-agents.md)
- [Treat long-horizon agents as asynchronous workers with evolving interfaces](treat-long-horizon-agents-as-asynchronous-workers-with-evolving-interfaces.md)
- [Choose AI coworker form factors by interaction mode](choose-ai-coworker-form-factors-by-interaction-mode.md)
- [Parallel Coding Agents Support Multitasking and Variation Search](parallel-coding-agents-support-multitasking-and-variation-search.md)
- [Continual Learning and Enablement Are One Loop With a Cold Start](continual-learning-and-enablement-are-one-loop-with-a-cold-start.md)

Sources:
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 05:23-10:13
