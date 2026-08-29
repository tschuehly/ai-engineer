# Reorder the generated task list to ship an MVP first

Summary: After a spec-driven agent generates an implementation task list, ask it to pull the top few tasks to the front as a self-contained MVP and build that first, so you get a running, viewable artifact early instead of implementing the full spec before seeing anything work.

Use when:
- A coding agent has produced a long task list from a spec and you want early validation of direction.
- Turning a big planned feature into an incremental delivery that surfaces a working slice quickly.

Details:
- Concrete tip: once the task list is created, tell the agent "please take the top four tasks, put them at the top, and create an MVP for me first," then implement the MVP version first so you can actually see it working. (12:35-12:52)
- The agent will rewrite the task list and reframe requirements to make the leading tasks a coherent MVP; in the demo Kiro reordered so tasks 1-4 delivered a working browsable movie grid with search, genre filtering, sorting, and theme, then the rest were implemented after. (16:29-17:00)
- This is an incremental-delivery lever on top of the spec flow: the spec still defines the whole feature, but reordering front-loads a demonstrable slice, giving an early checkpoint before the human commits review effort to the full implementation.
- **How to tell whether the thing you shipped is actually minimal-viable rather than merely minimal.** Izmit reads it off the beta request stream as a distribution: "you will start getting tons of requests. Can you connect this data? Can you connect that data. And then you are looking at where are the concentrations happening? Because that means that if you don't get those things in, you don't truly have an MVP." Concentration marks the missing capability; the long tail is deferred. The confirming signal is behavioral rather than stated — weekly-active users returning above 70%. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 06:12-06:58)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Spec-driven development is a tool-portable pattern, not a single product](spec-driven-development-is-a-tool-portable-pattern.md)
- [Spec-driven development turns prompts into requirements, design, and tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)
- [Start Coding Agents With Small Verifiable Chores](start-coding-agents-with-small-verifiable-chores.md)
- [Gate Each Rollout Phase on a Different Question](gate-each-rollout-phase-on-a-different-question.md)

Sources:
- [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](../sources/20260628_IddXPepIAS4.md), 12:35-12:52, 16:29-17:00
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 06:12-06:58
