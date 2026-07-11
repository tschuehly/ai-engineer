#!/usr/bin/env python3
"""Build a local index for recent AI Engineer YouTube videos."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any


DEFAULT_CHANNEL_URL = "https://www.youtube.com/@aiDotEngineer/videos"
DEFAULT_OUTPUT_DIR = Path("data/ai_engineer_youtube")
DEFAULT_DAYS = 365


@dataclass(frozen=True)
class DateRange:
    since: date
    until: date | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch AI Engineer YouTube metadata and transcripts, then build "
            "an index for downstream agent knowledge-base processing."
        )
    )
    parser.add_argument("--channel-url", default=DEFAULT_CHANNEL_URL)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--days",
        type=int,
        default=DEFAULT_DAYS,
        help="Rolling window to index when --since is omitted.",
    )
    parser.add_argument(
        "--since",
        help="Start date, inclusive. Accepts YYYY-MM-DD or YYYYMMDD.",
    )
    parser.add_argument(
        "--until",
        help="End date, inclusive. Accepts YYYY-MM-DD or YYYYMMDD.",
    )
    parser.add_argument(
        "--sub-langs",
        default="en-orig",
        help="yt-dlp subtitle language selector.",
    )
    parser.add_argument(
        "--yt-dlp",
        default="yt-dlp",
        help="Path to the yt-dlp executable.",
    )
    parser.add_argument(
        "--no-fetch",
        action="store_true",
        help="Only rebuild indexes from existing downloaded metadata.",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help=(
            "Re-fetch and overwrite metadata for every video in the window "
            "instead of only fetching new uploads. Use this to pick up "
            "descriptions or subtitles that were added after the first fetch."
        ),
    )
    return parser.parse_args()


def parse_date(value: str) -> date:
    normalized = value.strip()
    if len(normalized) == 8 and normalized.isdigit():
        return datetime.strptime(normalized, "%Y%m%d").date()
    return date.fromisoformat(normalized)


def yt_dlp_date(value: date) -> str:
    return value.strftime("%Y%m%d")


def ymd(value: str | None) -> str | None:
    if not value:
        return None
    if len(value) == 8 and value.isdigit():
        return f"{value[0:4]}-{value[4:6]}-{value[6:8]}"
    return value


def resolve_date_range(args: argparse.Namespace) -> DateRange:
    today = date.today()
    since = parse_date(args.since) if args.since else today - timedelta(days=args.days)
    until = parse_date(args.until) if args.until else None
    if until and until < since:
        raise SystemExit("--until must be on or after --since")
    return DateRange(since=since, until=until)


ARCHIVE_FILENAME = ".download-archive.txt"


def known_video_ids(raw_dir: Path) -> set[str]:
    ids: set[str] = set()
    for path in info_json_files(raw_dir):
        info = load_json(path)
        if info and info.get("id"):
            ids.add(str(info["id"]))
    return ids


def write_download_archive(ids: set[str], path: Path) -> None:
    # yt-dlp archive lines are "<extractor> <id>"; the YouTube extractor is "youtube".
    lines = "".join(f"youtube {video_id}\n" for video_id in sorted(ids))
    path.write_text(lines, encoding="utf-8")


def run_yt_dlp(args: argparse.Namespace, date_range: DateRange, raw_dir: Path) -> None:
    executable = shutil.which(args.yt_dlp) or args.yt_dlp
    if shutil.which(executable) is None and not Path(executable).exists():
        raise SystemExit(
            f"Could not find yt-dlp executable: {args.yt_dlp}. Install yt-dlp or pass --yt-dlp."
        )

    output_template = raw_dir / "%(upload_date)s_%(id)s" / "%(id)s.%(ext)s"
    command = [
        executable,
        "--ignore-errors",
        "--lazy-playlist",
        "--skip-download",
        "--write-info-json",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs",
        args.sub_langs,
        "--sub-format",
        "vtt",
        "--break-match-filters",
        f"upload_date >= {yt_dlp_date(date_range.since)}",
        "-o",
        str(output_template),
    ]

    if args.refresh:
        # Re-pull the whole window and overwrite existing files on disk.
        command.append("--force-overwrites")
    else:
        # Incremental: rebuild the archive from what is already on disk, then
        # let yt-dlp skip known uploads and stop paging at the first one it
        # recognizes (the channel lists newest-first).
        archive_path = raw_dir / ARCHIVE_FILENAME
        known = known_video_ids(raw_dir)
        write_download_archive(known, archive_path)
        command.extend(
            ["--download-archive", str(archive_path), "--break-on-existing"]
        )
        if known:
            print(
                f"Incremental fetch: {len(known)} videos already on disk; "
                "stopping at the first known upload. Use --refresh to re-pull all."
            )

    if date_range.until:
        command.extend(["--datebefore", yt_dlp_date(date_range.until)])
    command.append(args.channel_url)

    result = subprocess.run(command, check=False)
    if result.returncode not in (0, 101):
        raise subprocess.CalledProcessError(result.returncode, command)


def load_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def info_json_files(raw_dir: Path) -> list[Path]:
    return sorted(raw_dir.glob("*/*.info.json"))


def is_video_info(info: dict[str, Any]) -> bool:
    url = info.get("webpage_url") or info.get("original_url") or ""
    return bool(info.get("id") and info.get("title") and "watch?v=" in url)


def in_range(info: dict[str, Any], date_range: DateRange) -> bool:
    uploaded = parse_upload_date(info.get("upload_date"))
    if uploaded is None:
        return True
    if uploaded < date_range.since:
        return False
    if date_range.until and uploaded > date_range.until:
        return False
    return True


def parse_upload_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return parse_date(value)
    except ValueError:
        return None


def rel_path(path: Path, base: Path) -> str:
    return path.resolve().relative_to(base.resolve()).as_posix()


def transcript_candidates(video_dir: Path, video_id: str) -> list[Path]:
    return sorted(video_dir.glob(f"{video_id}.*.vtt"))


def transcript_priority(path: Path) -> tuple[int, str]:
    name = path.name
    priorities = [
        ".en-orig.vtt",
        ".en.vtt",
        ".en-US.vtt",
        ".en-GB.vtt",
    ]
    for index, suffix in enumerate(priorities):
        if name.endswith(suffix):
            return index, name
    return len(priorities), name


def choose_transcript(video_dir: Path, video_id: str) -> Path | None:
    candidates = transcript_candidates(video_dir, video_id)
    if not candidates:
        return None
    return sorted(candidates, key=transcript_priority)[0]


def build_entry(info_path: Path, info: dict[str, Any], output_dir: Path) -> dict[str, Any]:
    video_id = str(info["id"])
    video_dir = info_path.parent
    transcript = choose_transcript(video_dir, video_id)
    webpage_url = info.get("webpage_url") or f"https://www.youtube.com/watch?v={video_id}"
    upload_date = ymd(info.get("upload_date"))

    entry: dict[str, Any] = {
        "video_id": video_id,
        "title": info.get("title") or "",
        "description": info.get("description") or "",
        "video_url": webpage_url,
        "upload_date": upload_date,
        "duration_seconds": info.get("duration"),
        "channel": info.get("channel") or info.get("uploader"),
        "transcript_link": rel_path(transcript, output_dir) if transcript else None,
        "transcript_absolute_path": str(transcript.resolve()) if transcript else None,
        "transcript_format": "vtt" if transcript else None,
        "metadata_link": rel_path(info_path, output_dir),
    }
    return entry


def collect_entries(raw_dir: Path, output_dir: Path, date_range: DateRange) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    seen: set[str] = set()

    for path in info_json_files(raw_dir):
        info = load_json(path)
        if not info or not is_video_info(info) or not in_range(info, date_range):
            continue
        video_id = str(info["id"])
        if video_id in seen:
            continue
        entries.append(build_entry(path, info, output_dir))
        seen.add(video_id)

    entries.sort(key=lambda item: (item.get("upload_date") or "", item["video_id"]), reverse=True)
    return entries


def write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_jsonl(path: Path, entries: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(json.dumps(entry, ensure_ascii=False) + "\n")


def write_markdown(path: Path, entries: list[dict[str, Any]], index: dict[str, Any]) -> None:
    lines = [
        "# AI Engineer YouTube Index",
        "",
        f"- Channel: {index['channel_url']}",
        f"- Generated at: {index['generated_at']}",
        f"- Since: {index['since']}",
        f"- Until: {index['until'] or 'open'}",
        f"- Videos: {index['video_count']}",
        "",
    ]
    for entry in entries:
        transcript = entry["transcript_link"] or "No transcript file found"
        lines.extend(
            [
                f"## {entry['title']}",
                "",
                f"- Upload date: {entry['upload_date'] or 'unknown'}",
                f"- Video: {entry['video_url']}",
                f"- Transcript: {transcript}",
                f"- Metadata: {entry['metadata_link']}",
                "",
                entry["description"].strip() or "No description.",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    date_range = resolve_date_range(args)
    output_dir = args.output_dir
    raw_dir = output_dir / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)

    ids_before_fetch = known_video_ids(raw_dir)
    if not args.no_fetch:
        run_yt_dlp(args, date_range, raw_dir)

    entries = collect_entries(raw_dir, output_dir, date_range)
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    index = {
        "source": "youtube",
        "channel_url": args.channel_url,
        "generated_at": generated_at,
        "since": date_range.since.isoformat(),
        "until": date_range.until.isoformat() if date_range.until else None,
        "video_count": len(entries),
        "videos": entries,
    }

    write_json(output_dir / "index.json", index)
    write_jsonl(output_dir / "index.jsonl", entries)
    write_markdown(output_dir / "index.md", entries, index)

    new_ids = [entry["video_id"] for entry in entries if entry["video_id"] not in ids_before_fetch]
    missing_transcripts = sum(1 for entry in entries if not entry["transcript_link"])
    print(f"Wrote {len(entries)} videos to {output_dir / 'index.json'}")
    print(f"Wrote JSONL to {output_dir / 'index.jsonl'}")
    print(f"Wrote Markdown to {output_dir / 'index.md'}")
    print(f"New videos this run: {len(new_ids)}")
    if missing_transcripts:
        print(f"Warning: {missing_transcripts} videos have no downloaded transcript file")


if __name__ == "__main__":
    main()
