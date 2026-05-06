# AI Engineer YouTube Wiki Schema

This directory is a topical Markdown wiki compiled from local AI Engineer YouTube source artifacts.

## Ownership

Raw sources under `../raw/` are immutable. Read them for evidence, but do not edit them during wiki maintenance.

The LLM maintains the wiki. Human edits should normally happen through instructions to the agent rather than direct edits to topic, concept, source, index, or log files.

## Structure

- `index.md` is the content-oriented entry point. Keep it short and useful for navigation.
- `log.md` is the append-only chronological activity record.
- `topics/` contains synthesized articles that explain durable topical areas across sources.
- `concepts/` contains atomic, source-backed retrieval pages.
- `sources/` contains one provenance note per processed video.
- `indexes/concept-index.md` groups concept pages by topic.
- `indexes/processed-sources.md` lists each processed video exactly once.

## Ingest Workflow

Process exactly one unprocessed video per ingest.

Before writing, read `index.md`, `indexes/concept-index.md`, `indexes/processed-sources.md`, and the existing topic or concept pages likely to be affected.

Create or update:

- one source note in `sources/`
- relevant concept pages in `concepts/`
- relevant topic articles in `topics/`
- `index.md`
- `indexes/concept-index.md`
- `indexes/processed-sources.md`
- one append-only entry in `log.md`

Prefer strengthening existing topic and concept pages over creating new pages. Create a new page only when the knowledge is meaningfully distinct and likely to be reused.

## Page Semantics

Source notes preserve provenance and summarize what a video contributes.

Concept pages should be atomic: one reusable workflow, tradeoff, failure mode, architecture decision, evaluation method, tool pattern, model pattern, or operational practice per page. Every claim should be source-backed.

Topic pages should synthesize across sources and read like articles. They should not become chronological ingest logs.

## Query Workflow

For questions against the wiki, read `index.md` first, then relevant topic, concept, and source pages. If the answer adds durable value, file it back into the wiki as a concept page, topic update, or derived output page, and append a `query` entry to `log.md`.

## Lint Workflow

Lint passes should look for contradictions, stale claims, orphan pages, missing links, missing concept pages, duplicate concepts, weak source attribution, and source gaps worth researching. Append a `lint` entry to `log.md` when a lint pass changes or evaluates the wiki.
