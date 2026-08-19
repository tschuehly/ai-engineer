# Hide an Agentic Pipeline Behind Templates and a Manual Editor

Summary: For a mass-consumer product, delivering a multi-stage agentic workflow can be a harder problem than building it. Three moves hide it: put the surface where the behavior already happens (mobile), replace the prompt with directional templates so the product works with no prompt at all, and follow the agentic pass with a conventional manual editor so users can fix small things themselves instead of re-prompting.

Use when:
- Taking an agent pipeline that works for expert users to a consumer audience.
- Users struggle to write a prompt that expresses what they want in a non-text domain.
- Deciding what happens after the agent's output is almost right.

Details:
- The problem statement, after Deyneka walks the full pipeline: "it's a lot, right? It's like very complex workflow and ideally we don't want our users to even know anything about it. And this is even maybe a bigger problem how to deliver this complex agentic workflow to mass consumer" (08:19-08:35). The pipeline's complexity is treated as something to conceal, not as a feature to expose.
- **Mobile-first as a context decision, not a platform preference.** Reelful went mobile "so that users can edit videos while driving, walking or maybe lifting weights" (08:35-08:52) — the surface follows where consumer video capture and posting actually happen, rather than where an editing timeline is most comfortable.
- **Directional templates replace prompting.** "Prompting videos can sometimes be also challenging. That's why we create directional templates. For example, like speak to camera in videos or maybe you want to add B-rolls or voiceover so that users can just select these directional templates, drop their media and that's it. Even without any prompt it will work" (08:52-09:24). A template names an outcome the user recognizes and pre-loads the direction the prompt would have carried; the zero-prompt path is the default, not a fallback.
- **A manual editor as the escape hatch after generation.** "A lot of people are already sort of using regular video editors and that's why we want to provide this experience as well… User first generates a video agentically, but if they want to tweak it, for example, remove a second or maybe correct some word in the captions, they can go into building editor and edit it a little bit" (09:24-09:59). The ordering matters: the agent produces the draft and the familiar tool handles the last-mile corrections, so a near-miss costs a drag rather than another full generation.
- **Where the approval gate goes.** The one place the pipeline is deliberately visible is the creative plan, shown before editing begins "so that they can approve if they like it or not, what they want to change or maybe regenerate" (05:50-06:08). Consumers are asked to review intent, which they can judge, and not the composition or the sandbox, which they cannot.
- Read together, the three moves define the exposed surface as: media in, one recognizable direction, a plan to approve, a result to nudge. Everything between — media understanding, sandbox, skills, composition code, verification — stays invisible.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Reuse the Agentic App-Builder Architecture for Non-Code Artifacts](reuse-the-agentic-app-builder-shape-for-non-code-artifacts.md)
- [Editing Real Material Constrains an Agent More Than Generating From Scratch](editing-real-material-is-harder-for-agents-than-generating.md)
- [Text-First AI Interfaces Exclude People Who Don't Think in Text](text-first-interfaces-exclude-people-who-dont-think-in-text.md)
- [Nail Deterministic UX Before Probabilistic Delight](nail-deterministic-ux-before-probabilistic-delight.md)
- [Scope the Assistant to Getting the User Unstuck, Not One-Shotting the Artifact](scope-the-assistant-to-getting-users-unstuck-not-one-shotting.md)
- [Structured Canvas Outputs Make Agent Edits Inspectable and Editable](structured-canvas-outputs-make-agent-edits-inspectable-and-editable.md)

Sources:
- [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](../sources/20260818_pPj_tjlvYjA.md), 05:50-06:08, 08:19-09:59
