# Make Delegation Multiplayer So People See Larger Asks

Summary: Ambition in agent usage spreads by observation, so the delegation surface should be somewhere colleagues can read each other's prompts. A private CLI hides the best asks in the org; a shared channel where you tag the agent turns every good delegation into a demonstration, which is the transmission mechanism for raising what people ask for.

Use when:
- Choosing between a per-developer CLI and a shared-channel agent surface for team-wide delegation.
- Trying to raise agent usage sophistication across an org rather than in a few power users.
- Explaining why usage plateaus at "glorified assistant" even when the model can do much more.

Details:
- The property named as the reason the shared surface matters: "the reason it's really interesting is how multiplayer it is. And it reminds me of like Midjourney, like the fact that everyone was on Discord seeing how other people were using it." ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 09:02-09:11)
- Concrete transmission, reported first-hand by Anthropic's former chief product officer. Watching a colleague hand an agent standing ownership — "don't just fix this bug, but now you are responsible for this part of the code base and I want you to monitor this feedback channel and proactively take on tasks and then fix them and then also, if this API changes, do that" — moved his own ceiling: "I've totally underutilized this thing. I've just been using it as a glorified Claude Code in Slack." ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 09:13-09:39)
- The surfaces divide by interaction bandwidth, not by capability. The CLI is for "things that are more interactive or if you're iterating on a particular specific thing where you want a high bandwidth back and forth," while "most usage is actually much more delegating via tagging." The observability benefit belongs to the second mode. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 08:44-09:02)
- The end state is a standing participant rather than a per-task invocation: "thinking of it as a teammate that actually holds context, has memory, and can be proactive," which he says made the internal default "multiplayer async proactive" instead of "most people off in their own CLIs." ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 09:44-10:00)
- Design implication worth extracting: the value here is the *readable prompt*, not the chat client. Any surface that makes delegations visible and quotable to colleagues — a shared task queue, PR-attached prompts, a public transcript archive — captures the same effect, and any surface that keeps them per-user does not.
- Limits: entirely self-reported, with no usage data and no evidence separating the multiplayer effect from the ordinary effect of Anthropic employees building on their own models. The costs of a public delegation surface — channel noise, and the visibility pressure that makes people delegate performatively — are not discussed.

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Embed Agent Tools in Existing Work Surfaces](embed-agent-tools-in-existing-work-surfaces.md)
- [Platform-Native Agents Should Behave Like Good Teammates](platform-native-agents-should-behave-like-good-teammates.md)
- [Ask Size Lags Model Capability Because Early Products Boxed the Model In](ask-size-lags-model-capability-because-early-products-boxed-the-model-in.md)
- [Stage Agentic-Engineering Adoption With a Delegation Maturity Model](stage-agentic-engineering-adoption-with-a-delegation-maturity-model.md)
- [Start the workday by reviewing and dispatching agent work](start-the-workday-by-reviewing-and-dispatching-agent-work.md)

Sources:
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 08:44-10:00
