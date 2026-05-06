# AI Engineer YouTube Topical Wiki

Build a local index of recent videos from the AI Engineer YouTube channel, then use `gnhf` to analyze one transcript per iteration into a topical Markdown wiki.

The indexer fetches each video's current title, full description, YouTube URL, metadata path, and a local transcript link when English subtitles are available. Transcripts are saved as `.vtt` files so downstream agents can read a stable local artifact. The default subtitle language is `en-orig`; pass `--sub-langs` to use another `yt-dlp` subtitle selector.

## Index Videos

```bash
python3 scripts/build_ai_engineer_youtube_index.py
```

By default, the script indexes videos from the rolling last 365 days and writes:

- `data/ai_engineer_youtube/index.json`
- `data/ai_engineer_youtube/index.jsonl`
- `data/ai_engineer_youtube/index.md`
- `data/ai_engineer_youtube/raw/.../*.info.json`
- `data/ai_engineer_youtube/raw/.../*.vtt`

Use explicit dates when a run must be reproducible:

```bash
python3 scripts/build_ai_engineer_youtube_index.py --since 2025-05-06 --until 2026-05-06
```

Rebuild indexes from already downloaded metadata:

```bash
python3 scripts/build_ai_engineer_youtube_index.py --no-fetch
```

## Build the Wiki

Run `gnhf` with the committed prompt:

```bash
cat prompts/gnhf-build-knowledge-base.md | gnhf --agent codex --max-iterations 1
```

Each iteration analyzes exactly one previously unprocessed transcript from `data/ai_engineer_youtube/index.jsonl` and updates the compiled wiki under:

- `data/ai_engineer_youtube/wiki/`

The wiki uses:

- `wiki/AGENTS.md` as the wiki maintenance schema for future agents
- `wiki/index.md` as the entry point
- `wiki/log.md` as the append-only chronological activity log
- `wiki/topics/` for synthesized topic articles
- `wiki/concepts/` for atomic source-backed concept pages
- `wiki/sources/` for per-video source notes
- `wiki/indexes/` for the concept index and processed-source log

Run more iterations when you want the wiki to grow:

```bash
cat prompts/gnhf-build-knowledge-base.md | gnhf --agent codex --max-iterations 10
```

## Requirements

- Python 3.10+
- `yt-dlp` on `PATH`
- `gnhf` on `PATH`

Install or upgrade `yt-dlp` with:

```bash
python3 -m pip install --upgrade yt-dlp
```

Install `gnhf` with:

```bash
npm install -g gnhf
```
