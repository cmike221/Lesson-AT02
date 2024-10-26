import pytest
from main import count_russian_vowels


def test_only_vowels():
    assert count_russian_vowels("аеёийоуыэюя") == 10
    assert count_russian_vowels("АЕЁИЙОУЫЭЮЯ") == 10


def test_no_vowels():
    assert count_russian_vowels("бвгджзклмнпрстфхцчшщъь") == 0
    assert count_russian_vowels("") == 0


def test_mixed_strings():
    assert count_russian_vowels("Привет, мир!") == 3
    assert count_russian_vowels("Как дела?") == 3
    assert count_russian_vowels("Это тест!") == 3


if __name__ == "__main__":
    pytest.main()
