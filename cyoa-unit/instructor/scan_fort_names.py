# CTI 110
# CYOA UNIT - Fort name scan
# norris
# 10/15/26

# Scans the unit's files for the names the Fort on the Lake repository
# forbids. The patterns are NOT copied here. At run time this script reads
# them from the Fort repository's own tests:
#   generator/test.mjs  the FORBIDDEN line (any case) and the line after it
#                       (case-sensitive, whole word)
#   intro/test.mjs      the first four patterns of the "for (const bad of" line
#                       (the URL, script and link patterns are skipped)
#
#   python3 scan_fort_names.py
#   python3 scan_fort_names.py --fort-repo ~/games-osr-fort-on-lake some/file.md
#
# Prints "HIT path:line: match" for each hit, or "no hits".
# Exit code: 0 no hits, 1 at least one hit, 2 the patterns could not be read.

import argparse
import os
import re
import sys

COURSE = "/home/user/course-cti110-26fa"
STORMING = "/home/user/course-cti110-storming/cyoa-unit"
DEFAULT_FORT = "/home/user/games-osr-fort-on-lake"

# One JavaScript regex literal: /body/flags
JS_REGEX = re.compile(r"/((?:\\.|[^/\\\n])+)/([a-z]*)")


def read_lines(path):
    """Return the lines of a text file."""
    with open(path, encoding="utf-8") as file:
        return file.read().splitlines()


def to_python(body, flags):
    """Turn one JavaScript regex (body and flags) into a compiled Python one."""
    if "i" in flags:
        return re.compile(body, re.IGNORECASE)
    return re.compile(body)


def generator_patterns(fort_repo):
    """The FORBIDDEN pattern and the case-sensitive pattern on the next line."""
    lines = read_lines(os.path.join(fort_repo, "generator", "test.mjs"))
    for number, line in enumerate(lines):
        if re.match(r"\s*const FORBIDDEN\s*=", line):
            patterns = []
            first = JS_REGEX.search(line)
            if first is not None:
                patterns.append(to_python(first.group(1), first.group(2)))
            # The next line that holds a regex literal is the case-sensitive one.
            for later in lines[number + 1:number + 4]:
                found = JS_REGEX.search(later)
                if found is not None:
                    patterns.append(to_python(found.group(1), found.group(2)))
                    break
            return patterns
    return []


def intro_patterns(fort_repo):
    """The first four patterns of the 'for (const bad of [...])' line."""
    lines = read_lines(os.path.join(fort_repo, "intro", "test.mjs"))
    for line in lines:
        if "for (const bad of [" in line:
            inside = line.split("[", 1)[1]
            found = JS_REGEX.findall(inside)
            return [to_python(body, flags) for body, flags in found[:4]]
    return []


def wanted(path, endings):
    """True if the file name ends with one of the endings."""
    return path.lower().endswith(endings)


def files_under(folder, endings):
    """Every file under folder whose name ends with one of the endings."""
    found = []
    for root, dirs, names in os.walk(folder):
        dirs[:] = sorted(d for d in dirs if d not in ("__pycache__", ".git"))
        for name in sorted(names):
            path = os.path.join(root, name)
            if wanted(path, endings):
                found.append(path)
    return found


def default_paths():
    """The stories and blueprints, the class code, and the unit's pages."""
    stories = os.path.join(COURSE, "cyoa_kit", "stories")
    paths = [os.path.join(stories, name) for name in
             ("fort.json", "dead_drop.json", "fort_blueprint.md", "dead_drop_blueprint.md")]
    for folder in ("p5", "p6", "p7", "cyoa_kit"):
        paths = paths + files_under(os.path.join(COURSE, folder), (".md", ".py", ".json"))
    paths = paths + files_under(STORMING, (".md", ".html"))
    unique = []
    for path in paths:
        if path not in unique and os.path.isfile(path):
            unique.append(path)
    return unique


def expand(paths):
    """A folder on the command line means every .md, .py, .json and .html in it."""
    result = []
    for path in paths:
        if os.path.isdir(path):
            result = result + files_under(path, (".md", ".py", ".json", ".html"))
        else:
            result.append(path)
    return result


def scan_file(path, patterns):
    """Return a list of 'path:line: match' strings for one file."""
    hits = []
    try:
        lines = read_lines(path)
    except (OSError, UnicodeDecodeError) as error:
        print(f"SKIP {path}: {error}")
        return hits
    for number, line in enumerate(lines, start=1):
        for pattern in patterns:
            for match in pattern.finditer(line):
                hits.append(f"{path}:{number}: {match.group(0)}")
    return hits


def main():
    parser = argparse.ArgumentParser(description="Scan files for the Fort repository's forbidden names.")
    parser.add_argument("--fort-repo", default=DEFAULT_FORT,
                        help="the Fort on the Lake repository (default: %(default)s)")
    parser.add_argument("paths", nargs="*", help="files or folders to scan (default: the unit's files)")
    options = parser.parse_args()

    try:
        patterns = generator_patterns(options.fort_repo) + intro_patterns(options.fort_repo)
    except OSError as error:
        print(f"Cannot read the patterns: {error}")
        sys.exit(2)
    if len(patterns) < 6:
        print(f"Expected 6 patterns from the Fort repository, found {len(patterns)}. "
              "Check generator/test.mjs and intro/test.mjs.")
        sys.exit(2)

    paths = expand(options.paths) if options.paths else default_paths()
    hits = []
    for path in paths:
        hits = hits + scan_file(path, patterns)

    for hit in hits:
        print("HIT " + hit)
    if not hits:
        print("no hits")
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
