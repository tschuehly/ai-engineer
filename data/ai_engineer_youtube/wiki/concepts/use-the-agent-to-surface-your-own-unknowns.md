# Use the Agent to Surface Your Own Unknowns

Summary: With a strong model, your spec is "the map" and the codebase is "the territory"; anything the agent hits that isn't in the map is an *unknown* — an unspecified decision point it has to guess at. Because a capable model traverses so much territory it hits many unknowns, *your* ability to match map to territory becomes the bottleneck — so use the agent itself to surface your unknowns before and during the run.

Use when:
- A capable agent keeps making plausible-but-wrong decisions on under-specified parts of a task.
- Working in an unfamiliar codebase or domain where you don't yet know what you don't know.
- You want to stay genuinely in the loop (able to review/represent the work) rather than rubber-stamp a large diff.

Details:
- Map ≠ territory: the plan/prompt/spec in your head is the map; the real codebase and constraints are the territory; every gap is a "decision point I haven't specified." "Fable is one of the first models where I really have to figure out my unknowns, because if not it traverses such a large area it runs into a lot of them." The human bottleneck becomes "my ability to match the map and the territory to find my unknowns." (09:04-10:09)
- The knowns matrix to reason about coverage: known knowns (what you actually write in the prompt), known unknowns (you know you haven't figured it out), unknown knowns (so obvious you wouldn't write it — "know it when I see it"), unknown unknowns (haven't considered at all). Each quadrant maps to a different elicitation move. (10:12-10:48)
- **Blind-spot pass** (for unknown unknowns): e.g. "I'm working on a new auth provider I know nothing about — do a blind-spot pass to help me find my relevant unknown-unknowns and prompt better," pointing it at the module, git diff, or Slack for gotchas; also works to learn a whole new field (he used it for color grading). "The model knows more about almost everything than I do; I just need to get it out of it." (10:48-11:52)
- **Brainstorm / prototype variants** (for unknown knowns): "I have no visual taste — make me an HTML page with four widely different design decisions so I can react to them," turning know-it-when-you-see-it taste into something you can point at. (11:52-12:28)
- **Interview-me**: ask the agent to interview you, giving it context about you/the work/the stage; steer it with "prioritize questions that would change the architecture." (12:28-12:58)
- **Reference-as-map**: "the best way to give Claude a map is to give it another map" — hand it reference code (even a different language/system) or an HTML mock-up as the spec instead of writing the spec in prose. (12:58-13:35)
- **Implementation-note logging**: while it runs and hits an unknown, "ask it to log it" so you can see where it deviated and why, after the fact. (13:35-13:57)
- **Quiz-me**: have the agent quiz you on what happened so you understand it well enough to represent the work in a PR/merge — "one of the most important parts is staying in the loop." (13:57-14:23)
- Relationship to specs: this is the *discovery* front-end to structured spec work — [spec-driven development](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md) turns a settled intent into requirements/design/tasks, while these moves find the decision points and taste you didn't know to specify. It also complements accepting/rejecting work by clean failure vs. ambiguity ([accept agentic tasks by clean failures, not ambiguous specs](accept-agentic-tasks-by-clean-failures-not-ambiguous-specs.md)).

Related topics:
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Spec-driven development turns prompts into requirements, design, and tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)
- [Capability Overhang: Tools Decide Which Model Spikes You Reach](capability-overhang-tools-decide-which-model-spikes-you-reach.md)
- [Use PRDs to align agents on the design concept](use-prds-to-align-agents-on-the-design-concept.md)

Sources:
- [Field Guide to Fable — Thariq Shihipar, Anthropic](../sources/20260706_9fubhllmsBU.md), 09:04-14:23
