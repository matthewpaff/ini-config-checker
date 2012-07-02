import argparse
import json
import sys

from .core import read_config
from .fixture_check import check


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate a small INI service configuration as JSON.")
    parser.add_argument("path", nargs="?", default="-", help="UTF-8 file or - for stdin")
    parser.add_argument("--check-fixtures", metavar="JSONL")
    args = parser.parse_args(argv)
    try:
        if args.check_fixtures:
            if args.path != "-":
                parser.error("Use --check-fixtures alone")
            print("Verified {} synthetic fixtures.".format(check(args.check_fixtures, read_config)))
        else:
            if args.path == "-":
                text = sys.stdin.read()
            else:
                with open(args.path, encoding="utf-8") as handle:
                    text = handle.read()
            print(json.dumps(read_config(text), indent=2))
        return 0
    except ValueError as error:
        print("error: " + str(error), file=sys.stderr)
        return 2
    except OSError as error:
        print("error: " + str(error), file=sys.stderr)
        return 1
