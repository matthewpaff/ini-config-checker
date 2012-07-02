"""Construct original INI examples; no actual service configuration or secrets."""
import argparse
import json


def make_case(index):
    label = "synthetic-config-{:04d}".format(index)
    name, port, debug = "sample-{}".format(index), 1024 + index % 60000, index % 2 == 0
    text = "[service]\nname = {}\nport = {}\ndebug = {}\n".format(name, port, "true" if debug else "false")
    kind = index % 10
    if kind == 0:
        text = text.replace(str(port), "0")
    elif kind == 1:
        text = text.replace("debug = ", "unexpected = ")
    elif kind == 2:
        text += "name = duplicate\n"
    elif kind == 3:
        text = text.replace(name, "Invalid Name")
    elif kind == 4:
        text = text.replace("debug = " + ("true" if debug else "false"), "debug = perhaps")
    else:
        return {"id": label, "input": text, "expected": {"name": name, "port": port, "debug": debug}}
    return {"id": label, "input": text, "expected_error": True}


def main():
    parser = argparse.ArgumentParser(description="Print synthetic configuration cases as JSONL.")
    parser.add_argument("--count", type=int, default=20)
    args = parser.parse_args()
    if not 1 <= args.count <= 10000:
        parser.error("Count must be between 1 and 10000")
    for index in range(args.count):
        print(json.dumps(make_case(index), ensure_ascii=True, sort_keys=True))


if __name__ == "__main__":
    main()
