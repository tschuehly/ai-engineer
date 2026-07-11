# Pre-Bind Tool Arguments to Give Agents Safe Autonomy

Summary: Lock a tool's sensitive arguments before exposing it to the model — via partial function application — so the model neither sees nor can change them; this constrains the tool's blast radius (e.g. confines file access to one directory) and gives the agent unattended autonomy without a human-in-the-loop approval on every call.

Use when:
- An agent needs to run autonomously but a raw tool (file read/write, shell, API) is too powerful to expose directly.
- Human-in-the-loop approval is keeping the agent safe but making it too slow.
- Scoping a tool's authority declaratively instead of trusting the model to stay in bounds.

Details:
- The problem: interrupt/handler approval makes tools safe but slow — "the tricky part" is giving the agent "just enough capability so that you don't have to manually approve every single action, without giving it so much capability that it's able to do something destructive." ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 15:17-15:44)
- The technique — partial function application (PFA), borrowed from functional programming: take the `read` tool (which takes a `file_name` and a `directory`), call `partial` on it, and lock the `directory` argument to `demo`. ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 15:44-16:29)
- Why it constrains the model: after pre-binding, "the LLM isn't going to be able to change that argument — it's not even going to know that argument exists"; the tool now presents only a `file_name` parameter, so the agent can only read/write within the locked directory. "No human input is needed, but it's still safe." ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 16:29-17:08)
- Placement on the harness ladder: this is the autonomy rung between safety-via-approval and the reasoning loop — capability constraint replaces per-action human approval. ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 20:48-21:23)
- Complementary safety primitive in the same framework: standard-library tools that mutate, do something destructive, or read sensitive data raise an *interrupt* first, and interrupts can pause and later resume execution (even inside a loop, tool call, or sub-agent), so pre-binding scopes authority while interrupts gate the rest. ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 14:04-14:29, 29:52-31:10)

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Capability-based sandboxes start with no authority](capability-based-sandboxes-start-with-no-authority.md)
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md)
- [Build agent harnesses incrementally up a capability ladder](build-agent-harnesses-incrementally-up-a-capability-ladder.md)
- [Hackable agent runtimes need tight safety boundaries](hackable-agent-runtimes-need-tight-safety-boundaries.md)

Sources:
- [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](../sources/20260707_2e9ANoOEn28.md), 14:04-17:08, 29:52-31:10
