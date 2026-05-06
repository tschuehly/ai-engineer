# Build the AI Engineer YouTube Topical Wiki

Use the AI Engineer YouTube index to incrementally compile a topical Markdown wiki one video at a time.

## Inputs

- Read video records from `data/ai_engineer_youtube/index.jsonl`.
- Each record includes `video_id`, `title`, `description`, `video_url`, `upload_date`, `duration_seconds`, `transcript_link`, and `metadata_link`.
- `transcript_link` points to a local WebVTT transcript under `data/ai_engineer_youtube/`.
- Write the compiled wiki under `data/ai_engineer_youtube/wiki/`.

## Wiki Shape

Maintain this directory structure:

```text
data/ai_engineer_youtube/wiki/
  AGENTS.md
  index.md
  log.md
  topics/
    <topic-slug>.md
  concepts/
    <concept-slug>.md
  sources/
    <YYYYMMDD>_<video_id>.md
  indexes/
    concept-index.md
    processed-sources.md
```

The wiki is organized by durable topics and concepts. Source notes preserve provenance; topic and concept pages hold the compiled understanding.

`wiki/AGENTS.md` is the operating schema for future agents. Follow it whenever it exists, and update it only when the supported workflow or intended wiki conventions change.

`wiki/index.md` is content-oriented: it is the entry point for finding topics, important concepts, and secondary indexes.

`wiki/log.md` is chronological and append-only: it records ingests, query outputs filed into the wiki, and lint passes using parseable headings.

## Iteration Rule

Each gnhf iteration must analyze exactly one previously unprocessed video.

Choose the next video by this order:

1. `upload_date` descending.
2. `video_id` ascending for videos with the same upload date.
3. Skip videos already listed in `data/ai_engineer_youtube/wiki/indexes/processed-sources.md`.
4. If the next unprocessed video has no transcript, add a source note under `wiki/sources/`, add it to `indexes/processed-sources.md` with `transcript: unavailable`, add no concept pages for it, and stop the iteration.

Do not create Python, JavaScript, shell, or other extraction scripts for the knowledge-base transformation. The agent must read the selected transcript and perform the analysis directly in the iteration.

Before choosing page updates, read `wiki/AGENTS.md`, `wiki/index.md`, `wiki/indexes/concept-index.md`, `wiki/indexes/processed-sources.md`, and any relevant existing topic, concept, or source pages. The goal is to integrate the selected source into the existing synthesis, not to summarize it in isolation.

## Analysis Task

For the selected video:

1. Read the index record, video description, and transcript.
2. Clean WebVTT mentally while preserving useful timestamps for attribution.
3. Extract durable knowledge useful to an AI engineering agent:
   - core ideas
   - named tools, frameworks, models, companies, and protocols
   - workflows and implementation patterns
   - architecture decisions and tradeoffs
   - failure modes, caveats, and evaluation methods
   - concrete commands, code concepts, API patterns, or operational practices when present
4. Ignore sponsorship boilerplate, intros, outros, repeated captions, and low-signal commentary.
5. Do not invent facts not supported by the title, description, or transcript.

## Compilation Task

Compile the selected video into the wiki using four layers:

1. Source note: create `wiki/sources/<YYYYMMDD>_<video_id>.md`.
2. Concept pages: create or update focused pages under `wiki/concepts/`.
3. Topic articles: update existing topical articles under `wiki/topics/`, or create new ones when no current topic fits.
4. Navigation and history: update `wiki/index.md`, `wiki/indexes/concept-index.md`, `wiki/indexes/processed-sources.md`, and append one entry to `wiki/log.md`.

Prefer updating existing topic and concept pages when the new source strengthens, qualifies, or contradicts a current page. Create a new page only when the extracted knowledge is meaningfully distinct.

Use stable topic slugs such as:

- `agents`
- `context-engineering`
- `evaluation`
- `inference`
- `infrastructure`
- `models`
- `retrieval`
- `tools`
- `workflows`

Add more specific topics when the wiki needs them, for example `edge-inference`, `agent-memory`, or `coding-agents`.

## Page Templates

### Wiki Schema

Maintain `wiki/AGENTS.md` as the schema for future agents. It should describe only the supported current workflow and intended state:

- raw sources are immutable
- the wiki is LLM-maintained
- source notes preserve provenance
- concept pages are atomic source-backed retrieval units
- topic pages synthesize across sources
- `index.md` is the content catalog
- `log.md` is the append-only chronological record
- query outputs can be filed back into the wiki when they add durable value
- lint passes should look for contradictions, stale claims, orphan pages, missing concept pages, missing links, and source gaps

Describe only the supported workflow and intended wiki state in `wiki/AGENTS.md`.

### Source Note

```markdown
# Video Title

Source: [Video Title](URL)
Uploaded: YYYY-MM-DD
Transcript: `relative/path.vtt`

## Summary

One short paragraph summarizing the useful knowledge extracted from the source.

## Extracted Concepts

- [Concept Title](../concepts/concept-slug.md) - one-line reason this source supports the concept.

## Topic Links

- [Topic Title](../topics/topic-slug.md)

## Notes

- Source-backed observation with timestamp attribution when useful.
```

### Concept Page

```markdown
# Concept Title

Summary: One or two sentences describing the reusable insight.

Use when:
- Concrete retrieval cue.
- Another concrete retrieval cue.

Details:
- Specific technical observation, workflow, tradeoff, or failure mode.
- Another specific point, with timestamp attribution when useful.

Related topics:
- [Topic Title](../topics/topic-slug.md)

Related concepts:
- [Related Concept](related-concept-slug.md)

Sources:
- [Video Title](../sources/YYYYMMDD_video_id.md), MM:SS-MM:SS
```

### Topic Article

```markdown
# Topic Title

## Overview

A concise synthesis of the topic across sources. This should read like an article, not a list of ingestion events.

## Key Concepts

- [Concept Title](../concepts/concept-slug.md) - one-line explanation of why it matters.

## Open Questions

- Source-backed or clearly marked question that future iterations should resolve.

## Sources

- [Video Title](../sources/YYYYMMDD_video_id.md)
```

### Log Entry

Append one entry to `wiki/log.md`:

```markdown
## [YYYY-MM-DD] ingest | Video Title

- Source: [Video Title](sources/YYYYMMDD_video_id.md)
- Processed: `video_id`
- Updated topics: [Topic Title](topics/topic-slug.md)
- Updated concepts: [Concept Title](concepts/concept-slug.md)
- Notes: one sentence describing what changed in the compiled wiki.
```

## Linking Rules

- Every concept page must link back to at least one topic page and one source page.
- Every topic page must link to its key concept pages and source pages.
- Every source note must link to the concept pages and topic pages it contributed to.
- `wiki/index.md` must link to topic pages and the index files.
- `wiki/indexes/concept-index.md` must list all concept pages grouped by topic.
- `wiki/indexes/processed-sources.md` must list every processed video exactly once.
- `wiki/log.md` must have exactly one new `## [YYYY-MM-DD] ingest | ...` entry for the selected video.

## Validation

Before finishing the iteration:

- Confirm only one new video was marked as processed.
- Confirm every new or updated concept claim cites the selected source or a prior source already listed on that concept page.
- Confirm the selected source has a source note under `wiki/sources/`.
- Confirm related topic, concept, and source pages link to each other.
- Confirm `wiki/log.md` has one new append-only entry for the iteration.
- Confirm Markdown files are readable and use stable headings.
- Commit only the wiki update and any directly required prompt or documentation update.

When all videos in `index.jsonl` are listed in `wiki/indexes/processed-sources.md`, report that the wiki is complete.
