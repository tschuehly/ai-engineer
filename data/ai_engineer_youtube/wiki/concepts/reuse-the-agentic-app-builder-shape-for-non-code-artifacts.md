# Reuse the Agentic App-Builder Architecture for Non-Code Artifacts

Summary: The agentic app-builder stack — prompt UI, a sandbox on a remote machine, an agent with tools and skills, an editable artifact, a render step — is not specific to code. Swap the artifact type (a video composition instead of a codebase) and the render target (a rendered video instead of an app preview) and the same architecture builds creative artifacts, provided the artifact has a code-shaped representation and a mechanical render check.

Use when:
- Designing an agent product in a non-code domain (video, slides, music, documents, CAD) and deciding what infrastructure to build versus borrow.
- Evaluating whether an existing sandbox/agent-harness investment transfers to a new artifact type.
- Choosing where in a long creative pipeline to place a human approval gate.

Details:
- The claim stated plainly: "from the infrastructure standpoint, agentic video editor is very similar to agentic app builder." Both have a prompt UI — "in the video editor case, it's a media plus prompt" — and on the backend "there is a remote machine which is called sandbox… spinning up, and inside this machine, there is an agent with tools and skills, which is working on… what you're asking it to do." The only column-by-column differences on Deyneka's slide are the artifact (codebase versus video composition) and the output the user sees (app preview versus rendered video). (04:06 framing, 02:58-04:06)
- What makes the substitution work is the artifact's representation. Reelful's composition layer is Remotion, "an open-source framework to create videos as code, as React code… basically, it's just like a file with the order with all your assets and tracks and how they're following each other," chosen because "agents are really good at writing code and therefore we can use them to create videos with this remotion framework" (07:12-07:45). A domain without a code-shaped artifact format does not inherit this architecture for free — see [Match the agent's output medium to its native representation](match-agent-output-medium-to-its-native-representation.md).
- The second thing that transfers is the coding agent's feedback loop. Because the artifact is code, a mechanical validity check exists: "of course agent can make mistakes and that's why we develop this verification layer to make sure that all the composition is clean, is well defined, everything will be rendered and if there are some problems then the agent will reiterate on the composition" (07:45-08:19). This is the compile-or-retry loop of a coding agent applied to a video, and it is the reason a code representation beats a canvas one even before considering how well the model authors it.
- Domain judgment enters as skills rather than as a different architecture. Reelful's skills are "cut rules, how… to select the best moments… also font pairs, which fonts are more suitable for this use case, which are not… how to generate B-rolls, and this is where our taste and craft, uh, live, actually" (06:25-06:50). The harness is commodity; the skills are the proprietary layer — the same split argued in [General agents need skills for domain expertise](general-agents-need-skills-for-domain-expertise.md).
- The agent is an orchestrator, not only an author: it "can initiate some other sub-processes, for example, generating music that will fit this exact composition, generating voice-over, adding sounds, animating images" (06:50-07:12). Generative-media calls sit *under* the editing agent as tools rather than being the product.
- Placing the human gate: Reelful runs media understanding first (scene understanding plus speech transcription), then shows the user a creative plan "so that they can approve if they like it or not, what they want to change or maybe regenerate," explicitly "before actually starting editing," and only spins up the sandbox after approval (05:30-06:25). The gate sits at the cheapest point where intent is fully expressed and before the expensive render, which is the non-code analogue of reviewing a plan before an agent edits a repository.

Related topics:
- [Agents](../topics/agents.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Match the Agent's Output Medium to Its Native Representation](match-agent-output-medium-to-its-native-representation.md)
- [Author Visual Artifacts as HTML and Decouple the Editing Format from Delivery](author-visual-artifacts-as-html-decoupled-from-delivery-format.md)
- [Build High-Fidelity Engines to Create Verification Loops in Non-Code Domains](build-high-fidelity-engines-to-create-verification-loops-in-non-code-domains.md)
- [General Agents Need Skills for Domain Expertise](general-agents-need-skills-for-domain-expertise.md)
- [Editing Real Material Constrains an Agent More Than Generating From Scratch](editing-real-material-is-harder-for-agents-than-generating.md)
- [Do Not Roll Your Own Agent Code Sandbox](do-not-roll-your-own-agent-code-sandbox.md)

Sources:
- [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](../sources/20260818_pPj_tjlvYjA.md), 02:58-08:19
