import pytest
from string_utils import StringUtils

class TestStringUtils:
    def setup_method(self):
        self.utils = StringUtils()

    # Тестируем capitalize()
    def test_capitalize_normal(self):
        assert self.utils.capitalize("skypro") == "Skypro"

    def test_capitalize_empty_string(self):
        assert self.utils.capitalize("") == ""

    def test_capitalize_only_spaces(self):
        assert self.utils.capitalize("  ") == "  "

    def test_capitalize_lowercase_word(self):
        assert self.utils.capitalize("hello") == "Hello"

    def test_capitalize_already_capitalized(self):
        assert self.utils.capitalize("Hello") == "Hello"

    # Тестируем trim()
    def test_trim_leading_spaces(self):
        assert self.utils.trim("   skypro") == "skypro"

    def test_trim_middle_spaces_preserved(self):
        assert self.utils.trim(" sky pro ") == "sky pro "

    def test_trim_only_spaces(self):
        assert self.utils.trim("   ") == ""

    def test_trim_no_spaces(self):
        assert self.utils.trim("skypro") == "skypro"

    # Тестируем contains()
    def test_contains_true(self):
        assert self.utils.contains("SkyPro", "S") is True

    def test_contains_false(self):
        assert self.utils.contains("SkyPro", "U") is False

    def test_contains_empty_string(self):
        assert self.utils.contains("", "a") is False

    def test_contains_empty_symbol_returns_true(self):
        assert self.utils.contains("SkyPro", "") is True

    # Тестируем delete_symbol()
    def test_delete_symbol_normal(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_not_found(self):
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_symbol_empty_symbol(self):
        assert self.utils.delete_symbol("SkyPro", "") == "SkyPro"

    def test_delete_symbol_none_symbol(self):
        with pytest.raises(TypeError):
            self.utils.delete_symbol("SkyPro", None)



