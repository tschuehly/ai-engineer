# LLM codegen fails and how to stop 'em - Danilo Campos, PostHog

Source: [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](https://www.youtube.com/watch?v=juoNbJiZUi0)
Uploaded: 2026-04-30
Transcript: `raw/20260430_juoNbJiZUi0/juoNbJiZUi0.en-orig.vtt`

## Summary

Danilo Campos describes reliability patterns from PostHog Wizard, an autonomous code-generation product used for thousands of integrations. The talk frames codegen failures as a mix of stale model knowledge, poor architectural priors, over-improvised implementation paths, contradictory human-authored instructions, and unsafe file access, then shows how fresh Markdown context, exemplar projects, staged breadcrumbs, stop-hook self-interrogation, and narrow tools make the agent more reliable.

## Extracted Concepts

- [Fresh Markdown context mitigates model rot in codegen](../concepts/fresh-markdown-context-mitigates-model-rot-in-codegen.md) - supports serving current docs to agents instead of relying on model training snapshots.
- [Model airplanes give coding agents token-efficient exemplars](../concepts/model-airplanes-give-coding-agents-token-efficient-exemplars.md) - shows how thin example projects can encode the shape of a successful integration.
- [Breadcrumb coding agents through staged discovery and implementation](../concepts/breadcrumb-coding-agents-through-staged-discovery-and-implementation.md) - supports sequencing prompts so agents discover business-relevant files and event ideas before modifying code.
- [Ask agents after each run what blocked their success](../concepts/ask-agents-after-each-run-what-blocked-their-success.md) - shows a cheap stop-hook interrogation loop for finding missing tools, contradictory instructions, and wrong-language context.
- [Constrain sensitive file access with purpose-built tools](../concepts/constrain-sensitive-file-access-with-purpose-built-tools.md) - demonstrates replacing raw `.env` reads with narrow key-presence and key-write operations.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- PostHog Wizard is described as turning a long manual integration task into a shorter agent run and receiving substantial monthly use, making reliability failures visible at scale. 00:00-02:12
- Model rot appears when a model's training snapshot no longer reflects a fast-moving software project; PostHog mitigates this by letting the agent select fresh Markdown documentation from posthog.com and load it into context. 02:15-04:08
- Without current context, agents integrating PostHog made up keys, patterns, and nonexistent APIs; the product team treated that as their problem because users experience those failures as PostHog integration failures. 04:09-04:48
- "Model airplanes" are thin, auth-shaped example applications across frameworks and languages that show the correct shape of a PostHog integration without requiring full production apps. 05:27-06:47
- Breadcrumbing limits agent improvisation by asking for business-relevant files first, then likely events, then implementation, rather than telling the agent every final step upfront. 06:50-09:29
- Stop-hook self-interrogation asks the agent what would have set it up better; this surfaced missing MCP tools, contradictory directives, missing permissions, and JavaScript instructions being sent to a Python project. 10:22-12:05
- Early `.env` handling sent sensitive contents into inference/logging paths; a narrow replacement tool only checks whether a key exists and writes a new value for a key. 12:08-13:42
- Campos argues the Wizard is mostly Markdown and tools for delivering or processing Markdown, because plain-text prose can become more valuable as models improve while code remains a depreciating asset. 14:02-16:24
