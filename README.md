# AI Engineer YouTube Index

Build a local index of recent videos from the AI Engineer YouTube channel for downstream agent knowledge-base processing.

The indexer fetches each video's current title, full description, YouTube URL, metadata path, and a local transcript link when English subtitles are available. Transcripts are saved as `.vtt` files so downstream tools can read a stable local artifact. The default subtitle language is `en-orig`; pass `--sub-langs` to use another `yt-dlp` subtitle selector.

## Usage

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

## Requirements

- Python 3.10+
- `yt-dlp` on `PATH`

Install or upgrade `yt-dlp` with:

```bash
python3 -m pip install --upgrade yt-dlp
```
