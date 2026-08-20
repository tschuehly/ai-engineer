# Use stable agent harnesses as model-evolution boundaries

Summary: A maintained coding-agent harness can become the stable boundary between fast-changing model releases and product-specific user experience. This lets teams focus on domain workflows instead of retuning prompts, tools, context management, and safety plumbing for every model upgrade.

Use when:
- Deciding whether to build a coding-agent harness from scratch or integrate a maintained one.
- Designing an agent product that must survive model, API, and tool-surface changes.

Details:
- The talk defines a coding agent as user interface, model, and harness; the harness is the interface layer to the model and the surface it uses for prompts, tools, users, code, and multi-turn work. 02:06-04:24
- Harness maintenance includes custom-tool adaptation, model-specific prompts, latency and thinking UX, compaction, API changes, parallel tool-call thread merging, sandboxing, permissions, port forwarding, MCP plumbing, and image handling. 04:39-10:04
- Treating the harness as the abstraction layer reduces the need to optimize prompts and tools with every model upgrade and lets product teams spend more effort on the differentiating user workflow. 11:44-12:47
- The source is not saying all agent products should be thin wrappers. The stronger claim is that product differentiation often lives above the generic harness: IDE integration, review surface, CI/CD role, workflow fit, and domain-specific connectors. 12:18-15:28
- **Stable is not the same as static, and a model lab draws the line.** Anthropic's Applied AI team makes the same architectural argument — independent, swappable components inside an overall architecture that holds still — but attaches an explicit failure condition to it: "what you don't want to do is have a stale harness that takes weeks or even months to migrate to a new model," and the prescription is "designing for the model capabilities of tomorrow" rather than today's. The boundary earns its keep by making migration cheap, not by making it unnecessary; a harness that is stable because nobody can change it has failed at the thing this page recommends it for. See [a harness fix becomes overhead when the model outgrows it](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md) for the measurable form of that failure. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 09:03-10:13)
- **The same source names what stays with the developer at every rung.** Even on a fully managed runtime, "you own the product, you own the task, you own your context," and context management plus domain expertise is "what separates a coding agent from a legal agent or go-to-market agent" — which is the vendor-side restatement of this page's claim that differentiation lives above the generic harness. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 04:00-04:26, 15:50-16:47)
- **The boundary leaks in one specific direction: harness behavior that was trained cannot be re-implemented above it.** Codex's diff format, its shell tooling, and its compaction all exist in the shapes they do because the model was trained on them — apply patch is "a format that we trained the model on starting with GPT-5," ripgrep ships with the binary "because we know the model has been trained on using ripgrep," and auto compaction runs *server-side* because the model was trained with it ([Match Agent Tooling to the Model's Training Distribution](match-agent-tooling-to-the-models-training-distribution.md)). The practical consequence for anyone treating a harness as the stable layer: a feature that depends on training is not portable to another model behind the same harness, and if the provider moves it server-side it is not swappable at all. The abstraction still holds for prompts, tools, and UX; it does not hold for anything the weights were fitted to. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 10:15-11:05, 18:51-19:35)

- **Three reasons to stay swappable, one of which is rarely stated: the best model can be withdrawn.** Superconductor's first lesson is "to be model and harness agnostic," and the arguments are that "the best model and harness can change weekly," that open-weight models are now credible ("we've been really happy with GLM 5.2. They're much cheaper"), and that "the incentives of the people selling you tokens aren't really aligned with yours… They want to sell you more tokens. And you might be happy to pay for as many tokens as it takes, but you don't want to pay for more than that." The withdrawal case is the one with an anecdote attached: "Fable came out, and it was great. Kind of switched our default to that for like the few days we had it, and then it went away and switched back to Codex. But the most important thing is like because we're agnostic, like none of that had any meaningful disruption on our work." Note that "harness agnostic" here is a stronger commitment than this page's usual framing — the harness is a swappable component too, not the stable boundary, which is coherent for a vendor whose own product is the layer above both. ([Arjun Singh](../sources/20260809_OL7kfezynJM.md), 01:46-02:37, 15:04-15:26)
- **A stable harness is also a confound in any longitudinal measurement taken through it.** Denys Linkov re-runs the same hard task on each model release and is explicit that the harness does not hold still underneath: "models are getting significantly better along with harnesses." He observes the trajectory *shape* changing too — newer runs spawn sub-agents, make more plan calls, and issue more shell commands and verifications for the same task. If you use a harness as your fixed boundary and then read improvement off it, part of what you measured is your own harness upgrades; a longitudinal claim about model capability needs the harness version pinned or reported. See [Re-Run One Remembered Hard Task on Each New Model](re-run-one-remembered-hard-task-on-each-new-model.md). ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 09:39-11:22)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Unified coding-agent harnesses combine models, tools, environments, and safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Build internal AI engineering platforms when off-the-shelf tools lack enterprise context](build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md)
- [Tune Coding-Agent Harnesses Per Model Family](tune-coding-agent-harnesses-per-model-family.md)
- [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)
- [Model a Managed Agent as Agent, Environment, and Session](model-a-managed-agent-as-agent-environment-session.md)
- [Match Agent Tooling to the Model's Training Distribution](match-agent-tooling-to-the-models-training-distribution.md)
- [Re-Run One Remembered Hard Task on Each New Model](re-run-one-remembered-hard-task-on-each-new-model.md)

Sources:
- [Future-Proof Coding Agents - Bill Chen & Brian Fioca, OpenAI](../sources/20251205_wVl6ZjELpBk.md), 02:06-04:24, 04:39-10:04, 11:44-15:28
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 04:00-04:26, 09:03-10:13, 15:50-16:47
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 10:15-11:05, 18:51-19:35
- [Multiplayer agentic engineering — Arjun Singh, Superconductor](../sources/20260809_OL7kfezynJM.md), 01:46-02:37, 15:04-15:26
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 09:39-11:22
