# Use Reviewer Agents and Lints to Turn Review Lessons Into Guardrails

Summary: Repeated review findings should become harness guardrails that run automatically. Reviewer agents, CI checks, and bespoke lints can turn reliability and security lessons into recurring constraints instead of relying on humans to remember every non-functional requirement.

Use when:
- A team repeatedly catches the same reliability, security, or interface-quality issue in agent-written code.
- Designing CI and review automation for coding-agent workflows.

Details:
- Lopopolo describes security and reliability reviewer agents that run on pushes and CI, read documentation plus the proposed patch, and ask whether code satisfies local expectations. (12:00-12:20)
- Concrete review prompts include checking whether network code has retries and timeouts and whether new interfaces are secure and hard to misuse. (12:20-12:30)
- A recurring outage lesson can become a bespoke lint, such as checking every `fetch` call for retry and timeout handling, making the lesson durable across future agent output. (12:32-13:21)
- The talk argues that accepting short-term velocity hits to understand where agents struggle and add guardrails lets humans step back to higher-leverage work later. (09:36-10:07)
- Ankit Jain (Aviator) runs the same conversion retrospectively and in bulk rather than incident by incident: "mine your last 1,000 review comments and build out a[n] AI slo[p] register for the things which are repeatable," because "a vast majority of the comments that you're providing in your code review are something that we repeat over and over again." The corpus of past reviews already contains the rules, so mining precedes waiting for the next incident, and the two approaches compose. He also states the cost Lopopolo's velocity-hit framing implies: adoption "does follow a J curve. So, pain is real." (YgEv7IQzGdM 06:53-07:57, 14:12-15:08)
- **The same ratchet with a cost argument attached, and a different trigger.** "It's even better if when you find something that the agent has found to be useful, take the time to take that and encode into a deterministic flow. A deterministic flow that can be easily repeated is save[d] on tokens, save on time… and then you also know that you're using the LLM when it needs to reason, but when you have something that is already known and basically can be encoded into a test, spending that time always pays dividends." This page's trigger is a repeated review finding; Blum's is a discovery the agent itself made that would otherwise be re-derived at token cost on every run. The economic framing is the addition — freezing a discovery is not only a reliability move, it moves work out of the priced, non-deterministic layer. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 05:38-06:11)

- **A rung between the deterministic lint and the full reviewer agent, which Uber calls an AI linter**: a few-shot system where "developers can basically kind of deterministically get more context and then run rules with that context and like a file and find some systematic and mechanical issues." The context gathering is deterministic and only the rule application is a model, which catches classes a regex cannot express without paying an agent to explore the repository. Above it sits the custom team agent "link[ed] to like a knowledge base… link[ed] to their past PRs, [with] a skill to do the review," and below it a general per-file logic-bug pass. A guardrail library is therefore a ladder rather than one format: pick the cheapest rung whose context requirements the rule actually has. No accuracy or cost figure is given for any rung. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 07:37-08:41)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)
- [Agent rules should emerge from observed off-rail behavior](agent-rules-should-emerge-from-observed-off-rail-behavior.md)
- [Use agent hooks to automate session rituals](use-agent-hooks-to-automate-session-rituals.md)
- [Mine Recurring Review Comments Into an Invariant Registry](mine-recurring-review-comments-into-an-invariant-registry.md)
- [Write the Test First So the Agent Cannot Fit It to the Code](write-the-test-first-so-the-agent-cannot-fit-it-to-the-code.md)
- [Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem](distributed-rule-authoring-is-a-platform-problem.md)

Sources:
- [Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI](../sources/20260417_am_oeAoUhew.md), 09:36-13:21
- [How to Kill the Code Review — Ankit Jain, Aviator](../sources/20260817_YgEv7IQzGdM.md), 06:53-07:57, 14:12-15:08
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 05:38-06:11
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 07:37-08:41
