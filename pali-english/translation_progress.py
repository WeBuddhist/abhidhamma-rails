#!/usr/bin/env python3
"""Report translation coverage: source leaf verse-ids vs output file."""

import argparse
import re
import sys

LEAF_ID_RE = re.compile(r"\^([\w]+(?:-[\w]+)*-(?!0\b)\d+)\b")


def leaf_ids(text):
    return set(LEAF_ID_RE.findall(text))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    src = open(args.source, encoding="utf-8").read()
    try:
        out = open(args.output, encoding="utf-8").read()
    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    src_ids = leaf_ids(src)
    out_ids = leaf_ids(out)
    missing = sorted(src_ids - out_ids, key=lambda v: [int(x) for x in re.findall(r"\d+", v)])
    extra = sorted(out_ids - src_ids)

    print("Source leaf items : %d" % len(src_ids))
    print("Output leaf items : %d" % len(out_ids))
    print("Translated        : %d (%.1f%%)" % (len(out_ids & src_ids), 100.0 * len(out_ids & src_ids) / len(src_ids)))
    print("Missing           : %d" % len(missing))
    if missing:
        print("  first missing   : %s" % missing[0])
        print("  last missing    : %s" % missing[-1])
        print("  next 10 missing : %s" % missing[:10])
    if extra:
        print("Extra (not in source): %s" % extra[:10])


if __name__ == "__main__":
    main()
