# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A curated, community-maintained catalog of real job test assignments ("тестовые задания") from
Russian-speaking tech companies, published by Hexlet. There is no application code — the
deliverable is `README.md` plus the assignment texts and attachments it links to.

Content is in Russian. Assignment titles follow the pattern
`Тестовое задание для <роль>` with the stack in italics at the end, e.g.
`Тестовое задание для аналитика *(Python, SQL)*`.

## Commands

```sh
make lint        # rumdl check .   (markdown lint)
make lint-fix    # rumdl fmt .     (autofix)
```

No tests, no build, no dependency manifest. `rumdl` (0.2.19) is the only tool; config lives in
`.rumdl.toml` — ATX headings, `*` bullets, 4-space list indent, and a long disable list
(`MD013`, `MD033`, `MD041`, …). There is no CI workflow; `.github/` holds only the PR template.

Assignment files pulled in from external sources routinely fail rumdl (upstream authors don't
lint). Run `make lint-fix` after adding files, and prefer scoping the check when you only care
about your own additions: `rumdl check path/to/dir`.

## README.md is the index and the product

Every content change is paired: the assignment text lands under `{section-dir}/{company}/`, and a
link to it goes inside the matching `<details>` block in `README.md`. An orphan on either side is
a bug — commit `ad09bd5` exists solely to reconnect ten directories no README link reached.

Rules that come from the README itself and the PR checklist:

* Companies are listed **alphabetically** within a section.
* Add the **assignment description only, never a solution** — solutions destroy the exercise for
  the next candidate.
* Prefer local copies over external links. Dead or unreachable upstreams get removed
  (`84f2d6b`, `b4cc34a`) or annotated inline, e.g. `*сайт недоступен*`.

### Section → directory mapping

The 19 `<summary>` sections mostly map to a same-named top-level directory
(`Frontend` → `frontend/`, `Android` → `android/`, …). The exceptions:

| Section | Directory |
| --- | --- |
| `Аналитик` | `analytics/` |
| `Automation QA`, `Manual QA` | `qa/` (shared) |
| `C#` | `csharp/` |
| `Data Scientist` | `data-scientist/` |
| `Python` | `backend/python/` |
| `Clojure` | `backend/` |
| `full-stack` | `fullstack/` |

A section may also link across into another section's directory: `PHP` has one entry under
`backend/`, and `Other` has one under `analytics/`. The reason is not documented.

### Path naming

All paths are kebab-case with Cyrillic transliterated to Latin — `data-scientist/bst-digital/`,
`analytics/kaspi-kz-produktovyj-analitik/weekend-offer-produktovyj-analitik.pdf`. This was a repo-wide rename (`75e2804`, with fallout
fixed in `1e401cb`, `9e36694`); do not reintroduce spaces, uppercase, or Cyrillic in filenames.

Directories named `neizvestnye` hold assignments with no known company. `analytics/neizvestnye/`
carries an index README so its 15 files stay findable until someone attributes them.

### Binary attachments use Git LFS

PDFs, spreadsheets, `.docx`, large CSVs and zips are tracked through LFS via explicit per-file
entries in `.gitattributes`. **A new binary needs its own line there before it is committed** —
otherwise it lands as a plain blob (or, worse, an existing pointer breaks; see `9e36694`).

## scripts/download-assignments.py

Mirrors external assignment links into the repo and rewrites `README.md` to point at the local
copies.

```sh
python scripts/download-assignments.py --dry-run   # plan only, no network
python scripts/download-assignments.py             # fetch + rewrite README links in place
GITHUB_TOKEN=... python scripts/download-assignments.py   # raises GitHub rate limit
```

Behavior worth knowing before relying on it:

* Parses `README.md` directly: `<summary>` lines set the section, unindented bullets set the
  current company, 4-space-indented bullets are the assignments. Layout deviations make entries
  invisible to it.
* Only GitHub repos/blobs/trees, Gists, and Google Docs are fetchable. Hosts in
  `SKIP_URL_PATTERNS` (Google Drive, Notion, Yandex Disk, Dropbox, …) are skipped **by design** and
  stay as external links. Links to `https://github.com/Hexlet/` are ignored.
* Existing files are never overwritten — the README link is still rewritten to point at them.
* Its `SECTION_TO_DIR` table is **stale** relative to the layout above: it would write
  `python/`, `clojure/`, `data_scientist/` and `QA/`. Fix the destination or move the file
  afterwards rather than trusting the script's placement blindly.
* Takes an exclusive flock on `.download_assignments.lock` (gitignored).
