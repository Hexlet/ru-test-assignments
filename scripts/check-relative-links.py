#!/usr/bin/env python3
"""Verify every relative Markdown link in the repository resolves to a file.

This is the check that was missing when 75e2804 renamed every path to
kebab-case: README.md and 20 assignments kept pointing at the old names,
and nothing noticed for months. External links are not checked here —
lychee does that on a schedule.

Usage: python3 scripts/check-relative-links.py
Exit code 1 if any link is broken.
"""
import os
import re
import sys
import urllib.parse

SKIP_PREFIXES = ('http://', 'https://', 'mailto:', 'tel:', '#', '<')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def links(text):
    return re.findall(r'\]\(([^)\s]+)\)', text)


def main():
    broken = []
    checked = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != '.git']
        for name in filenames:
            if not name.endswith('.md'):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding='utf-8', errors='ignore') as fh:
                text = fh.read()
            for raw in links(text):
                if raw.startswith(SKIP_PREFIXES):
                    continue
                target = urllib.parse.unquote(raw.split('#')[0].split('?')[0])
                if not target:
                    continue
                checked += 1
                if not os.path.exists(os.path.normpath(os.path.join(dirpath, target))):
                    broken.append((os.path.relpath(path, ROOT), raw))

    print(f'checked {checked} relative links')
    if broken:
        print(f'\n{len(broken)} broken:')
        for path, raw in broken:
            print(f'  {path}: {raw}')
        return 1
    print('all resolve')
    return 0


if __name__ == '__main__':
    sys.exit(main())
