# Verification-First Prompts Make Parallel Agent Work Reviewable

Summary: Parallel agent work needs prompts that define observable success before dispatch. A task brief should tell the agent how it will know it is correct, provide relevant context, and name a broad approach so completed outputs can be compared and merged without endless manual inspection.

Use when:
- Prompting asynchronous coding agents to work without continuous supervision.
- Preparing tasks that will run in parallel and later need fast review.
- Converting vague backlog work into agent-executable requests.

Details:
- Banks says the secret to working in parallel is a clear definition of success, because developers cannot spend the day reviewing every PR manually. 11:13-11:24
- The prompt should create an agreement with the agent: do not stop until a concrete observable condition works or appears. 11:24-11:36
- His Jules prompt pattern includes a brief task overview, the condition that tells the agent it got the task right, helpful context, and a simple broad approach that can be changed across cloned runs. 11:45-12:04
- For simple web automation, he suggests giving the expected observed value, then asking the agent to keep going until it sees that value, such as logging a known number from a page. 12:04-12:18
- Verification-first prompting pairs with merge-and-test infrastructure; the end of a parallel workflow needs robust checks to combine outputs rather than only human confidence. 11:36-11:43

- **The same prompt discipline argued from throughput rather than reviewability.** Liguori arrives at verification-first from the parallelism side: a human who has not told the agent how to check itself must stay in the loop, and "it's very difficult to clone yourself into multiple agents." So feeding means supplying "what it needs to do **and how it can self-validate**," with the agent returning only at a stated bar — runs, compiles, passes tests, testable, high coverage. The step this adds to the pattern is promotion: once you know the criteria for a class of task, "put all of this content into your steering file so it does it every time without you having to prompt it," so the verification-first framing stops being a per-prompt discipline and becomes a property of the workspace. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 11:44-12:31)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Backlog-Scale Coding Agents Need Confidence and Self-Testing](backlog-scale-coding-agents-need-confidence-and-self-testing.md)
- [Use Multisensory Feedback Loops for Coding-Agent Validation](use-multisensory-feedback-loops-for-coding-agent-validation.md)
- [Return Typed Workspace Outputs From Coding Agents](return-typed-workspace-outputs-from-coding-agents.md)
- [Being in the Loop Is the Ceiling on Agent Parallelism](being-in-the-loop-is-the-ceiling-on-agent-parallelism.md)

Sources:
- [Your Coding Agent Just Got Cloned And Your Brain Isn't Ready - Rustin Banks, Google Jules](../sources/20250725_X4BwOu0GWb8.md), 11:13-12:18
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 11:44-12:31
