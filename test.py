import pytest
from main import count_vowels

def test_count_vowels():
    # Проверка стандартных случаев
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("python") == 1

    # Проверка строки с заглавными буквами
    assert count_vowels("HELLO") == 2

    # Проверка пустой строки
    assert count_vowels("") == 0

    # Проверка строки без гласных
    assert count_vowels("bcdfgh") == 0

    # Проверка строки с пробелами и знаками препинания
    assert count_vowels("Hello, how are you?") == 7

    # Проверка строки с повторяющимися гласными
    assert count_vowels("aabbcc") == 2

@pytest.mark.parametrize("string, expected_count", [
    ("count", 2),
    ("with", 1),
    ("limit", 2),
    ("PREMIUM", 3),
    ("", 0),
    ("nfrmtn", 0),
    ("Process finished with exit code 0", 10),
    ("alphavantage", 5)
])

# Запуск тестов
def test_count_vowels_parametrized(string, expected_count):
    assert count_vowels(string) == expected_count
