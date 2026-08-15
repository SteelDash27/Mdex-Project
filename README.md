# Mdex

A command-line tool that scans your computer for Markdown files, indexes them into a searchable dashboard, and flags duplicates and orphaned notes.

Built in public by a first-year CS student who had too many scattered Obsidian notes and no way to find any of them.

## The problem

Markdown files pile up everywhere over time — an Obsidian vault, half-finished lecture notes, project READMEs, exported AI chat logs, random saves in Downloads. There's no single place to see what exists, what's duplicated, or what's been quietly abandoned. Finding a specific note stops being about what you wrote and starts being about remembering where you put it.

## What Mdex does

- **Recursive scan** — walks one or more root folders you configure and finds every `.md` file
- **Metadata extraction** — pulls title (from YAML frontmatter or the first `#` heading), tags, word count, last-modified date, and a content hash for each file
- **Unified index** — generates a sortable, filterable `dashboard.html` and a plain `INDEX.md` grouped by tag/folder
- **Duplicate & orphan report** — flags files with identical/near-identical content hashes, and files with no incoming links from anywhere else, so you know what's safe to clean up

## Status

Early prototype, actively being built in public. Environment and repo setup are done, and the recursive file scanner is working. Indexing (SQLite) is next.

## Tech stack

Python 3.11+, standard library + PyYAML + pytest

## Usage (current)

```powershell
# Copy the example config and set your own root folders
copy config.example.json config.json

# Scan for markdown files (dry run — prints found files, doesn't index yet)
python mdex.py scan --dry-run
```

`config.json` lets you set which root folders to scan and which directories to ignore (`.git`, `.venv`, `node_modules`, etc.). It's gitignored so personal paths never get committed.

## Roadmap

- [x] Recursive markdown scanner
- [ ] SQLite indexing layer
- [ ] Dashboard.html generator
- [ ] INDEX.md generator
- [ ] Duplicate detection (content hash)
- [ ] Orphan detection (link analysis)

## Why this exists

This is primarily a personal tool — I use Obsidian for almost everything and needed a way to actually find my own notes. It's also a way to learn what it's like to take an idea from scratch to something I genuinely use day to day. Following along means seeing the real process: what works, what breaks, and what changes along the way.
