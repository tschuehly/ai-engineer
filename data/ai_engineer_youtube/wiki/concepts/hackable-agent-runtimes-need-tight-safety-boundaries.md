# Hackable agent runtimes need tight safety boundaries

Summary: Giving an agent direct runtime access can unlock richer workflows, but executable control over an app must be treated as a safety boundary. A local/offline experiment can tolerate risks that would be unacceptable in a shared or production user environment.

Use when:
- Considering whether an agent should call a structured editor API, execute code, inspect the DOM, or drive a browser runtime.
- Designing sandboxing and permission boundaries for agents that manipulate live user artifacts.

Details:
- tldraw's runtime API made code-based canvas control possible, and Ruiz notes that models are good at coding against such APIs (13:34-13:59).
- The team needed browser/DOM visibility and screenshots for richer canvas automation, which pushed them toward a desktop Electron wrapper rather than a normal web runtime (13:59-14:20).
- Ruiz describes opening an HTTP endpoint that treats posted content as JavaScript and runs it, then explicitly warns that this is a terrible idea for a normal app; he frames it as tolerable only for a constrained offline, file-based desktop experiment (14:20-14:48).
- Runtime access enables high-level bidirectional workflows such as asking the agent to visualize code as a diagram, editing the diagram, then asking it to update the code to match (15:05-15:22).

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)

Sources:
- [Agents on the Canvas in tldraw - Steve Ruiz, tldraw](../sources/20260501_sPUjIBH5Cwg.md), 13:34-15:22
