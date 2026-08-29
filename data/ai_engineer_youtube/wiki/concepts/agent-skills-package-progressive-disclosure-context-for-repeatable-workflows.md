# Agent skills package progressive-disclosure context for repeatable workflows

Summary: Agent skills are context packages that expose a small trigger surface first, then let the agent load deeper instructions, references, or scripts only when the task calls for them.

Use when:
- Designing product-specific or domain-specific context for agents.
- Deciding how much workflow guidance belongs in the agent's initial context.

Details:
- A skill is described as a folder with instructions, files for repeatable workflows, custom information, and optional scripts; the required `SKILL.md` contains front matter such as a name and description. 03:17-04:22
- Progressive disclosure keeps the full skill content out of initial context: the agent receives enough metadata to decide when the rest of the skill is relevant. 04:25-05:24
- Reference files can hold deeper Markdown context and can link to other reference files, so a skill can behave like an index plus chapters rather than one large prompt. 05:21-06:24
- Anthropic's skills framing uses the same folder primitive: only metadata is shown at runtime until the agent decides to load `SKILL.md`, core instructions, directories, scripts, or other assets for the current task. 03:00-04:56
- Skill-like prompts can also implement advanced product workflows when loaded on demand through commands; Cursor used this pattern for worktree and parallel model comparison commands, with server-controlled prompts so the workflow could improve without a client update. 08:24-09:05
- API-specific skills can combine stable orientation with links to current Markdown documentation, reducing stale embedded context while still teaching the agent which models, agents, or workflows are available. 23:34-24:34
- Matt Pocock decomposes a skill into two units — **steps** (the step-by-step procedure) and **reference** (supporting material) — and treats keeping the top-level `SKILL.md` as small as possible as a first-class constraint, because smaller skills are easier to maintain and audit and every word shaved is a token shaved off every invocation. UNzCG3lw6O0 07:29-09:00
- The concrete progressive-disclosure move is branch-driven: look at the skill's *branches* (ways it can be used) and move reference material used on only one branch behind a "context pointer" to an external Markdown file ("external reference") bundled with the skill, so the agent pulls it in only when that branch is taken. His `domain modeling` skill hides its ADR template and `context.md` template this way because they're needed on only some branches; his single-branch `to PRD` keeps its reference inline. UNzCG3lw6O0 09:00-11:53

- One team turns the authoring judgment into an enforceable number. Khandelwal: "even in your [SKILL.md] files, don't overload it. Like, we've kind of set a hard limit for like 100 lines in your [SKILL.md] cuz your skill is really a folder." The reasoning clause is the same one Pocock gives, but a stated cap survives many contributors in a way a principle does not — each addition becomes a trade against an existing line, and review has something to point at. He pairs it with the same rule one level up for the repo context file ("a thin index that can point through the right files") and with a verification test at the first prompt. See [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md). Note that line count is a crude proxy for tokens, and no derivation is offered for 100. ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 14:54-15:04, 15:36-15:50)
- **Progressive disclosure stated as the cost mechanism, and the unit it produces.** "The skills comes to solve a key problem around the context window… with the progressive disclosure pattern — the right skills, the right amount of skills in the right time to solve the right problem, and that's reduce the token usage." The unit this yields is know-how that is "executable, portable and cheap," with cheap being the disclosure property specifically. ([Touil](../sources/20260828_M05vON8i0aI.md), 09:35-09:57) Worth noting which of the three each design principle buys: specialization and composability buy executability, the open standard buys portability across harnesses, and only progressive disclosure buys cheapness. Nothing in the talk is measured.
- **The forcing function observed in a production system, in order.** Izmit's assistant launched with "a nine-page long agent instructions" and hit each limit in turn: business processes and workflows "couldn't fit them into the agent instructions anymore. And then the skills came… let's build a skill library"; then MCP servers arrived and needed orchestration instructions of their own, "we hit the limits on the agent instructions. What do we do? Okay, let's do the progressive disclosures." The system now carries close to 20 skills and five to six MCP connections. Two things are worth taking from the sequence: skills entered as an overflow mechanism for procedural knowledge rather than as a design choice, and progressive disclosure was forced a second time by tool orchestration text, not by the workflow content itself. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:14-05:31, 12:11-13:08)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

- Skills are also the unit a *scheduler* invokes, and the use is not coding. Ben Holmes packages personal knowledge-base maintenance as two skills — `enrich note` (stamp a timestamp, tag from a fixed reference list, research the source on the web, write key-term backlinks) and a wiki generator — then runs them nightly in a cloud sandbox with prompts that name the skill rather than restate the procedure: "instruct the agent run enriched note across [n] notes that are not enriched yet." Two properties of the skill format do the work there: the skill is harness-independent ("you can of course do it manually with whatever harness"), and it is a file that ships into a fresh sandbox alongside the corpus. Note also that the skill's reliability rests on a bundled *reference folder* of allowed tags, i.e. the reference-file half of the format carrying policy, not just documentation. See [Constrain Agent-Generated Tags to a Reference Vocabulary](constrain-agent-generated-tags-to-a-reference-vocabulary.md). ([LLM Knowledge Bases](../sources/20260812_I3bpdgFJCUY.md), 06:29-07:47, 07:49-07:53, 15:44-16:47)

Related concepts:
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Constrain Agent-Generated Tags to a Reference Vocabulary](constrain-agent-generated-tags-to-a-reference-vocabulary.md)
- [Run Recurring Knowledge Jobs in a Cloud Sandbox With Sync-Down/Sync-Back](run-recurring-knowledge-jobs-in-a-cloud-sandbox-with-sync-down-sync-back.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Prompt-coded product behavior reduces code but weakens hard guarantees](prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md)
- [Agent skills should point to current docs instead of embedding every API detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md)
- [Treat complex skills like software artifacts](treat-complex-skills-like-software-artifacts.md)
- [Prune skills with single source of truth, sediment removal, and no-op deletion tests](prune-skills-with-single-source-of-truth-sediment-and-no-op-deletion-tests.md)
- [Choose a skill's trigger by trading context load against cognitive load](choose-skill-trigger-by-trading-context-load-against-cognitive-load.md)
- [Split skills to hide future steps and force more leg work per step](split-skills-to-hide-future-steps-and-force-leg-work.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)
- [Budget a Third of Sprint Capacity for Re-Architecture](budget-a-third-of-sprint-capacity-for-re-architecture.md)
- [Let Users Author the Output Format as a Skill](let-users-author-the-output-format-as-a-skill.md)
- [Gate an Environment to Agents Only](gate-an-environment-to-agents-only.md)

Sources:
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md), 03:17-06:24
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](../sources/20251208_CEvIs9y1uog.md), 03:00-04:56
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md), 08:24-09:05
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md), 23:34-24:34
- [Building Great Agent Skills: The Missing Manual - Matt Pocock](../sources/20260629_UNzCG3lw6O0.md), 07:29-11:53
- [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../sources/20260812_I3bpdgFJCUY.md), 06:29-07:53, 15:44-16:47
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 14:54-15:04, 15:36-15:50
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 09:35-09:57
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:14-05:31, 12:11-13:08
