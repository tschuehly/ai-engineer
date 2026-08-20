# Match Agent Tooling to the Model's Training Distribution

Summary: A frontier model arrives with habits — a specific edit tool, a specific search binary, a specific shell, a specific compaction format — because it was trained on them. The harness gets more reliability from supplying what the model already expects, including shipping the binaries that expectation implies, than from designing a cleaner interface the model has never seen.

Use when:
- Choosing between a custom file-edit tool and the provider's canonical one.
- Debugging an agent that keeps reaching for a command your environment does not have.
- Deciding which harness behaviors you can implement yourself and which must come from the provider.

Details:
- **File edits.** "All of the recent models starting with GPT-5 have been trained on the concept of an apply patch tool to do file editing, which means that they're used to using that to change files by giving it a… diff, and then… also using that same thing to create new files." The tool is not merely supported; it is the shape the model was optimized to emit. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 10:15-10:35)
- **Search, and the operational consequence.** "You will see the model naturally trying to use Ripgrep… since that's what it got used to during training. So, we're actually in the Codex harness shipping Ripgrep with… the harness if you don't have it installed on your own." This is the sharpest instance: the training distribution created a *runtime dependency*, and the harness's job was to satisfy it rather than to prompt the habit away. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 10:35-10:56)
- **Shell dialect.** "On Windows, we also trained the model to use PowerShell natively. So, if you're running it on Windows, you'll see it… start writing… PowerShell code instead." The platform difference was handled in training, not by a translation layer in the harness. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 10:56-11:05)
- **Context compaction.** Auto compaction "trigger[s] compaction on the server side in a way that the model got trained with so that the performance stays the same," producing a new context window containing a compaction item. Compaction is usually treated as a harness string operation; here it is a trained model behavior with a canonical format, which is why it is served rather than implemented locally. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 18:51-19:35)
- **The portability corollary is the useful part for anyone not using this harness.** Because these behaviors depend on training, a third-party harness cannot reproduce them by writing better code — it can only reproduce them if the API exposes them. The talk's closing claim is exactly that: "most of the features that are stand out for Codex are actually features that are exposed in the responses API. So even if you want to build your own agent, you can leverage these things like tool search, apply patch, web sockets, or server side compaction. You can use those directly regardless of what harness you're using." Which is also why the harness can be Apache 2 without giving much away. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 19:44-20:16)
- The practical checklist this implies when adopting a new model: find out which edit tool it was trained on, which search and shell commands it reaches for unprompted, whether the provider has a canonical compaction format, and which of those are reachable through the API rather than only through the vendor's own client.
- **This complements rather than contradicts per-model harness tuning.** The wiki's [Tune Coding-Agent Harnesses Per Model Family](tune-coding-agent-harnesses-per-model-family.md) says harnesses need per-family adjustment; this page names *what* the adjustment is usually about — not prompt phrasing but tool identity and environment contents. It also puts a floor under [Keep the Harness Thick Early and Thin It as the Model Improves](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md): some harness weight is not compensation for a model deficiency and will not become removable, because it is the environment the model's competence assumes.
- **Provenance and expiry.** Every claim here is a vendor statement about its own models, with no measurement of what happens if you use a different edit tool or omit the binary. The version boundaries are explicit and dated (apply patch "starting with GPT-5," compaction "end of last year"), under a speaker disclaimer that "this is a current state of affairs. Like things change so quickly." Re-derive the list per model release rather than treating it as settled. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 01:34-01:53, Provenance and Caveats)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Tune Coding-Agent Harnesses Per Model Family](tune-coding-agent-harnesses-per-model-family.md)
- [Keep the Harness Thick Early and Thin It as the Model Improves](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md)
- [Use stable agent harnesses as model-evolution boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md)
- [Defer Tool Definitions Out of Context and Let the Model Search for Them](defer-tool-definitions-out-of-context-and-let-the-model-search-for-them.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)

Sources:
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 10:15-11:05, 18:51-20:16
