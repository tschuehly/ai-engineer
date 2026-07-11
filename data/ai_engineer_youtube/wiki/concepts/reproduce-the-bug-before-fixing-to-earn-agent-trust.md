# Reproduce the Bug Before Fixing to Earn Agent Trust

Summary: Agents are eager and confidently claim to know the fix, but a claim you cannot check is worthless. Requiring the agent to reproduce a bug before it fixes it converts intuition into a checkable feedback loop — the "first step to trust" that lets you stop hand-verifying and start running agents overnight and in parallel.

Use when:
- Deciding whether an agent's "it's all working perfectly" can be trusted without manual review.
- Trying to move from supervised, one-at-a-time agent use to unattended overnight runs or many parallel agents.
- Explaining why some engineers get great AI results on legacy code and others get "garbage."

Details:
- The greenfield/brownfield split is really a feedback-loop split: on greenfield "the agent's intuition is correct," while on brownfield "there be dragons" — dead ends, unused code, "things it hasn't even looked at" — and "the big difference between those two is the feedback loop." (01:58-02:46)
- Brownfield success is achievable, so the divide is not the codebase age: "we've seen people using AI in legacy applications with good success. I have myself." (00:42-00:51)
- A blindfolded agent's report is hollow: "it's all working perfectly" really means "to the best of what you have given me, that sounds like it should work… Maybe the agent was able to verify its work. Maybe it wasn't." (02:46-03:12)
- Reproduction is the trust gate: "until it reproduces the bug, I don't trust you" — agents are "very eager" ("you just need to add this code"), and reproducing the bug first forces the intuition through a real check. (04:57-05:22)
- Trust is what unlocks scale: without it "I'm going to have to go and verify it myself and I'm wasting time, and I cannot then take that agent and start running it overnight… This is a first step to trust." (05:29-05:45)
- The user split (AI is magic vs AI is garbage) is a verification gap, not personality: enthusiasts see it failing and say "try again, check those logs," while skeptics "just give up." (03:26-03:42)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Give Your Agent Eyes With a Product-Specific Observation Tool](give-your-agent-eyes-with-a-product-specific-observation-tool.md)
- [Make Agent Work More Trustworthy by Making It Verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [Greenfield AI Coding Gains Drop Off in Mature Codebases](greenfield-ai-coding-gains-drop-off-in-mature-codebases.md)

Sources:
- [Your agent is blindfolded — Johan Lajili, Poolside AI](../sources/20260708_iRcX54EO5g8.md), 00:42-05:45
