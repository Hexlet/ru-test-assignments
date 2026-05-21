#!/usr/bin/env python3
"""
Download external assignment links and save as local .md files.
Updates README.md links to point to local copies.

Usage:
    python scripts/download_assignments.py [--dry-run]

Environment:
    GITHUB_TOKEN  optional GitHub personal access token (raises rate limit)
"""

import fcntl
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

README_PATH = Path(__file__).parent.parent / "README.md"
REPO_ROOT = README_PATH.parent
LOCK_FILE = REPO_ROOT / ".download_assignments.lock"

SECTION_TO_DIR: dict[str, str] = {
    "Аналитик": "analytics",
    "Android": "android",
    "Automation QA": "QA",
    "Manual QA": "QA",
    "Backend": "backend",
    "C#": "csharp",
    "Data Scientist": "data_scientist",
    "DevOps": "devops",
    "Frontend": "frontend",
    "full-stack": "fullstack",
    "Go": "go",
    "iOS": "ios",
    "Java": "java",
    "Python": "python",
    "Clojure": "clojure",
    "PHP": "php",
    "Ruby": "ruby",
    "SQL": "sql",
    "Other": "other",
}

# Platforms we cannot reliably fetch without auth/browser
SKIP_URL_PATTERNS = [
    "drive.google.com",
    "notion.so",
    "notion.site",
    "paper.dropbox.com",
    "dropbox.com",
    "cloud.mail.ru",
    "disk.yandex",
    "colab.research.google.com",
    "dl.funbox.ru",
    "versta24.ru",
    "isdigi.ru",
    "www.reg.ru/company",
    "docs.xored.com",
    "gleaming-tent",
    "doc.clickup.com",
    "newgen-it.github.io",
]

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------


def http_get(url: str, timeout: int = 15) -> str | None:
    headers = {"User-Agent": "hexlet-assignments-downloader/1.0"}
    if GITHUB_TOKEN and "api.github.com" in url:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print(f"  [rate-limited] {url}", file=sys.stderr)
        return None
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Content fetchers
# ---------------------------------------------------------------------------


def fetch_github_repo(url: str) -> str | None:
    """Fetch README markdown from a GitHub repo/blob/tree URL."""
    # blob: github.com/owner/repo/blob/branch/path/to/file.md
    m = re.search(r"github\.com/([^/]+/[^/]+)/blob/([^/]+)/(.+)", url)
    if m:
        raw = f"https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}/{m.group(3)}"
        return http_get(raw)

    # tree with subpath: github.com/owner/repo/tree/branch/path
    m = re.search(r"github\.com/([^/]+/[^/]+)/tree/([^/]+)/(.+)", url)
    if m:
        repo, branch, path = m.group(1), m.group(2), m.group(3)
        content = http_get(
            f"https://raw.githubusercontent.com/{repo}/{branch}/{path}/README.md"
        )
        if content:
            return content
        return http_get(f"https://raw.githubusercontent.com/{repo}/{branch}/{path}")

    # tree without subpath: github.com/owner/repo/tree/branch
    m = re.search(r"github\.com/([^/]+/[^/]+)/tree/([^/?#]+)", url)
    if m:
        repo, branch = m.group(1), m.group(2)
        return http_get(f"https://raw.githubusercontent.com/{repo}/{branch}/README.md")

    # bare repo: github.com/owner/repo
    m = re.search(r"github\.com/([^/]+/[^/?#]+?)(?:\.git)?(?:[?#]|$)", url)
    if m:
        repo = m.group(1)
        for branch in ("main", "master"):
            content = http_get(
                f"https://raw.githubusercontent.com/{repo}/{branch}/README.md"
            )
            if content:
                return content

    return None


def fetch_gist(url: str) -> str | None:
    """Fetch content from a GitHub Gist URL."""
    m = re.search(r"gist\.github\.com/[^/]+/([a-f0-9]+)", url)
    if not m:
        return None
    gist_id = m.group(1)

    file_anchor = None
    if "#file-" in url:
        a = re.search(r"#file-(.+)$", url)
        if a:
            file_anchor = a.group(1)

    raw_api = http_get(f"https://api.github.com/gists/{gist_id}")
    if not raw_api:
        return None
    try:
        data = json.loads(raw_api)
    except json.JSONDecodeError:
        return None

    files = data.get("files", {})
    if not files:
        return None

    if file_anchor:
        for filename, file_data in files.items():
            anchor = filename.lower().replace(".", "-").replace(" ", "-")
            if anchor == file_anchor:
                raw_url = file_data.get("raw_url")
                return http_get(raw_url) if raw_url else file_data.get("content")

    # Prefer .md files, fall back to first file
    for filename, file_data in files.items():
        if filename.endswith(".md"):
            raw_url = file_data.get("raw_url")
            return http_get(raw_url) if raw_url else file_data.get("content")

    first = next(iter(files.values()))
    raw_url = first.get("raw_url")
    return http_get(raw_url) if raw_url else first.get("content")


def fetch_google_docs(url: str) -> str | None:
    """Export Google Docs as plain text."""
    m = re.search(r"docs\.google\.com/document/d/([a-zA-Z0-9_-]+)", url)
    if not m:
        return None
    doc_id = m.group(1)
    return http_get(
        f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
    )


def fetch_external(url: str) -> str | None:
    """Dispatch to the appropriate fetcher."""
    if "gist.github.com" in url:
        return fetch_gist(url)
    if "github.com/" in url:
        return fetch_github_repo(url)
    if "docs.google.com/document" in url:
        return fetch_google_docs(url)
    return None


def is_skippable(url: str) -> bool:
    return any(p in url for p in SKIP_URL_PATTERNS)


# ---------------------------------------------------------------------------
# Naming helpers
# ---------------------------------------------------------------------------


def sanitize_dir(name: str) -> str:
    """Make a string safe to use as a filesystem directory name."""
    # Unwrap markdown emphasis/strikethrough — keep the text content
    name = re.sub(r"\*+([^*]*)\*+", r"\1", name)  # *italic* / **bold** → content
    name = re.sub(r"~~([^~]*)~~", r"\1", name)     # ~~text~~ → text
    # Remove characters forbidden in directory names on common OSes
    name = re.sub(r'[<>:"/\\|?*()~]', "", name)
    return name.strip()[:60]


def slug_from_url(url: str) -> str:
    """Derive a unique filename slug from a URL (without .md extension)."""
    # GitHub blob: .../blob/branch/path/to/file.ext → file (no ext)
    # Use repo name when file is README to avoid generic README.md names
    m = re.search(r"github\.com/[^/]+/([^/]+)/blob/[^/]+/(?:.+/)?([^/?#]+)", url)
    if m:
        repo, name = m.group(1), m.group(2)
        base = re.sub(r"\.[a-z]+$", "", name)
        return repo if base.upper() == "README" else base

    # GitHub tree with subpath: .../tree/branch/subpath → path-with-dashes
    m = re.search(r"github\.com/[^/]+/[^/]+/tree/[^/]+/(.+)", url)
    if m:
        path = m.group(1).rstrip("/")
        return path.replace("/", "-")  # e.g. "backend/developer" → "backend-developer"

    # GitHub bare repo: .../owner/repo → repo
    m = re.search(r"github\.com/[^/]+/([^/?#]+?)(?:/tree/[^/?#]+)?(?:[?#]|$)", url)
    if m:
        return m.group(1)

    # Gist: gist.github.com/user/{id} → gist-{id[:8]}
    m = re.search(r"gist\.github\.com/[^/]+/([a-f0-9]+)", url)
    if m:
        return f"gist-{m.group(1)[:8]}"

    # Google Docs → use doc ID for uniqueness
    if "docs.google.com/document" in url:
        m = re.search(r"docs\.google\.com/document/d/([a-zA-Z0-9_-]+)", url)
        if m:
            return m.group(1)[:20]
        return "assignment"

    # Generic fallback
    m = re.search(r"https?://[^/]+/(.+?)(?:\?|#|$)", url)
    if m:
        slug = m.group(1).replace("/", "-")
        return slug[:40]
    return "assignment"


def _looks_like_assignment_url(url: str) -> bool:
    """Return True if URL looks like an assignment resource (not a company homepage)."""
    assignment_domains = [
        "gist.github.com",
        "docs.google.com",
        "drive.google.com",
        "notion.so",
        "notion.site",
        "dropbox.com",
        "cloud.mail.ru",
        "disk.yandex",
        "colab.research.google.com",
        "doc.clickup.com",
    ]
    if any(d in url for d in assignment_domains):
        return True
    # github.com with a specific repo (at least 2 path segments)
    m = re.search(r"github\.com/([^/]+)/([^/?#]+)", url)
    if m:
        return True
    return False


# ---------------------------------------------------------------------------
# README parser
# ---------------------------------------------------------------------------


def parse_assignments(readme_text: str) -> list[dict]:
    """
    Return a list of external assignment entries found in the README.

    Each entry contains:
        line_idx  int       0-based index into readme_text.split('\\n')
        section   str       section name (e.g. "Backend")
        company   str|None  company name or None for standalone entries
        title     str       link title text
        url       str       external URL
    """
    lines = readme_text.split("\n")
    entries: list[dict] = []
    current_section: str | None = None
    current_company: str | None = None

    for i, line in enumerate(lines):
        # Section header
        m = re.match(r"\s*<summary>(.+?)</summary>", line)
        if m:
            current_section = m.group(1).strip()
            current_company = None
            continue

        if "</details>" in line:
            current_company = None
            continue

        # Unindented bullet: * [Title](url)
        m = re.match(r"^\* \[(.+?)\]\((.+?)\)", line)
        if m:
            title, url = m.group(1), m.group(2)
            if url.startswith("./"):
                current_company = title
            elif url.startswith("http") and _looks_like_assignment_url(url):
                # Standalone unindented assignment — company=None, path derived from URL
                entries.append(
                    dict(
                        line_idx=i,
                        section=current_section,
                        company=None,
                        title=title,
                        url=url,
                    )
                )
                # Do NOT update current_company
            else:
                current_company = title
            continue

        # 4-space indented assignment bullet: "    * [Title](url)"
        m = re.match(r"^    \* \[(.+?)\]\((.+?)\)", line)
        if m:
            title, url = m.group(1), m.group(2)
            if url.startswith("http") and not url.startswith(
                "https://github.com/Hexlet/"
            ):
                entries.append(
                    dict(
                        line_idx=i,
                        section=current_section,
                        company=current_company,
                        title=title,
                        url=url,
                    )
                )

    return entries


# ---------------------------------------------------------------------------
# Path determination
# ---------------------------------------------------------------------------


def company_from_url(url: str) -> str:
    """Extract a company/org name from a URL for standalone entries."""
    m = re.search(r"github\.com/([^/]+)/", url)
    if m:
        return m.group(1)
    m = re.search(r"gist\.github\.com/([^/]+)/", url)
    if m:
        return m.group(1)
    if "docs.google.com" in url:
        return "google-docs"
    m = re.search(r"https?://([^/]+)", url)
    if m:
        return m.group(1).replace(".", "-")
    return "unknown"


def local_path_for(entry: dict) -> Path:
    """Determine the local file path: {section_dir}/{company_dir}/{slug}.md"""
    section_dir = SECTION_TO_DIR.get(entry["section"] or "", "other")
    slug = slug_from_url(entry["url"]) + ".md"

    if entry["company"]:
        company_dir = sanitize_dir(entry["company"])
    else:
        company_dir = sanitize_dir(company_from_url(entry["url"]))

    return REPO_ROOT / section_dir / company_dir / slug


def readme_link(local_file: Path) -> str:
    """Build the relative link to use in README.md."""
    rel = local_file.relative_to(REPO_ROOT)
    parts = [urllib.parse.quote(str(p), safe="") for p in rel.parts]
    return "./" + "/".join(parts)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run(dry_run: bool = False) -> None:
    if not dry_run:
        lock_fh = open(LOCK_FILE, "w")
        try:
            fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError:
            print("Another instance is already running.", file=sys.stderr)
            sys.exit(1)

    readme_text = README_PATH.read_text(encoding="utf-8")
    lines = readme_text.split("\n")

    entries = parse_assignments(readme_text)
    print(f"Found {len(entries)} external assignment links.\n")

    if dry_run:
        print("Planned local paths (no network requests in dry-run):\n")
        for e in entries:
            url = e["url"]
            if is_skippable(url):
                tag = "[SKIP]"
            else:
                local_file = local_path_for(e)
                rel = local_file.relative_to(REPO_ROOT)
                if local_file.exists():
                    tag = "[EXISTS]"
                else:
                    tag = f"[NEW] → {rel}"
            print(f"  {tag}  {url[:80]}")
        return

    skipped: list[str] = []
    failed: list[str] = []
    saved: list[tuple[str, str]] = []
    already_exist: list[str] = []
    line_replacements: dict[int, str] = {}
    saved_paths: dict[Path, str] = {}  # local_file → url already saved this run

    for entry in entries:
        url = entry["url"]

        if is_skippable(url):
            skipped.append(url)
            continue

        local_file = local_path_for(entry)

        if local_file.exists():
            already_exist.append(url)
            # Still update the README link even if file exists
            link = readme_link(local_file)
            original = lines[entry["line_idx"]]
            new_line = original.replace(f"]({url})", f"]({link})")
            if new_line != original:
                line_replacements[entry["line_idx"]] = new_line
            continue

        if local_file in saved_paths:
            # Same path already written this run (duplicate URL or path collision)
            already_exist.append(url)
            link = readme_link(local_file)
            original = lines[entry["line_idx"]]
            new_line = original.replace(f"]({url})", f"]({link})")
            if new_line != original:
                line_replacements[entry["line_idx"]] = new_line
            continue

        print(f"Fetching: {url}")
        content = fetch_external(url)
        time.sleep(0.4)

        if not content:
            failed.append(url)
            print("  -> FAILED")
            continue

        local_file.parent.mkdir(parents=True, exist_ok=True)
        local_file.write_text(content, encoding="utf-8")
        saved_paths[local_file] = url

        link = readme_link(local_file)
        original = lines[entry["line_idx"]]
        new_line = original.replace(f"]({url})", f"]({link})")
        if new_line != original:
            line_replacements[entry["line_idx"]] = new_line

        saved.append((url, str(local_file.relative_to(REPO_ROOT))))
        print(f"  -> saved to {local_file.relative_to(REPO_ROOT)}")

    if line_replacements:
        for idx, new_line in line_replacements.items():
            lines[idx] = new_line
        README_PATH.write_text("\n".join(lines), encoding="utf-8")
        print(f"\nUpdated {len(line_replacements)} links in README.md")

    print(f"\n{'='*60}")
    print(f"Saved:          {len(saved)}")
    print(f"Already local:  {len(already_exist)}")
    print(f"Skipped:        {len(skipped)}")
    print(f"Failed:         {len(failed)}")

    if skipped:
        print(f"\nSkipped ({len(skipped)} unsupported platform URLs):")
        for url in skipped:
            print(f"  {url}")

    if failed:
        print(f"\nFailed to fetch ({len(failed)}):")
        for url in failed:
            print(f"  {url}")


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    if dry:
        print("--- DRY RUN (no network requests) ---\n")
    run(dry_run=dry)
