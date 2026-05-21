#!/usr/bin/env python3
"""
Rename all tracked files/dirs to kebab-case, transliterating Cyrillic to Latin.
Updates README.md links accordingly.

Usage:
    python scripts/rename_to_kebab.py [--dry-run]
"""

import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
README_PATH = REPO_ROOT / "README.md"

# Cyrillic → Latin transliteration (lowercase; uppercase mapped to same)
TRANSLIT: dict[str, str] = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
}
TRANSLIT.update({k.upper(): v for k, v in TRANSLIT.items()})


def to_kebab(name: str) -> str:
    """Convert a single path component to kebab-case."""
    result = ''.join(TRANSLIT.get(c, c) for c in name)
    result = result.lower()
    result = re.sub(r'[ _]+', '-', result)
    result = re.sub(r'[^a-z0-9.\-]', '', result)
    result = re.sub(r'-+', '-', result)
    return result.strip('-')


KEEP_AS_IS = {'README.md', 'Makefile', 'LICENSE', 'LICENSE.md', 'CHANGELOG.md'}


def normalize_path(path: str) -> str:
    """Convert all path components to kebab-case."""
    parts = path.split('/')
    new_parts = []
    for i, part in enumerate(parts):
        is_last = (i == len(parts) - 1)
        if part in KEEP_AS_IS:
            new_parts.append(part)
        elif is_last and '.' in part:
            # File: split on last dot to preserve extension
            dot_idx = part.rfind('.')
            base, ext = part[:dot_idx], part[dot_idx:]
            new_base = to_kebab(base)
            new_parts.append((new_base + ext) if new_base else part)
        else:
            # Directory (or file without extension): replace all non-alnum with hyphens
            # Preserve leading dot for hidden dirs/files (e.g. .github, .gitignore)
            prefix = '.' if part.startswith('.') else ''
            inner = part[1:] if part.startswith('.') else part
            result = ''.join(TRANSLIT.get(c, c) for c in inner).lower()
            result = re.sub(r'[^a-z0-9]+', '-', result)
            result = result.strip('-')
            new_parts.append((prefix + result) if result else part)
    return '/'.join(new_parts)


def build_rename_plan(all_files: list[str]) -> list[tuple[str, str]]:
    """
    Return list of (old_path, new_path) pairs for files that need renaming.
    Detects and resolves path collisions with numeric suffixes.
    """
    target_claimed: set[str] = set()
    plan: list[tuple[str, str]] = []

    for old_path in sorted(all_files):
        new_path = normalize_path(old_path)
        if new_path == old_path:
            target_claimed.add(old_path)
            continue

        # Collision resolution
        if new_path in target_claimed:
            dot_idx = new_path.rfind('.')
            if dot_idx > 0 and '/' not in new_path[dot_idx:]:
                base, ext = new_path[:dot_idx], new_path[dot_idx:]
            else:
                base, ext = new_path, ''
            suffix = 2
            while True:
                candidate = f"{base}-{suffix}{ext}"
                if candidate not in target_claimed:
                    new_path = candidate
                    break
                suffix += 1

        target_claimed.add(new_path)
        plan.append((old_path, new_path))

    return plan


def update_readme(plan: list[tuple[str, str]]) -> None:
    """Update all local links in README.md based on the rename plan."""
    readme_text = README_PATH.read_text(encoding='utf-8')

    # Build set of affected directory prefixes for directory-style links
    dir_renames: dict[str, str] = {}
    for old_path, new_path in plan:
        old_parts = old_path.split('/')
        new_parts = new_path.split('/')
        # Register every directory prefix change
        for depth in range(1, len(old_parts)):
            old_dir = '/'.join(old_parts[:depth]) + '/'
            new_dir = '/'.join(new_parts[:depth]) + '/'
            if old_dir != new_dir:
                dir_renames[old_dir] = new_dir

    def replace_link(m: re.Match) -> str:
        raw = m.group(1)  # e.g. "./analytics/Aviasales%20..." or "./analytics/Avito/"
        if not raw.startswith('./'):
            return m.group(0)

        inner = raw[2:]  # strip "./"
        decoded = urllib.parse.unquote(inner)

        # Normalize the decoded path
        new_decoded = normalize_path(decoded.rstrip('/'))
        suffix = '/' if decoded.endswith('/') else ''

        if new_decoded + suffix == decoded:
            return m.group(0)  # no change

        return f"({'./' + new_decoded + suffix})"

    updated = re.sub(r'\((\./[^)\s]+)\)', replace_link, readme_text)
    README_PATH.write_text(updated, encoding='utf-8')


def main() -> None:
    dry_run = '--dry-run' in sys.argv

    result = subprocess.run(
        ['git', '-c', 'core.quotepath=false', 'ls-files'],
        capture_output=True, cwd=REPO_ROOT,
    )
    all_files = [
        f for f in result.stdout.decode('utf-8').strip().split('\n') if f
    ]

    plan = build_rename_plan(all_files)

    if dry_run:
        print(f"Would rename {len(plan)} paths:\n")
        for old, new in plan:
            print(f"  {old}\n  → {new}\n")
        return

    # Sort: deeper paths first so we don't move a parent before its children
    plan.sort(key=lambda x: -x[0].count('/'))

    renamed = 0
    failed = 0
    for old_path, new_path in plan:
        new_full = REPO_ROOT / new_path
        new_full.parent.mkdir(parents=True, exist_ok=True)

        r = subprocess.run(
            ['git', 'mv', '--', old_path, new_path],
            cwd=REPO_ROOT, capture_output=True,
        )
        if r.returncode == 0:
            renamed += 1
            print(f"  {old_path} → {new_path}")
        else:
            failed += 1
            print(f"  FAILED {old_path} → {new_path}: {r.stderr.decode().strip()}", file=sys.stderr)

    update_readme(plan)

    print(f"\nRenamed: {renamed}  Failed: {failed}")
    print("Updated README.md")


if __name__ == '__main__':
    main()
