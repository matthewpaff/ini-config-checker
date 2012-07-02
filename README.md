# Config Reader Lab

Validate a tiny INI service configuration and print normalized JSON without starting any service.

This original small project uses **Python 3.10+ and only its standard library**.
No packages, virtual environment, service, or network access are required.

## Run

From this repository directory:

```console
python config_reader.py --help
python config_reader.py examples/sample.ini
python config_reader.py --check-fixtures fixtures/cases.jsonl
python -m unittest discover -s tests -v
```

Exactly one [service] section and the options name, port, and debug are required; DEFAULT values and unknown options are rejected. Names start with a lowercase letter and allow lowercase letters, digits, and hyphens, up to 40 characters. Ports are 1–65535. Debug accepts ConfigParser boolean forms such as true/false and yes/no. Interpolation is disabled. This only validates text and makes no network connections.

Output is JSON (or a fixture-check summary). Exit codes are 0 for success,
1 for file failures, and 2 for invalid input. Errors go to stderr.
For file-based tools, `-` reads stdin. Use UTF-8 input files.

## Structure and branches

- `config_reader_lab/core.py`: pure parsing or analysis logic.
- `config_reader_lab/cli.py`: command arguments and file input/output.
- `config_reader_lab/generate_fixtures.py`: deterministic original sample cases.
- `config_reader_lab/fixture_check.py`: expected-result/error validation.
- `fixtures/cases.jsonl`: 366 synthetic cases, one added per artificial dated commit.
- `tests/`: independently chosen boundary cases plus corpus validation.

`feature/core` and `feature/cli` retain the corresponding development snapshots.
`data/synthetic-fixtures` marks the completed corpus; `docs/usage` and `main` contain
the final documentation and tests. There are no copied upstream commits.

## Generate examples

```console
python generate_fixtures.py --count 20
```

This prints reproducible JSONL and **does not create or date Git commits**. The
historical-looking Git timeline is a separate, documented simulation. Many cases
vary generated values; they do not imply separate design decisions or features.

Keep contributions focused, add a regression test for changed behavior, and run
the standard-library tests. Never add real private data or credentials. Record
actual dates for new work. Licensed under [MIT](LICENSE).

[History and provenance](HISTORY.md).
