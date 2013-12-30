from pathlib import Path
import unittest

from config_reader_lab.core import read_config
from config_reader_lab.fixture_check import check


class ConfigTests(unittest.TestCase):
    def test_valid_values_and_boolean_forms(self):
        self.assertEqual(read_config("[service]\nname=demo\nport=65535\ndebug=yes\n"), {"name": "demo", "port": 65535, "debug": True})

    def test_missing_unknown_defaults_and_duplicate_options_fail(self):
        base = "[service]\nname=demo\nport=8000\ndebug=false\n"
        for text in (base + "name=again\n", base + "extra=1\n", base.replace("port=8000\n", ""),
                     base.replace("8000", "65536"), "[DEFAULT]\nextra=1\n" + base):
            with self.subTest(text=text), self.assertRaises(ValueError):
                read_config(text)

    def test_percent_characters_are_not_interpolated(self):
        with self.assertRaisesRegex(ValueError, "Name must"):
            read_config("[service]\nname=%(missing)s\nport=8000\ndebug=false\n")

    def test_all_generated_fixtures(self):
        self.assertGreaterEqual(check(Path(__file__).resolve().parents[1] / "fixtures" / "cases.jsonl", read_config), 350)


if __name__ == "__main__":
    unittest.main()
