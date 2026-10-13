import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from translations import LANGUAGES, STRINGS, Translator, code_from_choice  # noqa: E402

SRC = Path(__file__).resolve().parent.parent / "src" / "app_gui.py"


@pytest.mark.parametrize("lang", list(LANGUAGES))
def test_every_language_has_every_key_with_same_placeholders(lang):
    base = STRINGS["en"]
    assert set(STRINGS[lang]) == set(base)
    for key, text in base.items():
        assert STRINGS[lang][key].count("{}") == text.count("{}"), (lang, key)


def test_every_key_used_in_the_gui_exists():
    used = set(re.findall(r"""\bt\(\s*f?["']([a-z_{}]+)["']""", SRC.read_text(encoding="utf-8")))
    used = {k for k in used if "{" not in k}
    assert used, "regex found nothing"
    assert used <= set(STRINGS["en"]), used - set(STRINGS["en"])


def test_country_choices_round_trip():
    t = Translator("pt")
    assert "Reino Unido (gb)" in t.country_choices()
    for choice in t.country_choices():
        assert code_from_choice(choice)
    assert code_from_choice("  NZ ") == "nz"
    assert code_from_choice("Brazil") is None


def test_number_format():
    assert Translator("pt").num(12480) == "12.480"
    assert Translator("en").num(12480) == "12,480"
