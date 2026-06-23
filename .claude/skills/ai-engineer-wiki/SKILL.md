---
name: ai-engineer-wiki
description: Field-tested knowledgebase distilled from AI Engineer conference talks for building AI software and building with AI — agents, coding agents, RAG/retrieval, evals, inference, context engineering, MCP/tools, models, voice, vision, security, AI product strategy. Use when answering a question or making a design decision about building AI/LLM systems and you want grounded patterns, tradeoffs, and failure modes with source citations; also use when another agent needs grounded AI-engineering knowledge.
---

# AI Engineer Wiki

A curated, source-backed wiki distilled from AI Engineer YouTube talks. Use it to ground AI-engineering questions and design decisions in field-tested patterns instead of answering from memory alone. It is **read-only** — you consume it over the network; you never edit it from here.

It is fetched on demand from GitHub raw URLs — no clone, no local copy. The source of truth is the `main` branch of `tschuehly/ai-engineer`.

```
BASE=https://raw.githubusercontent.com/tschuehly/ai-engineer/main/data/ai_engineer_youtube/wiki
```

Four page types live under `$BASE`:

- `topics/<slug>.md` — 21 synthesized articles. **Broad/orienting** questions ("how should I think about evals?").
- `concepts/<slug>.md` — ~780 atomic, source-backed pages. **Specific** claims, patterns, tradeoffs, failure modes. Each cites the originating video with timestamps.
- `sources/<file>.md` — one provenance note per video. Use when the user wants the original talk, speaker, or quote.
- `indexes/concept-index.md` — every concept title grouped by topic, with its link. The searchable map.

## Topic routing table

Map the question to one or more topics first — no fetch needed for this step. Slugs are stable.

| slug | covers |
|---|---|
| `agents` | agent architecture, autonomy, tool use, multi-agent orchestration |
| `coding-agents` | coding agents, harnesses, codegen, review, agent-legible codebases |
| `workflows` | workflows vs agents, structured pipelines, orchestration |
| `context-engineering` | context windows, memory, prompt/context management |
| `tools` | tool & MCP design, tool catalogs, agent connectivity |
| `retrieval` | RAG, search, embeddings, knowledge bases |
| `evaluation` | evals, benchmarks, agent-trajectory evaluation, LLM judges |
| `models` | model families, training, capabilities, post-training/RL |
| `inference` | serving, latency, throughput, caching, quantization, cost |
| `edge-inference` | on-device / edge model inference |
| `infrastructure` | platforms, sandboxes, agent runtimes, deployment infra |
| `security` | agent/LLM security, permissions, MCP risks, sandboxing |
| `voice-agents` | voice/speech agents, realtime audio |
| `vision-ai` | vision models, multimodal perception, OCR |
| `generative-media` | image/video/audio generation, diffusion |
| `robotics` | embodied agents, VLA models, robot control |
| `product-strategy` | AI product strategy, taste, adoption, org design |
| `ai-monetization` | pricing, business models, ROI for AI products |
| `architecture-copilots` | copilots, AI architects, design assistants |
| `business-intelligence` | AI for BI, analytics, data querying |
| `healthcare-operations` | AI in healthcare / clinical operations |

## Retrieval procedure

Use `curl -fsSL` (exact, greppable bytes). Fetch only what you need; follow links to go deeper.

1. **Route.** Pick the relevant topic slug(s) from the table above.

2. **Search the index** for candidate concept pages. Grep the concept-index for your keywords (run several greps with synonyms for recall — the index is large, so let `grep` filter it, don't pull it whole into context):
   ```bash
   curl -fsSL "$BASE/indexes/concept-index.md" | grep -iE 'eval|benchmark|llm.?judge'
   ```
   Each hit is a `- [Title](../concepts/<slug>.md)` line — the `<slug>.md` is the exact path you need.

3. **Read.** For orientation, fetch the topic article; for specifics, fetch the concept pages whose titles matched:
   ```bash
   curl -fsSL "$BASE/topics/evaluation.md"
   curl -fsSL "$BASE/concepts/evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md"
   ```

4. **Follow links.** Concept pages end with `Related concepts`, `Related topics`, and `Sources`. Fetch a few of these when the first pages don't fully answer the question. Stop when you have enough — you do not need to read the whole wiki.

5. **Answer with citations.** Synthesize across the pages you read. For every claim, name the concept page and the video provenance it cites (speaker, talk title, timestamp) so the answer is verifiable. When advising a coding agent on a build decision, give the concrete pattern/tradeoff and link the concept page it came from.

## Rules

- **Never fabricate a concept path.** Slugs are not a clean transform of titles (e.g. "Target High-Value AI Verticals as Capability Matures" → `target-high-value-ai-verticals.md`). Always copy the exact `<slug>.md` from a link in the index or a topic page. If you didn't see the link, search the index first.
- **Resolve relative links** to raw URLs: both `../concepts/x.md` and `concepts/x.md` become `$BASE/concepts/x.md`; `../sources/y.md` becomes `$BASE/sources/y.md`.
- **Prefer concept pages for specific claims** (they are atomic and carry source timestamps) and **topic pages for synthesis/orientation**.
- **Read-only.** Do not attempt to write back into the wiki from a consuming project. To add knowledge, work in the `tschuehly/ai-engineer` repo itself.
- **WebFetch is the fallback** only where no shell/`curl` is available. Prefer `curl` so the index stays greppable and content isn't summarized away.
- **On 404 / empty results:** the wiki may not be merged into `main` yet, or the path is wrong. Re-derive the path from a fresh index grep; if `$BASE/index.md` itself 404s, tell the user the wiki likely isn't on `main` yet.
