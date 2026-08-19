# Editing Real Material Constrains an Agent More Than Generating From Scratch

Summary: Generating a creative artifact from a blank canvas lets an agent pick any output it can defend; editing the user's own real material removes that freedom. The agent must judge which of several imperfect takes is best, what to discard, and how to order what remains — from footage that may be messy or incomplete — while still clearing a polish bar set by professionally made human work.

Use when:
- Deciding whether an AI creative product should generate new content or operate on content the user already has.
- Estimating why an editing agent is failing on material a generation model handles easily.
- Choosing what an agent's skills must encode: aesthetic production rules versus selection and omission criteria.

Details:
- The distinction Ekaterina Deyneka calls "actually the most interesting to me": Reelful "do[es] not generate a lot of content. We are expecting you to provide your real life, your personal content, and we will edit it for you. And actually, this is a more complex problem because if the agent has a blank canvas, it can do whatever they can. But in the editing case, the agent has to figure out which moments are the best… what to omit, what to use, how to organize everything together" (04:06-04:56).
- Two constraints compound. The input is not chosen by the system — "sometimes footage can be messy or incomplete" — and the output bar is absolute rather than relative to the input: the agent "still has to deliver a very polished result, professionally made, so that ideally the viewers of this content don't get if it is like AI or human edited" (04:56-05:17). A generation model that draws a bad frame can redraw it; an editor that has no good take of the moment cannot.
- The concrete failure surface is ordinary and unglamorous. Deyneka's second framing case is a speak-to-camera recording where "you have a lot of pauses, unsuccessful shots, and you expect an agent to figure it out" and return a shareable clip (02:19-02:39). None of that is a model-quality problem; it is a judgment problem over material the model did not produce.
- The consequence for what you build: the agent's domain knowledge has to be *selection* knowledge, not just production knowledge. Reelful's skills lead with "cut rules, how… to select the best moments" before font pairs and b-roll generation (06:25-06:50), and the pipeline starts with media understanding — scene understanding plus speech transcription — because the agent cannot choose among moments it has not perceived (05:30-05:50).
- Positioning corollary: editing real personal footage is the part of the market that generation models do not absorb as they improve, since the value is in the user's own material. This sits opposite the generative products elsewhere in this wiki that compete on distribution breadth or steerability of synthesized content.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Reuse the Agentic App-Builder Architecture for Non-Code Artifacts](reuse-the-agentic-app-builder-shape-for-non-code-artifacts.md)
- [Hide an Agentic Pipeline Behind Templates and a Manual Editor](package-agentic-pipelines-behind-templates-and-a-manual-editor.md)
- [Reliability and Stylistic Range Are Opposite Model Positions](reliability-and-stylistic-range-are-opposite-model-positions.md)
- [Anchor Generative Asset Cohesion on One Key-Art Image](anchor-generative-asset-cohesion-on-one-key-art-image.md)
- [Assemble Scene Context by Level of Detail Around the Edit Focus](assemble-scene-context-by-level-of-detail-around-the-edit-focus.md)

Sources:
- [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](../sources/20260818_pPj_tjlvYjA.md), 02:19-05:17, 06:25-06:50
