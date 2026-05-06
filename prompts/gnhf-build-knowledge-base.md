# Build the AI Engineer YouTube Knowledge Base

Use the AI Engineer YouTube index to build a progressive-disclosure Markdown knowledge base one video at a time.

## Inputs

- Read video records from `data/ai_engineer_youtube/index.jsonl`.
- Each record includes `video_id`, `title`, `description`, `video_url`, `upload_date`, `duration_seconds`, `transcript_link`, and `metadata_link`.
- `transcript_link` points to a local WebVTT transcript under `data/ai_engineer_youtube/`.
- Write the knowledge base to `data/ai_engineer_youtube/knowledge_base.md`.

## Iteration Rule

Each gnhf iteration must analyze exactly one previously unprocessed video.

Choose the next video by this order:

1. `upload_date` descending.
2. `video_id` ascending for videos with the same upload date.
3. Skip videos already listed under `## Processed Sources` in `data/ai_engineer_youtube/knowledge_base.md`.
4. If the next unprocessed video has no transcript, add it to `## Processed Sources` with `transcript: unavailable`, add no knowledge entries for it, and stop the iteration.

Do not create Python, JavaScript, shell, or other extraction scripts for the knowledge-base transformation. The agent must read the selected transcript and perform the analysis directly in the iteration.

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

## Markdown Structure

Maintain `data/ai_engineer_youtube/knowledge_base.md` as a progressive-disclosure knowledge base:

- `# AI Engineer YouTube Knowledge Base`
- `## How to Use This Knowledge Base`
- `## Concept Map`
- `## Knowledge Entries`
- `## Processed Sources`

Each knowledge entry should use this shape:

```markdown
### Short, Retrieval-Friendly Entry Title

Summary: One or two sentences describing the reusable insight.

Use when:
- Concrete retrieval cue.
- Another concrete retrieval cue.

Details:
- Specific technical observation, workflow, tradeoff, or failure mode.
- Another specific point, with timestamp attribution when useful.

Source:
- Video: [Title](URL)
- Uploaded: YYYY-MM-DD
- Transcript: `relative/path.vtt`
- Timestamp: MM:SS-MM:SS when available
```

Keep entries atomic: one concept, workflow, tradeoff, or failure mode per entry. Prefer a small number of strong entries over many broad summaries.

Update `## Concept Map` so readers can skim the knowledge base before expanding individual entries. Group entries under stable topic bullets such as agents, context engineering, evaluation, inference, infrastructure, models, retrieval, tools, or workflows.

Update `## Processed Sources` with the processed video id, title, upload date, transcript path, and a short note about what was extracted.

## Validation

Before finishing the iteration:

- Confirm only one new video was marked as processed.
- Confirm every new knowledge entry cites the selected video.
- Confirm the Markdown file is readable and uses stable headings.
- Commit only the Markdown knowledge-base update and any directly required documentation update.

When all videos in `index.jsonl` are listed under `## Processed Sources`, report that the knowledge base is complete.
